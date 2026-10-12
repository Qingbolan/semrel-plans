"""Run from any directory; requires only Python 3.10+."""
from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'src'))
from build import SiteBuilder
if __name__ == '__main__':
    print(f'Built {SiteBuilder(ROOT).build()} query plans.')
