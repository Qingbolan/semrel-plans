"""The repository must stay self-contained: no data or document may point into a sibling checkout."""
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'backend' / 'scripts'))
import vendor_upstream


class PortablePathTests(unittest.TestCase):
    def test_no_absolute_workspace_paths(self):
        markers = {vendor_upstream.WORKSPACE, '/'.join(['', 'Volumes', 'Element', 'Github2', ''])}
        offenders = [path.relative_to(ROOT).as_posix() for path in vendor_upstream.text_files()
                     if any(marker in path.read_text(errors='ignore') for marker in markers)]
        self.assertEqual([], offenders[:20], 'Run python3 backend/scripts/vendor_upstream.py')


if __name__ == '__main__':
    unittest.main()
