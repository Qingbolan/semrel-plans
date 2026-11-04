"""Check coverage and concrete source bindings, not merely renderer structure."""
import json
from pathlib import Path
import sys
import unittest
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT / 'backend' / 'atlas'))
from input_contracts import InputContracts

class InputContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.queries={json.loads(x)['query_id'] for x in (ROOT/'catalog/queries.jsonl').read_text().splitlines()}
        cls.contracts=InputContracts(ROOT,cls.queries).records

    def test_every_query_has_its_own_source_evidence(self):
        self.assertEqual(len(self.contracts),len(self.queries))
        self.assertGreaterEqual(len(self.contracts),3436)
        for qid,c in self.contracts.items():
            self.assertTrue((ROOT/c['evidence']['path']).is_file(),qid)
            self.assertTrue(c['tables'],qid)
            self.assertNotIn('engine',c['environment'])

    def test_movie_self_join_passes_two_reviews_from_same_table(self):
        c=self.contracts['sembench/movie/Q7']
        self.assertEqual(c['environment']['requirement'],'none')
        self.assertEqual(len(c['tables']),1)
        self.assertEqual(c['tables'][0]['name'],'movie.reviews')
        self.assertEqual(c['tables'][0]['passed_columns'],['reviewText'])
        self.assertIn('r1.reviewText',c['notes'][0])
        self.assertIn('r2.reviewText',c['notes'][0])

    def test_audio_column_keeps_source_name_and_audio_type(self):
        c=self.contracts['sembench/cars/Q2']
        t=next(t for t in c['tables'] if t['name']=='cars_dataset.audio_mm')
        self.assertEqual(t['passed_columns'],['image'])
        self.assertEqual(next(col['type'] for col in t['columns'] if col['name']=='image'),'audio')

    def test_fee_task_requires_manual(self):
        c=self.contracts['7-30/DABstep/1712']
        self.assertEqual(c['environment']['requirement'],'required')
        self.assertEqual(c['environment']['resources'][0]['name'],'manual.md')
        t=next(t for t in c['tables'] if t['name']=='payments.csv')
        self.assertIn('eur_amount',[col['name'] for col in t['columns']])

    def test_survey_files_are_not_claimed_as_minimal_query_reads(self):
        c=self.contracts['7-30/LongDA/Annual Survey of State Government Finances Summary: 2021:1']
        self.assertEqual(c['environment']['requirement'],'required')
        self.assertEqual([t['name'] for t in c['tables']],['ASFIN/data/21state35.txt'])
        self.assertTrue(any('itemcodes.xlsx' in r['name'] for r in c['environment']['resources']))

    def test_empty_source_is_explicit_and_not_invented(self):
        c=self.contracts['sembench/mmqa/q5']
        self.assertEqual(c['audit_status'],'source_gap')
        self.assertEqual(c['environment']['requirement'],'unspecified')

    def test_fda_uses_matching_historical_question(self):
        details=[json.loads(x) for x in (ROOT/'catalog/task_details.jsonl').read_text().splitlines()]
        for d in details:
            if d['query_id'].startswith('7-30/FDABench/'):
                self.assertEqual(self.contracts[d['query_id']]['upstream_record']['query'],d['original_record']['query'])
