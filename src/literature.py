"""Merge researched literature into the paper library without inventing reading notes."""
import hashlib
import json
from pathlib import Path


class LiteratureCatalog:
    def __init__(self, root: Path, identity):
        self.root = root
        self.identity = identity

    def apply(self, papers):
        entries = json.loads((self.root / 'config/literature-catalog.json').read_text())
        by_url = {self.identity(p['url']): p for p in papers}
        for entry in entries:
            if entry['reading_status'] == 'discovered':
                continue
            url = self.identity(entry['url'])
            paper = by_url.get(url)
            if paper is None:
                paper = {
                    'id': 'lit_' + hashlib.sha256(url.encode()).hexdigest()[:12],
                    'title': entry['title'], 'venue': entry['venue'],
                    'year': str(entry['year']), 'url': entry['url'],
                    'folder': None, 'sections': {}, 'usecase': '',
                }
                paper['sections']['overview'] = (
                    f"# {entry['title']}\n\n[原文]({entry['url']})\n\n"
                    f"检索日期：2026-10-14。阅读范围：{entry['reading_status_label']}。\n"
                )
                papers.append(paper)
                by_url[url] = paper
            if entry['reading_status'] == 'full_text_reviewed' or paper.get('year') == '0':
                paper.update(title=entry['title'], venue=entry['venue'], year=str(entry['year']))
            paper['literature_topics'] = entry['topics']
            paper['literature_domains'] = entry.get('domains', [])
            paper['literature_reading_status'] = entry['reading_status']
            paper['literature_evidence'] = entry['evidence']
