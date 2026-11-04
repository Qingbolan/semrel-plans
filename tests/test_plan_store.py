import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'backend' / 'atlas'))
from artifacts import write_text_atomic
from plan_store import PlanStore, PlanReadError


class PlanStoreTest(unittest.TestCase):
    def test_invalid_manifest_and_paths_are_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            folder = root / 'exports/eal'
            folder.mkdir(parents=True)
            manifest = folder / 'manifest.json'
            store = PlanStore(root)
            for value in ({}, [None], [{'query_id':'one','path':0}],
                          [{'query_id':'one','path':'../outside.eal'}],
                          [{'query_id':'one','path':'exports/eal/manifest.json'}]):
                write_text_atomic(manifest, json.dumps(value))
                with self.subTest(value=value), self.assertRaises(PlanReadError):
                    store.resolve('one')
            (folder / 'escape.eal').symlink_to(root / 'outside.eal')
            write_text_atomic(manifest, json.dumps([{'query_id':'one','path':'exports/eal/escape.eal'}]))
            with self.assertRaises(PlanReadError):
                store.resolve('one')

    def test_failed_publish_preserves_previous_complete_artifact(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'manifest.json'
            write_text_atomic(path, 'old')
            with patch('artifacts.os.replace', side_effect=OSError('failed')):
                with self.assertRaises(OSError):
                    write_text_atomic(path, 'new')
            self.assertEqual(path.read_text(), 'old')
            self.assertEqual(list(Path(tmp).iterdir()), [path])
            write_text_atomic(path, 'new')
            self.assertEqual(path.read_text(), 'new')
