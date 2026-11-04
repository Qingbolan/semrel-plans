import sys
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT / 'backend' / 'atlas'))
from scenario import Catalog
from groups import query_groups

class QueryGroupsTest(unittest.TestCase):
    def test_groups_use_explicit_evidence_and_allow_overlap(self):
        catalog=Catalog(ROOT)
        groups=query_groups(catalog)['memberships']
        self.assertEqual(set(groups['local-derived/derived/ContractNLI/conjunction']),{'nlp-tasks','sem-operator'})
        self.assertIn('sem-operator',groups['sembench/movie/Q1'])
        self.assertNotIn('nlp-tasks',groups['sembench/movie/Q1'])
        self.assertNotIn('7-30/FDABench/FDA0669',groups)
        self.assertIn('sem-operator',groups['7-30/DABstep/1712'])
        self.assertIn('sem-operator',groups['8-17/SEC10K/SEC10K-001'])
