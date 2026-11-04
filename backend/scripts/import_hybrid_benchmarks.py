"""Import query sets from pinned semantic-operator benchmark repositories as reference tasks.

Usage: python3 backend/scripts/import_hybrid_benchmarks.py <directory holding SWAN, SEMA-SQL, SemCEB, caesura checkouts>

Only query definitions are copied (into query/source-snapshots); databases and model outputs are not.
No logical DAG is reconstructed: each record keeps the upstream text and program verbatim.
"""
import ast
import csv
import hashlib
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'backend' / 'atlas'))
sys.path.insert(0, str(ROOT / 'backend' / 'scripts'))
from workload_import import canonical_url
from sql_plans import plan_sql, swan_dialect, plop_dialect, blendsql_dialect  # needs sqlglot==30.22.0
from code_plans import eleet_plan, semceb_plan
from reference_plans import ReferencePlan, dag_mixed_label as mixed_of

MANUAL = ROOT / 'query/manual-plans'


def manual_label(op, label):
    """Joins name their condition, not the DSL's binding aliases (long labels are shortened by display_label)."""
    join = re.match(r'(SEM_)?JOIN\((.*)\)$', label, re.S)
    if join:
        body = re.sub(r'^\s*(left|cross)\s*,\s*', '', join.group(2))
        body = re.sub(r'\b(left|right|join_type)\s*=\s*\w+\s*,?\s*', '', body).strip(' ,')
        name = {'LEFT_JOIN': 'LEFT JOIN', 'CROSS_JOIN': 'CROSS JOIN', 'JOIN': 'JOIN'}.get(op, op)
        label = f"{name} {body}" if body else name
    return label


def manual_plans(name):
    """Hand reconstructions {query_id: (nodes, edges, root, basis)} written in the reference plan notation."""
    path = MANUAL / f'{name}.json'
    if not path.exists():
        return {}
    return {row['query_id']: parse_manual(row['query_id'], row['plan'], row['basis']) for row in json.loads(path.read_text())}


def parse_manual(qid, text, basis):
    plan = ReferencePlan(qid, set(FAMILIES))
    root = plan.parse(text)
    strip = lambda rows: [{k: v for k, v in r.items() if k != 'query_id'} for r in rows]
    labels = {n['node_id']: manual_label(n['operator_type'], n['label']) for n in plan.nodes}
    # A join condition names its inputs by their DSL binding (t.kind_id); tag only bindings some label refers to.
    referenced = {name: node for name, node in plan.bindings.items()
                  if any(re.search(rf'\b{re.escape(name)}\.', text) for text in labels.values())}
    alias = {node: name for name, node in referenced.items()}
    nodes = [dict(n, label=labels[n['node_id']] + (f" [as {alias[n['node_id']]}]" if n['node_id'] in alias else ''))
             for n in strip(plan.nodes)]
    return nodes, strip(plan.edges), root, basis, text


def caesura_samples(source):
    """The paper's queries come from sample_queries() in run_experiment.py: for each dataset in order, every template's
    slot-value combinations, sampled 2 per template by one numpy Generator (seed 42), forbidden_queries empty at this
    commit. The upstream code is not run: templates and value lists are read as literals and the sampling is repeated here."""
    import itertools
    import numpy as np
    tree = ast.parse(source)
    functions = {f.name: f for f in tree.body if isinstance(f, ast.FunctionDef)}
    rng = np.random.default_rng(seed=42)
    samples = []
    for dataset in ('artwork', 'rotowire'):
        body = functions[f'query_templates_{dataset}'].body
        table = next(n.value for n in body if isinstance(n, ast.Assign) and getattr(n.targets[0], 'id', '') == 'template_values')
        values = {k.arg: ast.literal_eval(k.value) for k in table.keywords}  # template_values = dict(name=[...], ...)
        if dataset == 'artwork':  # template_values["genre_slash_century"] = template_values["century"] + template_values["genre"]
            values['genre_slash_century'] = values['century'] + values['genre']
        calls = [c for c in ast.walk(functions[f'query_templates_{dataset}']) if isinstance(c, ast.Call) and getattr(c.func, 'id', '') == 'Template']
        for call in sorted(calls, key=lambda c: (c.lineno, c.col_offset)):
            template = call.args[0].value
            slots = re.findall(r'{([^}]+)}', template)
            options = []
            for combo in itertools.product(*[values[slot.split(' ')[0]] for slot in slots]):
                text = template
                for slot, value in zip(slots, combo):
                    text = text.replace('{' + slot + '}', value)
                options.append((text, dict(zip(slots, combo))))
            for i in rng.choice(len(options), min(2, len(options)), replace=False):
                samples.append(dict(dataset=dataset, line=call.lineno, template=template, query=options[i][0], values=options[i][1]))
    return samples


def caesura_instance(plan, values):
    """Fill a template plan's slots; where the template plan names alternatives, keep the one the value selects."""
    v = values.get
    order = lambda first: 'ASC' if first else 'DESC'
    rules = [
        (r"FILTER\(\{religious_artwork\}: genre/movement match, no filter for 'painting'\) -> ",
         lambda: '' if v('religious_artwork') == 'painting' else f"FILTER(genre or movement is {v('religious_artwork')}) -> "),
        (r"COMPUTE\(derive \{genre_slash_century\}: century/year from inception, or use genre/movement column\) -> ",
         lambda: f"COMPUTE({v('genre_slash_century')} of inception) -> " if v('genre_slash_century') in ('century', 'year') else ''),
        (r"COMPUTE\(\{century\} of inception\)", lambda: f"COMPUTE({v('century')} of inception)"),
        (r"SORT\(inception \{oldest\}\)", lambda: f"SORT(inception {order(v('oldest') == 'oldest')})"),
        (r"row with \{oldest\} (inception|birth_date|founded)",
         lambda: None),  # handled below with the matched column
        (r"SORT\(founded \{oldest\}\)", lambda: f"SORT(founded {order(v('oldest') == 'oldest')})"),
        (r"SORT\(\{tallest\}: height or birth_date\)",
         lambda: {'tallest': 'SORT(height DESC)', 'smallest': 'SORT(height ASC)', 'oldest': 'SORT(birth_date ASC)', 'youngest': 'SORT(birth_date DESC)'}[v('tallest')]),
        (r"row with \{tallest\} height/birth_date",
         lambda: {'tallest': 'row with max height', 'smallest': 'row with min height', 'oldest': 'row with earliest birth_date', 'youngest': 'row with latest birth_date'}[v('tallest')]),
        (r"COMPUTE\(\{age_player\}: age from birth_date, or height\) -> ", lambda: 'COMPUTE(age from birth_date) -> ' if v('age_player') == 'age' else ''),
        (r"\{age_team\}: age from founded", lambda: 'age from founded'),
        (r"FILTER\(conference/division = \{eastern_conference\}\)",
         lambda: f"FILTER({'conference' if 'conference' in v('eastern_conference') else 'division'} = '{v('eastern_conference').split()[0]}')"),
        (r"SORT\((num_\{\w+\}|value) \{highest\}\)", lambda: None),
        (r"\{highest\}\(", lambda: 'MAX(' if v('highest') == 'highest' else 'MIN('),
    ]
    for pattern, replace in rules:
        if pattern.startswith('row with \\{oldest'):
            plan = re.sub(pattern, lambda m: f"row with {'earliest' if v('oldest') == 'oldest' else 'latest'} {m.group(1)}", plan)
        elif pattern.startswith('SORT\\((num_'):
            plan = re.sub(pattern, lambda m: f"SORT({m.group(1)} {'DESC' if v('highest') == 'highest' else 'ASC'})", plan)
        else:
            plan = re.sub(pattern, lambda m: replace(), plan)
    plan = re.sub(r'num_\{(\w+)\}', lambda m: 'num_' + values[m.group(1)].replace(' ', '_'), plan)
    plan = re.sub(r'\{(\w+)\}', lambda m: values[m.group(1)], plan)
    assert '{' not in plan, plan
    return plan

# Q26 reuses two CTEs inside another CTE and the main query; that shared-node DAG has no crossing-free
# layered layout, so its reuses are drawn as CTE_REF leaves (repo convention, see sembench/cars/Q6).
CTE_REF_QUERIES = {26}
FAMILIES = {o['operator_type']: o['family'] for o in json.loads((ROOT / 'config/operators.json').read_text())}


CHECKED = '2026-11-03'
TABLES = ('queries', 'nodes', 'edges', 'sources', 'query_sources', 'task_details', 'input_contracts', 'original_queries')
REPOS = {
    'swan': ('ZhaoFuheng/SWAN', 'SWAN', '0ba4c936ae3a087a66037656894633081f880aa5'),
    'sema-sql': ('semasql/SEMA-SQL', 'SEMA-SQL', 'b4866921ad0843c73a6966aca0cdd89082da1cf1'),
    'semceb': ('utndatasystems/SemCEB', 'SemCEB', 'fec6bde7d1b23fc751f8701872fafda777a63942'),
    'caesura': ('DataManagementLab/caesura', 'caesura', '00ebb188bf9e83c36ad06e9504594a74f169a23c'),
    'plop': ('DMoRanSky/Morrila', 'Morrila', '56780d9623c4bcc3e95c722b3d7328bdedb161a5'),
    'blendsql': ('parkervg/blendsql', 'blendsql', '8a75abeca64b662aa8d1d7b5fdb52d3e31b052db'),
    'eleet': ('DataManagementLab/eleet', 'eleet', '4c2c70ae70fb91bd0899c2d79cb4cb141b0f503a'),
    'dataagentbench': ('ucbepic/DataAgentBench', 'DataAgentBench', 'ac11ab6854dec9e1add75720850b0c891e2ff6b5'),
}
PAPERS = {
    'swan': ('https://arxiv.org/abs/2408.00884', 'Hybrid Querying Over Relational Databases and Large Language Models', 'CIDR 2025'),
    'sema-sql': ('https://arxiv.org/abs/2604.23477', 'SEMA-SQL: Beyond Traditional Relational Querying with Large Language Models', 'arXiv 2026'),
    'semceb': ('https://arxiv.org/abs/2606.23081', 'SemCEB: A Cardinality Estimation Benchmark for Semantic Operators', 'arXiv 2026'),
    'caesura': ('https://arxiv.org/abs/2308.03424v1', 'CAESURA: Language Models as Multi-Modal Query Planners', 'arXiv 2023'),
    'plop': ('https://arxiv.org/abs/2604.09944', 'PLOP: Cost-Based Placement of Semantic Operators in Hybrid Query Plans', 'arXiv 2026'),
    'eleet': ('https://arxiv.org/abs/2410.22522', 'ELEET: Efficient Learned Query Execution over Text and Tables', 'PVLDB 2024'),
    'dataagentbench': ('https://arxiv.org/abs/2603.20576', 'Can AI Agents Answer Your Data Questions? A Benchmark for Data Agents', 'arXiv 2026'),
    'blendsql': ('https://arxiv.org/abs/2402.17882', 'BlendSQL: A Scalable Dialect for Unifying Hybrid Question Answering in Relational Algebra', 'arXiv 2024'),
}
AI_CALL = re.compile(r'\bai_(filter|classify|complete|agg)\s*\(', re.I)
RELATIONAL = re.compile(r'\b(JOIN|GROUP\s+BY|ORDER\s+BY|COUNT|SUM|AVG|MIN|MAX|DISTINCT|UNION|INTERSECT|EXCEPT|HAVING)\b|\bWHERE\b[^;]*?(=|<|>|\bLIKE\b|\bIN\b)', re.I | re.S)


SEMANTIC_CALL = {
    'swan': AI_CALL,
    'plop': re.compile(r'\bsemantic(_int|_string|_double)?\s*\(', re.I),
    'blendsql': re.compile(r'\{\{.*?\}\}', re.S),
}


def mixed_label(bench, sql):
    """实质混合 when relational clauses remain after removing comments, setup statements and semantic calls."""
    body = re.sub(r'--[^\n]*', '', sql)
    statements = [st for st in body.split(';') if st.strip() and not re.match(r'\s*(CREATE|DROP|INSERT)\b', st, re.I)]
    stripped = SEMANTIC_CALL[bench].sub('', ' ; '.join(statements))
    return '实质混合' if RELATIONAL.search(stripped) else '轻混合（仅投影）'


# Q25 repeats Q15's question word for word upstream; only the semantic prompts differ.
PLOP_TITLE_SUFFIX = {25: ' (same question as Q15, different prompt wording)'}
# Q21-Q24 ask for an aggregate or a top-k, but the upstream SQL only returns sorted detail rows.
PLOP_NOTES = {n: '题目要求聚合或取前几名，上游 SQL 只返回按评分/时间排序的明细行，没有聚合或 LIMIT；图按 SQL。' for n in (21, 22, 23, 24)}

# BlendSQL publishes queries without questions: one-line summaries written from each query's SQL.
# "(no LLM)" marks the financials queries, which use only deterministic test ingredients.
BLENDSQL_TITLES = {
    '1966_nba_draft/q01': 'Former Knicks players with over a year of NBA experience who played more than one position',
    '1966_nba_draft/q02': 'Players matched to their Wikipedia page who stayed more than 5 years with the franchise',
    'financials/q01': "Regional exposure of IT-sector holdings whose description starts with 'A' (no LLM)",
    'financials/q02': "Dividend payouts from IT companies whose name starts with 'A' (no LLM)",
    'financials/q03': "Dividend payouts from IT companies whose name starts with 'A', unqualified columns (no LLM)",
    'financials/q04': 'Shortest-named held stock with account activity after 2021-02-23 (no LLM)',
    'financials/q05': 'Shortest-named held stock with account activity after 2021-02-23, unqualified columns (no LLM)',
    'financials/q06': "Number of distinct portfolio rows whose symbol starts with 'F' and is longer than 2 characters (no LLM)",
    'financials/q07': "Account share of small 'F' holdings joined to their regional breakdown (no LLM)",
    'national_parks/q01': "Largest park in Alaska, with an image caption and its size in km²",
    'national_parks/q02': 'Parks whose description shows no park facilities',
    'national_parks/q03': 'Location of the park that protects an ash flow',
    'national_parks/q04': 'Number of parks that span more than one state',
    'national_parks/q05': 'Caption of one park image',
    'rugby/q01': 'Games played in the city 120 miles west of Sydney',
    'rugby/q02': 'Sydney venues of games with more than 30 total points',
    'rugby/q03': 'Games against the NSW Waratahs, with the rival team description',
    'rugby/q04': 'Rivals played in the city with the Mount Panorama racetrack',
}


def plan_title(prefix, plan, skip=('SCAN', 'PROJECT', 'DISTINCT')):
    """A readable title for queries published without a question: the plan's operators bottom-up."""
    labels = [n['label'].split(': extract', 1)[0] for n in plan[0] if n['operator_type'] not in skip]
    return prefix + ' → '.join(labels)


ELEET_PHRASES = [  # operator labels as short phrases for titles, in plan order (inputs first)
    (r'^MMScan$', 'extract rows from text'), (r'^MMJoin on (.+)$', r'join text on \1'), (r'^MMUnion$', 'union table and text rows'),
    (r'^MMSelection on (.+?) \(selectivity (.+?)\).*$', r'text filter on \1 (sel. \2)'),
    (r'^MMAggregation: group text reports by extracted (.+)$', r'group text by \1'),
    (r'^Join on (.+)$', r'join on \1'), (r'^Selection on (.+?) \(selectivity (.+?)\)$', r'filter \1 (sel. \2)'),
    (r'^Project (.+)$', r'project \1')]


def eleet_title(dataset, plan):
    """Text collection read, then what the plan does, as short phrases."""
    texts = sorted({n['label'].rsplit(' ', 1)[1] for n in plan[0] if n['label'].startswith('Scan text collection')})
    steps = []
    for n in plan[0]:
        if n['operator_type'] in ('SCAN', 'DISTINCT', 'UNION_ALL'):
            continue
        label = n['label'].split(': extract', 1)[0]
        for pattern, phrase in ELEET_PHRASES:
            if re.match(pattern, label):
                label = re.sub(pattern, phrase, label)
                break
        steps.append(label)
    return f"{dataset} · {', '.join(texts)}: " + ' → '.join(steps)


def template_title(text):
    """SemCEB filters embed prompt slots ('{review_text}'). Later sentences that carry slots are input lists and are
    dropped; in the first sentence, cut at the colon that introduces the slots, else remove inline slots."""
    sentences = re.split(r'(?<=[.?!])\s+', text.strip())
    first = sentences[0]
    if '{' in first:
        colon = first.find(':', 0, first.index('{'))
        first = first[:colon] if colon > 0 else re.sub(r"\s*'?\{[^}]*\}'?", '', first)
    kept = [first] + [x for x in sentences[1:] if '{' not in x and not x.rstrip().endswith(':')]
    return re.sub(r'\s+', ' ', ' '.join(kept)).strip(' :-,') or text


def sha(data):
    return hashlib.sha256(data if isinstance(data, bytes) else data.encode()).hexdigest()


def sid(text):
    return 'src_' + sha(text)[:16]


def paper_source_id(url):
    # Same identity scheme as LiteratureCatalog, so paper page ids stay stable.
    return 'lit_' + sha(canonical_url(url))[:12]


def read_jsonl(name):
    return [json.loads(l) for l in (ROOT / 'query' / f'{name}.jsonl').read_text().splitlines() if l.strip()]


def write_json(rel, value):
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')


class Importer:
    def __init__(self, checkouts):
        self.checkouts = Path(checkouts)
        self.tables = {n: read_jsonl(n) for n in TABLES}
        self.prefixes = tuple(f'{b}/' for b in REPOS)
        own = {paper_source_id(url) for url, _, _ in PAPERS.values()}
        for name in TABLES:
            self.tables[name] = [r for r in self.tables[name] if not r.get('query_id', '').startswith(self.prefixes)
                                 and not r.get('source_id', '').startswith('hyb_') and r.get('source_id') not in own]
        self.catalog = json.loads((ROOT / 'config/catalog.json').read_text())
        self.catalog['scenarios'] = [s for s in self.catalog['scenarios'] if not s.startswith(tuple(f'files/{b}/' for b in REPOS))]
        self.order = max(q['display_order'] for q in self.tables['queries']) + 1
        self.scenarios = {}
        self.manual = {name: manual_plans(name) for name in ('tag-plus', 'dataagentbench')}
        self.manual_raw = {'caesura': {r['query_id']: r for r in json.loads((MANUAL / 'caesura.json').read_text())}}  # template plans, instantiated per sample

    # Sources -------------------------------------------------------------
    def snapshot(self, bench, relpath):
        repo, folder, commit = REPOS[bench]
        checkout = self.checkouts / folder
        head = subprocess.run(['git', '-C', str(checkout), 'rev-parse', 'HEAD'], capture_output=True, text=True, check=True).stdout.strip()
        if head != commit:
            raise SystemExit(f'{folder} is at {head}, expected {commit}')
        target = ROOT / 'query/source-snapshots' / repo / commit / relpath
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(checkout / relpath, target)
        rel = target.relative_to(ROOT).as_posix()
        source_id = 'hyb_' + sha(rel)[:16]
        if not any(s['source_id'] == source_id for s in self.tables['sources']):
            self.tables['sources'].append(dict(source_id=source_id, location=rel, title=f'{repo}/{relpath}', source_type='task_definition',
                                               version=commit, verification='Copied from pinned upstream commit', checked_on=CHECKED,
                                               publication_label='', publication_url=f'https://github.com/{repo}/blob/{commit}/{relpath}'))
        return source_id, target

    def paper(self, bench):
        url, title, label = PAPERS[bench]
        source_id = paper_source_id(url)
        if not any(s['source_id'] == source_id for s in self.tables['sources']):
            self.tables['sources'].append(dict(source_id=source_id, location=url, title=title, source_type='paper', version=label,
                                               verification='arXiv abstract page checked', checked_on=CHECKED,
                                               publication_label=label.replace(' ', ''), publication_url=f'https://github.com/{REPOS[bench][0]}'))
        return source_id

    def dataset(self, url, title):
        source_id = 'hyb_' + sha(url)[:16]
        if not any(s['source_id'] == source_id for s in self.tables['sources']):
            self.tables['sources'].append(dict(source_id=source_id, location=url, title=title, source_type='dataset', version='not downloaded',
                                               verification='Named by the benchmark repository; data not copied', checked_on=CHECKED,
                                               publication_label='', publication_url=url))
        return source_id

    def scenario(self, bench, scenario_id, name, engine, data_source, schema, note):
        if scenario_id in self.scenarios:
            return
        self.scenarios[scenario_id] = name
        write_json(f'environment/{scenario_id}/manifest.json', dict(
            environment_id=scenario_id, dataset_id=scenario_id, runtime_status='unconfigured', engine=engine, model=None, hardware=None,
            execution_status='not_executed', record_batch_size=None, query_batch=None, model_batch_size=None, concurrency=None, resources=[]))
        write_json(f'data/{scenario_id}/manifest.json', dict(
            dataset_id=scenario_id, source_ids=[data_source], availability='not_downloaded', local_path=None, schema=schema,
            record_count=None, version=REPOS[bench][2], file_count=None, total_bytes=None, inventory_path=None, verification=note))

    # Records -------------------------------------------------------------
    def add(self, bench, scenario_id, source_query_id, text, selector, source, path, paper, data_source, collection, category,
            programs, gold, contract_tables, notes, mixed_label='', semop_count=None, evidence_locator='', kind='natural_language',
            plan=None, title=None, manual=None, note=''):
        qid = f'{scenario_id}/{source_query_id}'
        manual_plan = (manual or {}).get(qid)
        if manual_plan is not None:
            plan = manual_plan[:3]
            notes = notes + [f'人工重建依据：{manual_plan[3]}']
            programs = programs + [dict(type='manual_plan', program=manual_plan[4],
                                        note='Hand reconstruction from the question and the schema; not an upstream plan.')]
        if plan is not None:
            nodes, edges, root = plan
            for n in nodes:
                if n['operator_type'] not in FAMILIES:
                    raise ValueError(f'{qid}: unknown operator {n["operator_type"]}')
            self.tables['nodes'].extend(dict(query_id=qid, **n) for n in nodes)
            self.tables['edges'].extend(dict(query_id=qid, **e) for e in edges)
            mixed_label = mixed_of([n['operator_type'] for n in nodes], FAMILIES)
            semop_count = sum(FAMILIES[n['operator_type']] == 'semantic' for n in nodes)
        raw = path.read_bytes()
        rel = path.relative_to(ROOT).as_posix()
        self.tables['queries'].append(dict(
            query_id=qid, benchmark_id=bench, scenario_id=scenario_id, source_query_id=source_query_id, title=(title or text).strip(),
            plan_origin='end_to_end_interpretation' if manual_plan else 'source_reconstruction' if plan else 'supplied_reference',
            plan_status_label=('人工依据问题与 schema 重建的逻辑计划（非上游计划）' if manual_plan else
                               '由上游源码自动转换的逻辑计划' if plan else '上游查询原文（未重建逻辑计划）'),
            source_id=source, root_node_id=plan[2] if plan else None,
            notes=f'人工重建依据：{manual_plan[3]}' if manual_plan else note, display_order=self.order, group_label=collection, mixed_label=mixed_label, environment_id=scenario_id,
            plan_format='logical_dag' if plan else 'reference_program', collection_label=collection, category_label=category))
        self.order += 1
        note = 'Query text and program copied verbatim from the pinned upstream commit; no plan reconstructed or executed.'
        for source_id, role, relationship in [(source, 'task_definition', 'query_source'), (paper, 'paper', 'query_source'), (data_source, 'dataset', 'dataset_origin')]:
            self.tables['query_sources'].append(dict(query_id=qid, source_id=source_id, role=role, locator=evidence_locator or rel,
                                                     attribution_note=note, relationship=relationship, evidence_paths=[rel]))
        self.tables['original_queries'].append(dict(query_id=qid, text=text, kind=kind, language='en', verification='upstream_original',
                                                    upstream_comparison=None, source_path=rel, source_sha256=sha(raw), text_sha256=sha(text), selector=selector))
        self.tables['task_details'].append(dict(query_id=qid, reference_programs=programs,
                                                gold=gold or dict(gold_answer=None, answer_schema=None),
                                                evaluation=dict(primary_metric=None), annotation={} if semop_count is None else dict(semop_count=semop_count)))
        repo, _, commit = REPOS[bench]
        self.tables['input_contracts'].append(dict(
            query_id=qid, environment=dict(requirement='unspecified', resources=[]), tables=contract_tables, output=None,
            evidence=dict(path=rel, url=f'https://github.com/{repo}/blob/{commit}/{path.relative_to(ROOT / "query/source-snapshots" / repo / commit).as_posix()}',
                          locator=evidence_locator, sha256=sha(raw), excerpt=text.strip()),
            notes=notes, audit_status='source_checked'))

    # Benchmarks ----------------------------------------------------------
    def swan(self):
        paper = self.paper('swan')
        data = self.dataset('https://bird-bench.github.io/', 'BIRD databases (SWAN masks selected columns)')
        self.snapshot('swan', 'data/masked_columns.json')
        self.snapshot('swan', 'data/swan2.json')
        for db in ('california_schools', 'superhero', 'formula_1', 'european_football_2'):
            source, path = self.snapshot('swan', f'data/questions/{db}.csv')
            scenario_id = f'swan/{db}'
            self.scenario('swan', scenario_id, f'SWAN 2.0 · {db}', 'SWAN-AISQL (DuckDB aisql)', data,
                          [dict(name=db, type='database', description='BIRD database with masked columns')],
                          'BIRD database named by SWAN; masked columns in data/masked_columns.json snapshot; not downloaded')
            for row in csv.DictReader(path.read_text().splitlines(keepends=True)):
                _, aisql_path = self.snapshot('swan', f'queries/aisql/{row["qid"]}.sql')
                _, oracle_path = self.snapshot('swan', f'queries/oracle/{row["qid"]}.sql')
                aisql, oracle = aisql_path.read_text(), oracle_path.read_text()
                calls = len(AI_CALL.findall(aisql))
                mixed = mixed_label('swan', aisql)
                plan = plan_sql(aisql, swan_dialect())
                programs = [dict(type='aisql', program=aisql, source=aisql_path.relative_to(ROOT).as_posix()),
                            dict(type='sql_oracle', program=oracle, source=oracle_path.relative_to(ROOT).as_posix(),
                                 note='Oracle query over the unmasked database; used to compute gold answers')]
                gold = dict(gold_answer=None, answer_schema=None, gold_sql=row['gold_sql'], note='BIRD gold SQL from the question file')
                self.add('swan', scenario_id, row['qid'], row['question'], dict(type='csv_row', id_field='qid', id=row['qid'], field='question'),
                         source, path, paper, data, 'SWAN 2.0', db, programs, gold,
                         [dict(name=db, columns=[], passed_columns=[], row_unit='record', scope='database')],
                         [f'BIRD evidence: {row["evidence"]}', f'difficulty={row["difficulty"]}; shape={row["shape"]}',
                          f'{calls} AI calls in the AISQL query. The logical DAG is converted automatically from the AISQL (backend/scripts/sql_plans.py); the mixed label follows the DAG.'],
                         mixed, calls, f'qid={row["qid"]}', plan=plan)

    def tag_plus(self):
        paper = self.paper('sema-sql')
        data = self.dataset('https://bird-bench.github.io/', 'BIRD databases (SWAN masks selected columns)')
        source, path = self.snapshot('sema-sql', 'data/queries/tag_plus_queries.csv')
        scenario_id = 'sema-sql/tag-plus'
        self.scenario('sema-sql', scenario_id, 'SEMA-SQL TAG+', 'SEMA-SQL', data,
                      [dict(name='BIRD MINIDEV databases', type='database', description='Named per query in the DB used column')],
                      'BIRD MINIDEV databases named by SEMA-SQL; not downloaded')
        for row in csv.DictReader(path.read_text().lstrip('﻿').splitlines(keepends=True)):
            q = row['Query ID']
            self.add('sema-sql', scenario_id, q, row['Query'], dict(type='csv_row', id_field='Query ID', id=q, field='Query'),
                     source, path, paper, data, 'SEMA-SQL TAG+', row['DB used'],
                     [dict(type='upstream_record', program=json.dumps(row, ensure_ascii=False, indent=2),
                           note='No reference program is published; this is the verbatim upstream CSV row, not a plan.')],
                     dict(gold_answer=row['answer'], answer_schema=None),
                     [dict(name=row['DB used'], columns=[], passed_columns=[], row_unit='record', scope='database')],
                     ['TAG+ is an additional query set published with SEMA-SQL; the repository gives the question and answer only, no reference program.'],
                     evidence_locator=f'Query ID={q}', manual=self.manual['tag-plus'])

    def semceb(self):
        paper = self.paper('semceb')
        data = self.dataset('https://github.com/utndatasystems/SemCEB/tree/fec6bde7d1b23fc751f8701872fafda777a63942/tools/amazon-reviews', 'SemCEB Amazon reviews/products dataset')
        source, path = self.snapshot('semceb', 'benchmark_queries/queries.jsonl')
        scenario_id = 'semceb/amazon-reviews'
        self.scenario('semceb', scenario_id, 'SemCEB', 'Cardinality estimation (no engine)', data,
                      [dict(name='amazon-reviews', type='table', description='Products and reviews with text and images')],
                      'Prepared by SemCEB tools/amazon-reviews; not downloaded')
        for line in path.read_text().splitlines():
            row = json.loads(line)
            program = {k: v for k, v in row.items() if k != 'embeddings'}
            self.add('semceb', scenario_id, str(row['id']), row['filter'], dict(type='jsonl_task', id_field='id', id=row['id'], field='filter'),
                     source, path, paper, data, 'SemCEB', row['type'],
                     [dict(type='semceb_query', program=json.dumps(program, ensure_ascii=False, indent=2), note='Query embeddings omitted here; kept in the snapshot')],
                     None, [dict(name=d, columns=[], passed_columns=[], row_unit='record', scope='used') for d in row['datasets']],
                     [f'category={", ".join(row["category"])}', 'Single semantic filter or join evaluated for cardinality estimation only.'],
                     '', 1, f'id={row["id"]}', plan=semceb_plan(row, template_title(row['filter'])), title=template_title(row['filter']))

    def caesura(self):
        paper = self.paper('caesura')
        source, path = self.snapshot('caesura', 'scripts/run_experiment.py')
        datasets = {'artwork': self.dataset('https://www.wikidata.org/', 'Wikidata paintings (CAESURA artwork database)'),
                    'rotowire': self.dataset('https://github.com/harvardnlp/boxscore-data', 'Rotowire box scores with Wikidata team/player tables')}
        code = path.read_text()
        templates = {c.lineno: c for c in ast.walk(ast.parse(code)) if isinstance(c, ast.Call) and getattr(c.func, 'id', None) == 'Template'}
        samples = caesura_samples(code)
        # The sampled queries are not a file upstream: keep them as a derived snapshot tied to the script's hash.
        derived = path.parent / 'run_experiment.sample_queries.json'
        tasks = []
        for sample in samples:
            k = sum(t['template_line'] == sample['line'] for t in tasks) + 1
            tasks.append(dict(id=f"{sample['dataset']}/L{sample['line']}-{k}", template_line=sample['line'], template=sample['template'],
                              query=sample['query'], values=sample['values']))
        derived.write_text(json.dumps(dict(source='scripts/run_experiment.py', source_sha256=sha(path.read_bytes()),
                                           method='sample_queries(): itertools.product of slot values, numpy default_rng(seed=42).choice 2 per template',
                                           tasks=tasks), indent=2, ensure_ascii=False) + '\n')
        rel = derived.relative_to(ROOT).as_posix()
        derived_source = 'hyb_' + sha(rel)[:16]
        self.tables['sources'].append(dict(source_id=derived_source, location=rel, title='CAESURA sampled queries (derived from run_experiment.py)',
                                           source_type='task_definition', version=REPOS['caesura'][2],
                                           verification='Sampling of the pinned run_experiment.py repeated from its literal templates and value lists; upstream code not executed',
                                           checked_on=CHECKED, publication_label='', publication_url=f"https://github.com/{REPOS['caesura'][0]}/blob/{REPOS['caesura'][2]}/scripts/run_experiment.py"))
        for task in tasks:
            call = templates[task['template_line']]
            _, multi, output, scenario = (ast.literal_eval(a) for a in call.args)
            scenario_id = f'caesura/{scenario}'
            self.scenario('caesura', scenario_id, f'CAESURA {scenario}', 'CAESURA', datasets[scenario],
                          [dict(name=scenario, type='database', description='Multi-modal database built by CAESURA scripts')],
                          'Built by CAESURA scripts from public sources; not downloaded')
            template_qid = f"{scenario_id}/L{task['template_line']}"
            template_plan = self.manual_raw['caesura'][template_qid]
            qid = f"caesura/{task['id']}"
            plan_text = caesura_instance(template_plan['plan'], task['values'])
            # The template's basis text speaks in slots; the instance note names the values its plan was fixed by.
            basis = f"模板 L{task['template_line']} 的采样实例，取值：{'；'.join(f'{k} → {v}' for k, v in task['values'].items())}。计划由人工模板计划按这些取值确定。"
            kind = ('multi-modal' if multi else 'single-table') + ' · ' + output
            self.add('caesura', scenario_id, task['id'].split('/', 1)[1], task['query'], dict(type='json_task', id_field='id', id=task['id'], field='query'),
                     derived_source, derived, paper, datasets[scenario], 'CAESURA', kind,
                     [dict(type='query_template', program=ast.get_source_segment(code, call))], None,
                     [dict(name=scenario, columns=[], passed_columns=[], row_unit='record', scope='database')],
                     ['One of the 48 queries the paper samples from 24 templates (sample_queries, numpy seed 42, 2 per template), regenerated from the pinned script; '
                      'the paper does not list its instances, so they are not checked against it.'],
                     evidence_locator=f"run_experiment.py line {task['template_line']}; sample_queries()",
                     manual={qid: parse_manual(qid, plan_text, basis)})

    def plop(self):
        paper = self.paper('plop')
        data = self.dataset('https://github.com/DMoRanSky/Morrila/tree/56780d9623c4bcc3e95c722b3d7328bdedb161a5/test/semantic/agent_bench/dataset',
                            'Morrila agent_bench datasets (book_review, googlelocal, stockindex, tpcds, tpch, yelp)')
        scenario_id = 'plop/agent-bench'
        self.scenario('plop', scenario_id, 'PLOP / Morrila agent_bench', 'Morrila (DuckDB fork)', data,
                      [dict(name='agent_bench datasets', type='files', description='CSV/Parquet files read by each query')],
                      'Datasets live in the Morrila repository; not copied')
        directory = self.checkouts / 'Morrila/test/semantic/agent_bench'
        for number in sorted((int(p.stem[1:]) for p in directory.glob('Q*.sql'))):
            source, path = self.snapshot('plop', f'test/semantic/agent_bench/Q{number}.sql')
            sql = path.read_text()
            question = next(l for l in sql.splitlines() if l.startswith('-- Question: '))[len('-- Question: '):].strip()
            tables = sorted(set(re.findall(r"dataset/([^'\\]+?)\.(?:csv|parquet)", sql)))
            if not tables:  # tables loaded outside the file: base relations named in FROM/JOIN, minus CTEs
                body = re.sub(r"'(?:[^']|'')*'", "''", re.sub(r'--[^\n]*', '', sql))
                ctes = set(re.findall(r'\b([A-Za-z_]\w*)\s+AS\s*\(', body, re.I))
                tables = sorted(set(re.findall(r'\b(?:FROM|JOIN)\s+([A-Za-z_][\w.]*)', body, re.I)) - ctes)
            calls = len(SEMANTIC_CALL['plop'].findall(sql))
            self.add('plop', scenario_id, f'Q{number}', question, dict(type='comment_line', prefix='-- Question: '),
                     source, path, paper, data, 'PLOP agent_bench', tables[0].split('/')[0] if tables else 'agent_bench',
                     [dict(type='sql', program=sql, source=path.relative_to(ROOT).as_posix())], None,
                     [dict(name=t, columns=[], passed_columns=[], row_unit='record', scope='used') for t in tables],
                     [f'{calls} semantic() calls; the 14 SemBench E-Commerce queries of the paper are the existing SemBench ecomm records.',
                      'The logical DAG is converted automatically from the SQL; setup statements define the scanned tables.'],
                     mixed_label('plop', sql), calls, f'Q{number}.sql', plan=plan_sql(sql, plop_dialect(), cte_refs=number in CTE_REF_QUERIES), title=re.sub(r'^(Projection Optimization Query \d+|[A-Za-z]+ Q\d+):\s*', '', question) + PLOP_TITLE_SUFFIX.get(number, ''), note=PLOP_NOTES.get(number, ''))

    def blendsql(self):
        paper = self.paper('blendsql')
        for directory in sorted((self.checkouts / 'blendsql/benchmark').iterdir()):
            if not directory.is_dir():
                continue
            name = directory.name
            data = self.dataset(f'https://github.com/parkervg/blendsql/tree/8a75abeca64b662aa8d1d7b5fdb52d3e31b052db/benchmark/{name}',
                                f'BlendSQL benchmark database {name}')
            scenario_id = f'blendsql/{name.replace("_", "-")}'
            self.scenario('blendsql', scenario_id, f'BlendSQL benchmark · {name}', 'BlendSQL', data,
                          [dict(name=name, type='database', description='Benchmark database named by the directory')],
                          'Database referenced by the BlendSQL benchmark directory; not copied')
            for query in sorted((directory / 'queries').glob('*.sql')):
                source, path = self.snapshot('blendsql', f'benchmark/{name}/queries/{query.name}')
                sql = path.read_text()
                calls = len(SEMANTIC_CALL['blendsql'].findall(sql))
                plan = plan_sql(sql, blendsql_dialect())
                title = BLENDSQL_TITLES[f'{name}/{query.stem}']
                self.add('blendsql', scenario_id, query.stem, sql, dict(type='text'),
                         source, path, paper, data, 'BlendSQL benchmark', name,
                         [dict(type='blendsql', program=sql, source=path.relative_to(ROOT).as_posix())], None,
                         [dict(name=name, columns=[], passed_columns=[], row_unit='record', scope='database')],
                         [f'{calls} ingredients ({{{{...}}}}); only LLMMap / LLMQA / LLMJoin / ImageCaption are semantic, test ingredients such as test_starts_with are deterministic functions.',
                          'No natural-language question is published; the title is a one-line summary written for this catalog, and the original text is the query. The logical DAG is converted automatically from the BlendSQL query.'],
                         mixed_label('blendsql', sql), calls, f'benchmark/{name}/queries/{query.name}', kind='sql',
                         plan=plan, title=title)

    def eleet(self):
        paper = self.paper('eleet')
        source, path = self.snapshot('eleet', 'eleet/benchmark.py')
        code = path.read_text()
        tree = ast.parse(code)
        for fn in tree.body:
            if not (isinstance(fn, ast.FunctionDef) and fn.name.startswith('get_') and fn.name.endswith('_queries') and fn.name != 'get_queries'):
                continue
            dataset = fn.name[len('get_'):-len('_queries')]
            data = self.dataset(f'https://github.com/DataManagementLab/eleet/tree/4c2c70ae70fb91bd0899c2d79cb4cb141b0f503a#{dataset}',
                                f'ELEET {dataset} dataset (tables plus text reports)')
            scenario_id = f'eleet/{dataset}'
            self.scenario('eleet', scenario_id, f'ELEET · {dataset}', 'ELEET', data,
                          [dict(name=dataset, type='database', description='Tables and text collections loaded by ELEET')],
                          'Dataset prepared by ELEET scripts; not downloaded')
            plans = {n.targets[0].id: ast.get_source_segment(code, n) for n in ast.walk(fn)
                     if isinstance(n, ast.Assign) and len(n.targets) == 1 and isinstance(n.targets[0], ast.Name)}
            ret = next(n for n in ast.walk(fn) if isinstance(n, ast.Return) and isinstance(n.value, ast.Tuple) and len(n.value.elts) == 3)
            values = {n.targets[0].id: n.value for n in ast.walk(fn)
                      if isinstance(n, ast.Assign) and len(n.targets) == 1 and isinstance(n.targets[0], ast.Name)}
            for index, item in enumerate(ret.value.elts[2].elts):
                segment = ast.get_source_segment(code, item)
                variants = [(None, item)]
                if isinstance(item, ast.Starred):
                    # (Query(q, ...) for q, proj in zip(union_projections, PROJECTIONS)): expand the list built by the loop
                    loop = next(n for n in ast.walk(fn) if isinstance(n, ast.For))
                    template = next(n for n in ast.walk(loop) if isinstance(n, ast.Call) and getattr(n.func, 'id', '') == 'MMUnion')
                    projections = ast.literal_eval(values[loop.iter.id])
                    variants = []
                    for k, projection in enumerate(projections):
                        tree = ast.parse(ast.unparse(template).replace(loop.target.id, repr(projection))).body[0].value
                        variants.append((k, tree))
                for k, expression in variants:
                    call = expression.value if isinstance(expression, ast.Starred) else expression
                    first = call.args[0] if isinstance(call, ast.Call) and getattr(call.func, 'id', '') == 'Query' and call.args else call
                    name = first.id if isinstance(first, ast.Name) else 'union_projection'
                    plan = eleet_plan(values, first)
                    program = '\n\n'.join(p for p in [plans.get(name) if k is None else ast.unparse(first), segment] if p)
                    suffix = f'{index:02d}-{name}' if k is None else f'{index:02d}-{name}-{k:02d}'
                    title = eleet_title(dataset, plan) + ('' if k is None else f' (projection {k + 1}/{len(variants)})')
                    self.add('eleet', scenario_id, suffix, segment, dict(type='python_return_item', function=fn.name, index=index),
                             source, path, paper, data, 'ELEET benchmark', dataset,
                             [dict(type='eleet_plan', program=program)], None,
                             [dict(name=dataset, columns=[], passed_columns=[], row_unit='record', scope='database')],
                             ['Query plan defined in code; no natural-language question. The logical DAG is converted from the operator objects (backend/scripts/code_plans.py).'] +
                             ([f'Expanded from the generator over PROJECTIONS; projection {k + 1} of {len(variants)}.'] if k is not None else []),
                             '', None, f'{fn.name} return item {index}', kind='python_plan', plan=plan, title=title)

    def dataagentbench(self, collected):
        """Only datasets absent from the 7-30 collection; those 54 queries keep their existing records."""
        paper = self.paper('dataagentbench')
        root = self.checkouts / 'DataAgentBench'
        manifest = (root / 'dataset_manifest.tsv').read_text().splitlines()
        for directory in sorted(root.glob('query_*')):
            name = directory.name[len('query_'):]
            queries = sorted(directory.glob('query*/query.json'), key=lambda p: int(p.parent.name[len('query'):]))
            if not queries or any(f'{directory.name}/{q.parent.name}' in collected for q in queries):
                continue
            files = [l.split('\t')[0] for l in manifest if l.startswith(directory.name + '/')]
            data = self.dataset(f'https://github.com/ucbepic/DataAgentBench/tree/ac11ab6854dec9e1add75720850b0c891e2ff6b5/{directory.name}',
                                f'DataAgentBench {name} databases')
            scenario_id = f'dataagentbench/{name.lower().replace("_", "-")}'
            _, description = self.snapshot('dataagentbench', f'{directory.name}/db_description.txt')
            self.scenario('dataagentbench', scenario_id, f'DataAgentBench · {name}', 'Data agent (no engine)', data,
                          [dict(name=f, type='file', description='Listed in dataset_manifest.tsv') for f in files],
                          'Databases listed in dataset_manifest.tsv and fetched by download.sh; not downloaded')
            for query in queries:
                number = query.parent.name
                source, path = self.snapshot('dataagentbench', f'{directory.name}/{number}/query.json')
                _, validator = self.snapshot('dataagentbench', f'{directory.name}/{number}/validate.py')
                _, truth = self.snapshot('dataagentbench', f'{directory.name}/{number}/ground_truth.csv')
                self.add('dataagentbench', scenario_id, number, json.loads(path.read_text()), dict(type='json_value'),
                         source, path, paper, data, 'DataAgentBench', name,
                         [dict(type='validator', program=validator.read_text(), source=validator.relative_to(ROOT).as_posix(),
                               note='Answer checker published with the query; DataAgentBench gives no reference plan.')],
                         dict(gold_answer=truth.read_text(), answer_schema=None, source_path=truth.relative_to(ROOT).as_posix()),
                         [dict(name=f.split('/')[-1], columns=[], passed_columns=[], row_unit='document' if f.endswith('.bson') else 'record', scope='database') for f in files],
                         [f'Database description: {description.relative_to(ROOT).as_posix()}',
                          'Dataset absent from the 7-30 DataAgentBench analysis; the other 54 queries are the existing 7-30/DAB records.'],
                         evidence_locator=f'{directory.name}/{number}/query.json', manual=self.manual['dataagentbench'])

    def finish(self):
        for scenario_id, name in self.scenarios.items():
            rel = f'files/{scenario_id}/scenario.json'
            write_json(rel, dict(id=scenario_id, name=name, query_ids=[q['query_id'] for q in self.tables['queries'] if q['scenario_id'] == scenario_id]))
            self.catalog['scenarios'].append(rel)
        self.catalog['source_commits'].update({folder: commit for _, folder, commit in REPOS.values()})
        for name in TABLES:
            (ROOT / 'query' / f'{name}.jsonl').write_text(''.join(json.dumps(r, ensure_ascii=False) + '\n' for r in self.tables[name]))
        write_json('config/catalog.json', self.catalog)
        counts = {b: sum(q['benchmark_id'] == b for q in self.tables['queries']) for b in REPOS}
        print(json.dumps(counts))


def main():
    importer = Importer(sys.argv[1])
    importer.swan()
    importer.tag_plus()
    importer.semceb()
    importer.caesura()
    importer.plop()
    importer.blendsql()
    importer.eleet()
    collected = {m.group(1) for r in importer.tables['task_details'] if r['query_id'].startswith('7-30/DAB/')
                 for m in [re.search(r'DataAgentBench/(query_[^/]+/query\d+)/query.json', json.dumps(r))] if m}
    importer.dataagentbench(collected)
    importer.finish()


if __name__ == '__main__':
    main()
