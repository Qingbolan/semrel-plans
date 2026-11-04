"""Ensure imported evidence is lossless and never masquerades as executable DAGs."""
import csv
import hashlib
import json
from pathlib import Path
import sys
import unittest
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'backend' / 'atlas'))
from scenario import Catalog


class SuppliedCollectionsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalog = Catalog(ROOT)
        cls.details = {qid: detail for qid, detail in cls.catalog.details.items() if qid.startswith(('8-17/', '7-30/'))}

    def test_full_source_coverage_and_original_records(self):
        for path in (ROOT / 'query/imports/8-17').glob('*.json'):
            original = json.loads(path.read_text())
            original = original['tasks'] if isinstance(original, dict) else original
            for task in original:
                matches = [d for d in self.details.values() if d['query_id'].startswith('8-17/') and d['original_record']['task_id'] == task['task_id']]
                self.assertEqual(len(matches), 1)
                self.assertEqual(matches[0]['original_record'], task)
        for path in (ROOT / 'query/imports/7-30').glob('*_per_query.csv'):
            with path.open() as stream:
                for row in csv.DictReader(stream):
                    self.assertEqual(self.details[f"7-30/{row['benchmark']}/{row['task_id']}"]['original_record'], row)
        self.assertEqual(sum(q['benchmark_id'] == '8-17' for q in self.catalog.tables['queries']), 228)
        self.assertEqual(sum(q['benchmark_id'] == '7-30' for q in self.catalog.tables['queries']), 3120)

    def test_snapshots_match_receipts(self):
        for source in self.catalog.tables['sources']:
            if source['location'].startswith(('query/imports/8-17/', 'query/imports/7-30/')):
                digest = hashlib.sha256((ROOT / source['location']).read_bytes()).hexdigest()
                self.assertIn(digest, source['version'])

    def test_reference_tasks_have_derived_logical_plans(self):
        for query in self.catalog.tables['queries']:
            if query['query_id'] not in self.details:
                continue
            self.assertEqual(query['plan_format'], 'logical_dag')
            nodes, edges = self.catalog.graph(query['query_id'])
            self.assertIn(query['root_node_id'], nodes)
            self.assertIn(query['plan_origin'], ('supplied_reference', 'supplied_analysis'))
        manifest = json.loads((ROOT / 'exports/eal/manifest.json').read_text())
        self.assertGreaterEqual(len(manifest), len(self.details))
        self.assertTrue(set(self.details) <= {e['query_id'] for e in manifest})

    def test_july_data_is_not_claimed_available(self):
        for identity, dataset in self.catalog.datasets.items():
            if identity.startswith('7-30/'):
                self.assertEqual(dataset['availability'], 'not_provided')
                self.assertIsNone(dataset['local_path'])
                self.assertIsNone(dataset['record_count'])

    def test_reference_graph_rejected(self):
        catalog = Catalog(ROOT)
        query = next(q for q in catalog.tables['queries'] if q['query_id'] in self.details)
        query['plan_format'] = 'reference_program'
        query['root_node_id'] = 'invented'
        with self.assertRaisesRegex(ValueError, 'no fabricated graph'):
            catalog.validate()

    def test_inventory_counts_and_declared_inputs(self):
        for identity, dataset in self.catalog.datasets.items():
            if not identity.startswith('8-17/'):
                continue
            inventory = json.loads((ROOT / dataset['inventory_path']).read_text())
            self.assertEqual(dataset['file_count'], len(inventory))
            self.assertEqual(dataset['total_bytes'], sum(f['bytes'] for f in inventory))
            self.assertIsNone(dataset['record_count'])
        inputs = [i for d in self.details.values() for i in d['inputs']]
        self.assertEqual(len(inputs), 385)
        self.assertTrue(all(i['binding_status'] == 'path_verified' for i in inputs))
