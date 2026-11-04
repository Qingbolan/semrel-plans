"""Coverage, source preservation and dataset-safe deduplication for project imports."""
import hashlib
import json
from pathlib import Path
import unittest
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1] / 'backend' / 'atlas'))
from workload_import import canonical_url
ROOT=Path(__file__).resolve().parents[1]

class WorkloadImportTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report=json.loads((ROOT/'exports/semantic-workload-import.json').read_text())
        cls.queries={q['query_id']:q for q in json.loads((ROOT/'dist/assets/plans.json').read_text())['queries']}

    def test_complete_atlas_and_public_task_coverage(self):
        self.assertEqual(self.report['atlas_records'],785)
        self.assertEqual(self.report['total_source_records'],len(self.report['queries']))
        self.assertEqual(self.report['added_queries']+self.report['linked_queries']+self.report['superseded_queries'],self.report['total_source_records'])
        self.assertEqual(len({r['source_query_id'] for r in self.report['queries']}),self.report['total_source_records'])
        for item in self.report['queries']:
            q=self.queries[item['query_id']]
            source=json.loads((ROOT/item['record_path']).read_text())
            self.assertEqual(q['task_record']['query'].split(),source['query'].split(),item['source_query_id'])
            self.assertTrue(any(r['location']==item['record_path'] for r in q['provenance']))
            self.assertTrue(any(r['role']=='paper' for r in q['provenance']),item['source_query_id'])

    def test_source_files_match_snapshot_hashes(self):
        for item in self.report['files']:
            self.assertEqual(hashlib.sha256((ROOT/item['path']).read_bytes()).hexdigest(),item['sha256'],item['path'])

    def test_identical_requests_for_different_lakes_remain_separate(self):
        mapping={r['source_query_id']:r['query_id'] for r in self.report['queries']}
        self.assertEqual(len({mapping[f'{lake}-Q4-v1'] for lake in ['stard','annoctr','codiesp','hscodecomp','udrp']}),5)

    def test_papers_and_notes_are_accessible(self):
        papers=json.loads((ROOT/'dist/assets/papers.js').read_text().removeprefix('window.SEMREL_PAPERS = ').strip().removesuffix(';'))
        imported=json.loads((ROOT/'query/imports/semantic-workload-bench/literature.json').read_text())
        for item in imported:
            self.assertEqual(sum(item['source_id'] in p.get('source_ids',[]) for p in papers),1,item['source_id'])
            for doc in item['documents']:self.assertTrue((ROOT/doc).is_file())

    def test_medical_queries_use_their_own_modalities(self):
        q=self.queries['swb/sembench/medical/Q1']
        self.assertEqual([t['name'] for t in q['input_contract']['tables']],['Patient','SymptomsText'])
        self.assertEqual(q['input_contract']['tables'][1]['passed_columns'],['symptom'])
        self.assertEqual(q['input_contract']['environment']['requirement'],'none')
        q=self.queries['swb/sembench/medical/Q10']
        self.assertEqual(q['input_contract']['environment']['requirement'],'required')

    def test_explicit_collections_and_paper_identity(self):
        registry=json.loads((ROOT/'config/workload-registry.json').read_text())
        self.assertEqual(set(registry['queries']),{r['source_query_id'] for r in self.report['queries']})
        for item in self.report['queries']:
            q=self.queries[item['query_id']]
            self.assertNotEqual(q['collection_label'],'semantic-workload-bench')
            if item['status']=='added':
                self.assertEqual(q['collection_label'],registry['queries'][item['source_query_id']]['collection'])
            if item['source_query_id'].startswith('quest/'):
                papers=[r for r in q['provenance'] if r['role']=='paper']
                self.assertEqual(len(papers),1)
                self.assertEqual(papers[0]['location'],'https://arxiv.org/abs/2507.06515')
                self.assertEqual(papers[0]['relationship'],'query_source')

    def test_version_specific_and_derived_attribution(self):
        for q in self.queries.values():
            if not q['query_id'].startswith('swb/'):continue
            papers=[r for r in q['provenance'] if r['role']=='paper']
            if 'audit-20260908-v208/' in q['query_id']:
                self.assertEqual([p['location'] for p in papers],['https://aclanthology.org/2020.mwe-1.14'])
            if 'audit-20260908-v67/' in q['query_id']:
                self.assertEqual([p['location'] for p in papers],['https://arxiv.org/abs/2211.07342'])
            if q['collection_label'].endswith(' · Derived'):
                self.assertTrue(all(p['relationship']=='dataset_origin' for p in papers))

    def test_papers_expose_reading_notes_and_query_links(self):
        papers=json.loads((ROOT/'dist/assets/papers.js').read_text().removeprefix('window.SEMREL_PAPERS = ').strip().removesuffix(';'))
        for paper in papers:
            if paper.get('research_documents'):
                self.assertIn('research',paper['sections'])
                self.assertTrue(all(doc in paper['sections']['research'] for doc in paper['research_documents']))
        quest=next(p for p in papers if canonical_url(p['url'])=='https://arxiv.org/abs/2507.06515')
        self.assertIn('查询与任务清单',quest['sections']['queries'])
        self.assertIn('QUEST',quest['sections']['research'])

    def test_redundant_public_task_versions_fold_into_one_query(self):
        items={r['source_query_id']:r for r in self.report['queries']}
        public=[r for r in items.values() if r['source_query_id'].startswith('public-task/')]
        kept=[r for r in public if r['status']!='superseded']
        self.assertEqual(len(kept),len({r['query_id'] for r in kept}))
        for r in public:
            if r['status']=='superseded':
                target=items[r['superseded_by']]
                self.assertNotEqual(target['status'],'superseded')
                self.assertEqual(r['query_id'],target['query_id'])
                self.assertTrue(any(ref['location']==r['record_path'] for ref in self.queries[r['query_id']]['provenance']))
        for r in kept:
            q=self.queries[r['query_id']]
            self.assertNotIn('/',q['category_label'],r['source_query_id'])
            self.assertEqual({p['type'] for p in q['reference_programs']} if q['plan_format']=='reference_program' else {'task_definition'},{'task_definition'})

    def test_duplicate_publication_urls_share_one_paper(self):
        papers=json.loads((ROOT/'dist/assets/papers.js').read_text().removeprefix('window.SEMREL_PAPERS = ').strip().removesuffix(';'))
        sources={s['location']:s['source_id'] for s in map(json.loads,(ROOT/'query/sources.jsonl').read_text().splitlines()) if s['source_type']=='paper'}
        aliases=json.loads((ROOT/'config/paper-identities.json').read_text())['aliases']
        for alias,canonical in aliases.items():
            pair={sources[url] for url in (alias,canonical) if url in sources}
            if pair:
                self.assertEqual(sum(pair<=set(p.get('source_ids',[])) for p in papers),1,alias)
            matching=[p for p in papers if aliases.get(canonical_url(p['url']),canonical_url(p['url']))==canonical]
            self.assertLessEqual(len(matching),1,alias)

    def test_every_linked_paper_has_a_query_list(self):
        papers=json.loads((ROOT/'dist/assets/papers.js').read_text().removeprefix('window.SEMREL_PAPERS = ').strip().removesuffix(';'))
        linked={r['source_id'] for q in self.queries.values() for r in q['provenance'] if r['role']=='paper'}
        for p in papers:
            if linked.intersection(p.get('source_ids',[])):self.assertIn('queries',p['sections'],p['title'])
