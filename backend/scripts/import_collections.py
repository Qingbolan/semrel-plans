"""Import the two supplied local collections; large corpora remain externally bound."""
import argparse
from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'backend' / 'atlas'))
from imports import CollectionImporter

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--august', type=Path, required=True)
    parser.add_argument('--july', type=Path, required=True)
    args = parser.parse_args()
    importer = CollectionImporter(ROOT)
    importer.import_august(args.august)
    importer.import_july(args.july)
    importer.save()
    print('Imported 8-17 and 7-30 with source snapshots and local data bindings.')
