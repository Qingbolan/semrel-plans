import sys
import unittest
import sqlite3
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'src'))
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
        with sqlite3.connect(ROOT / 'exports/catalog.sqlite') as db:
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
        with sqlite3.connect(ROOT / 'exports/catalog.sqlite') as db:
            count = db.execute('SELECT COUNT(*) FROM query_sources').fetchone()[0]
            covered = db.execute('SELECT COUNT(DISTINCT query_id) FROM query_sources').fetchone()[0]
        self.assertEqual(count, len(self.catalog.tables['query_sources']))
        self.assertEqual(covered, len(self.catalog.queries))
        self.assertTrue(all(q['provenance'] for q in self.catalog.queries))
