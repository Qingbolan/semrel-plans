"""Import Abacus's official workload definitions and locally acquired input artifacts."""
import ast
import hashlib
import json
import sys
from pathlib import Path
import numpy as np
import pandas as pd
import pyarrow.parquet as pq

ROOT=Path(__file__).resolve().parents[2]
COMMIT='807ed301c4d2457ef304647e6095184556bd1e83'
SOURCE=ROOT/'upstream/snapshots/abacus'/COMMIT/'abacus-research'
ARTIFACT=ROOT/'data/abacus/artifacts/extracted'
TABLES=['queries','nodes','edges','sources','query_sources','task_details','input_contracts','original_queries']
sys.path.insert(0,str(ROOT / 'backend' / 'atlas'))
from reference_plans import ReferencePlan, dag_mixed_label
# Logical DAGs of the three official pipelines (the "construct plan" code of each script); every MMQA question runs the same one.
PLANS={
 'biodex':'''SCAN_DOCS(biodex medical articles) -> SEM_MAP("reactions experienced by the patient") -> SEM_TOPK("closest standard reaction terms from the reaction-term index") -> SEM_MAP("ranked list of reaction labels")''',
 'cuad':'''SCAN_DOCS(cuad contracts) -> SEM_MAP("extract text spans for each of the 41 CUAD clause categories")''',
 'mmqa':'''q = SCAN_TABLE(questions)
texts = SCAN_DOCS(mmqa texts)
tables = SCAN_DOCS(mmqa tables)
images = SCAN_DOCS(mmqa images)
qt = q -> SEM_MAP("text search string for the question")
t = SEM_LEFT_JOIN(qt, texts, "the text snippet is relevant to the question") -> GROUP_BY(qid, question; concatenate text)
qb = q -> SEM_MAP("table search string for the question")
b = SEM_LEFT_JOIN(qb, tables, "the table is relevant to the question") -> GROUP_BY(qid, question; concatenate tables)
qi = q -> SEM_MAP("image search string for the question")
i = SEM_LEFT_JOIN(qi, images, "the image is relevant to the question") -> GROUP_BY(qid, question; list images)
tb = JOIN(left=t, right=b, on qid, question)
JOIN(left=tb, right=i, on qid, question) -> SEM_MAP("answer the question from the text, tables and images")''',
}
TITLES={'biodex':'BioDEX：为每篇医学论文排序不良反应标签（工作流）','cuad':'CUAD：从合同中抽取 41 类条款文本（工作流）','mmqa':'MMQA：结合文本、表格与图片回答问题（工作流）'}
def pipeline_excerpt(code,slug):
 """The plan-construction lines of the script, not the whole experiment harness."""
 lines=code.splitlines()
 if slug=='cuad':
  start=next(i for i,l in enumerate(lines) if l.startswith('def build_cuad_query'));end=next(i for i in range(start+1,len(lines)) if lines[i].startswith('def '))
 else:
  start=next(i for i,l in enumerate(lines) if l.strip().startswith(('text_plan = ','plan = BiodexDataset')))
  end=max(i for i,l in enumerate(lines) if '.sem_map(' in l)+1
 return '\n'.join(lines[start:end]).strip()

def write(path,value):
 path=ROOT/path;path.parent.mkdir(parents=True,exist_ok=True);path.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')
def jsonl(path,rows):
 path=ROOT/path;path.parent.mkdir(parents=True,exist_ok=True);path.write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in rows))
def sha(path):
 digest=hashlib.sha256()
 with path.open('rb') as stream:
  for chunk in iter(lambda:stream.read(1024*1024),b''):digest.update(chunk)
 return digest.hexdigest()
def rel(path):return path.relative_to(ROOT).as_posix()
def schema(path,var):
 assignment=next(n for n in ast.walk(ast.parse(path.read_text())) if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id==var for t in n.targets))
 out=[]
 for d in assignment.value.elts:
  fields={ast.literal_eval(k):v for k,v in zip(d.keys,d.values)}
  out.append(dict(name=ast.literal_eval(fields['name']),type=ast.unparse(fields['type']).replace('ImageBase64','image').replace('str','string'),description=ast.literal_eval(fields['desc'])))
 return out

def main():
 tables={name:[r for r in map(json.loads,(ROOT/'catalog'/f'{name}.jsonl').read_text().splitlines()) if not r.get('query_id','').startswith('abacus/') and not r.get('source_id','').startswith('abacus_')] for name in TABLES}
 config=json.loads((ROOT/'config/catalog.json').read_text());config['scenarios']=[s for s in config['scenarios'] if not s.startswith('files/abacus/')]
 order=max(q['display_order'] for q in tables['queries'])+1
 source_rows={}
 def source(sid,path,title,kind='task_definition'):
  location=rel(path) if isinstance(path,Path) else path
  source_rows[sid]=dict(source_id=sid,location=location,title=title,source_type=kind,version=COMMIT if kind=='task_definition' else 'Abacus v3 / official data',verification='Source checked against pinned official artifact',checked_on='2026-10-14',publication_label='PVLDB2026' if kind=='paper' else '',publication_url='https://github.com/mitdbg/palimpzest')
  return sid
 paper=source('abacus_paper','https://arxiv.org/abs/2505.14661v3','Abacus: A Cost-Based Optimizer for Semantic Operator Systems','paper')

 # Preserve test data and labels separately; use the exact sampling algorithm from the scripts.
 bio=pq.read_table(ROOT/'data/abacus/biodex/test.parquet').to_pandas()
 bio_inputs=bio[['pmid','title','abstract','fulltext']].to_dict('records')
 jsonl(Path('data/abacus/biodex/inputs.jsonl'),bio_inputs)
 jsonl(Path('data/abacus/biodex/gold.jsonl'),bio[['pmid','reactions']].to_dict('records'))
 write(Path('data/abacus/biodex/selections.json'),{str(seed):bio.sample(n=250,random_state=seed).pmid.tolist() for seed in range(10)})
 cuad=json.loads((ROOT/'data/abacus/cuad/source/test.json').read_text())['data']
 contracts=[dict(contract_id=a['paragraphs'][0]['qas'][0]['id'],title=a['title'].strip(),contract=a['paragraphs'][0]['context'].strip()) for a in cuad]
 jsonl(Path('data/abacus/cuad/contracts.jsonl'),contracts)
 cats=ast.literal_eval(next(n.value for n in ast.parse((SOURCE/'cuad-demo.py').read_text()).body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='CUAD_CATEGORIES' for t in n.targets)))
 write(Path('environment/abacus/cuad/categories.json'),cats)
 selections={}
 for seed in range(10):
  titles=[c['title'] for c in contracts];np.random.default_rng(seed).shuffle(titles);selections[str(seed)]=titles[:100]
 write(Path('data/abacus/cuad/selections.json'),selections)
 dev=[json.loads(line) for line in (ARTIFACT/'data/MMQA_dev.jsonl').read_text().splitlines()]
 eligible=[r for r in dev if 'image' in r['metadata']['modalities'] and len(r['metadata']['modalities'])>1]
 selected={};used={}
 for seed in [0,1,2,3,4,6,8,9]:
  records=eligible.copy();np.random.default_rng(seed).shuffle(records);selected[str(seed)]=[r['qid'] for r in records[:100]]
  for r in records[:100]:used[r['qid']]=r
 jsonl(Path('data/abacus/mmqa/questions.jsonl'),[dict(qid=r['qid'],question=r['question']) for r in used.values()])
 jsonl(Path('data/abacus/mmqa/gold.jsonl'),[dict(qid=r['qid'],answers=r['answers'],supporting_context=r['supporting_context']) for r in used.values()])
 write(Path('data/abacus/mmqa/selections.json'),selected)
 pools={}
 for seed,ids in selected.items():
  pools[seed]={part:sorted({c['doc_id'] for qid in ids for c in used[qid]['supporting_context'] if c['doc_part']==part}) for part in ['text','table','image']}
 write(Path('environment/abacus/mmqa/pools.json'),pools)
 # Preserve repeated candidate rows and their order, exactly as the official dataset classes do.
 pool_rows={seed:{part:[c['doc_id'] for qid in ids for c in used[qid]['supporting_context'] if c['doc_part']==part] for part in ['text','table','image']} for seed,ids in selected.items()}
 write(Path('environment/abacus/mmqa/pool-records.json'),pool_rows)
 image_manifest=json.loads((ROOT/'data/abacus/mmqa/image-manifest.json').read_text())
 images={r['image_id']:r for r in image_manifest['images']}
 context_counts={}
 for part,plural in [('text','texts'),('table','tables'),('image','images')]:
  needed={id for pool in pools.values() for id in pool[part]};rows=[]
  for line in (ARTIFACT/f'data/MMQA_{plural}.jsonl').read_text().splitlines():
   record=json.loads(line)
   if record['id'] not in needed:continue
   if part=='text':value=record['title']+': '+record['text']
   elif part=='table':
    table=record['table'];header=table['header'];empty={i for i,c in enumerate(header) if c['column_name']==''}
    value=record['title']+': '+table['table_name']+'\n\n'+','.join(c['column_name'] for c in header if c['column_name'])+'\n'
    value+=''.join(','.join(c['text'] for i,c in enumerate(row) if i not in empty)+'\n' for row in table['table_rows'])
   else:value=images[record['id']]['path']
   rows.append({part+'_id':record['id'],part:value})
  assert len(rows)==len(needed),(part,len(rows),len(needed))
  jsonl(Path(f'environment/abacus/mmqa/{plural}.jsonl'),rows);context_counts[plural]=len(rows)
 # Optimization examples are recorded separately from evaluation inputs and context.
 bio_train=pd.concat([pq.read_table(p).to_pandas() for p in sorted((ROOT/'data/abacus/biodex').glob('train-*.parquet'))],ignore_index=True)
 write(Path('data/abacus/biodex/optimization-selections.json'),{str(seed):bio_train.sample(n=20,random_state=seed).pmid.tolist() for seed in range(10)})
 cuad_train=json.loads((ROOT/'data/abacus/cuad/source/train_separate_questions.json').read_text())['data']
 train_titles=list(dict.fromkeys(a['title'].strip() for a in cuad_train));train_selections={}
 for seed in range(10):
  titles=train_titles.copy();np.random.default_rng(seed).shuffle(titles);train_selections[str(seed)]=titles[:25]
 write(Path('data/abacus/cuad/optimization-selections.json'),train_selections)
 mmqa_train=[json.loads(line) for line in (ARTIFACT/'data/MMQA_train.jsonl').read_text().splitlines()]
 mmqa_train=[r for r in mmqa_train if 'image' in r['metadata']['modalities'] and len(r['metadata']['modalities'])>1];train_selections={}
 for seed in selected:
  records=mmqa_train.copy();np.random.default_rng(int(seed)).shuffle(records);train_selections[seed]=[r['qid'] for r in records[:20]]
 write(Path('data/abacus/mmqa/optimization-selections.json'),train_selections)

 workloads=[('biodex','biodex-demo.py','biodex_entry_cols','The ranked list of medical conditions experienced by the patient.',len(bio_inputs),250,'inputs.jsonl',['pmid','title','abstract','fulltext'],'ranked_reaction_labels','RP@5'),('cuad','cuad-demo.py','input_cols','Extract the text spans (if they exist) from the contract.',len(contracts),100,'contracts.jsonl',['contract'],'41 clause categories','micro_f1'),('mmqa','mmqa-complex-demo.py','mmqa_entry_cols','The answer(s) to the question.',len(used),100,'questions.jsonl',['question'],'answers','f1')]
 for slug,filename,var,prefix,count,per_run,datafile,passed,out,metric in workloads:
  path=SOURCE/filename;code=path.read_text();tree=ast.parse(code)
  literal=next(n for n in ast.walk(tree) if isinstance(n,ast.Constant) and isinstance(n.value,str) and n.value.startswith(prefix))
  instruction=literal.value;cols=schema(path,var);qid='abacus/'+slug+'/workflow';identity='abacus/'+slug
  sid=source('abacus_'+slug+'_code',path,filename)
  dataset_url={'biodex':'https://huggingface.co/datasets/BioDEX/BioDEX-Reactions','cuad':'https://github.com/TheAtticusProject/cuad','mmqa':'https://github.com/allenai/multimodalqa'}[slug]
  dsid=source('abacus_'+slug+'_data',dataset_url,slug.upper()+' official dataset','dataset')
  evidence=dict(path=rel(path),url=f'https://github.com/mitdbg/palimpzest/blob/{COMMIT}/abacus-research/{filename}',locator=f'line {literal.lineno}; input classes and plan construction',sha256=sha(path),excerpt=code)
  resources=[]
  if slug=='biodex':
   resources=[dict(name='reaction_terms',path=rel(ARTIFACT/'data/reaction_terms.txt'),source_type='table',columns=[dict(name='term',type='string',description='Standardized reaction label')]),dict(name='biodex-reaction-terms Chroma index',path=rel(ARTIFACT/'.chroma-biodex'),source_type='index')]
  elif slug=='cuad':resources=[dict(name='CUAD category definitions',path='environment/abacus/cuad/categories.json',source_type='table',columns=[dict(name=k,type='string',description=k) for k in cats[0]])]
  else:
   resources=[dict(name='mmqa-'+mod,source_type='table',path=f'environment/abacus/mmqa/{mod}.jsonl',columns=schema(path,'mmqa_'+singular+'_cols'),record_count=context_counts[mod],source_path=rel(ARTIFACT/f'data/MMQA_{mod}.jsonl')) for mod,singular in [('texts','text'),('tables','table'),('images','image')]]
  if slug=='mmqa':
   for resource in resources:
    resource['selection']='Candidate records follow supporting contexts of the 100 selected questions per seed, preserving duplicates and order; see environment/abacus/mmqa/pool-records.json'
    if resource['name']=='mmqa-images':resource['storage_encoding']='Local image file paths; the official loader encodes image bytes as base64 before passing them to the operator.'
  batching=dict(unit={'biodex':'medical article','cuad':'contract','mmqa':'question'}[slug],records_per_run=per_run,seeds=list(range(10)) if slug!='mmqa' else [0,1,2,3,4,6,8,9],selection_path=f'data/abacus/{slug}/selections.json',optimization_examples_per_seed=25 if slug=='cuad' else 20,optimization_selection_path=f'data/abacus/{slug}/optimization-selections.json',model_batch_size=None,selection_algorithm='pandas.DataFrame.sample(random_state=seed)' if slug=='biodex' else 'numpy.random.default_rng(seed).shuffle; first N',scope='One parameterized operator workflow evaluated over the selected records; model batch size is not specified.')
  write(Path('environment')/identity/'resources.json',dict(resources=resources,batching=batching))
  write(Path('environment')/identity/'manifest.json',dict(environment_id=identity,dataset_id=identity,runtime_status='unconfigured',engine='Palimpzest / Abacus',model=None,hardware=None,execution_status='not_executed',record_batch_size=None,query_batch=None,model_batch_size=None,concurrency=None,resources=resources,batching=batching))
  write(Path('data')/identity/'manifest.json',dict(dataset_id=identity,source_ids=[dsid,sid],availability='local_files',local_path=f'data/{identity}/{datafile}',schema=cols,record_count=count,version=COMMIT,file_count=None,total_bytes=(ROOT/f'data/{identity}/{datafile}').stat().st_size,inventory_path=f'data/{identity}/selections.json',verification='Downloaded source inputs; experiment selections reconstructed from official code'))
  contract=dict(query_id=qid,environment=dict(requirement='required',resources=resources),tables=[dict(name=slug,columns=cols,passed_columns=passed,row_unit='document' if slug!='mmqa' else 'record',scope='used',path=f'data/{identity}/{datafile}',record_count=count,selection=f'{per_run} records per seed; see selections.json')],output=dict(type='table',columns=[c['Category'] for c in cats] if slug=='cuad' else [out]),evidence=evidence,notes=[],audit_status='source_checked',batching=batching)
  programs=[dict(type='python',program=pipeline_excerpt(code,slug),note=f'Plan-construction excerpt of {filename}; the full script is the evidence file.')]
  graph=ReferencePlan(qid,{o['operator_type'] for o in json.loads((ROOT/'config/operators.json').read_text())});root=graph.parse(PLANS[slug])
  def add(qid,text,original,contract,number,collection='Abacus',gold=None,title=None):
   nonlocal order
   tables['queries'].append(dict(query_id=qid,benchmark_id='abacus',scenario_id=identity,source_query_id=str(number),title=title or text,plan_origin='source_reconstruction',plan_status_label='依据官方实验脚本重建的逻辑计划'+('（所有 MMQA 问题共用同一工作流）' if slug=='mmqa' else ''),source_id=sid,root_node_id=root,notes='',display_order=order,group_label=collection+' / '+slug.upper() if collection=='Abacus' else collection,mixed_label=dag_mixed_label([n['operator_type'] for n in graph.nodes],{o['operator_type']:o['family'] for o in json.loads((ROOT/'config/operators.json').read_text())}),environment_id=identity,plan_format='logical_dag',collection_label=collection,category_label=slug.upper()));order+=1
   tables['nodes'].extend(dict(n,query_id=qid) for n in graph.nodes);tables['edges'].extend(dict(e,query_id=qid) for e in graph.edges)
   tables['task_details'].append(dict(query_id=qid,reference_programs=programs,gold=gold or dict(gold_answer=None,answer_schema=contract['output'],source_path=f'data/{identity}/gold.jsonl' if slug!='cuad' else 'data/abacus/cuad/source/test.json'),evaluation=dict(primary_metric=metric,scorer=rel(SOURCE/('score_mmqa_complex.py' if slug=='mmqa' else 'score_'+slug+'.py'))),annotation=dict(semop_count={'biodex':3,'cuad':1,'mmqa':7}[slug])))
   tables['input_contracts'].append(dict(contract,query_id=qid))
   tables['original_queries'].append(dict(query_id=qid,text=text,kind='natural_language',language='en',verification='upstream_original',upstream_comparison=None,source_path=original['path'],source_sha256=sha(ROOT/original['path']),text_sha256=hashlib.sha256(text.encode()).hexdigest(),selector=original['selector']))
   for ref,role,relation in [(sid,'task_definition','system_implementation'),(paper,'paper','query_source'),(dsid,'dataset','dataset_origin')]:tables['query_sources'].append(dict(query_id=qid,source_id=ref,role=role,locator=filename,attribution_note='Official Abacus experiment workload pinned to source commit.',relationship=relation,evidence_paths=[rel(path)]))
  add(qid,instruction,dict(path=rel(path),selector=dict(type='python_string',line=literal.lineno,column=literal.col_offset)),contract,len([q for q in tables['queries'] if q['benchmark_id']=='abacus'])+1,title=TITLES[slug])
  if slug=='mmqa':
   originalfile=ARTIFACT/'data/MMQA_dev.jsonl'
   for i,r in enumerate(used.values(),1):
    c=json.loads(json.dumps(contract));c['tables'][0]['selection']='qid = '+r['qid'];c['tables'][0]['selected_record_count']=1;c['batching']=dict(batching,question_id=r['qid'],included_in_seeds=[int(s) for s,ids in selected.items() if r['qid'] in ids]);c['supplementary_evidence']=[c['evidence']];c['evidence']=dict(path=rel(originalfile),url='https://palimpzest-workloads.s3.us-east-1.amazonaws.com/abacus-data.tar.gz',locator='MMQA_dev.jsonl qid='+r['qid'],sha256=sha(originalfile),excerpt=json.dumps(r,ensure_ascii=False,indent=2))
    add('abacus/mmqa/'+r['qid'],r['question'],dict(path=rel(originalfile),selector=dict(type='jsonl_task',id_field='qid',id=r['qid'],field='question')),c,i,'Abacus MMQA',dict(gold_answer=r['answers'],answer_schema=c['output']))
  scenario=f'files/abacus/{slug}/scenario.json';config['scenarios'].append(scenario);write(Path(scenario),dict(id=identity,name='Abacus '+slug.upper(),query_ids=[q['query_id'] for q in tables['queries'] if q['scenario_id']==identity]))
 tables['sources'].extend(source_rows.values())
 for name,rows in tables.items():jsonl(Path('catalog')/(name+'.jsonl'),rows)
 write(Path('config/catalog.json'),config)
 types=json.loads((ROOT/'config/paper-types.json').read_text());types[paper]='research';write(Path('config/paper-types.json'),types)
 write(Path('exports/abacus-import.json'),dict(commit=COMMIT,context_records=context_counts,mmqa_image_files=len(images),workflows=3,mmqa_questions=len(used),biodex_test_rows=len(bio_inputs),cuad_test_contracts=len(contracts),mmqa_eligible_dev_questions=len(eligible),seeds=selected))
 receipt=[]
 for file in (ROOT/'data/abacus').rglob('*'):
  if file.is_file() and file.suffix in {'.gz','.parquet','.zip'}:receipt.append(dict(path=rel(file),bytes=file.stat().st_size,sha256=sha(file)))
 write(Path('exports/abacus-downloads.json'),receipt)
 print('Imported 3 workflows and',len(used),'verbatim MMQA questions')

if __name__=='__main__':main()
