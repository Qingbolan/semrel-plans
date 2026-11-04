"""Check every delivered query against its selected source field."""
import json
import sys
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT / 'backend' / 'atlas'))
from query_originals import extract_text

class QueryOriginalTest(unittest.TestCase):
    def test_all_source_fields_and_delivered_records(self):
        records=[json.loads(s) for s in (ROOT/'query/original_queries.jsonl').read_text().splitlines()]
        delivered={q['query_id']:q for q in json.loads((ROOT/'dist/assets/plans.json').read_text())['queries']}
        self.assertEqual(len(records),len(delivered))
        self.assertGreaterEqual(len(records),3436)
        self.assertEqual(len({r['query_id'] for r in records}),len(records))
        for record in records:
            qid=record['query_id']
            self.assertEqual(extract_text(ROOT/record['source_path'],record['selector']),record['text'],qid)
            self.assertEqual(delivered[qid]['task_record']['query'],record['text'],qid)
            self.assertEqual(delivered[qid]['original_query'],record,qid)
        movie=delivered['sembench/movie/Q7']
        self.assertTrue(movie['task_record']['query'].startswith('All Pairs of reviews'))
        self.assertNotEqual(movie['task_record']['query'],movie['title'])
        mismatches=[r for r in records if (r['upstream_comparison'] or {}).get('status')=='version_mismatch']
        self.assertEqual(len(mismatches),3)
