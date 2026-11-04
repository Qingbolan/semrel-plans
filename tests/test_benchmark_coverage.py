"""Coverage counts come from the catalog; new papers are added once, existing ones are annotated."""
import json
import sys
import tempfile
import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'src'))
from benchmark_coverage import BenchmarkCoverage


class BenchmarkCoverageTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        for d in ('config', 'query', 'docs'):
            (self.root / d).mkdir()
        queries = [dict(query_id=f't{i}', benchmark_id='tag', scenario_id='tag', mixed_label='实质混合') for i in range(3)]
        queries.append(dict(query_id='x', benchmark_id='7-30', scenario_id='7-30-DAB', mixed_label=''))
        queries.append(dict(query_id='y', benchmark_id='7-30', scenario_id='7-30-Other', mixed_label=''))
        (self.root / 'query/queries.jsonl').write_text('\n'.join(json.dumps(q) for q in queries) + '\n')
        repo = [dict(url='https://github.com/a/b', commit='0123456789', link_source='论文原文')]
        entries = [
            dict(key='tag', group='benchmark', paper_id='p1', repositories=repo, query_scale='5', scale_source='摘要',
                 catalog=[dict(benchmark_id='tag')], expected_queries=5, status_note='', mixed='yes', mixed_note=''),
            dict(key='dab', group='agent', paper_id='p2', repositories=[], query_scale='?', scale_source='摘要',
                 catalog=[dict(benchmark_id='7-30', scenario_id='7-30-DAB')], status='partial', status_note='', mixed='unknown', mixed_note=''),
            dict(key='new', group='benchmark', title='New', url='https://arxiv.org/abs/1', venue='arXiv', year=2026, kind='benchmark',
                 repositories=[], query_scale='9', scale_source='摘要', catalog=[], expected_queries=9, status_note='', mixed='no', mixed_note=''),
        ]
        (self.root / 'config/benchmark-coverage.json').write_text(json.dumps(dict(
            checked_on='2026-11-03', scope='s', groups=dict(benchmark='A', agent='C'), entries=entries)))

    def tearDown(self):
        self.tmp.cleanup()

    def test_counts_status_and_new_records(self):
        papers = [dict(id='p1', title='Tag', venue='CIDR', year='2025', url='https://tag', sections={'overview': 'x'}),
                  dict(id='p2', title='Dab', venue='arXiv', year='2026', url='https://dab', sections={'overview': 'x'})]
        BenchmarkCoverage(self.root, lambda u: u).apply(papers)
        self.assertEqual(len(papers), 3)
        self.assertIn('已收录 3/5 条', papers[0]['sections']['coverage'])
        self.assertIn('◐ 部分', papers[0]['sections']['coverage'])
        self.assertEqual(papers[0]['repositories'][0]['commit'], '0123456789')
        self.assertIn('| 图册已收录 | 1 条', papers[1]['sections']['coverage'])
        self.assertEqual(papers[2]['kind'], 'benchmark')
        self.assertIn('✗ 未收录', papers[2]['sections']['coverage'])
        table = (self.root / 'docs/benchmark-coverage.md').read_text()
        self.assertEqual(table.count('| [Tag]'), 1)
        self.assertIn('## C', table)
        self.assertIn('无逻辑 DAG', papers[0]['sections']['coverage'])

    def test_dag_mixed_ignores_structural_nodes(self):
        (self.root / 'config/operators.json').write_text(json.dumps([
            dict(operator_type='SEM_FILTER', family='semantic'), dict(operator_type='PROJECT', family='relational'),
            dict(operator_type='JOIN', family='relational'), dict(operator_type='SCAN', family='input')]))
        rows = [dict(query_id='t0', node_id='a', operator_type='SEM_FILTER'), dict(query_id='t0', node_id='b', operator_type='JOIN'),
                dict(query_id='t1', node_id='a', operator_type='SEM_FILTER'), dict(query_id='t1', node_id='b', operator_type='PROJECT')]
        (self.root / 'query/nodes.jsonl').write_text('\n'.join(json.dumps(r) for r in rows) + '\n')
        self.assertEqual(BenchmarkCoverage(self.root, lambda u: u).dag_mixed, {'t0'})

    def test_unknown_paper_id_fails(self):
        with self.assertRaises(ValueError):
            BenchmarkCoverage(self.root, lambda u: u).apply([])

    def test_registry_entries_are_unique_and_complete(self):
        registry = json.loads((ROOT / 'config/benchmark-coverage.json').read_text())
        keys = [e['key'] for e in registry['entries']]
        self.assertEqual(len(keys), len(set(keys)))
        for e in registry['entries']:
            self.assertTrue(e.get('paper_id') or e.get('url'), e['key'])
            self.assertTrue('status' in e or 'expected_queries' in e, e['key'])
            self.assertIn(e['mixed'], {'yes', 'partial', 'no', 'unknown'})


if __name__ == '__main__':
    unittest.main()
