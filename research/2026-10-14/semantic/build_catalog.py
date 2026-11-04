import json
from pathlib import Path
R=Path(__file__).parent
m=json.loads((R/'metadata.json').read_text());reviews={x['key']:x for x in json.loads((R/'review_index.json').read_text())}
full={'2407.11418':'lotus','2410.12189':'docetl','2505.14661':'abacus','2507.06515':'quest'}
topics=['semantic-operator-model','declarative-ai-analytics','agentic-document-rewriting','constrained-physical-optimization','instance-optimized-extraction','multimodal-query-planning','adaptive-semantic-sql','hybrid-operator-placement','hybrid-question-answering','unstructured-analytics-system','unstructured-query-engine','output-quality-semantics','compiled-semantic-execution','learned-predicate-ordering','document-analytics','batched-semantic-join','llm-as-database','kv-cache-batch-analytics','agentic-logical-optimization','semantic-join-decomposition','in-database-llm-functions','schema-extraction','multiobjective-agentic-rewrites','semantic-query-benchmark']
rows=[]
for x,t in zip(m,topics):
 r=dict(title=x['citation_title'],url=x['url'],year=int(x['citation_date'][:4]),venue='arXiv',topic=t,reading_status='abstract_only',evidence=[x['url'],str(R/'metadata.json')],review_folder=None,first_submitted=x['citation_date'],checked_on='2026-10-14')
 if x['id'] in full:
  v=reviews[full[x['id']]]
  r.update({k:v[k] for k in ['title','url','year','venue','reading_status','review_folder']})
  r['evidence']=[v['url'],str(R/'pdfs'/f"{v['key']}.pdf"),v['loc']]
  r['pdf_sha256']=v['pdf_sha256']
  if v['key']=='quest':r['venue']='PVLDB';r['publication_url']='https://www.vldb.org/pvldb/vol18/p4560-chai.pdf'
 rows.append(r)
extra=[
('ThalamusDB: Approximate Query Processing on Multi-Modal Data','https://doi.org/10.1145/3654989',2024,'PACMMOD','approximate-multimodal-query-processing','metadata_only',['https://github.com/itrummer/thalamusdb','https://par.nsf.gov/servlets/purl/10577787']),
('Aero: Adaptive Query Processing of ML Queries','https://doi.org/10.1145/3725408',2025,'PACMMOD','adaptive-ml-query-processing','metadata_only',['https://faculty.cc.gatech.edu/~jarulraj/pages/research.html','https://faculty.cc.gatech.edu/~jarulraj/pages/code.html']),
('Semantic Integrity Constraints: Declarative Guardrails for AI-Augmented Data Processing Systems','https://www.vldb.org/pvldb/vol18/p4073-lee.pdf',2025,'PVLDB','semantic-output-constraints','abstract_only',['https://www.vldb.org/pvldb/vol18/p4073-lee.pdf'])]
for title,url,year,venue,topic,status,e in extra:rows.append(dict(title=title,url=url,year=year,venue=venue,topic=topic,reading_status=status,evidence=e,review_folder=None,checked_on='2026-10-14'))
# Use official publication labels only when directly verified in proceedings / paper.
updates={'2407.09522':(2024,'NeurIPS'),'2403.05821':(2025,'MLSys'),'2504.01157':(2025,'PVLDB'),'2409.00847':(2025,'CIDR')}
for r in rows:
 for id_,(y,v) in updates.items():
  if r['url'].endswith(id_):r.update(year=y,venue=v)
(R/'catalog.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
aliases=[
{'urls':['https://arxiv.org/abs/2407.11418','https://www.vldb.org/pvldb/vol18/p4171-patel.pdf'],'relation':'preprint_and_published_version','evidence':'PVLDB LOTUS paper §6 and reference54; same authors/system. Titles differ.'},
{'urls':['https://arxiv.org/abs/2410.12189','https://www.vldb.org/pvldb/vol18/p3035-shankar.pdf'],'relation':'preprint_and_published_version','evidence':'Same title/authors, published PDF first page.'},
{'urls':['https://arxiv.org/abs/2505.14661','https://arxiv.org/abs/2505.14661v3','https://www.vldb.org/pvldb/vol19/p1060-russo.pdf'],'relation':'preprint_and_published_version','evidence':'arXiv v3 first page gives PVLDB19(5):1060–1073.'},
{'urls':['https://arxiv.org/abs/2507.06515','https://arxiv.org/abs/2507.06515v2','https://www.vldb.org/pvldb/vol18/p4560-chai.pdf'],'relation':'preprint_and_published_version','evidence':'Same title/authors, official PDF first page gives PVLDB18(11):4560–4573.'},
{'urls':['https://arxiv.org/abs/2405.14696','https://www.vldb.org/cidrdb/papers/2025/p12-liu.pdf'],'relation':'technical_report_and_conference_paper','evidence':'CIDR paper refers to comprehensive workload technical report; distinct version and title, do not overwrite version-specific evaluations.'},
{'urls':['https://arxiv.org/abs/2504.01157','https://www.vldb.org/pvldb/vol18/p5415-mhedhbi.pdf'],'relation':'preprint_and_published_version','evidence':'Official DuckDB publication page links paper at VLDB2025.'},
{'urls':['https://arxiv.org/abs/2604.09944'],'relation':'title_changed_same_arxiv_id','evidence':'Old search index title Horrila; primary arXiv current title PLOP. Keep one entry.'}
]
(R/'aliases.json').write_text(json.dumps(aliases,ensure_ascii=False,indent=2)+'\n')
print('catalog',len(rows),'full_text',sum(r['reading_status']=='full_text_reviewed' for r in rows))
