"""Sidebar folders: map each source collection to one documented presentation folder."""
import json
from pathlib import Path


class CollectionFolders:
    def __init__(self, root: Path):
        self.config = json.loads((root / 'config/collections.json').read_text())
        self.folders = self.config['folders']
        for folder in self.folders:
            if folder['kind'] not in self.config['kinds']:
                raise ValueError(f"Unknown folder kind: {folder['kind']}")

    @staticmethod
    def source(q):
        """Collection the importer assigned; unchanged by presentation."""
        return q['collection_label'] or (
            q['source_query_id'].split('/')[0] if q['benchmark_id'] == 'local-derived'
            else {'sembench': 'SemBench', 'tag-bench': 'TAG-Bench', 'uda-bench': 'UDA-Bench'}[q['benchmark_id']])

    def match(self, q):
        source = self.source(q)
        hits = [(i, rule) for i, folder in enumerate(self.folders) for rule in folder['sources']
                if (rule.get('collection') == source or ('suffix' in rule and source.endswith(rule['suffix'])))
                and rule.get('category', q['category_label']) == q['category_label']]
        if len(hits) != 1:
            raise ValueError(f"{q['query_id']}: source collection {source!r} matches {len(hits)} folders")
        return hits[0]

    def rank(self, q):
        return self.match(q)[0]

    def place(self, q, detail):
        """Return (folder name, tag); tag None keeps the imported category and group labels."""
        index, rule = self.match(q)
        source, kind = self.source(q), rule.get('tag')
        if kind == 'category':
            tag = q['category_label']
        elif kind == 'subset':
            tag = (detail or {}).get('original_record', {}).get('subset')
            if not tag:
                raise ValueError(f"{q['query_id']}: missing original_record.subset")
        elif kind == 'source':
            tag = source.removesuffix(rule.get('suffix', ''))
        else:
            tag = None
        return self.folders[index]['name'], tag

    def export(self, queries):
        counts = {}
        for q in queries:
            counts[q['collection_name']] = counts.get(q['collection_name'], 0) + 1
        missing = [f['name'] for f in self.folders if f['name'] not in counts]
        if missing:
            raise ValueError(f'Folders without queries: {missing}')
        return {'kinds': self.config['kinds'],
                'folders': {f['name']: {'kind': f['kind'], 'summary': f['summary'], 'papers': f['papers']} for f in self.folders}}
