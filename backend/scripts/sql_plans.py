"""Convert benchmark SQL with embedded semantic calls into the catalog's logical DAG.

Used only at import time (requires sqlglot==30.22.0, see backend/scripts/audit/requirements.txt).
Operator types are the existing ones in config/operators.json. Deterministic predicates are
drawn below semantic ones, as a dependency picture, not a claim about the engine's order.
"""
import re

import logging

import sqlglot
from sqlglot import exp

logging.getLogger('sqlglot').setLevel(logging.ERROR)

LABEL = 160


def short(text):
    """At most LABEL characters, cut at a word boundary."""
    text = re.sub(r'\s+', ' ', text).strip()
    if len(text) <= LABEL:
        return text
    head = text[:LABEL - 1]
    return (head[:head.rfind(' ')] if head.rfind(' ') > LABEL // 2 else head).rstrip(' ,(') + ' …'


class Dialect:
    """How a benchmark writes semantic calls."""

    def __init__(self, name, read, calls, prepare=None):
        self.name, self.read, self.calls, self.prepare = name, read, calls, prepare
        self.restore = lambda text: text

    def semantic(self, node):
        """Return (operator_type, prompt) for a semantic call, else None."""
        if isinstance(node, exp.Anonymous) or isinstance(node, exp.Func):
            name = (node.name if isinstance(node, exp.Anonymous) else node.sql_name()).lower()
            if name in self.calls:
                return self.calls[name](node)
        return None


def first_string(node):
    s = node.find(exp.Literal)
    return s.this if s is not None and s.is_string else node.sql()


def render_prompt(node):
    """A prompt built as 'text' || column || 'text', rendered in source order with columns as {col}."""
    arg = node.expressions[0] if isinstance(node, exp.Anonymous) else node.this

    def render(e):
        if isinstance(e, exp.DPipe):
            return render(e.this) + render(e.expression)
        if isinstance(e, exp.Literal) and e.is_string:
            return e.this
        return '{' + e.sql() + '}'
    return render(arg)


def swan_prompt(node):
    """SWAN wraps the prompt as Context «…» Claim: … and may end it with an answer-format suffix."""
    text = render_prompt(node)
    text = text.split('Claim:', 1)[1] if 'Claim:' in text else text
    text = re.sub(r'\s*Answer with the (value|number) only[^.]*\.?\s*$', '', text)
    return prompt_with_columns(text)


def prompt_with_columns(text):
    """'Question? field: {t.col}' or 'Question? col' -> 'Question? (t.col)': the ask first, the inputs in parentheses."""
    columns = re.findall(r'\{([^}]+)\}', text)
    text = re.sub(r'\s*\b[\w ]{1,30}:\s*\{[^}]+\}', '', text)
    text = re.sub(r'\{[^}]+\}', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    tail = re.search(r'([?.])\s+(\w+)$', text)  # SWAN ai_filter claims end with the bare column name
    if tail:
        columns = columns or [tail.group(2)]
        text = text[:tail.start(2)].strip()
    return text + (f" ({', '.join(dict.fromkeys(columns))})" if columns else '')


def swan_dialect():
    return Dialect('swan', 'duckdb', {
        'ai_filter': lambda n: ('SEM_FILTER', swan_prompt(n)),
        'ai_classify': lambda n: ('SEM_CLASSIFY', swan_prompt(n)),
        'ai_complete': lambda n: ('SEM_MAP', swan_prompt(n)),
        'ai_agg': lambda n: ('SEM_AGG', swan_prompt(n)),
    })


def plop_prompt(node):
    """The sentence that asks something: slots, header lines, answer-format boilerplate and role preambles are dropped."""
    text = render_prompt(node).replace('\\n', '\n')
    columns = re.findall(r'\{([^}]+)\}', text)
    text = re.sub(r'(?<![\w(])[A-Za-z][\w ]{0,30}:\s*\{[^}]+\}\)?\s*;?', '', text)  # 'Part Name: {p.p_name}' slots, inline or per line
    text = re.sub(r'(?m)(^|(?<=[.?!]) )[^\n.?!]{0,60}:\s*$', '', text)   # header phrases ending a line, e.g. 'Customer profile check:'
    text = re.sub(r'\s*\{[^}]+\}', '', re.sub(r'\s+', ' ', text)).strip()
    boilerplate = re.compile(r"^(Otherwise|If (unsure|uncertain))\b|^(Answer|Return|Respond|Output)\b(?!.*\bif\b)", re.I)
    sentences = [x.strip(' )') for x in re.split(r'(?<=[.?!])\s+', text)]
    sentences = [x for x in sentences if x and not boilerplate.match(x) and not x.startswith('Rule:') and not x.endswith(':')]
    questions = [x for x in sentences if x.endswith('?')]
    if questions:
        ask = questions[0]
    elif len(sentences) > 1 and sentences[0].startswith('You are'):
        ask = sentences[1]
    else:
        ask = sentences[0] if sentences else text
    ask = re.sub(r'^Task:\s*', '', ask).rstrip(' :.')
    return ask + (f" ({', '.join(dict.fromkeys(columns))})" if columns else '')


def plop_dialect():
    return Dialect('plop', 'duckdb', {
        'semantic': lambda n: ('SEM_FILTER', plop_prompt(n)),
        'semantic_int': lambda n: ('SEM_MAP', plop_prompt(n)),
        'semantic_string': lambda n: ('SEM_MAP', plop_prompt(n)),
        'semantic_double': lambda n: ('SEM_MAP', plop_prompt(n)),
    })


def blendsql_dialect():
    """{{Ingredient(...)}} blocks become placeholder calls; only LLM ingredients are semantic."""
    ingredients = []
    innermost = re.compile(r'\{\{((?:(?!\{\{|\}\}).)*)\}\}', re.S)

    def prepare(sql):
        ingredients.clear()

        def replace(match):
            ingredients.append(match.group(1).strip())
            return f' blendsql_ingredient({len(ingredients) - 1}) '
        while innermost.search(sql):
            sql = innermost.sub(replace, sql)
        return sql

    def restore(text):
        # sqlglot uppercases the placeholder name when it re-renders SQL, so match case-insensitively.
        return re.sub(r'blendsql_ingredient\((\d+)\)', lambda m: restore(ingredients[int(m.group(1))]), text, flags=re.I)

    def call(node):
        text = ingredients[int(node.expressions[0].this)]
        kind = text.split('(', 1)[0].strip()
        if kind not in ('LLMMap', 'LLMQA', 'LLMJoin', 'ImageCaption'):
            return None
        op = {'LLMMap': 'SEM_MAP', 'LLMQA': 'SEM_AGG', 'LLMJoin': 'SEM_JOIN', 'ImageCaption': 'SEM_MAP'}[kind]
        prompt = re.search(r"'([^']*)'", text)
        args = [a.strip() for a in re.sub(r'\s+', ' ', restore(text)[len(kind):]).strip(' ()').split(',')]
        if kind == 'LLMJoin':
            label = f"LLMJoin: match {args[0]} ≈ {args[1]}" if len(args) > 1 else 'LLMJoin'
        elif prompt:
            label = f"{kind}: {prompt.group(1)}"
        else:
            label = f"{kind} of {', '.join(args)}"
        return op, label, restore(text)
    dialect = Dialect('blendsql', 'sqlite', {'blendsql_ingredient': call}, prepare)
    dialect.restore = restore
    dialect.ingredients = ingredients
    return dialect


class Plan:
    def __init__(self, dialect, cte_refs=False):
        self.dialect = dialect
        self.nodes, self.edges = [], []
        # cte_refs: draw a reused CTE once (CTE node) and later uses as CTE_REF leaves, as in sembench/cars/Q6.
        self.cte_refs, self.ctes, self.cte_used = cte_refs, set(), set()
        self.names = {}  # semantic call SQL -> output name shown in relational labels

    def semantic_node(self, op, call, info, inputs):
        """One node per semantic call; its output gets the SQL alias or llm_N, and the label says so."""
        alias = call.find_ancestor(exp.Alias, exp.Select)
        name = alias.alias if isinstance(alias, exp.Alias) and alias.alias else f'llm_{len(self.names) + 1}'
        if call.sql() not in self.names and name in self.names.values():  # two calls inside one aliased expression
            name = f'{name}_{sum(v.startswith(name) for v in self.names.values()) + 1}'
        name = self.names.setdefault(call.sql(), name)
        return self.node(op, f'{name} = {info[1]}', inputs)

    def node(self, op, label, inputs=()):
        if len(label) > LABEL:  # long CASE/CAST expressions: keep their shape, not their text
            label = re.sub(r'CAST\((.*?) AS \w+\)', r'\1', re.sub(r'CASE WHEN .*? END', 'CASE…', label))
        nid = f'n{len(self.nodes):03d}'
        self.nodes.append(dict(node_id=nid, operator_type=op, label=short(self.dialect.restore(label)) or op))
        for i, child in enumerate(inputs):
            self.edges.append(dict(parent_id=nid, child_id=child, input_position=i))
        return nid

    # Semantic call helpers -------------------------------------------------
    def calls_in(self, expression):
        found = []
        for n in expression.find_all(exp.Anonymous, exp.Func):
            info = self.dialect.semantic(n)
            if info:
                found.append((n, info))
        return found

    def sql(self, expression):
        """Expression text for a relational label, each semantic call shown as the operator node it became."""
        def mark(node):
            if self.dialect.semantic(node) and node.sql() in self.names:
                return exp.Var(this=self.names[node.sql()])
            return node
        return expression.copy().transform(mark).sql()

    def output_names(self, projections):
        """Projection list as output names; a computed column without an alias keeps its expression."""
        def name(p):
            if not isinstance(p, exp.Alias):
                return self.sql(p)
            wraps = self.calls_in(p.this) and not self.dialect.semantic(p.this)
            return f'{p.alias} = {self.sql(p.this)}' if wraps else p.alias
        names = [name(p) for p in projections]
        return ', '.join(names) if len(names) <= 6 else f"{len(names)} columns: {', '.join(names[:4])}, …"

    def context_plans(self, info, env):
        """Ingredient context subqueries (BlendSQL LLMQA) become extra inputs."""
        if len(info) < 3:
            return []
        plans = []
        for sub in re.findall(r'\(\s*(SELECT\b.*?)\)\s*(?:,|$)', info[2], flags=re.S | re.I):
            try:
                plans.append(self.query(sqlglot.parse_one(sub, read=self.dialect.read), env))
            except sqlglot.errors.ParseError:
                table = re.search(r'\bFROM\s+(\w+)', sub, re.I)
                plans.append(self.node('SCAN', f"Context search over {table.group(1) if table else 'documents'}"))
        return plans

    def apply_semantic(self, current, expression, env, as_filter=False, skip_scalars=False):
        """Semantic calls inside an expression: one node each, chained above current. A question answered from its own
        context (BlendSQL LLMQA) is a single value, drawn separately when skip_scalars is set."""
        for call, info in self.calls_in(expression):
            if skip_scalars and info[0] == 'SEM_AGG' and len(info) > 2 and self.context_plans(info, env):
                continue
            op = 'SEM_MAP' if info[0] == 'SEM_FILTER' and not as_filter else info[0]
            current = self.semantic_node(op, call, info, [current] + self.context_plans(info, env))
        return current

    # Relations ---------------------------------------------------------------
    def relation_name(self, source):
        """A joined relation as a label names it: tables keep their SQL, subqueries and unnests their alias."""
        if isinstance(source, exp.Table):
            return source.sql()
        kind = 'unnest' if isinstance(source, (exp.Lateral, exp.Unnest)) else 'subquery'
        return f'{kind} {source.alias}' if source.alias else kind

    def relation(self, source, env):
        if isinstance(source, exp.Table):
            if isinstance(source.this, exp.Anonymous) or isinstance(source.this, exp.Func):
                path = source.this.find(exp.Literal)
                name = path.this.rsplit('/', 1)[-1] if path is not None and path.is_string else source.this.sql()
                return self.node('SCAN', f'Scan {name}' + (f' AS {source.alias}' if source.alias else ''))
            name = source.name.lower()
            if name not in env:
                return self.node('SCAN', f'Scan {source.sql()}')
            if self.cte_refs and name in self.ctes:
                if name in self.cte_used:
                    return self.node('CTE_REF', f'CTE REF {name}')
                self.cte_used.add(name)
                return self.node('CTE', f'CTE {name}', [env[name]])
            return env[name]
        if isinstance(source, exp.Subquery):
            return self.query(source.this, env)
        if isinstance(source, (exp.Unnest, exp.Lateral)):
            return self.node('UNNEST', f"Unnest {source.alias or 'values'}")
        return self.node('SCAN', f'Scan {source.sql()}')

    def query(self, expression, env):
        env = dict(env)
        with_ = expression.args.get('with_') or expression.args.get('with')
        if with_:
            for cte in with_.expressions:
                env[cte.alias_or_name.lower()] = self.query(cte.this, env)
                self.ctes.add(cte.alias_or_name.lower())
        if isinstance(expression, (exp.Union, exp.Intersect, exp.Except)):
            left, right = self.query(expression.this, env), self.query(expression.expression, env)
            if isinstance(expression, exp.Union):
                op = 'UNION_DISTINCT' if expression.args.get('distinct', True) else 'UNION_ALL'
            else:
                op = 'INTERSECT' if isinstance(expression, exp.Intersect) else 'ANTI_JOIN'
            return self.node(op, expression.key.upper(), [left, right])
        if isinstance(expression, exp.Subquery):
            return self.query(expression.this, env)
        if not isinstance(expression, exp.Select):
            return self.node('SCAN', f'Scan {expression.sql()}')
        return self.select(expression, env)

    def select(self, s, env):
        from_ = s.args.get('from_') or s.args.get('from')
        current = self.relation(from_.this, env) if from_ else self.node('SCAN', 'Values (no FROM)')
        for join in s.args.get('joins') or []:
            right = self.relation(join.this, env)
            on = join.args.get('on')
            side, kind = (join.side or '').upper(), (join.kind or '').upper()
            if on is not None and self.calls_in(on):
                call, info = self.calls_in(on)[0]
                label = info[1] if on is call else f'{info[1]} | ON {on.sql()}'
                current = self.node('SEM_JOIN', label, [current, right])
            elif on is None and not join.args.get('using') or kind == 'CROSS':
                current = self.node('CROSS_JOIN', f'Cross join {self.relation_name(join.this)}', [current, right])
            else:
                op = 'LEFT_JOIN' if side == 'LEFT' else 'JOIN'
                cond = on.sql() if on is not None else 'USING ' + ', '.join(c.sql() for c in join.args['using'])
                current = self.node(op, f'Join {self.relation_name(join.this)} ON {cond}', [current, right])
        where = s.args.get('where')
        if where is not None:
            current = self.predicates(current, where.this, env)
        projections = s.expressions
        aggregates = [a for p in projections for a in p.find_all(exp.AggFunc)]
        group = s.args.get('group')
        semantic_aggs = [(c, i) for p in projections for c, i in self.calls_in(p) if i[0] == 'SEM_AGG']
        for p in projections + (group.expressions if group else []):
            for call, info in self.calls_in(p):
                if info[0] != 'SEM_AGG':
                    current = self.semantic_node('SEM_CLASSIFY' if info[0] == 'SEM_CLASSIFY' else 'SEM_MAP', call, info,
                                                 [current] + self.context_plans(info, env))
        keys = ', '.join(g.sql() for g in group.expressions) if group else ''
        for call, info in semantic_aggs:
            current = self.semantic_node('SEM_AGG', call, (info[0], info[1] + (f' | GROUP BY {keys}' if keys else '')),
                                         [current] + self.context_plans(info, env))
        if group or aggregates:
            computed = ', '.join(sorted({self.sql(a) for a in aggregates}))
            if len(computed) > 100:  # long CASE/aggregate lists: name the outputs instead
                computed = self.output_names([p for p in projections if p.find(exp.AggFunc)])
            label = ('Group by ' + keys + ('; ' + computed if computed else '') if keys else 'Aggregate ' + computed)
            current = self.node('AGGREGATE', label, [current])
        having = s.args.get('having')
        if having is not None:
            current = self.predicates(current, having.this, env)
        if any(p.find(exp.Window) for p in projections):
            current = self.node('COMPUTE', 'Window ' + '; '.join(w.sql() for p in projections for w in p.find_all(exp.Window)), [current])
        subqueries = [self.query(q.this, env) for p in projections for q in p.find_all(exp.Subquery)]
        if s.args.get('distinct'):
            current = self.node('DISTINCT', 'Distinct', [current])
        order = s.args.get('order')
        if order is not None:
            current = self.node('SORT', 'Order by ' + ', '.join(o.sql() for o in order.expressions), [current])
        limit = s.args.get('limit')
        if limit is not None:
            current = self.node('LIMIT', limit.sql(), [current])
        if subqueries or not (len(projections) == 1 and isinstance(projections[0], exp.Star)):
            if isinstance(projections[0], exp.Star) and all(isinstance(p, exp.Alias) for p in projections[1:]):
                derived = [f'{p.alias} = {self.sql(p.this)}' if len(self.sql(p.this)) <= 80 else p.alias for p in projections[1:]]
                label = 'Derive ' + ', '.join(derived)  # keeps every column, adds computed ones
            else:
                label = 'Project ' + self.output_names(projections)
            current = self.node('PROJECT', label, [current] + subqueries)
        return current

    def predicates(self, current, condition, env):
        conjuncts = list(condition.flatten()) if isinstance(condition, exp.And) else [condition]
        plain, special = [], []
        for c in conjuncts:
            target = c.this if isinstance(c, exp.Not) else c
            if isinstance(target, exp.Exists) or (isinstance(target, exp.In) and target.args.get('query')) or self.calls_in(c):
                special.append(c)
            elif c.find(exp.Subquery):
                special.append(c)
            else:
                plain.append(c)
        grouped = lambda c: f'({self.sql(c)})' if isinstance(c, exp.Or) and len(conjuncts) > 1 else self.sql(c)
        if plain:
            current = self.node('FILTER', 'Filter ' + ' AND '.join(grouped(c) for c in plain), [current])
        for c in special:
            negated = isinstance(c, exp.Not)
            target = c.this if negated else c
            if isinstance(target, exp.Exists) or (isinstance(target, exp.In) and target.args.get('query')):
                sub = target.this if isinstance(target, exp.Exists) else target.args['query']
                sub_plan = self.query(sub.this if isinstance(sub, exp.Subquery) else sub, env)
                key = target.this.sql() if isinstance(target, exp.In) else 'EXISTS'
                current = self.node('ANTI_JOIN' if negated else 'SEMI_JOIN', f"{'Anti' if negated else 'Semi'}-join on {key}", [current, sub_plan])
                continue
            calls = self.calls_in(c)
            if len(calls) == 1 and calls[0][1][0] == 'SEM_FILTER' and (c is calls[0][0] or c == calls[0][0]):
                current = self.node('SEM_FILTER', calls[0][1][1], [current] + self.context_plans(calls[0][1], env))  # result is the row set, no name
                continue
            scalars = [self.semantic_node('SEM_AGG', call, info, self.context_plans(info, env))
                       for call, info in calls if info[0] == 'SEM_AGG' and self.context_plans(info, env)]
            current = self.apply_semantic(current, c, env, skip_scalars=True)
            subs = [self.query(q.this, env) for q in c.find_all(exp.Subquery)]
            current = self.node('FILTER', 'Filter ' + grouped(c), [current] + scalars + subs)
        return current


def plan_sql(sql, dialect, cte_refs=False):
    """Return (nodes, edges, root) for a SQL script; the last SELECT is the query, earlier statements define tables."""
    text = dialect.prepare(sql) if dialect.prepare else sql
    plan = Plan(dialect, cte_refs)
    env, root = {}, None
    lone = re.fullmatch(r'\s*blendsql_ingredient\((\d+)\)\s*;?\s*', text)
    if lone:  # a whole script that is one ingredient wrapping a query
        inner = dialect.ingredients[int(lone.group(1))]
        body = re.search(r'\(\s*\(\s*(.*)\)\s*\)\s*$', inner, re.S) or re.search(r'\(\s*(.*)\)\s*$', inner, re.S)
        query = plan.query(sqlglot.parse_one(body.group(1), read=dialect.read), env)
        root = plan.node('COMPUTE', inner.split('(', 1)[0].strip() + ' (non-LLM ingredient over the query)', [query])
        return plan.nodes, plan.edges, root
    for statement in sqlglot.parse(text, read=dialect.read):
        if statement is None:
            continue
        if isinstance(statement, exp.Create):
            target = statement.this.this if isinstance(statement.this, exp.Schema) else statement.this
            name = target.name.lower()
            body = statement.expression
            env[name] = plan.query(body, env) if body is not None else plan.node('SCAN', f'Scan {target.sql()} (created in script)')
        elif isinstance(statement, (exp.Insert, exp.Drop)):
            continue
        elif isinstance(statement, (exp.Select, exp.Union, exp.Intersect, exp.Except, exp.Subquery)):
            root = plan.query(statement, env)
    if root is None:
        raise ValueError('No query statement')
    reachable, stack = set(), [root]
    children = {}
    for e in plan.edges:
        children.setdefault(e['parent_id'], []).append(e['child_id'])
    while stack:
        n = stack.pop()
        if n not in reachable:
            reachable.add(n)
            stack.extend(children.get(n, []))
    nodes = [n for n in plan.nodes if n['node_id'] in reachable]
    edges = [e for e in plan.edges if e['parent_id'] in reachable]
    return nodes, edges, root
