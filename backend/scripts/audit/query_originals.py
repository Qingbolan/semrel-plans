"""Trace every displayed/exported query to its precise source field."""
import json, csv, hashlib, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT / 'backend' / 'atlas'))
from query_originals import extract_text

def text_equal(a,b):return a==b

def rows(p):return [json.loads(s) for s in p.read_text().splitlines() if s.strip()]
qs=rows(ROOT/'catalog/queries.jsonl');details={r['query_id']:r for r in rows(ROOT/'catalog/task_details.jsonl')};sources={r['source_id']:r for r in rows(ROOT/'catalog/sources.jsonl')}
index=json.loads((ROOT/'upstream/snapshots/index.json').read_text())
contracts={r['query_id']:r for r in rows(ROOT/'catalog/input_contracts.jsonl')}
json_tasks={}
for p in (ROOT/'upstream/imports/8-17').glob('*.json'):
    data=json.loads(p.read_text())
    if isinstance(data,dict):data=data['tasks']
    for i,r in enumerate(data):json_tasks[r['task_id']]=(p,i)
csv_tasks={(r['benchmark'],r['task_id']):p for p in (ROOT/'upstream/imports/7-30').glob('*_per_query.csv') for r in csv.DictReader(p.open())}
revision='8c2cac89b21c6782239e8e5b03d326d0c029b655'
imported={r['query_id']:r for r in rows(ROOT/'catalog/original_queries.jsonl') if r['query_id'].startswith(('swb/','abacus/'))}
records=[]
for q in qs:
    if q['query_id'] in imported:
        record=imported[q['query_id']]
        assert extract_text(ROOT/record['source_path'],record['selector'])==record['text']
        records.append(record)
        continue
    qid=q['query_id'];benchmark=q['benchmark_id'];kind='natural_language';verification='upstream_original';comparison=None
    if benchmark=='sembench':
        group=q['scenario_id'];tid=q['source_query_id']
        rel=f'files/{group}/queries/{tid}.toml' if group=='ecomm' else f'files/{group}/query/natural_language/{tid}.'+('json' if group=='mmqa' else 'txt')
        path=ROOT/'upstream/snapshots/sembench/SemBench'/revision/rel
        selector={'type':'toml'} if group=='ecomm' else {'type':'json_field','field':'nl_question'} if group=='mmqa' else {'type':'text'}
    elif benchmark=='tag-bench':
        path=ROOT/index[sources[q['source_id']]['location'].split('#')[0]];selector={'type':'python_query','function':'pipeline_'+q['source_query_id']}
    elif benchmark=='uda-bench':
        path=ROOT/index[sources[q['source_id']]['location']];selector={'type':'sql_statement','index':int(qid.split('/')[-1])-1};kind='sql'
    elif benchmark=='8-17':
        original=details[qid]['original_record'];path,_=json_tasks[original['task_id']];selector={'type':'json_task','id_field':'task_id','id':original['task_id'],'field':'query'};verification='supplied_original'
    elif benchmark=='7-30':
        original=details[qid]['original_record'];path=csv_tasks[(original['benchmark'],original['task_id'])];selector={'type':'csv_task','id':original['task_id']};verification='supplied_original'
        c=contracts[qid]; evidence_path=ROOT/c['evidence']['path']
        family=original['benchmark']; task_id=original['task_id']
        if c.get('upstream_record'):
            upstream_text=c['upstream_record']['query']
        elif family=='DABstep':
            upstream_text=next(r['question'] for r in rows(evidence_path) if str(r['task_id'])==task_id)
        elif family=='LongDA':
            upstream_text=next(r['query'] for r in csv.DictReader(evidence_path.open()) if r['source']+':'+r['internal_id']==task_id)
        elif family=='KramaBench':
            upstream_text=next(r['query'] for r in json.loads(evidence_path.read_text()) if r['id']==task_id)
        elif family=='DAB':
            upstream_text=json.loads(evidence_path.read_text())
        else:raise ValueError('Unverified benchmark '+family)
        status='exact_match' if text_equal(original['query'],upstream_text) else 'whitespace_only' if original['query'].split()==upstream_text.split() else 'version_mismatch'
        comparison={'status':status,'source_path':c['evidence']['path']}
        if status!='exact_match':comparison['upstream_text']=upstream_text

    else:
        path=ROOT/sources[q['source_id']]['location'];verification='local_definition';kind='local_sql'
        short=q['source_query_id'].split('/')[0]
        if short in ['TAR','TREC-Legal','ContractNLI','MAUD','ShARC']:
            selector={'type':'sql_block','index':['TAR','TREC-Legal','ContractNLI','MAUD','ShARC'].index(short)}
        elif short in ['ClinGen','TalentCLEF']:selector={'type':'text'}
        elif qid.endswith('/Q1'):selector={'type':'sql_block','index':0}
        else:selector={'type':'heading'};kind='local_natural_language'
    text=extract_text(path,selector)
    assert text.strip(),qid
    if qid in details:assert text==details[qid]['original_record']['query'],qid
    records.append({'query_id':qid,'text':text,'kind':kind,'verification':verification,'source_path':path.relative_to(ROOT).as_posix(),'selector':selector,'source_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'text_sha256':hashlib.sha256(text.encode()).hexdigest(),'upstream_comparison':comparison})
(ROOT/'catalog/original_queries.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in records))
with (ROOT/'exports/query_text_audit.csv').open('w',newline='') as f:
    writer=csv.writer(f);writer.writerow(['query_id','kind','verification','source_path','selector','upstream_comparison','original_query'])
    for r in records:writer.writerow([r['query_id'],r['kind'],r['verification'],r['source_path'],json.dumps(r['selector']),json.dumps(r['upstream_comparison']),r['text']])
print('Verified',len(records),'query texts against source selectors')
