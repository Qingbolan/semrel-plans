"""Query data requirements, independent of execution configuration."""
import json
import csv
from collections import Counter


class InputContracts:
    def __init__(self, root, query_ids):
        rows = [json.loads(line) for line in (root / 'catalog/input_contracts.jsonl').read_text().splitlines() if line.strip()]
        self.records = {row['query_id']: row for row in rows}
        if len(rows) != len(self.records) or self.records.keys() != query_ids:
            raise ValueError('Input contracts must cover every query exactly once')
        for row in rows:
            if row['environment']['requirement'] not in {'none', 'required', 'unspecified'}:
                raise ValueError('Invalid environment requirement')
            for table in row['tables']:
                if not set(table['passed_columns'] or []) <= {c['name'] for c in table['columns']}:
                    raise ValueError('Passed column missing from input table')

    def project(self, query):
        return self.records[query['query_id']]

    def export(self, root, queries):
        with (root/'exports/query_inputs.csv').open('w',newline='') as stream:
            writer=csv.writer(stream)
            writer.writerow(['query_id','question','environment_requirement','context_resources','input_tables','columns','semantic_columns','audit_status','notes','source'])
            for q in queries:
                c=self.records[q['query_id']]
                writer.writerow([q['query_id'],q['title'],c['environment']['requirement'],json.dumps(c['environment']['resources'],ensure_ascii=False),json.dumps([t['name'] for t in c['tables']],ensure_ascii=False),json.dumps({t['name']:[x['name'] for x in t['columns']] for t in c['tables']},ensure_ascii=False),json.dumps({t['name']:t['passed_columns'] for t in c['tables']},ensure_ascii=False),c['audit_status'],'; '.join(c['notes']),c['evidence']['path']])
        records=list(self.records.values())
        summary={'total':len(records),'states':dict(Counter(c['audit_status'] for c in records)),'issues':[{'query_id':c['query_id'],'status':c['audit_status'],'notes':c['notes']} for c in records if c['audit_status'] in ['source_gap','version_mismatch']]}
        (root/'exports/input_audit.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
        return summary
