"""Lower supplied plan notation, preserving opaque expressions and explicit data flow."""
import ast
import json
import re
from pathlib import Path


class PlanSyntaxError(ValueError):
    pass


def split_top(text, separators):
    """Split only outside strings and balanced expression delimiters."""
    parts, stack, quote, start, i = [], [], None, 0, 0
    while i < len(text):
        ch = text[i]
        if quote:
            if ch == '\\':
                i += 2
                continue
            if ch == quote and not (ch == "'" and i > 0 and i + 1 < len(text) and text[i-1].isalnum() and text[i+1].isalnum()):
                quote = None
        elif ch in "\"'":
            quote = ch
        elif ch in '([{':
            stack.append(ch)
        elif ch in ')]}':
            if not stack or '([{'.index(stack.pop()) != ')]}'.index(ch):
                raise PlanSyntaxError('Unbalanced delimiter')
        elif not stack:
            sep = next((s for s in separators if text.startswith(s, i)), None)
            if sep:
                parts.append(text[start:i].strip())
                i += len(sep)
                start = i
                continue
        i += 1
    if stack or quote:
        raise PlanSyntaxError('Unclosed expression or string')
    parts.append(text[start:].strip())
    return [p for p in parts if p]


LABEL_LIMIT = 120


def cut_prompt(text, limit=100):
    """A prompt cut at its first clause boundary, or at a word near the limit."""
    if len(text) <= limit:
        return text
    head = re.split(r';|\s\(|\s—\s|, (?:and |which |where |despite )', text, maxsplit=1)[0]
    return head + ' …' if 25 <= len(head) <= limit else text[:limit - 1].rsplit(' ', 1)[0] + ' …'


def display_label(label):
    """Graph-node text for a plan step over LABEL_LIMIT characters; the full step stays in the reference program.
    Semantic steps keep their prompt, not their output schema or input bindings; long output lists keep their names."""
    # input bindings ({filing_text: document_text}) and output schemas ({n: integer}) are plumbing at any length
    label = re.sub(r""",\s*(?:input_bindings\w*\s*=\s*)?\{[^{}'"]*:[^{}'"]*\}""", '', label)
    if len(label) <= LABEL_LIMIT:
        return label
    call = re.match(r'([A-Z_]+)\((.*)\)(\s*(?:AS \w+|\[as \w+\])?)$', label, re.S)
    if not call:
        return cut(label)
    op, body, suffix = call.groups()
    prompt = re.search(r"""(['"])((?:(?!\1).){12,}?)\1""", body, re.S)
    if op.startswith('SEM_') and prompt:
        return f"{op}('{cut_prompt(prompt.group(2))}'){suffix}"
    if op == 'PROJECT':  # every output column: its alias (AS x or x=expr), or the column itself
        items = split_top(body.strip().strip('[]'), [','])
        def name(item):
            alias = re.search(r'AS (\w+)\s*$', item) or re.match(r'\s*(\w+)\s*=(?!=)', item)
            return alias.group(1) if alias else item.strip()
        return cut(f"PROJECT({', '.join(name(i) for i in items)}){suffix}")
    names = re.findall(r'\bAS (\w+)', body)
    if op == 'COMPUTE' and not names:  # COMPUTE(x = expr, y = expr)
        names = [m.group(1) for m in (re.match(r'\s*(\w+)\s*=(?!=)', i) for i in split_top(body, [','])) if m]
    if names and op in ('GROUP_BY', 'AGGREGATE', 'COMPUTE'):
        keys = re.match(r'\s*\[([^\[\]]*)\]\s*,', body) or re.match(r'\s*([^;\[]+);', body)
        return f"{op}({keys.group(1).strip() + '; ' if keys else ''}→ {', '.join(names)}){suffix}"[:LABEL_LIMIT * 2]
    body = re.sub(r',?\s*right=\(.*\)\s*$', '', body, flags=re.S)                                   # inline right sub-plan, drawn as a child
    body = re.sub(r',\s*(?:input_bindings\w*\s*=\s*)?\{[^{}]*\}', '', body)  # a bare or input_bindings= brace argument; aggs={...} stays
    body = re.sub(r'\[([^\[\]]{60,})\]', lambda m: f"[{m.group(1).count(',') + 1} fields]", body)  # long field lists
    return cut(f'{op}({body}){suffix}')


def cut(text):
    """At most LABEL_LIMIT characters, cut at a token boundary."""
    if len(text) <= LABEL_LIMIT:
        return text
    head = text[:LABEL_LIMIT - 1]
    boundary = max(head.rfind(', '), head.rfind(' '))
    return (head[:boundary] if boundary > LABEL_LIMIT // 2 else head).rstrip(' ,(') + ' …'


class ReferencePlan:
    ALIASES = {'SCAN_TABLE': 'SCAN', 'SCAN_DOCS': 'SCAN', 'ORDER_BY': 'SORT',
               'GROUP_BY': 'AGGREGATE', 'DEDUP': 'DISTINCT',
               'SEM_EXTRACT': 'SEM_MAP', 'SEM_AGGREGATE': 'SEM_AGG'}
    COARSE = {
        'SCAN heterogeneous databases': 'SCAN',
        'deterministic SQL/Python, including fixed regex/LIKE or enumerated mappings where applicable': 'COMPUTE',
        'deterministic tabular/JSON aggregation or statistical analysis': 'COMPUTE',
        'relational/SQL/Python analysis only': 'COMPUTE',
        'relational analysis': 'COMPUTE', 'deterministic answer logic': 'COMPUTE',
        'deterministic JSON/tabular computation': 'COMPUTE',
        'deterministic file parsing/cleaning': 'COMPUTE',
        'relational, statistical, geospatial, or ML computation': 'COMPUTE',
        'relational/statistical analysis': 'COMPUTE',
    }

    def __init__(self, query_id, operators):
        self.query_id, self.operators = query_id, operators
        self.nodes, self.edges, self.bindings = [], [], {}

    def node(self, operator, label, inputs):
        if operator not in self.operators:
            raise PlanSyntaxError(f'Unknown operator {operator}: {label}')
        nid = f'ref_{len(self.nodes):03d}'
        self.nodes.append(dict(query_id=self.query_id, node_id=nid, operator_type=operator, label=display_label(label)))
        for index, child in enumerate(inputs):
            self.edges.append(dict(query_id=self.query_id, parent_id=nid, child_id=child, input_position=index))
        return nid

    def parse(self, program):
        # Newlines are statement boundaries only when no arrow continues the chain.
        statements = split_top(program, ['|||', ';', '\n'])
        combined = []
        for statement in statements:
            if statement.startswith('->') and combined:
                combined[-1] += '\n' + statement
            else:
                combined.append(statement)
        for statement in combined:
            assign = re.match(r'^(\w+)\s*(?::=|=)\s*(.*)$', statement, re.S)
            if assign:
                name, statement = assign.groups()
                self.bindings[name] = self.chain(statement)
            else:
                self.chain(statement)
        consumed = {e['child_id'] for e in self.edges}
        roots = [n['node_id'] for n in self.nodes if n['node_id'] not in consumed]
        if not roots:
            raise PlanSyntaxError('Empty reference plan')
        if len(roots) == 1:
            return roots[0]
        names = {v: k for k, v in self.bindings.items()}
        return self.node('PROJECT', 'Return named result branches: ' + ', '.join(names.get(r, r) for r in roots), roots)

    def chain(self, text):
        text = text.strip()
        if text.startswith('(') and text.endswith(')'):
            text = text[1:-1].strip()
        previous = None
        for step in split_top(text, ['->']):
            alias = re.search(r'\s+AS\s+(\w+)\s*$', step)
            name = alias.group(1) if alias else None
            expression = step[:alias.start()].strip() if alias else step
            if expression in self.bindings:
                previous = self.bindings[expression]
            else:
                previous = self.operation(expression, previous)
            if name:
                self.bindings[name] = previous
        return previous

    def operation(self, expression, previous):
        # 'step <- name' adds the named binding as a further input of any step, coarse phrases included.
        reverse = split_top(expression, ['<-'])
        if len(reverse) == 2:
            expression, right_name = reverse
            if right_name not in self.bindings:
                raise PlanSyntaxError('Unknown reverse-arrow input')
        if expression in self.COARSE:
            extra = [self.bindings[right_name]] if len(reverse) == 2 else []
            return self.node(self.COARSE[expression], expression, ([previous] if previous else []) + extra)
        call = re.fullmatch(r'([A-Z_]+)\s*\((.*)\)', expression, re.S)
        if not call:
            raise PlanSyntaxError(f'Unsupported reference expression: {expression}')
        source_op, body = call.groups()
        operator = self.ALIASES.get(source_op, source_op)
        inputs = [previous] if previous else []
        if source_op in ('JOIN', 'SEM_JOIN', 'SEM_LEFT_JOIN'):
            args = split_top(body, [','])
            explicit = {}
            for arg in args:
                match = re.match(r'^(left|right)\s*=\s*(.*)$', arg, re.S)
                if match:
                    side, value = match.groups()
                    explicit[side] = self.bindings[value] if value in self.bindings else self.chain(value)
            if explicit:
                inputs = [explicit.get('left', previous), explicit.get('right')]
                if any(i is None for i in inputs):
                    raise PlanSyntaxError('Join missing input')
            else:
                # Only unquoted relation names resolve to graph inputs; prompts remain opaque.
                unquoted = re.sub(r'''"(?:\\.|[^"\\])*"|'(?:\\.|[^'\\])*' ''', '', body, flags=re.X)
                positional = [arg for arg in args if arg in self.bindings]
                for token in positional or re.findall(r'\b\w+\b', unquoted):
                    if token in self.bindings and self.bindings[token] not in inputs:
                        inputs.append(self.bindings[token])
            if source_op == 'JOIN':
                if re.search(r'^\s*left\s*,|\bjoin_type\s*=\s*left\b', body):
                    operator = 'LEFT_JOIN'
                elif re.match(r'\s*cross\s*,', body):
                    operator = 'CROSS_JOIN'
            if not inputs:
                raise PlanSyntaxError('Join has no resolved relation')
        if len(reverse) == 2 and self.bindings[right_name] not in inputs:
            inputs.append(self.bindings[right_name])
        return self.node(operator, expression, inputs)


STRUCTURAL = {'PROJECT', 'CTE', 'CTE_REF', 'UNRESOLVED', 'RESULT_BUNDLE'}


def dag_mixed_label(op_types, families):
    """Mixing of a logical DAG. 实质混合 is the coverage statistic's rule: a semantic plus a non-structural relational
    operator. Otherwise the plan is semantic with only a projection, semantic only, or relational only."""
    op_types = list(op_types)
    semantic = any(families[o] == 'semantic' for o in op_types)
    relational = any(families[o] == 'relational' and o not in STRUCTURAL for o in op_types)
    if semantic and relational:
        return '实质混合'
    if semantic:
        return '轻混合（仅投影）' if 'PROJECT' in op_types else '纯语义'
    return '纯关系' if relational else ''


SKETCH_STATUS = '按语义需求类别给出的粗粒度计划（同类查询共用，非逐查询重建）'
SKETCH_NOTE = '7-30 只按类别标注是否需要语义算子及其位置，同一类查询共用一个计划；关系运算以一个概括性的节点表示，未逐查询展开。数据表取自该查询的输入清单。'


def sketch_program(program, table_names):
    """7-30 programs are category sketches written as one chain. Draw the data the chain reads, and make a mid-chain
    document scan a second input of the next step instead of a step that consumes the previous result."""
    data = ''
    if table_names:
        count = len(table_names)
        while count > 1 and len(', '.join(table_names[:count])) > 80:
            count -= 1
        shown = ', '.join(table_names[:count]) + (f', … (+{len(table_names) - count})' if len(table_names) > count else '')
        data = f'SCAN_TABLE({shown}) -> '
    if data and program.startswith('SCAN heterogeneous databases'):  # name the databases the query reads
        program = data[:-4] + program[len('SCAN heterogeneous databases'):]
        data = ''
    steps = [x.strip() for x in program.split(' -> ')]
    scan = next((i for i, x in enumerate(steps) if x.startswith('SCAN_DOCS(')), None)
    if scan is None:
        return program if steps[0].startswith('SCAN') else data + program
    if scan == 0:  # documentation read by a semantic step, then a computation over the data tables
        docs = ' -> '.join(steps[:2])
        rest = steps[2:]
        return f"docs = {docs}\n{data}{rest[0]} <- docs" + ''.join(' -> ' + x for x in rest[1:]) if rest else program
    before, after = steps[:scan], steps[scan + 1:]
    return (f"docs = {steps[scan]}\n{data}{' -> '.join(before)} -> {after[0]} <- docs" + ''.join(' -> ' + x for x in after[1:]))


def choice_note(original, repo):
    """FDABench choice questions keep their options in the source record, not in the query text: show them."""
    upstream = ((original or {}).get('upstream_comparison') or {}).get('source_path', '')
    path = Path(repo) / upstream if upstream.endswith('.jsonl') else None
    if path is None or not path.exists():
        return ''
    task = original.get('selector', {}).get('id')
    row = next((json.loads(l) for l in path.read_text().splitlines() if f'"{task}"' in l and json.loads(l).get('task_id') == task), None)
    if not row or not row.get('options'):
        return ''
    options = row['options'] if isinstance(row['options'], dict) else ast.literal_eval(row['options'])
    return '选择题：计划只覆盖取数分析，不含对选项的判断。选项：' + ' '.join(f'{k}. {v}' for k, v in options.items())


def lower_collections(tables, operators, repo=None):
    """Replace only imported logical projections; original evidence stays untouched."""
    details = {d['query_id']: d for d in tables['task_details']}
    contracts = {c['query_id']: c for c in tables['input_contracts']}
    originals = {o['query_id']: o for o in tables.get('original_queries', [])}
    families = {o['operator_type']: o['family'] for o in json.loads((Path(repo) / 'config/operators.json').read_text())} if repo else None
    ids = {q['query_id'] for q in tables['queries'] if q['benchmark_id'] in ('8-17', '7-30')}
    nodes, edges = [], []
    for query in tables['queries']:
        if query['query_id'] not in ids:
            continue
        plan = ReferencePlan(query['query_id'], operators)
        programs = details[query['query_id']]['reference_programs']
        if len(programs) != 1:
            raise PlanSyntaxError('Expected one reference plan')
        sketch = query['benchmark_id'] == '7-30'
        program = programs[0]['program']
        if sketch:
            names = [t['name'] for t in contracts.get(query['query_id'], {}).get('tables', [])]
            program = sketch_program(program, names)
        try:
            root = plan.parse(program)
        except PlanSyntaxError as exc:
            raise PlanSyntaxError(f"{query['query_id']}: {exc}") from exc
        if families:
            query['mixed_label'] = dag_mixed_label([n['operator_type'] for n in plan.nodes], families)
        query.update(plan_format='logical_dag', root_node_id=root,
                     plan_status_label=SKETCH_STATUS if sketch else 'Reference-derived logical plan · not execution-verified',
                     notes=' '.join(filter(None, [SKETCH_NOTE, repo and choice_note(originals.get(query['query_id']), repo)])) if sketch
                     else query.get('notes', ''))
        nodes.extend(plan.nodes)
        edges.extend(plan.edges)
    tables['nodes'] = [n for n in tables['nodes'] if n['query_id'] not in ids] + nodes
    tables['edges'] = [e for e in tables['edges'] if e['query_id'] not in ids] + edges
