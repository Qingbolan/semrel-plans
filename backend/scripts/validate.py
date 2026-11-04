from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'backend' / 'atlas'))
from scenario import Catalog
if __name__ == '__main__':
    print(f'Validated {Catalog(ROOT).validate()} query records.')
