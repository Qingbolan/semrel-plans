"""UDA completeness means every pinned file/ordinal, including repeated SQL."""
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'backend' / 'atlas'))
from sql_source import query_text, sql_statements
from uda_source import UdaSourceCatalog


class SqlSourceTest(unittest.TestCase):
    def test_literals_comments_and_escaped_quotes_do_not_split_statements(self):
        text = "-- Query 1; annotation\nSELECT 'GPT-3; GPT-4', 'it''s; SQL', '--literal';\n/* ; */ SELECT 2; -- end;\n"
        statements = sql_statements(text)
        self.assertEqual(len(statements), 2)
        self.assertEqual(query_text(statements[0]), "SELECT 'GPT-3; GPT-4', 'it''s; SQL', '--literal';")
        self.assertEqual(query_text(statements[1]), 'SELECT 2;')

    def test_incomplete_source_is_rejected(self):
        with self.assertRaises(ValueError):
            sql_statements("SELECT 'unfinished;")


class UdaCoverageTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        commit = json.loads((ROOT / 'config/catalog.json').read_text())['source_commits']['UDA-Bench']
        cls.source = UdaSourceCatalog(ROOT, commit)
        cls.report = json.loads((ROOT / 'exports/uda-source-coverage.json').read_text())
        cls.queries = {q['query_id']: q for q in json.loads((ROOT / 'dist/assets/plans.json').read_text())['queries']
                       if q['collection_name'] == 'UDA-Bench'}

    def test_every_source_occurrence_has_its_own_delivered_query(self):
        self.assertEqual(self.report['sql_files'], 43)
        self.assertEqual(self.report['source_occurrences'], 608)
        self.assertEqual(self.report['distinct_sql'], 602)
        mapping = {r['source_query_id']: r['query_id'] for r in self.report['queries']}
        self.assertEqual(set(mapping), set(self.source.records))
        self.assertEqual(len(set(mapping.values())), 608)
        self.assertEqual(set(mapping.values()), set(self.queries))
        self.assertEqual(self.report['domains'], dict(Art=86, CSPaper=86, Finan=86, Legal=86, Med=132, Player=132))
        for identity, qid in mapping.items():
            query = self.queries[qid]
            self.assertEqual(query['task_record']['query'], self.source.records[identity]['text'])
            self.assertEqual(query['original_query'], self.source.original(identity, qid))
            self.assertTrue((ROOT / 'dist' / query['task_path']).is_file())
            self.assertTrue(query['eal'])

    def test_repeated_sql_preserves_both_ordinals(self):
        mapping = {r['source_query_id']: r['query_id'] for r in self.report['queries']}
        first = mapping['bench-u/CSPaper/Agg/agg_queries_CSPaper/1']
        sixth = mapping['bench-u/CSPaper/Agg/agg_queries_CSPaper/6']
        self.assertNotEqual(first, sixth)
        self.assertEqual(self.queries[first]['task_record']['query'], self.queries[sixth]['task_record']['query'])

    def test_original_six_query_links_are_preserved(self):
        originals = [r for r in self.queries if r.startswith('uda-bench/uda/')]
        self.assertEqual(len(originals), 6)

    def test_incomplete_or_changed_import_cannot_claim_complete_coverage(self):
        records = [dict(id=i, query=r['text']) for i, r in self.source.records.items()]
        self.source.validate_records(records)
        with self.assertRaises(ValueError):
            self.source.validate_records(records[:-1])
        records[0] = dict(records[0], query='SELECT fabricated;')
        with self.assertRaises(ValueError):
            self.source.validate_records(records)
