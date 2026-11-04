from contextlib import closing
import sys
import unittest
import sqlite3
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'backend' / 'atlas'))
from scenario import Catalog

class CatalogIntegrityTest(unittest.TestCase):
    def setUp(self):
        self.catalog = Catalog(ROOT)

    def test_cycle_rejected(self):
        q = self.catalog.tables['queries'][0]
        leaf = next(n for n in self.catalog.tables['nodes'] if n['query_id'] == q['query_id'] and n['operator_type'] == 'SCAN')
        self.catalog.tables['edges'].append({'query_id': q['query_id'], 'parent_id': leaf['node_id'], 'child_id': q['root_node_id'], 'input_position': 0})
        with self.assertRaisesRegex(ValueError, 'Cycle'):
            self.catalog.validate()

    def test_missing_environment_rejected(self):
        self.catalog.tables['queries'][0]['environment_id'] = 'missing'
        with self.assertRaisesRegex(ValueError, 'Missing environment'):
            self.catalog.validate()

    def test_missing_dataset_rejected(self):
        next(iter(self.catalog.environments.values()))['dataset_id'] = 'missing'
        with self.assertRaisesRegex(ValueError, 'Missing dataset'):
            self.catalog.validate()

    def test_unknown_dataset_source_rejected(self):
        next(iter(self.catalog.datasets.values()))['source_ids'] = ['missing']
        with self.assertRaisesRegex(ValueError, 'Unknown dataset source'):
            self.catalog.validate()

    def test_environment_and_input_projection(self):
        for query in self.catalog.queries:
            self.assertEqual(query['environment']['dataset_id'], query['dataset']['dataset_id'])
            if query['query_id'] not in self.catalog.details:
                self.assertTrue(query['inputs'])
                self.assertTrue(all(i['binding_status'] == 'logical_only' for i in query['inputs']))
            self.assertIsNone(query['dataset']['record_count'])
        with closing(sqlite3.connect(ROOT / 'exports/catalog.sqlite')) as db:
            self.assertEqual(db.execute('SELECT COUNT(*) FROM queries q JOIN environments e USING(environment_id) JOIN datasets d USING(dataset_id)').fetchone()[0], len(self.catalog.queries))

    def test_orphan_rejected(self):
        self.catalog.tables['edges'][0]['child_id'] = 'missing'
        with self.assertRaisesRegex(ValueError, 'Dangling'):
            self.catalog.validate()

    def test_unknown_operator_rejected(self):
        self.catalog.tables['nodes'][0]['operator_type'] = 'UNKNOWN'
        with self.assertRaisesRegex(ValueError, 'Unknown operator'):
            self.catalog.validate()

    def test_duplicate_node_rejected(self):
        self.catalog.tables['nodes'].append(self.catalog.tables['nodes'][0].copy())
        with self.assertRaisesRegex(ValueError, 'Duplicate'):
            self.catalog.validate()

    def test_sql_coverage_counts_queries_not_nodes(self):
        with closing(sqlite3.connect(ROOT / 'exports/catalog.sqlite')) as db:
            actual = db.execute("SELECT node_count,query_count FROM operator_statistics WHERE benchmark_id='sembench' AND operator_type='SEM_FILTER'").fetchone()
        qids = {q['query_id'] for q in self.catalog.tables['queries'] if q['benchmark_id'] == 'sembench'}
        nodes = [n for n in self.catalog.tables['nodes'] if n['query_id'] in qids and n['operator_type'] == 'SEM_FILTER']
        self.assertEqual(actual, (len(nodes), len({n['query_id'] for n in nodes})))
        self.assertGreater(actual[0], actual[1])

    def test_dangling_provenance_rejected(self):
        self.catalog.tables['query_sources'][0]['source_id'] = 'missing'
        with self.assertRaisesRegex(ValueError, 'Dangling provenance'):
            self.catalog.validate()

    def test_missing_paper_rejected(self):
        qid = self.catalog.tables['queries'][0]['query_id']
        self.catalog.tables['query_sources'] = [r for r in self.catalog.tables['query_sources'] if not (r['query_id'] == qid and r['role'] == 'paper')]
        with self.assertRaisesRegex(ValueError, 'Missing paper'):
            self.catalog.validate()

    def test_provenance_export_and_projection_coverage(self):
        with closing(sqlite3.connect(ROOT / 'exports/catalog.sqlite')) as db:
            count = db.execute('SELECT COUNT(*) FROM query_sources').fetchone()[0]
            covered = db.execute('SELECT COUNT(DISTINCT query_id) FROM query_sources').fetchone()[0]
        self.assertEqual(count, len(self.catalog.tables['query_sources']))
        self.assertEqual(covered, len(self.catalog.queries))
        self.assertTrue(all(q['provenance'] for q in self.catalog.queries))
