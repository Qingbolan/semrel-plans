"""Run from any directory; requires only Python 3.10+."""
from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'backend' / 'atlas'))
from build import SiteBuilder
if __name__ == '__main__':
    print(f'Built {SiteBuilder(ROOT).build()} query records.')
