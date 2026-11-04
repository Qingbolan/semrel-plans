"""Source identity, selection and input/gold separation for the Abacus artifact."""
import json
import sys
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT / 'backend' / 'atlas'))
from query_originals import extract_text

class AbacusImportTests(unittest.TestCase):
 def test_original_queries_match_official_source(self):
  rows=[r for r in map(json.loads,(ROOT/'catalog/original_queries.jsonl').read_text().splitlines()) if r['query_id'].startswith('abacus/')]
  self.assertGreater(len(rows),100)
  for r in rows:self.assertEqual(r['text'],extract_text(ROOT/r['source_path'],r['selector']))
 def test_seeds_are_covered_once_per_distinct_question(self):
  seeds=json.loads((ROOT/'data/abacus/mmqa/selections.json').read_text())
  self.assertEqual(set(seeds),{'0','1','2','3','4','6','8','9'})
  for ids in seeds.values():self.assertEqual(len(ids),100)
  ids={qid for values in seeds.values() for qid in values}
  rows=[r for r in map(json.loads,(ROOT/'catalog/queries.jsonl').read_text().splitlines()) if r['collection_label']=='Abacus MMQA']
  self.assertEqual({r['query_id'].split('/')[-1] for r in rows},ids)
 def test_gold_is_not_passed_as_input(self):
  for line in (ROOT/'data/abacus/mmqa/questions.jsonl').read_text().splitlines():self.assertEqual(set(json.loads(line)),{'qid','question'})
  first=json.loads((ROOT/'data/abacus/biodex/inputs.jsonl').read_text().splitlines()[0]);self.assertEqual(set(first),{'pmid','title','abstract','fulltext'})
  cats=json.loads((ROOT/'environment/abacus/cuad/categories.json').read_text());self.assertEqual(len(cats),41)
 def test_context_resources_and_actual_images_are_present(self):
  manifest=json.loads((ROOT/'data/abacus/mmqa/image-manifest.json').read_text())
  self.assertEqual(len(manifest['images']),450)
  for r in manifest['images']:
   self.assertEqual((ROOT/r['path']).stat().st_size,r['bytes'])
  pools=json.loads((ROOT/'environment/abacus/mmqa/pool-records.json').read_text())
  for part in ['text','table','image']:
   rows=[json.loads(line) for line in (ROOT/f'environment/abacus/mmqa/{part}s.jsonl').read_text().splitlines()]
   ids={r[part+'_id'] for r in rows}
   self.assertEqual(ids,{id for pool in pools.values() for id in pool[part]})
   self.assertTrue(all(set(r)=={part+'_id',part} for r in rows))
 def test_every_query_links_to_abacus_paper(self):
  queries=[r['query_id'] for r in map(json.loads,(ROOT/'catalog/queries.jsonl').read_text().splitlines()) if r['benchmark_id']=='abacus']
  refs=list(map(json.loads,(ROOT/'catalog/query_sources.jsonl').read_text().splitlines()))
  self.assertEqual(set(queries),{r['query_id'] for r in refs if r['source_id']=='abacus_paper' and r['role']=='paper'})

if __name__=='__main__':unittest.main()
