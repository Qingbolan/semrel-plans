from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'src'))
from scenario import Catalog
if __name__ == '__main__':
    print(f'Validated {Catalog(ROOT).validate()} query plans.')
