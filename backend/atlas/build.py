"""Build portable browser assets and documentation from scenario query files."""
from pathlib import Path
import shutil
import hashlib
import re
from papers import PaperExporter
from groups import query_groups
import json
from scenario import Catalog
from task_records import TaskRecords
from export import StatisticsExporter
from eal import EalExporter
from eal_reader import EalCompiler
from query_translations import QueryTranslations

def text_tree(node, prefix='', root=True, last=True):
    line = prefix + ('' if root else '└─ ' if last else '├─ ') + node['label']
    child_prefix = prefix + ('' if root else '   ' if last else '│  ')
    lines = [line]
    for i, child in enumerate(node['children']):
        lines.extend(text_tree(child, child_prefix, False, i == len(node['children']) - 1))
    return lines

class SiteBuilder:
    def __init__(self, root: Path):
        self.root = root
        self.catalog = Catalog(root)

    DETAIL_FIELDS = ('input_contract', 'task_record', 'tree', 'annotation', 'gold', 'evaluation')

    @classmethod
    def split_details(cls, assets, queries):
        """Keep the page index small: per-query plan snapshots and records load on demand."""
        directory = assets / 'details'
        if directory.exists():
            for old in directory.glob('*.js'):
                old.unlink()
        directory.mkdir(exist_ok=True)
        index = []
        for q in queries:
            detail = {field: q.get(field) for field in cls.DETAIL_FIELDS}
            light = {k: v for k, v in q.items() if k not in cls.DETAIL_FIELDS}
            if q.get('eal'):
                snapshot = q['eal']['snapshot']
                detail['snapshot'] = snapshot
                light['eal'] = {k: v for k, v in q['eal'].items() if k != 'snapshot'}
                # Enough per-node data for search, statistics and the analysis view.
                light['eal']['ops'] = [{'label': n['label'], 'ability': n['ability'], 'family': n['family'], 'phase': n.get('phase', 0),
                                        'op': (n.get('arguments') or {}).get('operator_type') or n['ability']}
                                       for n in snapshot['graph']['nodes']]
            payload = json.dumps([q['query_id'], detail], ensure_ascii=False)
            key = hashlib.sha256(payload.encode()).hexdigest()[:16]
            light['detail_path'] = f'assets/details/{key}.js'
            (directory / f'{key}.js').write_text(f'window.SemRelDetails.receive(...{payload});\n')
            index.append(light)
        return index

    RUNTIME = ('.js', '.css')

    def copy_frontend(self, dist):
        """The static site is self-contained in dist/: plain viewer scripts are copied next to the bundles."""
        viewer = dist / 'viewer'
        shutil.rmtree(viewer, ignore_errors=True)
        viewer.mkdir(parents=True)
        source = self.root / 'frontend'
        for path in source.iterdir():
            if path.is_file() and path.suffix in self.RUNTIME:
                shutil.copy2(path, viewer / path.name)
        shutil.copy2(source / 'migration.html', dist / 'migration.html')

    def build(self):
        count = self.catalog.validate()
        StatisticsExporter(self.catalog).export()
        self.catalog.input_contracts.export(self.root, self.catalog.tables['queries'])
        eal = EalExporter(self.catalog).export()
        compiler = EalCompiler()
        for entry in eal.values():
            entry['snapshot'] = compiler.compile(entry.pop('source'))
        queries = [{**q, 'eal': eal.get(q['query_id'])} for q in self.catalog.queries]
        TaskRecords.export(self.root, queries)
        payload = {**self.catalog.metadata, 'count': count, 'queries': queries}
        dist = self.root / 'dist'
        assets = dist / 'assets'
        assets.mkdir(parents=True, exist_ok=True)
        self.copy_frontend(dist)
        PaperExporter(self.root).export(queries)
        (assets / 'collections.js').write_text('window.SEMREL_COLLECTIONS = ' + json.dumps(self.catalog.folders.export(queries), ensure_ascii=False) + ';\n')
        (assets / 'query-groups.js').write_text('window.SEMREL_QUERY_GROUPS = ' + json.dumps(query_groups(self.catalog), ensure_ascii=False) + ';\n')
        (assets / 'plans.json').write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n')
        (assets / 'plans.js').write_text('window.SEMREL_PLANS = ' + json.dumps(self.split_details(assets, queries), ensure_ascii=False) + ';\n')
        query_translations = QueryTranslations(self.root, self.catalog.tables['queries'])
        (assets / 'query-zh.js').write_text('window.SEMREL_QUERY_ZH = ' + json.dumps(query_translations.by_source(), ensure_ascii=False) + ';\n')
        translations = json.loads((self.root / 'config/content-en.json').read_text())
        (assets / 'content-en.js').write_text('window.SEMREL_CONTENT_EN = ' + json.dumps(translations, ensure_ascii=False) + ';\n')
        template = (self.root / 'frontend/index.html').read_text()
        resources = re.findall(r'(?:src|href)="((?:viewer/|assets/)[^"]+)"', template)
        revision = hashlib.sha256(b''.join((dist / path).read_bytes() for path in resources)).hexdigest()[:12]
        template = template.replace('{{COUNT}}', str(count)).replace('{{BUILD}}', revision)
        for path in resources:
            template = template.replace(f'"{path}"', f'"{path}?v={revision}"')
        (dist / 'index.html').write_text(template)
        sections = ['# 逐查询逻辑计划\n\n由 `python3 backend/scripts/build.py` 生成；请编辑 query/ 下的规范化数据表。\n\n[论文与数据来源](sources.md) · [范围与限制](scope.md) · [交互图册](../index.html)\n']
        bibliography = ['# 论文与数据来源\n\n原有查询代码沿用 2026-10-05 固定版本收据；本地集合于 2026-10-13 接入。各来源的核对日期与边界见条目。论文背景、提供的任务定义和分析记录分别标注。\n\n来源关系规范表：`query/query_sources.jsonl`；来源元数据：`query/sources.jsonl`。数据集链接不等于已经下载、许可审查或完整复现。\n']
        roles = {'paper': '论文', 'dataset': '数据', 'protocol': '规则协议', 'task_definition': '提供的任务定义', 'analysis': '提供的查询分析'}
        used = {ref['source_id'] for ref in self.catalog.tables['query_sources']}
        for source in self.catalog.tables['sources']:
            if source['source_id'] not in used:
                continue
            bibliography.append(f"## {source['title']}\n\n[来源]({source['location']}) · {source['version']}\n\n{source['verification']}；记录日期 {source['checked_on']}。\n")
        (self.root / 'docs/sources.md').write_text('\n'.join(bibliography))
        for q in self.catalog.queries:
            source = q['source'] if q['source'].startswith('https://') else '../' + q['source']
            provenance = '\n'.join(f"- **{roles[ref['role']]}**：[{ref['title']}]({ref['location']})。{ref['version']}；定位：{ref['locator']}。{ref['attribution_note']}" for ref in q['provenance'])
            plan = '\n'.join(text_tree(q['tree'])) if q['tree'] else '\n\n'.join(p['program'] for p in q['reference_programs'])
            sections.append(f"## {q['group']} / {q['display_number']} — {q['title']}\n\n{q['status']}；{q['mixed']}。[查询定义 / 实现]({source})\n\n{provenance}\n\n```text\n" + plan + '\n```\n\n' + q['note'] + '\n')
            env = q['environment']['environment_id']
            dataset = q['dataset']['dataset_id']
            inputs = '\n'.join('- ' + json.dumps(i, ensure_ascii=False) for i in q['inputs']) or '未提供逐查询输入绑定。'
            availability = q['dataset']['availability']
            sections.append(f"### 环境与输入\n\n[环境](../environment/{env}/manifest.json) · [数据](../data/{dataset}/manifest.json)\n\n数据状态：{availability}\n\n{inputs}\n\n查询未执行；模型 batch size 未定义。文件存在不等于结果已复现；LIMIT / TopK 不是输入批次大小。\n")

        (self.root / 'docs/catalog.md').write_text('\n'.join(sections))
        return count
