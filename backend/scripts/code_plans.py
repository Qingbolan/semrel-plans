"""Logical DAGs for benchmarks whose plans are written as code objects (ELEET) or records (SemCEB)."""
import ast
import re

LABEL = 160


def short(text):
    """At most LABEL characters, cut at a word boundary."""
    text = re.sub(r'\s+', ' ', str(text)).strip()
    if len(text) <= LABEL:
        return text
    head = text[:LABEL - 1]
    return (head[:head.rfind(' ')] if head.rfind(' ') > LABEL // 2 else head).rstrip(' ,(') + ' …'


class Graph:
    def __init__(self):
        self.nodes, self.edges = [], []

    def node(self, op, label, inputs=()):
        nid = f'n{len(self.nodes):03d}'
        self.nodes.append(dict(node_id=nid, operator_type=op, label=short(label)))
        for i, child in enumerate(inputs):
            self.edges.append(dict(parent_id=nid, child_id=child, input_position=i))
        return nid


class EleetPlan:
    """ELEET operator objects: MM* operators read text collections ("reports.Player"), others are relational."""

    def __init__(self, assignments):
        self.assignments = assignments  # variable name -> AST value inside the dataset function
        self.graph = Graph()

    def value(self, node):
        if isinstance(node, ast.Name) and node.id in self.assignments:
            return self.value(self.assignments[node.id])
        try:
            return ast.literal_eval(node)
        except ValueError:
            return ast.unparse(node)

    def build(self, node):
        if isinstance(node, ast.Name) and node.id in self.assignments:
            return self.build(self.assignments[node.id])
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            kind = 'text collection' if '.' in node.value else 'table'
            return self.graph.node('SCAN', f'Scan {kind} {node.value}')
        if not (isinstance(node, ast.Call) and isinstance(node.func, ast.Name)):
            raise ValueError(f'Unsupported plan expression: {ast.unparse(node)}')
        name = node.func.id
        kw = {k.arg: k.value for k in node.keywords}
        operands = [self.build(o) for o in (kw.get('operands') or node.args[0]).elts]  # keyword or positional
        g = self.graph
        if name == 'MMScan':
            out = g.node('SEM_MAP', 'MMScan: extract table rows from text', operands)
        elif name == 'MMJoin':
            out = g.node('SEM_JOIN', f"MMJoin on {self.value(kw['join_key'])}: extract matching rows from text", operands)
        elif name == 'MMUnion':
            extracted = g.node('SEM_MAP', 'MMUnion: extract rows from text', operands[1:])
            out = g.node('UNION_ALL', 'MMUnion with table rows', [operands[0], extracted])
        elif name == 'MMSelection':
            # ELEET selects on an attribute it extracts from the text itself, so the selection sits below the MMScan that reads the rest.
            op_of = {n['node_id']: n['operator_type'] for n in g.nodes}
            pushed = ' (pushed into the text scan)' if all(op_of[o] == 'SCAN' for o in operands) else ''
            out = g.node('SEM_FILTER', f"MMSelection on {self.value(kw['attribute'])} (selectivity {self.value(kw['selectivity'])}){pushed}", operands)
        elif name == 'MMAggregation':
            out = g.node('SEM_AGG', f"MMAggregation: group text reports by extracted {self.value(kw['attribute'])}", operands)
        elif name == 'Join':
            out = g.node('JOIN', f"Join on {self.value(kw['join_key'])}", operands)
        elif name == 'Selection':
            target = self.value(kw['attribute']) if 'attribute' in kw else self.value((kw.get('operands') or node.args[0]).elts[0])
            out = g.node('FILTER', f"Selection on {target} (selectivity {self.value(kw['selectivity'])})", operands)
        elif name == 'Projection':
            out = g.node('PROJECT', f"Project {', '.join(self.value(kw['project_columns']))}", operands)
        else:
            raise ValueError(f'Unknown ELEET operator {name}')
        if 'project_columns' in kw and name != 'Projection':
            out = g.node('PROJECT', f"Project {', '.join(self.value(kw['project_columns']))}", [out])
        return out


def eleet_plan(assignments, expression):
    plan = EleetPlan(assignments)
    root = plan.build(expression)
    return plan.graph.nodes, plan.graph.edges, root


def semceb_plan(record, predicate):
    """One semantic filter over a dataset, or one semantic join over two aliased datasets; the label is the predicate sentence."""
    g = Graph()
    scans = [g.node('SCAN', f'Scan {d}') for d in record['datasets']]
    op = 'SEM_JOIN' if len(scans) == 2 else 'SEM_FILTER'
    root = g.node(op, predicate, scans)
    return g.nodes, g.edges, root
