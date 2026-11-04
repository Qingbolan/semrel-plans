"""Publish source-backed reading notes independently of query imports and paper identities."""
import hashlib
import json
from pathlib import Path


REVIEW_SECTIONS = {
    'overview': 'README.md', 'motivation': '出发点分析.md',
    'problem': '解决的问题分析.md', 'novelty': 'Novelty分析.md',
    'workload': 'workload分析.md', 'usecase': 'usecase分析.md',
    'benchmark': 'benchmark分析.md',
}


class PaperReviews:
    def __init__(self, root, identity):
        self.root = Path(root)
        self.identity = identity
        self.entries = json.loads((self.root / 'research/paper-completion/reviews.json').read_text())

    def apply(self, papers):
        indexed = {self.identity(p['url']): p for p in papers}
        seen = set()
        for entry in self.entries:
            key = self.identity(entry['url'])
            if key in seen or key not in indexed:
                raise ValueError('Invalid paper review identity: ' + key)
            seen.add(key)
            if entry['status'] not in {'READ', 'EVIDENCE_CHECKED'}:
                raise ValueError('Only completed readings can publish analysis')
            source = self.root / entry['fulltext']
            if hashlib.sha256(source.read_bytes()).hexdigest() != entry['sha256']:
                raise ValueError('Changed paper source: ' + key)
            sections = {}
            for section, filename in REVIEW_SECTIONS.items():
                text = (self.root / entry['note_directory'] / filename).read_text()
                if not text.strip():
                    raise ValueError('Empty paper review: ' + key + '/' + section)
                sections[section] = text
            paper = indexed[key]
            paper['sections'].update(sections)
            paper['usecase'] = sections['usecase']
            paper['review_status'] = entry['status']
            paper['review_evidence'] = entry['evidence']
            paper['review_source'] = {k: entry[k] for k in ('fulltext', 'sha256', 'version', 'read_sections')}
            paper['literature_reading_status'] = 'full_text_reviewed'
