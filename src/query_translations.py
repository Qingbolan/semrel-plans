"""Query-title translations keyed by stable identity and checked against source text."""
import hashlib
import json
from pathlib import Path


class QueryTranslations:
    def __init__(self, root, queries):
        self.records = json.loads((Path(root) / 'config/translations/queries-zh.json').read_text())
        titles = {q['query_id']: q['title'] for q in queries}
        required = {qid for qid, q in ((q['query_id'], q) for q in queries) if q['benchmark_id'] in ('8-17', '7-30')}
        if not required <= set(self.records) or not set(self.records) <= set(titles):
            raise ValueError('Chinese query translations do not cover the current collections')
        for qid in self.records:  # 8-17/7-30 are required; SQL-titled benchmarks may add generated summaries
            source = titles[qid]
            entry = self.records[qid]
            if entry['source'] != source or entry['source_sha256'] != hashlib.sha256(source.encode()).hexdigest():
                raise ValueError(f'Stale Chinese query translation: {qid}')
            if not isinstance(entry['zh'], str) or not entry['zh'].strip():
                raise ValueError(f'Empty Chinese query translation: {qid}')

    def by_source(self):
        result = {}
        for entry in self.records.values():
            source, target = entry['source'], entry['zh']
            if source in result and result[source] != target:
                raise ValueError('Conflicting translations for identical query text')
            result[source] = target
        return result
