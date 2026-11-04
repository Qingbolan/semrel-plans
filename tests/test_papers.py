import hashlib
import json
from pathlib import Path
import sys
import unittest
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'backend' / 'atlas'))
from papers import PaperExporter, SECTIONS

ROOT = Path(__file__).resolve().parents[1]

class PaperTests(unittest.TestCase):
    def test_snapshot_and_usecases(self):
        manifest = json.loads((ROOT / 'papers/survey/manifest.json').read_text())
        self.assertTrue(manifest)
        self.assertEqual(len(manifest), len({p['folder'] for p in manifest}))
        for paper in manifest:
            folder = ROOT / 'papers/survey' / paper['folder']
            for filename, digest in paper['sha256'].items():
                self.assertEqual(digest, hashlib.sha256((folder / filename).read_bytes()).hexdigest())
            for filename in SECTIONS.values():
                self.assertTrue((folder / filename).read_text().strip())
            workload = (folder / 'workload分析.md').read_text()
            case_file = folder / 'usecase分析.md'
            case = case_file.read_text() if case_file.exists() else PaperExporter.usecase(workload)
            self.assertTrue(case, paper['folder'])
            if not case_file.exists():
                self.assertIn(case, workload)

    def test_benchmark_retains_evaluation_evidence(self):
        for entry in json.loads((ROOT / 'papers/survey/manifest.json').read_text()):
            workload = (ROOT / 'papers/survey' / entry['folder'] / 'workload分析.md').read_text()
            benchmark = PaperExporter.benchmark(workload)
            self.assertTrue(benchmark.startswith('# Benchmark'))
            case = PaperExporter.usecase(workload)
            if case:
                self.assertNotIn(case, benchmark)
            for paragraph in workload.split('\n\n'):
                if paragraph.strip() and not paragraph.startswith('# ') and paragraph.strip() not in case:
                    self.assertIn(paragraph.strip(), benchmark)

    def test_preserves_caveats_before_baseline(self):
        source = '# Workload\n\n## 具体用例\n\nInput and output.\n\nNo single-case speedup reported.\n\n## Baseline\nOther text.'
        case = PaperExporter.usecase(source)
        self.assertIn('No single-case speedup reported.', case)
        self.assertNotIn('Other text.', case)
        self.assertEqual('', PaperExporter.usecase('# Workload\nNo case reported.'))

    def test_dedicated_reading_sections(self):
        records = PaperExporter(ROOT).export()
        eddies = next(p for p in records if p['title'].startswith('Eddies:'))
        folder = ROOT / 'papers/survey' / eddies['folder']
        self.assertEqual((folder / 'usecase分析.md').read_text(), eddies['usecase'])
        self.assertEqual((folder / 'benchmark分析.md').read_text(), eddies['sections']['benchmark'])
        self.assertNotEqual(eddies['sections']['benchmark'], eddies['sections']['workload'])

if __name__ == '__main__':
    unittest.main()
