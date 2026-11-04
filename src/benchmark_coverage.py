"""Attach benchmark coverage and code repositories to papers; counts come from the catalog."""
from collections import Counter
import hashlib
import json
from pathlib import Path

DOMAIN = 'Semantic operator benchmark coverage'
STATUS = {'complete': '✅ 完整', 'partial': '◐ 部分', 'reused': '◐ 经由复用集合', 'none': '✗ 未收录'}
MIXED = {'yes': '✅', 'partial': '◐', 'no': '✗', 'unknown': '?'}
# Structural nodes do not make a query relational in the sense of the mixed statistic.
STRUCTURAL = {'PROJECT', 'CTE', 'CTE_REF', 'UNRESOLVED', 'RESULT_BUNDLE'}


class BenchmarkCoverage:
    def __init__(self, root, identity):
        self.root = Path(root)
        self.identity = identity
        self.registry = json.loads((self.root / 'config/benchmark-coverage.json').read_text())
        self.queries = [json.loads(l) for l in (self.root / 'query/queries.jsonl').read_text().splitlines() if l.strip()]
        operators = self.root / 'config/operators.json'
        families = {o['operator_type']: o['family'] for o in json.loads(operators.read_text())} if operators.exists() else {}
        kinds = {}
        nodes = self.root / 'query/nodes.jsonl'
        for line in (nodes.read_text().splitlines() if nodes.exists() else []):
            n = json.loads(line)
            family = families.get(n['operator_type'])
            if family == 'semantic' or (family == 'relational' and n['operator_type'] not in STRUCTURAL):
                kinds.setdefault(n['query_id'], set()).add(family)
        self.dag_mixed = {qid for qid, k in kinds.items() if k == {'semantic', 'relational'}}

    def counts(self, entry):
        selected = [q for q in self.queries if any(
            q['benchmark_id'] == c['benchmark_id'] and c.get('scenario_id', q['scenario_id']) == q['scenario_id']
            for c in entry['catalog'])]
        labels = Counter(q.get('mixed_label') or '未标注' for q in selected)
        dags = [q for q in selected if q.get('plan_format') == 'logical_dag']
        self.last_dag = (len(dags), sum(q['query_id'] in self.dag_mixed for q in dags))
        return len(selected), labels

    def dag_text(self):
        total, mixed = self.last_dag
        if not total:
            return '无逻辑 DAG（参考程序记录不做此判定）'
        return f'{total} 条有逻辑 DAG，其中 {mixed} 条同时含语义算子与关系算子（不计 PROJECT/CTE 等结构节点）'

    @staticmethod
    def repo_text(repo):
        commit = f" @ `{repo['commit'][:8]}`" if repo.get('commit') else ''
        return f"[{repo['url'].removeprefix('https://')}]({repo['url']}){commit}（{repo['link_source']}）"

    def apply(self, papers):
        by_id = {p['id']: p for p in papers}
        by_url = {self.identity(p['url']): p for p in papers if p.get('url')}
        checked = self.registry['checked_on']
        rows = []
        for entry in self.registry['entries']:
            if entry.get('paper_id'):
                paper = by_id.get(entry['paper_id'])
                if paper is None:
                    raise ValueError('Unknown coverage paper: ' + entry['paper_id'])
            else:
                key = self.identity(entry['url'])
                paper = by_url.get(key)
                if paper is not None:
                    paper.setdefault('kind', entry['kind'])
                else:
                    paper = {
                        'id': 'lit_' + hashlib.sha256(key.encode()).hexdigest()[:12],
                        'title': entry['title'], 'venue': entry['venue'], 'year': str(entry['year']),
                        'url': entry['url'], 'folder': None, 'usecase': '', 'kind': entry['kind'],
                        'literature_reading_status': 'abstract_only', 'literature_topics': [],
                        'sections': {'overview': f"# {entry['title']}\n\n[原文]({entry['url']})\n\n核对日期：{checked}。阅读范围：已核对原始元数据与摘要（{entry['scale_source']}）。\n"},
                    }
                    papers.append(paper)
                    by_url[key] = by_id[paper['id']] = paper
            count, labels = self.counts(entry)
            if 'expected_queries' in entry:
                # Status follows the live catalog when the paper states its query count.
                expected = entry['expected_queries']
                entry = dict(entry, status='complete' if count >= expected else 'partial' if count else 'none',
                             status_note=f"已收录 {count}/{expected} 条。{entry['status_note']}".strip())
            paper['repositories'] = entry['repositories']
            paper['literature_domains'] = sorted(set(paper.get('literature_domains', [])) | {DOMAIN})
            label_text = '、'.join(f'{k} {v}' for k, v in labels.items()) or '—'
            repos = '\n'.join(f'- {self.repo_text(r)}' for r in entry['repositories']) or '- 未找到公开代码仓库'
            paper['sections']['coverage'] = '\n'.join([
                '# 收录核对', '', f'核对日期：{checked}。{self.registry["scope"]}', '',
                '| 项目 | 内容 |', '|---|---|',
                f"| 分类 | {self.registry['groups'][entry['group']]} |",
                f"| 论文查询规模 | {entry['query_scale']}（{entry['scale_source']}） |",
                f"| 图册已收录 | {count} 条；混合标签：{label_text} |",
                f"| 逻辑计划判定 | {self.dag_text()} |",
                f"| 收录状态 | {STATUS[entry['status']]}：{entry['status_note']} |",
                f"| 结构化 + 语义混合 | {MIXED[entry['mixed']]} {entry['mixed_note']} |",
                '', '## 代码仓库', '', repos, ''])
            rows.append((entry, paper, count, self.last_dag))
        self.write_table(rows)

    def write_table(self, rows):
        lines = ['# 语义算子 Benchmark 收录核对', '',
                 f"核对日期：{self.registry['checked_on']}。{self.registry['scope']}", '',
                 '图例：✅ 是／完整　◐ 部分　✗ 否　? 未核对。已收录数量由构建从 `query/queries.jsonl` 计算；登记源为 `config/benchmark-coverage.json`。',
                 '“DAG 混合”= 有逻辑 DAG 的已收录查询中，同时含语义算子与关系算子（不计 PROJECT、CTE、CTE_REF、UNRESOLVED、RESULT_BUNDLE）的条数；只读节点表计算，不改写人工混合标签。参考程序记录没有 DAG，记为 —。']
        for group, heading in self.registry['groups'].items():
            lines += ['', f'## {heading}', '', '| 论文 | 年份 | 代码仓库 | 论文查询规模 | 已收录 | DAG 混合 | 状态 | 混合 |', '|---|---|---|---|---:|---:|---|:-:|']
            for entry, paper, count, (dag_total, dag_mixed) in rows:
                if entry['group'] != group:
                    continue
                repo = '<br>'.join(f"[{r['url'].removeprefix('https://')}]({r['url']})" + (f" `{r['commit'][:8]}`" if r.get('commit') else '') for r in entry['repositories']) or '—'
                title = paper['title'].replace('|', '/')
                link = paper['url'] if paper['url'].startswith('http') else '../' + paper['url']
                lines.append(f"| [{title}]({link}) | {paper['year']} | {repo} | {entry['query_scale']} | {count} | {f'{dag_mixed}/{dag_total}' if dag_total else '—'} | {STATUS[entry['status']]} | {MIXED[entry['mixed']]} |")
        (self.root / 'docs/benchmark-coverage.md').write_text('\n'.join(lines) + '\n')
