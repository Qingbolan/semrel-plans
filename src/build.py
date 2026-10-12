"""Build portable browser assets and documentation from scenario query files."""
from pathlib import Path
from papers import PaperExporter
import json
from scenario import Catalog
from export import StatisticsExporter
from eal import EalExporter
from eal_reader import EalCompiler

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

    def build(self):
        count = self.catalog.validate()
        StatisticsExporter(self.catalog).export()
        eal = EalExporter(self.catalog).export()
        compiler = EalCompiler()
        for entry in eal.values():
            entry['snapshot'] = compiler.compile(entry.pop('source'))
        queries = [{**q, 'eal': eal[q['query_id']]} for q in self.catalog.queries]
        payload = {**self.catalog.metadata, 'count': count, 'queries': queries}
        assets = self.root / 'assets'
        assets.mkdir(exist_ok=True)
        PaperExporter(self.root).export()
        (assets / 'plans.json').write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n')
        (assets / 'plans.js').write_text('window.SEMREL_PLANS = ' + json.dumps(queries, ensure_ascii=False) + ';\n')
        translations = json.loads((self.root / 'config/content-en.json').read_text())
        (assets / 'content-en.js').write_text('window.SEMREL_CONTENT_EN = ' + json.dumps(translations, ensure_ascii=False) + ';\n')
        template = (self.root / 'src/viewer/index.html').read_text()
        (self.root / 'index.html').write_text(template.replace('{{COUNT}}', str(count)))
        sections = ['# 逐查询逻辑计划\n\n由 `python3 scripts/build.py` 生成；请编辑 data/ 下的规范化数据表。\n\n[论文与数据来源](sources.md) · [范围与限制](scope.md) · [交互图册](../index.html)\n']
        bibliography = ['# 论文与数据来源\n\n核对日期：2026-10-12。查询代码沿用 2026-10-05 固定版本收据。论文用于确认任务与数据背景；每条 plan 的具体归属见逐查询说明。\n\n来源关系规范表：`data/query_sources.jsonl`；来源元数据：`data/sources.jsonl`。数据集链接不等于已经下载、许可审查或完整复现。\n']
        roles = {'paper': '论文', 'dataset': '数据', 'protocol': '规则协议'}
        used = {ref['source_id'] for ref in self.catalog.tables['query_sources']}
        for source in self.catalog.tables['sources']:
            if source['source_id'] not in used:
                continue
            bibliography.append(f"## {source['title']}\n\n[来源]({source['location']}) · {source['version']}\n\n{source['verification']}；记录日期 {source['checked_on']}。\n")
        (self.root / 'docs/sources.md').write_text('\n'.join(bibliography))
        for q in self.catalog.queries:
            source = q['source'] if q['source'].startswith('https://') else '../' + q['source']
            provenance = '\n'.join(f"- **{roles[ref['role']]}**：[{ref['title']}]({ref['location']})。{ref['version']}；定位：{ref['locator']}。{ref['attribution_note']}" for ref in q['provenance'])
            sections.append(f"## {q['group']} / {q['id']} — {q['title']}\n\n{q['status']}；{q['mixed']}。[查询定义 / 实现]({source})\n\n{provenance}\n\n```text\n" + '\n'.join(text_tree(q['tree'])) + '\n```\n\n' + q['note'] + '\n')
        (self.root / 'docs/catalog.md').write_text('\n'.join(sections))
        return count
