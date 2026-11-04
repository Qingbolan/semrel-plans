"""Raw datasets may contain their own manifest.json without joining the atlas catalog."""
import json
from pathlib import Path
import sys
import tempfile
import unittest
sys.path.insert(0,str(Path(__file__).resolve().parents[1] / 'backend' / 'atlas'))
from scenario import Catalog

class ManifestOwnershipTest(unittest.TestCase):
    def test_only_referenced_manifests_are_loaded(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            for name in ['data/active','data/source-inputs/foreign']:(root/name).mkdir(parents=True)
            (root/'data/active/manifest.json').write_text(json.dumps({'dataset_id':'active'}))
            (root/'data/source-inputs/foreign/manifest.json').write_text('{"foreign_schema":true}')
            catalog=object.__new__(Catalog);catalog.root=root
            self.assertEqual(catalog.load_manifests('data','dataset_id',{'active'}),{'active':{'dataset_id':'active'}})
            (root/'data/active/manifest.json').write_text('{"dataset_id":"wrong"}')
            with self.assertRaises(ValueError):catalog.load_manifests('data','dataset_id',{'active'})

if __name__=='__main__':unittest.main()
