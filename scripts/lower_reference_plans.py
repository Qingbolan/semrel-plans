"""Regenerate logical plans from the immutable supplied reference descriptions."""
import json
from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'src'))
from scenario import Catalog
from reference_plans import lower_collections

if __name__ == '__main__':
    catalog = Catalog(ROOT)
    contracts = [json.loads(line) for line in (ROOT / 'query/input_contracts.jsonl').read_text().splitlines() if line.strip()]
    originals = [json.loads(line) for line in (ROOT / 'query/original_queries.jsonl').read_text().splitlines() if line.strip()]
    tables = dict(catalog.tables, input_contracts=contracts, original_queries=originals)
    lower_collections(tables, catalog.families, ROOT)
    catalog.tables.update(nodes=tables['nodes'], edges=tables['edges'])
    catalog.validate()
    for name in ('queries', 'nodes', 'edges'):
        (ROOT / 'query' / f'{name}.jsonl').write_text(''.join(json.dumps(r, ensure_ascii=False) + '\n' for r in catalog.tables[name]))
    print('Lowered 8-17 and 7-30 reference plans.')
