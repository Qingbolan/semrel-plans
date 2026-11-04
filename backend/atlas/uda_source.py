"""Pinned UDA source occurrences, keyed by file and ordinal rather than SQL text."""
import hashlib
import json
from pathlib import Path

from sql_source import query_text, sql_statements


class UdaSourceCatalog:
    def __init__(self, root, commit):
        self.root = Path(root)
        self.base = Path('upstream/snapshots/unimib-datAI/UDA-Bench') / commit
        self.manifest = json.loads((self.root / self.base / 'manifest.json').read_text())
        if self.manifest['commit'] != commit:
            raise ValueError('UDA snapshot commit mismatch')
        expected = {entry['path'] for entry in self.manifest['files']}
        actual = {p.relative_to(self.root / self.base).as_posix()
                  for p in (self.root / self.base / 'Query').rglob('*.sql')}
        if expected != actual or len(expected) != len(self.manifest['files']):
            raise ValueError('UDA snapshot SQL file inventory mismatch')
        self.records = {}
        for entry in self.manifest['files']:
            path = self.base / entry['path']
            content = (self.root / path).read_bytes()
            if hashlib.sha256(content).hexdigest() != entry['sha256']:
                raise ValueError('UDA source hash mismatch: ' + str(path))
            for index, statement in enumerate(sql_statements(content.decode())):
                identity = self.identity(entry['path'], index)
                if identity in self.records:
                    raise ValueError('Duplicate UDA source occurrence: ' + identity)
                self.records[identity] = dict(
                    identity=identity, path=path.as_posix(), index=index,
                    text=query_text(statement), sha256=entry['sha256'],
                    url=f"{self.manifest['repository']}/blob/{commit}/{entry['path']}")

    @staticmethod
    def identity(path, index):
        relative = str(path).split('Query/', 1)[1]
        return f'bench-u/{Path(relative).with_suffix("").as_posix()}/{index + 1}'

    def existing(self, originals):
        result = {}
        for row in originals:
            if not row['query_id'].startswith('uda-bench/'):
                continue
            identity = self.identity(row['source_path'], row['selector']['index'])
            if identity not in self.records or identity in result:
                raise ValueError('Invalid existing UDA source occurrence: ' + identity)
            result[identity] = row['query_id']
        return result

    def validate_records(self, records):
        selected = [r for r in records if r['id'].startswith('bench-u/')]
        if len(selected) != len(self.records) or {r['id'] for r in selected} != set(self.records):
            raise ValueError('UDA imported records do not cover the pinned source occurrences')
        for record in selected:
            source = self.records[record['id']]
            if record['query'].split() != source['text'].split():
                raise ValueError('UDA imported SQL differs from pinned source: ' + record['id'])

    def original(self, identity, query_id):
        source = self.records[identity]
        return dict(query_id=query_id, text=source['text'], kind='sql',
                    verification='pinned_repository_source', source_path=source['path'],
                    selector={'type': 'sql_query', 'index': source['index']},
                    source_sha256=source['sha256'],
                    text_sha256=hashlib.sha256(source['text'].encode()).hexdigest(),
                    upstream_comparison={'status': 'matched', 'commit': self.manifest['commit'],
                                         'url': source['url'], 'source_query_id': identity})

    def coverage(self, imported):
        mapping = {r['source_query_id']: r['query_id'] for r in imported
                   if r['source_query_id'] in self.records}
        if set(mapping) != set(self.records) or len(set(mapping.values())) != len(self.records):
            raise ValueError('UDA source occurrences must map one-to-one to catalog queries')
        counts = {}
        for identity in self.records:
            domain = identity.split('/')[1]
            counts[domain] = counts.get(domain, 0) + 1
        return dict(repository=self.manifest['repository'], commit=self.manifest['commit'],
                    checked_on=self.manifest['checked_on'], sql_files=len(self.manifest['files']),
                    source_occurrences=len(self.records), catalog_queries=len(mapping),
                    distinct_sql=len({(r['identity'].split('/')[1], ' '.join(r['text'].split()))
                                      for r in self.records.values()}), domains=counts,
                    paper_scope={'version': '2510.27119v1', 'datasets': 5, 'queries': 240,
                                 'query_mapping': 'not_established'},
                    queries=[dict(source_query_id=identity, query_id=mapping[identity],
                                  source_path=r['path'], selector={'type': 'sql_query', 'index': r['index']},
                                  source_sha256=r['sha256'], url=r['url'])
                             for identity, r in self.records.items()])
