"""Verify the delivered page carries original records and one coherent asset version."""
import hashlib
import json
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]


class RecordDeliveryTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.queries = {q['query_id']: q for q in json.loads((ROOT / 'dist/assets/plans.json').read_text())['queries']}

    def test_817_task_documents_preserve_every_supplied_field(self):
        for line in (ROOT / 'query/task_details.jsonl').read_text().splitlines():
            detail = json.loads(line)
            if detail['query_id'].startswith('8-17/'):
                self.assertEqual(self.queries[detail['query_id']]['task_record'], detail['original_record'])

    def test_every_query_has_the_817_task_structure_and_download(self):
        fields={'task_id','datasets','query','tags','inputs','reference_semantic_plan','gold','evaluation'}
        for q in self.queries.values():
            record=q['task_record']
            self.assertEqual(set(record),fields,q['query_id'])
            self.assertIsInstance(record['query'],str)
            self.assertIsInstance(record['inputs'],list)
            self.assertTrue(record['reference_semantic_plan'])
            self.assertEqual(json.loads((ROOT/q['task_path']).read_text()),record)
            for source in record['inputs']:
                self.assertTrue({'source_id','dataset','source_type','role'} <= source.keys())

    def test_movie_dag_preserves_both_self_join_dependencies(self):
        record=self.queries['sembench/movie/Q7']['task_record']
        self.assertEqual(record['inputs'][0]['semantic_columns'],['reviewText'])
        self.assertIsNone(record['gold']['gold_answer'])
        self.assertIn('r1',record['reference_semantic_plan'][0]['program'])
        self.assertIn('r2',record['reference_semantic_plan'][0]['program'])

    def test_asset_versions_match_the_built_contents(self):
        html = (ROOT / 'dist/index.html').read_text()
        resources = re.findall(r'(?:src|href)="((?:viewer/|assets/)[^?\"]+)\?v=([a-f0-9]+)"', html)
        self.assertTrue(resources)
        revision = hashlib.sha256(b''.join((ROOT / 'dist' / path).read_bytes() for path, _ in resources)).hexdigest()[:12]
        self.assertEqual({version for _, version in resources}, {revision})
        self.assertIn(f'window.SEMREL_BUILD = "{revision}"', html)

    def test_numbers_are_contiguous_within_each_collection(self):
        collections = {}
        for q in self.queries.values():
            self.assertIsInstance(q['display_number'], int)
            collections.setdefault(q['collection_name'], []).append(q['display_number'])
        for numbers in collections.values():
            self.assertEqual(numbers, list(range(1, len(numbers) + 1)))
        self.assertEqual(len(collections['SemBench']), 70)
        self.assertEqual(len(collections['8-17']), 228)
        self.assertEqual(len(collections['7-30']), 3120)

class InputContractDeliveryTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.queries = {q['query_id']: q for q in json.loads((ROOT / 'dist/assets/plans.json').read_text())['queries']}

    def test_zebra_count_receives_images_without_context_data(self):
        contract = self.queries['sembench/animals/Q1']['input_contract']
        self.assertEqual(contract['environment']['requirement'], 'none')
        self.assertEqual(len(contract['tables']), 1)
        table = contract['tables'][0]
        self.assertEqual(table['passed_columns'], ['image'])
        self.assertEqual(table['columns'], [{'name': 'image', 'type': 'image'}])
        self.assertEqual(contract['output']['columns'], ['count'])
        self.assertTrue((ROOT / contract['evidence']['path']).is_file())

    def test_grouping_column_is_not_a_model_input(self):
        table = self.queries['sembench/animals/Q3']['input_contract']['tables'][0]
        self.assertIn('City', [c['name'] for c in table['columns']])
        self.assertEqual(table['passed_columns'], ['image'])

    def test_missing_contract_is_not_declared_context_free(self):
        contract = self.queries['sembench/mmqa/q5']['input_contract']
        self.assertEqual(contract['environment']['requirement'], 'unspecified')
