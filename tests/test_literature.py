"""Literature evidence must never fabricate completed reading or duplicate a paper."""
import json
import sys
import tempfile
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'backend' / 'atlas'))
from literature import LiteratureCatalog


class LiteratureTests(unittest.TestCase):
    def test_merge_preserves_review_and_excludes_unverified_discovery(self):
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory);(root/'config').mkdir()
            def entry(url,status):
                return dict(title='Paper',url=url,venue='arXiv',year=2026,reading_status=status,reading_status_label=status,topics=['Data agents'],evidence=[url])
            rows=[entry('https://paper/one','full_text_reviewed'),entry('https://paper/two','metadata_only'),entry('https://paper/unverified','discovered')]
            (root/'config/literature-catalog.json').write_text(json.dumps(rows))
            papers=[dict(id='original',url='https://paper/one',sections={'motivation':'Detailed source-based reading'})]
            LiteratureCatalog(root,lambda url:url).apply(papers)
            self.assertEqual(len(papers),2)
            self.assertEqual(papers[0]['id'],'original')
            self.assertEqual(papers[0]['sections']['motivation'],'Detailed source-based reading')
            self.assertEqual(set(papers[1]['sections']),{'overview'})
            self.assertEqual(papers[1]['literature_reading_status'],'metadata_only')

if __name__=='__main__':unittest.main()
