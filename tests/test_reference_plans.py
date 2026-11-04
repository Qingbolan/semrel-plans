"""Reference notation contracts: branch identity, opaque text, and repeatable lowering."""
import json
from pathlib import Path
import sys
import unittest
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'backend' / 'atlas'))
from reference_plans import ReferencePlan, PlanSyntaxError, lower_collections

OPS = {o['operator_type'] for o in json.loads((ROOT / 'config/operators.json').read_text())}

class ReferencePlansTest(unittest.TestCase):
    def parse(self, source):
        plan = ReferencePlan('test', OPS)
        root = plan.parse(source)
        return plan, root

    def test_shared_branch_and_multiple_results(self):
        plan, root = self.parse('SCAN_TABLE(data) AS base ||| base -> FILTER(x > 0) AS positive ||| base -> FILTER(x < 0) AS negative')
        self.assertEqual(len(plan.nodes), 4)
        self.assertEqual(plan.nodes[-1]['operator_type'], 'PROJECT')
        self.assertEqual([e['child_id'] for e in plan.edges if e['parent_id'] == root], ['ref_001', 'ref_002'])
        self.assertEqual(sum(e['child_id'] == 'ref_000' for e in plan.edges), 2)

    def test_join_does_not_reintroduce_ancestor_as_third_input(self):
        plan, root = self.parse('a = SCAN_TABLE(a); b = SCAN_TABLE(b); c = SCAN_TABLE(c); a -> JOIN(b, a.id=b.id) -> JOIN(c, a.id=c.id)')
        self.assertEqual([e['child_id'] for e in plan.edges if e['parent_id'] == root], ['ref_003', 'ref_002'])

    def test_nested_join_and_ordered_ports(self):
        plan, root = self.parse('SCAN_TABLE(a) -> JOIN(left, right=(SCAN_TABLE(b) -> FILTER(ok)))')
        self.assertEqual(plan.nodes[-1]['operator_type'], 'LEFT_JOIN')
        self.assertEqual([e['child_id'] for e in plan.edges if e['parent_id'] == root], ['ref_000', 'ref_002'])

    def test_assignment_and_reverse_arrow(self):
        plan, root = self.parse('a := (SCAN_TABLE(a))\nb := (SCAN_TABLE(b))\na -> JOIN(inner, a.id=b.id) <- b')
        self.assertEqual([e['child_id'] for e in plan.edges if e['parent_id'] == root], ['ref_000', 'ref_001'])

    def test_expression_delimiters_and_apostrophe_are_opaque(self):
        label = "SEM_EXTRACT('company's business -> strategy; [x]', {name:string})"
        plan, _ = self.parse('SCAN_DOCS(data) -> ' + label + ' -> PROJECT(case(a -> 1; else 0))')
        self.assertEqual(len(plan.nodes), 3)
        # The output schema is plumbing and leaves the label; the quoted prompt stays intact.
        self.assertEqual(plan.nodes[1]['label'], "SEM_EXTRACT('company's business -> strategy; [x]')")

    def test_unknown_notation_fails_instead_of_fabricating_a_stage(self):
        with self.assertRaises(PlanSyntaxError):
            self.parse('invent missing details')
        with self.assertRaises(PlanSyntaxError):
            self.parse('SCAN_TABLE(unclosed')

    def test_full_reference_lowering_is_reproducible(self):
        tables = {name: [json.loads(line) for line in (ROOT / 'catalog' / (name + '.jsonl')).read_text().splitlines()] for name in ('queries','nodes','edges','task_details','input_contracts','original_queries')}
        original = json.loads(json.dumps(tables))
        lower_collections(tables, OPS, ROOT)
        self.assertEqual(tables, original)
        # The 7-30 annotation supplies no finer relational steps.
        plan, _ = self.parse('relational/SQL/Python analysis only')
        self.assertEqual(len(plan.nodes), 1)
        self.assertEqual(plan.nodes[0]['operator_type'], 'COMPUTE')
