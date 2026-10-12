"""Check exported plans against the real EAL compiler when available."""
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'src'))
from scenario import Catalog
from eal import EalExporter


@unittest.skipUnless(shutil.which('easynet'), 'EasyNet compiler not installed')
class EalCompilerTest(unittest.TestCase):
    def test_all_plans_preserve_nodes_and_ordered_edges(self):
        catalog = Catalog(ROOT)
        manifest = json.loads((ROOT / 'exports/eal/manifest.json').read_text())
        self.assertEqual({e['query_id'] for e in manifest}, {q['query_id'] for q in catalog.tables['queries']})
        for entry in manifest:
            with self.subTest(query=entry['query_id']):
                result = subprocess.run(['easynet', 'mission', 'compile', str(ROOT / entry['path']), '--emit-ir'], capture_output=True, text=True, check=True)
                ir = json.loads(result.stdout)
                nodes, children = catalog.graph(entry['query_id'])
                steps = {s['static_arguments']['node_id']: s for s in ir['steps']}
                self.assertEqual(set(nodes), set(steps))
                binding_nodes = {s['output_binding']: nid for nid, s in steps.items()}
                for nid, step in steps.items():
                    self.assertEqual(step['static_arguments']['label'], nodes[nid]['label'])
                    self.assertEqual(step['ability'], 'semrel.' + nodes[nid]['operator_type'].lower())
                    actual = {int(k.removeprefix('input_')): binding_nodes[v] for k, v in step.get('input_refs', {}).items()}
                    self.assertEqual(actual, {e['input_position']: e['child_id'] for e in children[nid]})

    def test_shared_child_emitted_once_and_string_escaping(self):
        class SharedCatalog:
            families = {'JOIN': 'relational', 'SCAN': 'input'}
            def graph(self, qid):
                return ({'root': {'operator_type': 'JOIN', 'label': 'join'}, 'leaf': {'operator_type': 'SCAN', 'label': 'quote " slash \\ newline\n中文'}}, {'root': [{'child_id': 'leaf', 'input_position': 0}, {'child_id': 'leaf', 'input_position': 1}], 'leaf': []})
        source = EalExporter(SharedCatalog()).render({'query_id': 'shared', 'root_node_id': 'root', 'plan_origin': 'derived_workload'})
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'shared.eal'
            path.write_text(source)
            ir = json.loads(subprocess.run(['easynet', 'mission', 'compile', str(path), '--emit-ir'], capture_output=True, text=True, check=True).stdout)
        self.assertEqual(len(ir['steps']), 2)
        refs = ir['steps'][1]['input_refs']
        self.assertEqual(refs['input_0'], refs['input_1'])
