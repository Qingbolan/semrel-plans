"""Portable paper catalog built only from versioned local reading notes."""
from pathlib import Path
import hashlib
import json
import re
from urllib.parse import quote

SECTIONS = {'overview': 'README.md', 'motivation': '出发点分析.md', 'problem': '解决的问题分析.md', 'novelty': 'Novelty分析.md', 'workload': 'workload分析.md'}

class PaperExporter:
    def __init__(self, root: Path):
        self.root = root

    def export(self):
        records = []
        for entry in json.loads((self.root / 'Survey/manifest.json').read_text()):
            folder = entry['folder']
            title, venue, year = folder.rsplit('-', 2)
            sections = {key: (self.root / 'Survey' / folder / name).read_text() for key, name in SECTIONS.items()}
            urls = re.findall(r'\]\((https?://[^\s)]+)\)', sections['overview'])
            local_pdf = next((self.root / 'Survey' / folder).glob('*.pdf'), None)
            paper_url = urls[0] if urls else quote(local_pdf.relative_to(self.root).as_posix()) if local_pdf else ''
            usecase = self.usecase(sections['workload'])
            sections['benchmark'] = self.benchmark(sections['workload'])
            records.append({'id': hashlib.sha256(folder.encode()).hexdigest()[:12], 'title': title.replace('- ', ': ', 1), 'venue': venue, 'year': year, 'folder': folder, 'url': paper_url, 'sections': sections, 'usecase': usecase})
        sources = [json.loads(line) for line in (self.root / 'data/sources.jsonl').read_text().splitlines()]
        for source in sources:
            if source['source_type'] != 'paper':
                continue
            existing = next((p for p in records if p['url'] == source['location']), None)
            if existing:
                existing.setdefault('source_ids', []).append(source['source_id'])
                continue
            label = source['publication_label']
            year = re.search(r'\d{4}', label)
            year = year.group() if year else '0'
            overview = f"# {source['title']}\n\n{label}\n\n{source['version']}\n\n[原文]({source['location']})\n\n此条目已关联图册来源；尚未纳入完整阅读调研。"
            records.append({'id': source['source_id'], 'source_ids': [source['source_id']], 'title': source['title'], 'venue': label.split(year)[0], 'year': year, 'publication_label': label, 'folder': None, 'url': source['location'], 'sections': {'overview': overview}, 'usecase': ''})
        types = json.loads((self.root / 'config/paper-types.json').read_text())
        for paper in records:
            paper['kind'] = types[paper['id']]
        records.sort(key=lambda p: (-int(p['year']), p['title']))
        (self.root / 'assets/papers.js').write_text('window.SEMREL_PAPERS = ' + json.dumps(records, ensure_ascii=False) + ';\n')
        return records

    @staticmethod
    def usecase(markdown):
        # Preserve whole source paragraphs, including result boundaries and citations.
        lines = markdown.splitlines()
        start = next((i for i, line in enumerate(lines) if (line.startswith('#') or line.startswith('**')) and re.search(r'use\s*case|具体用例|代表.*例|最.*例', line, re.I)), None)
        if start is None:
            return ''
        end = next((i for i in range(start + 1, len(lines)) if lines[i].startswith('## ') or re.match(r'^\*\*(?:Baseline|baseline|基线|证据|依据|边界|比较)', lines[i])), len(lines))
        return '\n'.join(lines[start:end]).strip()

    @classmethod
    def benchmark(cls, markdown):
        """Expose evaluation evidence without duplicating the separate case study."""
        case = cls.usecase(markdown)
        content = markdown.replace(case, '', 1) if case else markdown
        content = re.sub(r'^# [^\n]*\n', '# Benchmark\n', content, count=1)
        return re.sub(r'\n{3,}', '\n\n', content).strip()
