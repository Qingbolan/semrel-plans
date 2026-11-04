"""Verify evidence-backed reviews preserve query provenance when published."""
import copy
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'backend' / 'atlas'))
from paper_reviews import PaperReviews, REVIEW_SECTIONS
from papers import PaperExporter


class PaperReviewTests(unittest.TestCase):
    def setUp(self):
        self.publisher = PaperReviews(ROOT, PaperExporter(ROOT).identity)
        self.records = [dict(url=e['url'], sections={'queries': 'existing query provenance'})
                        for e in self.publisher.entries]

    def test_complete_reviews_preserve_query_provenance(self):
        self.publisher.apply(self.records)
        for paper, entry in zip(self.records, self.publisher.entries):
            self.assertTrue(set(REVIEW_SECTIONS) <= paper['sections'].keys())
            self.assertEqual('existing query provenance', paper['sections']['queries'])
            self.assertEqual(paper['usecase'], paper['sections']['usecase'])
            self.assertTrue(entry['evidence'])
            self.assertTrue(all(e['locator'] for e in entry['evidence']))
            self.assertTrue(all(e['basis'] in {'explicit', 'inference'} for e in entry['evidence']))
            if entry['status'] == 'EVIDENCE_CHECKED':
                self.assertTrue(entry['reviewer'])
                self.assertNotEqual(entry['reader'], entry['reviewer'])
                self.assertTrue(entry['checked_evidence'])

    def test_changed_source_cannot_publish(self):
        self.publisher.entries = copy.deepcopy(self.publisher.entries[:1])
        self.publisher.entries[0]['sha256'] = '0' * 64
        with self.assertRaisesRegex(ValueError, 'Changed paper source'):
            self.publisher.apply(self.records)

    def test_incomplete_reading_cannot_publish(self):
        self.publisher.entries = copy.deepcopy(self.publisher.entries[:1])
        self.publisher.entries[0]['status'] = 'FULLTEXT_ACQUIRED'
        with self.assertRaisesRegex(ValueError, 'Only completed readings'):
            self.publisher.apply(self.records)

    def test_queue_completion_matches_published_reviews(self):
        queue = json.loads((ROOT / 'papers/readings/queue.json').read_text())['papers']
        identity = self.publisher.identity
        published = {identity(e['url']) for e in self.publisher.entries}
        completed = {identity(e['url']) for e in queue if e['status'] in {'READ', 'EVIDENCE_CHECKED'}}
        self.assertEqual(published, completed)


if __name__ == '__main__':
    unittest.main()
