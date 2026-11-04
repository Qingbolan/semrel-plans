"""Import the ThalamusDB benchmark queries (55, logical DAGs) and the 16 MLSys-2025 LLM-SQL queries (reference records).

Usage: python3 backend/scripts/import_thalamus_mlsys.py
Inputs (already in the repository):
- query/source-snapshots/saehanjo/thalamusdb/<commit>/{benchmark.py,nldbs.py,README.md} copied from the pinned commit, and
  benchmark.expanded.json: the 55 SQL strings produced by benchmark.py's query generators, expanded in order.
- query/source-snapshots/arxiv/2403.05821v2/queries.json: verbatim transcription of the paper's queries (no public code).
Only rows with the thalamusdb/ and mlsys-llmsql/ prefixes (and their thm_ sources) are replaced on re-run.
No data is copied and nothing is executed.
"""
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CHECKED = '2026-11-03'
COMMIT = 'c17a1ea7c8a3bca1fba13537002e99ba00a3e130'
THAL_DIR = f'query/source-snapshots/saehanjo/thalamusdb/{COMMIT}'
THAL_BLOB = f'https://github.com/saehanjo/thalamusdb/blob/{COMMIT}'
MLSYS_FILE = 'query/source-snapshots/arxiv/2403.05821v2/queries.json'
THAL_PAPER, MLSYS_PAPER = 'swb_2da9ce74a4218a0a', 'swb_7748082aec82fe14'  # existing paper records
PREFIXES = ('thalamusdb/', 'mlsys-llmsql/')
TABLES = ('queries', 'nodes', 'edges', 'sources', 'query_sources', 'task_details', 'input_contracts', 'original_queries')
CONTENT = json.loads((ROOT / 'config/content-en.json').read_text())
EN = {}  # new Chinese -> English entries


def sha(data):
    return hashlib.sha256(data if isinstance(data, bytes) else data.encode()).hexdigest()


def zh(text, en):
    if CONTENT.get(text, en) != en or EN.get(text, en) != en:
        raise ValueError('conflicting translation: ' + text)
    if text not in CONTENT:
        EN[text] = en
    return text


def read(name):
    return [json.loads(l) for l in (ROOT / 'query' / f'{name}.jsonl').read_text().splitlines() if l.strip()]


def write_json(rel, value):
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')


class Importer:
    def __init__(self):
        self.t = {n: [r for r in read(n) if not r.get('query_id', '').startswith(PREFIXES) and not r.get('source_id', '').startswith('thm_')]
                  for n in TABLES}
        # sources rows carry no query_id; drop only our own source ids from that table.
        self.order = max(q['display_order'] for q in self.t['queries']) + 1
        self.scenarios = {}

    def source(self, key, location, title, source_type, version, verification, publication_url=''):
        source_id = 'thm_' + sha(key)[:16]
        if not any(s['source_id'] == source_id for s in self.t['sources']):
            self.t['sources'].append(dict(source_id=source_id, location=location, title=title, source_type=source_type, version=version,
                                          verification=verification, checked_on=CHECKED, publication_label='', publication_url=publication_url))
        return source_id

    def scenario(self, scenario_id, name, engine, data_source, schema, version, note):
        self.scenarios[scenario_id] = name
        write_json(f'environment/{scenario_id}/manifest.json', dict(
            environment_id=scenario_id, dataset_id=scenario_id, runtime_status='unconfigured', engine=engine, model=None, hardware=None,
            execution_status='not_executed', record_batch_size=None, query_batch=None, model_batch_size=None, concurrency=None, resources=[]))
        write_json(f'data/{scenario_id}/manifest.json', dict(
            dataset_id=scenario_id, source_ids=[data_source], availability='not_downloaded', local_path=None, schema=schema,
            record_count=None, version=version, file_count=None, total_bytes=None, inventory_path=None, verification=note))

    def query(self, **row):
        defaults = dict(notes='', collection_label='', category_label='')
        self.t['queries'].append({**defaults, **row, 'display_order': self.order})
        self.order += 1

    # ThalamusDB ------------------------------------------------------------
    NL = {  # nl column -> (table, passed text column, zh, en)
        'img': ('images', 'img', '图片符合', 'image matches'),
        'title_u': ('furniture', 'title', '标题涉及', 'title about'),
        'audio': ('youtube', 'audio', '音频含', 'audio contains'),
        'description_u': ('youtube', 'description', '描述涉及', 'description about'),
        'featured_review_u': ('movies', 'featured_review', '精选影评为', 'featured review is'),
    }
    DATASETS = {
        'craigslist': ('Craigslist 家具', 'Craigslist furniture', ['craigslist/furnitures.csv', 'craigslist/imgs.csv'],
                       {'images': [('img', 'image'), ('aid', None)], 'furniture': [('aid', None), ('title', 'string'), ('price', None)]},
                       '家具帖 CSV 在上游仓库；图片文件需按 README 另行下载（186 MB）。'),
        'youtube': ('YouTube 音频', 'YouTube audio', ['audiocaps/youtube.csv'],
                    {'youtube': [('audio', 'audio'), ('description', 'string'), ('likes', None)]},
                    'youtube.csv 在上游仓库；AudioCaps 原始波形需另行下载（32.26 GB）。'),
        'netflix': ('Netflix 电影', 'Netflix movies', ['netflix/movies_with_reviews.csv'],
                    {'movies': [('movieid', None), ('featured_review', 'string')], 'ratings': [('movieid', None), ('rating', None)]},
                    'movies_with_reviews.csv 在上游仓库；评分 CSV 需按 README 另行下载（2.71 GB）。'),
    }

    def thalamus(self):
        bench = ROOT / THAL_DIR / 'benchmark.py'
        expanded_path = ROOT / THAL_DIR / 'benchmark.expanded.json'
        expanded = json.loads(expanded_path.read_text())
        assert expanded['source_sha256'] == sha(bench.read_bytes())
        definition = self.source(THAL_DIR + '/benchmark.py', THAL_DIR + '/benchmark.py', 'saehanjo/thalamusdb benchmark.py', 'task_definition',
                                 COMMIT, 'Copied from pinned upstream commit; queries expanded from its generator functions', f'{THAL_BLOB}/benchmark.py')
        lines = bench.read_text().splitlines()
        counts = {}
        for task in expanded['tasks']:
            ds = task['dataset']
            zh_name, en_name, csvs, schema, data_note = self.DATASETS[ds]
            scenario_id = f'thalamusdb/{ds}'
            if scenario_id not in self.scenarios:
                data = self.source('thalamusdb-data/' + ds, f'https://github.com/saehanjo/thalamusdb/tree/{COMMIT}/{csvs[0].split("/")[0]}',
                                   f'ThalamusDB {en_name} data', 'dataset', COMMIT, 'Named by the pinned repository; data not copied')
                self.data_source = getattr(self, 'data_source', {}); self.data_source[ds] = data
                self.scenario(scenario_id, f'ThalamusDB / {ds}', 'ThalamusDB', data,
                              {t: [c for c, _ in cols] for t, cols in schema.items()}, COMMIT, data_note)
            sql = task['sql']
            plan, title_zh, title_en, used, mixed, note_zh, note_en = self.thalamus_plan(sql, zh_name, en_name, schema)
            qid = f"thalamusdb/{task['id']}"
            fn_line = next(i for i, l in enumerate(lines, 1) if l.startswith(f"def {task['function']}("))
            self.query(query_id=qid, benchmark_id='thalamusdb', scenario_id=scenario_id, source_query_id=task['id'].split('/')[1],
                       title=zh(title_zh, title_en), plan_origin='source_reconstruction', plan_status_label='源码重建逻辑计划', source_id=definition,
                       root_node_id='n000', notes=zh(note_zh, note_en) if note_zh else '', group_label=f'ThalamusDB / {ds}', mixed_label=mixed,
                       environment_id=scenario_id, plan_format='logical_dag', collection_label='ThalamusDB', category_label=ds)
            self.add_graph(qid, plan)
            locator = f"{task['function']}() at benchmark.py line {fn_line}, generated query #{task['index'] + 1}"
            for source_id, role, locator_text in [(THAL_PAPER, 'paper', '§7.1, Table 4'), (definition, 'task_definition', locator),
                                                  (self.data_source[ds], 'dataset', 'README.md; nldbs.py')]:
                self.t['query_sources'].append(dict(query_id=qid, source_id=source_id, role=role, locator=locator_text,
                                                    attribution_note=zh('ThalamusDB 查询由固定版本 benchmark.py 的生成函数按顺序展开；逻辑计划依据 SQL 重建，未执行。',
                                                                        'ThalamusDB queries are expanded in order from the generator functions of the pinned benchmark.py; the logical plan is reconstructed from the SQL and not executed.')))
            self.t['original_queries'].append(dict(query_id=qid, text=sql, kind='sql', language='en', verification='upstream_template_expansion',
                                                   upstream_comparison=None, source_path=THAL_DIR + '/benchmark.expanded.json',
                                                   source_sha256=sha(expanded_path.read_bytes()), text_sha256=sha(sql),
                                                   selector=dict(type='json_task', id_field='id', id=task['id'], field='sql')))
            tables = []
            for table in used:
                cols = schema[table]
                passed = [c for c, t in cols if t in ('image', 'audio', 'string') and c in used[table]]
                tables.append(dict(name=table, columns=[{'name': c, 'type': t} for c, t in cols if c in used[table]], passed_columns=passed,
                                   row_unit='image' if table == 'images' else 'record', scope='used'))
            self.t['input_contracts'].append(dict(
                query_id=qid, environment=dict(requirement='none', resources=[]), tables=tables, output=plan[0][2],
                evidence=dict(path=THAL_DIR + '/benchmark.py', url=f'{THAL_BLOB}/benchmark.py#L{fn_line}', locator=locator,
                              sha256=sha(bench.read_bytes()), excerpt=sql),
                notes=[zh('nl(col, 文本) 谓词由 ThalamusDB 的图像、音频或文本模型评估；*_u 列是对应原始列的模型处理句柄，图中记为原始列。',
                          'nl(col, text) predicates are evaluated by ThalamusDB image, audio or text models; *_u columns are model-processed handles of the underlying columns, which the contract lists instead.')],
                audit_status='source_checked'))
            counts[ds] = counts.get(ds, 0) + 1
        return counts

    def thalamus_plan(self, sql, zh_name, en_name, schema):
        m = re.fullmatch(r"select (.+?) from (.+?) where (.+?)(?: limit (\d+))?", sql)
        select, from_, where, limit = m.groups()
        tables = [t.strip() for t in from_.split(',')]
        join = re.search(r' and (\w+)\.(\w+) = (\w+)\.(\w+)$', where)
        if join:
            where = where[:join.start()]
        preds = re.findall(r"nl\((\w+), '([^']+)'\)", where)
        connective = 'or' if ' or ' in where else 'and'
        used = {t: set() for t in tables}
        if join:
            used[join.group(1)].add(join.group(2)); used[join.group(3)].add(join.group(4))
        for col, _ in preds:
            used[self.NL[col][0]].add(self.NL[col][1])
        agg = None if select == '*' else select
        if agg and agg != 'count(*)':
            col = re.search(r'\((\w+)\)', agg).group(1)
            used[next(t for t in tables if col in [c for c, _ in schema[t]])].add(col)
        label = lambda col, cond: f"nl({col}, '{cond}')"
        lines, inputs = [], {}
        for t in tables:
            lines.append((f's_{t}', 'SCAN', f'Scan {t}', []))
            inputs[t] = f's_{t}'
        if connective == 'and' or len(preds) == 1:
            for i, (col, cond) in enumerate(preds):
                t = self.NL[col][0]
                lines.append((f'f{i}', 'SEM_FILTER', 'SEM_FILTER ' + label(col, cond), [inputs[t]]))
                inputs[t] = f'f{i}'
        top = None
        if join:
            lines.append(('j', 'JOIN', f'⋈ {join.group(1)}.{join.group(2)} = {join.group(3)}.{join.group(4)}', [inputs[t] for t in tables]))
            top = 'j'
        else:
            top = inputs[tables[0]]
        if connective == 'or' and len(preds) > 1:
            lines.append(('f_or', 'SEM_FILTER', 'SEM_FILTER ' + ' ∨ '.join(label(c, v) for c, v in preds), [top]))
            top = 'f_or'
        root = ('r', 'AGGREGATE', f'γ {agg}', [top]) if agg else ('r', 'LIMIT', f'LIMIT {limit}', [top])
        spec = {sym: (op, lab, kids) for sym, op, lab, kids in lines + [root]}
        ids, order = {}, []
        def visit(s):
            if s in ids: return
            ids[s] = f'n{len(ids):03d}'; order.append(s)
            for k in spec[s][2]: visit(k)
        visit('r')
        plan = [(ids[s], spec[s][0], spec[s][1], [ids[k] for k in spec[s][2]]) for s in order]
        cond_zh = ('且' if connective == 'and' else '或').join(f"{self.NL[c][2]} '{v}'" for c, v in preds)
        cond_en = (' and ' if connective == 'and' else ' or ').join(f"{self.NL[c][3]} '{v}'" for c, v in preds)
        out_zh = '前10行' if not agg else '行数' if agg == 'count(*)' else agg
        out_en = 'first 10 rows' if not agg else 'row count' if agg == 'count(*)' else agg
        # Without a join, a multi-table dataset's title names the one table queried (Q01 reads images only, Q13 joins furniture).
        only_zh, only_en = (f'（仅 {tables[0]} 表）', f' ({tables[0]} only)') if not join and len(schema) > 1 else ('', '')
        title_zh, title_en = f'{zh_name}{only_zh}：{cond_zh}，{out_zh}', f'{en_name}{only_en}: {cond_en}, {out_en}'
        mixed = '实质混合' if join or agg else '轻混合（仅投影）'
        note_zh = note_en = ''
        if join and connective == 'and' and len(preds) > 1:
            note_zh, note_en = '合取的单表 nl 谓词画在各自表上、连接之前；SQL 本身不规定执行顺序。', 'Conjunctive single-table nl predicates are drawn on their tables below the join; the SQL itself fixes no execution order.'
        elif join and connective == 'or' and len(preds) > 1:
            note_zh, note_en = '跨表析取的 nl 谓词只能在连接之后判断。', 'The disjunction spans both tables, so it is evaluated after the join.'
        elif not join and not agg:
            note_zh, note_en = '只有语义过滤和 LIMIT，没有其他关系算子。', 'Only a semantic filter and LIMIT; no other relational operator.'
        return plan, title_zh, title_en, used, mixed, note_zh, note_en

    def add_graph(self, qid, plan):
        for node_id, op, lab, kids in plan:
            self.t['nodes'].append(dict(query_id=qid, node_id=node_id, operator_type=op, label=lab))
        for node_id, _, _, kids in reversed(plan):
            for pos, kid in enumerate(kids):
                self.t['edges'].append(dict(query_id=qid, parent_id=node_id, child_id=kid, input_position=pos))

    # MLSys 2025 ----------------------------------------------------------
    TITLES = {
        'movies/T1': ('Movies：LLM 过滤，电影是否适合儿童', 'Movies: LLM filter, is the movie suitable for kids'),
        'movies/T2': ('Movies：LLM 投影，总结获好评的优点', 'Movies: LLM projection, summarize qualities behind a favorable rating'),
        'movies/T3': ('Movies：负面影评过滤后再总结优点（两次 LLM）', 'Movies: summarize qualities after filtering negative reviews (two LLM calls)'),
        'movies/T4': ('Movies：LLM 情感打分后求平均', 'Movies: average of LLM sentiment scores'),
        'products/T1': ('Products：LLM 过滤，评论情感三分类', 'Products: LLM filter, three-way review sentiment'),
        'products/T2': ('Products：LLM 投影，商品总结与描述一致性', 'Products: LLM projection, product summary and description consistency'),
        'products/T3': ('Products：情感过滤后再做商品总结（两次 LLM）', 'Products: product summary after sentiment filtering (two LLM calls)'),
        'products/T4': ('Products：LLM 情感打分后求平均', 'Products: average of LLM sentiment scores'),
        'bird/T1': ('BIRD：LLM 过滤，帖子是否与统计相关', 'BIRD: LLM filter, is the post related to statistics'),
        'bird/T2': ('BIRD：LLM 投影，评论与帖子正文的关系', 'BIRD: LLM projection, how the comment relates to the post body'),
        'pdmx/T1': ('PDMX：LLM 过滤，乐曲信息是否提及特定个人', 'PDMX: LLM filter, does song information reference a specific individual'),
        'pdmx/T2': ('PDMX：LLM 投影，50 词乐曲概述', 'PDMX: LLM projection, 50-word music overview'),
        'beer/T1': ('Beer：LLM 过滤，啤酒是否源自欧洲', 'Beer: LLM filter, does the beer have European origin'),
        'beer/T2': ('Beer：LLM 投影，20 词啤酒与评论概述', 'Beer: LLM projection, 20-word beer and review overview'),
        'squad/T5': ('SQuAD：检索 5 段上下文后问答（RAG）', 'SQuAD: answer with 5 retrieved contexts (RAG)'),
        'fever/T5': ('FEVER：检索 4 段证据后判断主张（RAG）', 'FEVER: verify the claim with 4 retrieved evidence passages (RAG)'),
    }
    MIXED = {'T1': '纯语义', 'T2': '纯语义', 'T3': '纯语义', 'T4': '实质混合', 'T5': '纯语义'}  # matches mlsys_plan's DAGs

    def mlsys_plan(self, task, title_en):
        """Logical DAG from the paper's query type (Table 1, §6.1.2): T1 filter, T2 projection, T3 filter then projection,
        T4 AVG over LLM scores, T5 retrieval then answer. Root first, as add_graph expects."""
        ds, kind = task['id'].split('/')
        what = re.sub(r'^LLM (filter|projection), ', '', title_en.split(': ', 1)[1])
        scan = ('SCAN', f'Scan {ds}')
        chain = {
            'T1': [('SEM_FILTER', f'LLM filter: {what}'), scan],
            'T2': [('SEM_MAP', f'LLM projection: {what}'), scan],
            'T3': [('SEM_MAP', 'LLM projection: summarize (second LLM call)'), ('SEM_FILTER', 'LLM filter: review sentiment is POSITIVE (first LLM call)'), scan],
            'T4': [('AGGREGATE', 'AVG(sentiment score)'), ('SEM_MAP', 'LLM projection: sentiment score 1–5'), scan],
        }.get(kind)
        if chain:
            return [(f'n{i:03d}', op, label, [f'n{i + 1:03d}'] if i + 1 < len(chain) else []) for i, (op, label) in enumerate(chain)]
        k = 5 if ds == 'squad' else 4
        return [('n000', 'SEM_MAP', 'LLM answer from the question and retrieved contexts', ['n001', 'n003']),
                ('n001', 'SEM_TOPK', f'Retrieve top-{k} contexts by embedding similarity (FAISS)', ['n002', 'n003']),
                ('n002', 'SCAN', 'Scan context passages', []),
                ('n003', 'SCAN', f'Scan {ds} questions', [])]

    def mlsys(self):
        path = ROOT / MLSYS_FILE
        doc = json.loads(path.read_text())
        raw = path.read_bytes()
        definition = self.source(MLSYS_FILE, MLSYS_FILE, 'Transcribed queries of arXiv 2403.05821v2 (Appendix A–C)', 'task_definition',
                                 f"arXiv 2403.05821v2; PDF sha256 {doc['pdf_sha256']}", 'Verbatim transcription from the paper PDF; no public code repository found',
                                 doc['pdf_url'])
        counts = {}
        for task in doc['tasks']:
            ds, kind = task['id'].split('/')
            info = doc['datasets'][ds]
            scenario_id = f'mlsys-llmsql/{ds}'
            data = self.source('mlsys-data/' + ds, doc['paper'], f"{info['name']} (as used by Liu et al., MLSys 2025)", 'dataset',
                               'arXiv 2403.05821v2 §6.1.1, Appendix B', 'Dataset named and described by the paper; data not downloaded')
            if scenario_id not in self.scenarios:
                self.scenario(scenario_id, f'MLSys 2025 LLM-SQL / {ds}', None, data, {ds: info['columns']}, '2403.05821v2',
                              zh('论文 §6.1.1 与附录 B 给出数据集与列；本仓未下载数据。', 'The paper (§6.1.1, Appendix B) names the dataset and its columns; no data downloaded here.'))
            qid = f'mlsys-llmsql/{task["id"]}'
            title_zh, title_en = self.TITLES[task['id']]
            notes = []
            if 'sql_example' in task:
                notes.append(zh('附录 A 的示例 SQL 与附录 C 的实验提示措辞不同；两者都保留，查询原文取附录 C。',
                                'The Appendix A example SQL is worded differently from the Appendix C prompt used in experiments; both are kept and the original text is taken from Appendix C.'))
            else:
                notes.append(zh('论文未给出本条 SQL；逻辑计划按论文的查询类型画出，不补造 SQL。', 'The paper gives no SQL for this query; the logical plan follows the paper\'s query type and no SQL is invented.'))
            if kind == 'T5':
                notes.append(zh('检索加单次 LLM 调用，不含关系算子。', 'Retrieval plus one LLM call; no relational operator.'))
            note = ''.join(notes)
            self.query(query_id=qid, benchmark_id='mlsys-llmsql', scenario_id=scenario_id, source_query_id=task['id'], title=zh(title_zh, title_en),
                       plan_origin='end_to_end_interpretation',
                       plan_status_label=zh('依据论文查询类型重建的逻辑计划（论文未给出完整 SQL）', 'Logical plan rebuilt from the paper query type (no full SQL in the paper)'),
                       source_id=definition, root_node_id='n000', notes=note, group_label='MLSys 2025 LLM-SQL', mixed_label=self.MIXED[kind],
                       environment_id=scenario_id, plan_format='logical_dag', collection_label='MLSys 2025 LLM-SQL', category_label=task['type'])
            self.add_graph(qid, self.mlsys_plan(task, title_en))
            if note:
                EN.setdefault(note, ' '.join(EN.get(n) or CONTENT[n] for n in notes))
            locator = f"Table 1; §6.1.2 {task['type']}; Appendix C" + ('; Appendix A' if 'sql_example' in task else '')
            for source_id, role in [(MLSYS_PAPER, 'paper'), (definition, 'task_definition'), (data, 'dataset')]:
                self.t['query_sources'].append(dict(query_id=qid, source_id=source_id, role=role, locator=locator,
                                                    attribution_note=zh('查询文本按论文 PDF 原文转录；没有公开代码，逻辑计划依据论文查询类型重建，未执行。',
                                                                        'Query text transcribed verbatim from the paper PDF; no public code; the logical plan is rebuilt from the paper query type and not executed.')))
            self.t['original_queries'].append(dict(query_id=qid, text=task['query'], kind='natural_language', language='en', verification='paper_transcription',
                                                   upstream_comparison=None, source_path=MLSYS_FILE, source_sha256=sha(raw), text_sha256=sha(task['query']),
                                                   selector=dict(type='json_task', id_field='id', id=task['id'], field='query')))
            programs = [dict(type='llm_user_prompt', program=task['query'])]
            if 'sql_example' in task:
                programs.append(dict(type='paper_sql_example', program=task['sql_example']))
            self.t['task_details'].append(dict(query_id=qid, reference_programs=programs, gold=dict(gold_answer=None, answer_schema=None),
                                               evaluation=dict(primary_metric=None), annotation={}))
            self.t['input_contracts'].append(dict(
                query_id=qid, environment=dict(requirement='required' if kind == 'T5' else 'none',
                                               resources=[{'name': 'vector index over contexts (FAISS, gte-base-en-v1.5)', 'source_type': 'document'}] if kind == 'T5' else []),
                tables=[dict(name=ds, columns=[{'name': c, 'type': None} for c in info['columns']], passed_columns=None, row_unit='record', scope='database')],
                output=None, evidence=dict(path=MLSYS_FILE, url=doc['paper'], locator=locator, sha256=sha(raw), excerpt=task['query']),
                notes=[zh('列来自附录 B；论文未说明每条查询传入哪些列（附录 A 只给出 Movies/FEVER 示例），passed_columns 记为未知。',
                          'Columns come from Appendix B; the paper does not state which fields each query passes (Appendix A shows only Movies/FEVER examples), so passed_columns is unknown.')],
                audit_status='source_checked'))
            counts[ds] = counts.get(ds, 0) + 1
        return counts

    def finish(self):
        catalog = json.loads((ROOT / 'config/catalog.json').read_text())
        catalog['scenarios'] = [s for s in catalog['scenarios'] if not s.startswith(tuple(f'files/{p}' for p in PREFIXES))]
        for scenario_id, name in self.scenarios.items():
            rel = f'files/{scenario_id}/scenario.json'
            write_json(rel, dict(id=scenario_id, name=name, query_ids=[q['query_id'] for q in self.t['queries'] if q['scenario_id'] == scenario_id]))
            catalog['scenarios'].append(rel)
        catalog['source_commits']['thalamusdb'] = COMMIT
        write_json('config/catalog.json', catalog)
        coverage = json.loads((ROOT / 'config/benchmark-coverage.json').read_text())
        for entry in coverage['entries']:
            if entry['key'] == 'thalamusdb':
                entry['catalog'] = [{'benchmark_id': 'thalamusdb'}]
                repo = {'url': 'https://github.com/saehanjo/thalamusdb', 'commit': COMMIT, 'link_source': '第一作者仓库；benchmark.py 的生成函数展开出 55 条查询'}
                entry['repositories'] = [r for r in entry['repositories'] if r['url'] != repo['url']] + [repo]
                entry['status_note'] = f'按 saehanjo/thalamusdb@{COMMIT[:8]} 的 benchmark.py 生成函数展开 55 条（Craigslist 25、YouTube 24、Netflix 6），与 §7.1 一致；均重建为逻辑计划。'
            if entry['key'] == 'llm-sql-mlsys':
                entry['catalog'] = [{'benchmark_id': 'mlsys-llmsql'}]
                entry['status_note'] = '未找到官方代码仓库；按 arXiv v2 附录 A–C 原文转录 16 条（提示词全部，SQL 仅论文给出的 5 个示例），未重建逻辑计划。'
        write_json('config/benchmark-coverage.json', coverage)
        for name in TABLES:
            (ROOT / 'query' / f'{name}.jsonl').write_text(''.join(json.dumps(r, ensure_ascii=False) + '\n' for r in self.t[name]))
        CONTENT.update(EN)
        write_json('config/content-en.json', CONTENT)


def main():
    importer = Importer()
    counts = {'thalamusdb': importer.thalamus(), 'mlsys-llmsql': importer.mlsys()}
    importer.finish()
    print(json.dumps(counts))


if __name__ == '__main__':
    main()
