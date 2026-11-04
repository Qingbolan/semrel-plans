"""Every sidebar folder is documented, non-empty and links papers that exist."""
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


def asset(name, prefix):
    return json.loads((ROOT / 'assets' / name).read_text().removeprefix(prefix).strip().removesuffix(';'))


class CollectionFoldersTest(unittest.TestCase):
    def test_folders_are_documented_and_papers_resolve(self):
        folders = asset('collections.js', 'window.SEMREL_COLLECTIONS = ')
        papers = {p['id'] for p in asset('papers.js', 'window.SEMREL_PAPERS = ')}
        queries = json.loads((ROOT / 'assets/plans.json').read_text())['queries']
        self.assertEqual({q['collection_name'] for q in queries}, set(folders['folders']))
        for name, info in folders['folders'].items():
            self.assertIn(info['kind'], folders['kinds'])
            self.assertTrue(info['summary']['zh'] and info['summary']['en'], name)
            self.assertLessEqual(set(info['papers']), papers, name)

    def test_derived_and_example_sources_are_merged(self):
        names = {q['collection_name'] for q in json.loads((ROOT / 'assets/plans.json').read_text())['queries']}
        self.assertFalse([n for n in names if n.endswith((' · Derived', ' · Examples'))])


if __name__ == '__main__':
    unittest.main()
