"""Build explicit per-query data contracts from pinned source records and code.

Run with --upstream pointing to Awesome-Dymatic-Operator/Benchmark/code.
No benchmark code is executed. Source revisions and excerpts accompany each record.
"""
import argparse, ast, csv, hashlib, json, re, shutil, sys
from collections import Counter
from pathlib import Path
from sql_inputs import extract_sql

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'src'))
from input_contracts import InputContracts


def rows(path):
    return [json.loads(x) for x in path.read_text().splitlines() if x.strip()]


def table(name, columns=(), passed=None, row_unit='record', **kwargs):
    return dict(name=name, columns=[{'name': c, 'type': None} if isinstance(c,str) else c for c in columns], passed_columns=passed, row_unit=row_unit, scope='used', **kwargs)


class ContractAudit:
    def __init__(self, upstream):
        self.upstream = upstream
        self.queries = rows(ROOT/'query/queries.jsonl')
        self.sources = {r['source_id']:r for r in rows(ROOT/'query/sources.jsonl')}
        self.details = {r['query_id']:r for r in rows(ROOT/'query/task_details.jsonl')}
        self.nodes = rows(ROOT/'query/nodes.jsonl')
        self.index = json.loads((ROOT/'query/source-snapshots/index.json').read_text())
        self.saved = {}
        fda_root = ROOT/'query/source-snapshots/FDAbench2026/FDAbench-Full/46bcbbbaca95defddb99e411931763a47b3f5b65'
        self.fda = {r['task_id']:(r,p) for p in fda_root.glob('*/data.jsonl') for r in rows(p)}
        self.gold_tables_path=upstream/'Spider2/methods/gold-tables/spider2-lite-gold-tables.jsonl'
        self.gold_tables={r['instance_id']:r['gold_tables'] for r in rows(self.gold_tables_path)}
        self.longda = json.loads((ROOT/'query/source-snapshots/EvilBench/LongDA/inventory.json').read_text())

    def evidence(self, path, locator='', excerpt=None, url=None):
        path=Path(path)
        if not path.is_relative_to(ROOT):
            relative=path.relative_to(self.upstream)
            target=ROOT/'query/source-snapshots/local'/relative
            if path not in self.saved:
                target.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(path,target);self.saved[path]=target
            path=target
        return {'path':str(path.relative_to(ROOT)), 'url':url or str(path.relative_to(ROOT)), 'locator':locator,
                'sha256':hashlib.sha256(path.read_bytes()).hexdigest(), 'excerpt':excerpt}

    def base(self, q):
        return {'query_id':q['query_id'],'environment':{'requirement':'none','resources':[]},'tables':[],
                'output':self.details.get(q['query_id'],{}).get('output') or next((n['label'] for n in self.nodes if n['query_id']==q['query_id'] and n['node_id']==q['root_node_id']),None),
                'evidence':None,'notes':[], 'audit_status':'source_checked'}

    def source(self,q):
        url=self.sources[q['source_id']]['location'];return ROOT/self.index[url.split('#')[0]],url

    def sembench(self,q):
        c=self.base(q);p,url=self.source(q);sql=p.read_text();c['evidence']=self.evidence(p,excerpt=sql,url=url)
        if not sql.strip():
            c['environment']['requirement']='unspecified';c['audit_status']='source_gap'
            c['notes']=['来源 SQL 文件为空；目录中的计划为本地提出，无法据此确认上游输入列。']
            c['tables']=[table('lizzy_caplan_text_data（目录提出的输入）',['title','text'],['text'],scope_note='本地计划；来源 SQL 未定义')]
            return c
        c['tables']=extract_sql(sql)
        if '/animals/' in q['query_id'] and q['source_query_id'] in ['Q1','Q2']:c['output']={'columns':['count']}
        # These fields are unqualified in the source's three-table joins.
        if '/ecomm/' in q['query_id']:
            styles=next((t for t in c['tables'] if t['name'].endswith('STYLES_DETAILS')),None)
            if styles:
                for name in ['id','price','baseColour','masterCategory.typeName','subCategory.typeName','productDisplayName','productDescriptors.description.value','styleImages.default.imageURL']:
                    if re.search(r'(?<![\w])'+re.escape(name)+r'(?![\w])',sql) and name not in [x['name'] for x in styles['columns']]:styles['columns'].append({'name':name,'type':None})
                if q['source_query_id'] in ['q10','q11']:
                    styles['passed_columns']=['productDisplayName','productDescriptors.description.value']
                styles['columns']=[x for x in styles['columns'] if x['name'] not in ['colour1','colour2']]
        for t in c['tables']:
            t['row_unit']='review' if t['name']=='movie.reviews' else 'audio' if 'audio' in t['name'] else 'image' if t['name'].endswith(('IMAGES','images','image_data_mm','car_mm')) else 'record'
            for col in t['columns']:
                name=col['name'];col['type']='audio' if name in ['image','audio'] and 'audio' in t['name'] else 'image' if name in ['image','ref'] else 'string' if name in ['reviewText','summary','text','title','City','Airlines','Destinations'] else None
        if '/movie/' in q['query_id']:
            sample=self.upstream/'SemBench/files/movie/data/sf_2000/Reviews.csv'
            records=list(csv.DictReader(sample.open()));target=ROOT/'data/sembench/movie/Reviews.sf2000.csv'
            shutil.copyfile(sample,target)
            t=c['tables'][0];t['path']=str(target.relative_to(ROOT));t['record_count']=len(records)
            film='taken_3' if q['source_query_id'] in ['Q2','Q3','Q4','Q8'] else 'ant_man_and_the_wasp_quantumania' if q['source_query_id'] in ['Q5','Q6','Q7','Q9'] else None
            t['selection']=('id = '+film) if film else '全部评论'
            t['selected_record_count']=sum(r['id']==film for r in records) if film else len(records)
            t['scope_note']='本地提供 sf_2000 评论样本；记录数描述此样本，不代表论文全部实验规模。'
            for col in t['columns']:
                col['description']={'id':'Movie identifier','reviewId':'Review identifier','reviewText':'Review text'}.get(col['name'],'')
            c['supplementary_evidence']=[self.evidence(self.upstream/'SemBench/src/scenario/movie/setup/bigquery.py')]
        if '/animals/' in q['query_id']:
            for t in c['tables']:
                modality='audio' if 'audio' in t['name'] else 'image'
                sample=self.upstream/f'SemBench/files/animals/data/sf_200/{modality}_data.csv'
                records=list(csv.DictReader(sample.open()));target=ROOT/f'data/sembench/animals/{modality}_data.sf200.csv';shutil.copyfile(sample,target)
                t['path']=str(target.relative_to(ROOT));t['record_count']=len(records)
                t['scope_note']='本地文件是 sf_200 路径及标签索引；图片或音频内容未随该索引提供。SQL 的多模态列由加载过程绑定。'
        if '/movie/' in q['query_id'] and q['source_query_id'] in ['Q5','Q6','Q7']:
            ids=Counter(r['reviewId'] for r in records if r['id']==film and r['reviewId'])
            c['tables'][0]['comparison_pairs']=sum(ids.values())**2-sum(n*n for n in ids.values())
            c['notes'].append('movie.reviews 自连接为 r1、r2；每次比较传入 r1.reviewText 与 r2.reviewText。按同一电影且 reviewId 不同组成评论对。')
        if '/mmqa/' in q['query_id'] and q['source_query_id'] in ['q2a','q2b','q7']:
            c['notes'].append('来源的匹配提示实际传入图片 uri 字符串；不能将它标成直接传入图片内容。')
        return c

    def tag(self,q):
        c=self.base(q);p,url=self.source(q);tree=ast.parse(p.read_text());fn=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='pipeline_'+q['source_query_id'])
        snippet=ast.get_source_segment(p.read_text(),fn);c['evidence']=self.evidence(p,f'{fn.name}, lines {fn.lineno}-{fn.end_lineno}',snippet,url)
        specs={
          '0':[('satscores',['rtype','AvgScrMath','cname'],['cname'])],
          '1':[('satscores',['rtype','cname','AvgScrRead','cds'],['cname']),('schools',['CDSCode','Phone'],[])],
          '3':[('satscores',['rtype','cds','NumTstTakr'],[]),('schools',['County','CDSCode'],['County'])],
          '4':[('schools',['County','Longitude','GSoffered'],['County'])],
          '5':[('schools',['AdmFName1'],['AdmFName1'])],
          '6':[('users',['Id','DisplayName'],[]),('posts',['ParentId','OwnerUserId','Body'],['Body'])],
          '8':[('comments',['Score','Text'],['Text'])],
          '10':[('posts',['ViewCount','Body'],['Body'])],
          '11':[('circuits',['country','circuitId'],['country']),('races',['circuitId','name'],[])],
          '48':[('circuits',['name'],['name'])],
          '50':[('schools',['Magnet','CDSCode','School'],['School']),('satscores',['rtype','NumTstTakr','cds'],[])],
          '85':[('users',['Id','DisplayName'],[]),('posts',['OwnerUserId','Title'],['Title'])]}
        paths=re.findall(r'pd.read_csv\("([^"]+)"\)',snippet)
        c['tables']=[table(next(p for p in paths if p.endswith('/'+name+'.csv')),cols,passed) for name,cols,passed in specs[q['source_query_id']]]
        c['notes']=['输入为源码读取的 CSV；地理、人口或词义判断由模型提示完成，源码没有另外读取知识资料表。']
        return c

    def uda(self,q):
        c=self.base(q);p,url=self.source(q);number=int(q['query_id'].split('/')[-1]);sql=p.read_text().split(';')[number-1].strip()+';'
        c['evidence']=self.evidence(p,f'Query {number}',sql,url)
        ts=extract_sql(sql);c['tables']=[]
        for t in ts:
            name=t['name'];cols=re.findall(r'\b(?:Med_)?'+re.escape(name)+r'\.([A-Za-z_]\w*)',sql) or [x['name'] for x in t['columns']]
            c['tables'].append(table(name+' 原始文档',[{'name':'document','type':'string','description':'Logical document content field, not a physical SQL column'}],['document'],row_unit='document',extracted_columns=sorted(set(cols))))
        c['notes']=['SQL 描述目标属性表；目录采用从对应原始文档抽取这些属性的解释。document 是逻辑输入列，来源 SQL 未给出文档文件名与物理字段绑定。']
        c['audit_status']='interpreted';return c

    def supplied(self,q):
        c=self.base(q);d=self.details[q['query_id']];program='\n'.join(r['program'] for r in d['reference_programs']);c['evidence']=self.evidence(ROOT/'query/task_details.jsonl',q['query_id'],program)
        bound=set()
        for bindings in re.findall(r'(?:input_bindings=)?\{([^{}]+)\}',program):
            for key,value in re.findall(r'(\w+):\s*([\w.]+)',bindings):
                if value not in {'string','integer','boolean','float','number','enum'}:bound.add(value)
        for i in d['inputs']:
            cols=i['schema'] or []
            if i['source_type']=='document':
                cols=[{'name':'document','type':'string','description':'Logical document content field'}];passed=['document']
            else:passed=sorted(bound.intersection(cols)) or None
            t=table(i['source_id'],cols,passed,row_unit=i['source_type'],path=i['local_path'])
            t['scope']='declared';t['selection']=program
            c['tables'].append(t)
        c['notes']=['输入路径取自该任务 inputs，表列取自对应 CSV 表头；筛选范围及多表连接见该条参考计划。']
        return c

    def fda_contract(self,q):
        c=self.base(q);d=self.details[q['query_id']]['original_record'];r,p=self.fda[d['task_id']]
        if r['query']!=d['query']:raise ValueError('FDA query version mismatch '+q['query_id'])
        c['evidence']=self.evidence(p,r['task_id']);c['upstream_record']={k:v for k,v in r.items() if k not in ['ground_truth_report','correct_answer','rubric','dag']}
        sqls=[s['expected_SQL'] for s in r.get('gold_subtasks',[]) if s.get('expected_SQL')]
        original=self.upstream/'Spider2/spider2-lite/evaluation_suite/gold/sql'/f"{r['instance_id']}.sql"
        if not sqls and original.is_file():
            sqls=[original.read_text()];c['supplementary_evidence']=[self.evidence(original)]
        for sql in sqls:
            try:c['tables'].extend(extract_sql(sql,'bigquery' if r['instance_id'].startswith('bq') else 'snowflake' if r['instance_id'].startswith('sf') else 'sqlite'))
            except Exception:
                c['notes'].append('参考 SQL 已保留；其方言未能解析为逐表列清单。')
        if not c['tables'] and r['instance_id'] in self.gold_tables:
            c['tables']=[table(name,[],None,scope_note='上游基础问题标注的输入表；扩展问题未提供逐列定义') for name in self.gold_tables[r['instance_id']]]
            c['supplementary_evidence']=[self.evidence(self.gold_tables_path,r['instance_id'])]
            c['audit_status']='declared_files'
        if not c['tables']:
            c['tables']=[table(r['db'],[],None,database_type=r['database_type'])]
            c['notes'].append('任务指定数据库 '+r['db']+'；该条来源未提供可定位的查询 SQL，具体表与列未在任务记录中列出。')
            c['audit_status']='source_gap'
        for t in c['tables']:t['database']=r['db'];t['scope']='reference_sql'
        resources=[]
        for s in r.get('gold_subtasks',[]):
            if s.get('tool') in ['web_search','vector_search']:
                resources.append({'name':s.get('input',{}).get('query') or s.get('description',''), 'kind':s['tool'], 'files':s.get('input',{}).get('files',[])})
        for kind in ['frozen_web_search','frozen_vector_search']:
            for s in r.get(kind,{}).get('searches',[]):
                resources.append({'name':s.get('query',kind),'kind':kind,'files':s.get('urls',[]) or s.get('files',[])})
        if resources:c['environment']={'requirement':'required','resources':resources}
        elif d['semop_count']!='0':
            c['environment']={'requirement':'unspecified','resources':[]};c['notes'].append('提供的分析包含语义步骤，但该条公开任务没有列出对应资料，不能据此断言环境为无。')
        c['reference_sql']=sqls
        return c

    def longda_contract(self,q):
        c=self.base(q);r=self.details[q['query_id']]['original_record'];survey=r['subset'];paths=[x['rfilename'] for x in self.longda['siblings']]
        data=[x for x in paths if x.startswith(survey+'/data/')];docs=[x for x in paths if x.startswith(survey+'/docs/')]
        c['tables']=[table(x,[],None,row_unit='survey_record',scope_note='该调查提供的数据文件；逐题最小读取子集未在 benchmark.csv 指定') for x in data]
        c['environment']={'requirement':'required','resources':[{'name':x,'kind':'survey_documentation'} for x in docs]}
        p=next((ROOT/'query/source-snapshots/EvilBench/LongDA').glob('*/benchmark.csv'))
        matches=[x for x in csv.DictReader(p.open()) if x['source']+':'+x['internal_id']==r['task_id']]
        if len(matches)!=1 or matches[0]['query']!=r['query']:raise ValueError('LongDA mismatch')
        c['evidence']=self.evidence(p,r['task_id'],json.dumps(matches[0],ensure_ascii=False));c['audit_status']='declared_files'
        c['notes']=['逐题问题已匹配；这里列出该题所属调查提供的数据文件和资料。发布的任务表没有逐题变量代码或参考 SQL，不能把全部调查文件说成该题实际读取的最小集合。']
        return c

    def dabstep(self,q):
        c=self.base(q);r=self.details[q['query_id']]['original_record'];base=self.upstream/'DABstep/data';p=base/'tasks/all.jsonl';task=next(x for x in rows(p) if str(x['task_id'])==r['task_id'])
        if task['question']!=r['query']:raise ValueError('DABstep mismatch')
        c['evidence']=self.evidence(p,r['task_id'],json.dumps(task,ensure_ascii=False))
        fee='manual.md' in r['minimal_plan'];c['environment']={'requirement':'required' if fee else 'none','resources':[{'name':'manual.md','kind':'fee_rules','path':self.evidence(base/'context/manual.md')['path']}] if fee else []}
        for name in ['payments.csv','fees.json','merchant_data.json','merchant_category_codes.csv','acquirer_countries.csv']:
            p=base/'context'/name
            if name.endswith('.csv'):cols=next(csv.reader(p.open()))
            else:
                data=json.loads(p.read_text());cols=sorted(set(k for record in (data if isinstance(data,list) else data.values()) if isinstance(record,dict) for k in record))
            t=table(name,cols,[],path=str(p),scope_note='任务提供的共享数据文件；是否读取由该问题的条件决定')
            t['scope']='available';c['tables'].append(t)
        c['audit_status']='declared_files';c['notes']=['逐题 task_id 和问题文本已核对。列出提供给该题的数据文件及真实字段；公开任务不含逐题参考代码，未将共享文件伪称为实际读取清单。']
        return c

    def krama(self,q):
        c=self.base(q);r=self.details[q['query_id']]['original_record'];p=self.upstream/'Kramabench/workload'/f"{r['subset']}.json";record=next(x for x in json.loads(p.read_text()) if x['id']==r['task_id'])
        if ' '.join(record['query'].split())!=' '.join(r['query'].split()):
            c['notes'].append('同 task_id 的上游问题文本已变更；输入文件清单属于当前上游版本，不能视为旧题完整核验。');c['audit_status']='version_mismatch'
        c['evidence']=self.evidence(p,r['task_id']);sol=self.upstream/'Kramabench/solutions'/r['subset']/f"{r['task_id']}.py"
        c['tables']=[table(x,[],[],row_unit=Path(x).suffix.lstrip('.') or 'file') for x in record['data_sources']]
        c['reference_steps']=[x['step'] for x in record.get('subtasks',[]) if x.get('step')]
        if sol.exists():
            code=sol.read_text();c['supplementary_evidence']=[self.evidence(sol,excerpt=code)]
            c['notes']+=['逐题输入文件来自 data_sources；参考代码与步骤列出具体读取方式、工作表、清理和计算列。']
            c['column_references']=sorted(set(re.findall(r'\[[\'"]([^\'"\n]+)[\'"]\]',code)))
        if c['audit_status']!='version_mismatch':c['audit_status']='declared_files'
        return c

    def dab(self,q):
        c=self.base(q);r=self.details[q['query_id']]['original_record'];subset,number=r['task_id'].split('/');base=self.upstream/'DataAgentBench'/('query_'+subset);p=base/number/'query.json'
        record=json.loads(p.read_text());c['evidence']=self.evidence(p,excerpt=json.dumps(record,ensure_ascii=False))
        desc=(base/'db_description.txt').read_text();c['schema_description']=desc;c['supplementary_evidence']=[self.evidence(base/'db_description.txt')]
        if ' '.join(str(record).split())!=' '.join(r['query'].split()):
            c['notes'].append('当前上游问题与提供的旧题文本不同；以下为同 task_id 的数据库定义，待核对旧版本。');c['audit_status']='version_mismatch'
        current=None; field_indent=None; database=''
        for line in desc.splitlines():
            db=re.match(r'^\d+\.\s+(\w+)',line)
            if db:database=db.group(1)
            field=re.match(r'^(\s*)- Fields:\s*(.*)',line)
            if field and current:
                field_indent=len(field.group(1))
                if field.group(2) and not field.group(2).startswith('over '):
                    current['columns']=[{'name':x.strip(),'type':None} for x in field.group(2).split(',') if x.strip()]
                continue
            item=re.match(r'^(\s*)- ([\w][\w ]*)(?:\s*\(([^)]+)\))?(?::(.*))?$',line)
            if not item:continue
            indent=len(item.group(1));name=item.group(2).strip()
            if field_indent is not None and indent>field_indent and current:
                current['columns'].append({'name':name,'type':item.group(3),'description':(item.group(4) or '').strip()});continue
            if indent<=5 and not name.startswith(('This ','It ','Fields','Each ','One ','Every ')):
                current=table(database+'.'+name,[],None,scope_note='该题数据库中可用的表；来源未提供逐列执行清单')
                current['scope']='available';c['tables'].append(current);field_indent=None
        if not c['tables']:c['tables']=[table(subset+' 数据库',[],None,scope_note='数据表与字段见下方该题数据库定义')]
        if c['audit_status']!='version_mismatch':c['audit_status']='declared_files'
        c['notes']+=['查询文件与所属数据库说明逐题关联；数据库说明列出了集合、关系和字段。题目未提供逐列执行轨迹。']
        return c

    def derived(self,q):
        c=self.base(q);p=ROOT/self.sources[q['source_id']]['location'];c['evidence']=self.evidence(p)
        key=q['source_query_id'].split('/')[0]
        specs={
          'TAR':([('候选论文',['PMID','title','abstract'],['title','abstract'])],['CD005139 初筛协议']),
          'TREC-Legal':([('messages',['message_id','body'],['body']),('attachments',['message_id','content'],['content'])],['Topic301 披露请求']),
          'ContractNLI':([('contracts',['contract_id','text'],['text'])],['预先冻结的原 17 项 NDA 假设子集']),
          'MAUD':([('deal_points',['deal_id','text'],['text'])],['MAE 前瞻标准问题及其选项']),
          'ShARC':([('cases',['case_id','scenario','history'],['scenario','history'])],['固定 rule 与 question']),
          'ClinGen':([('animal_model_evidence',['record_id','gene','disease','inheritance','paper','supplements','background','evidence_target'],['gene','disease','inheritance','paper','supplements','background','evidence_target'])],['environment/SOP8.pdf']),
          'TalentCLEF':([('candidates',['candidate_id','resume','profile','projects','notes'],['resume','profile','projects','notes'])],['jobs/29243.html']),
          'Trial':([('Pairs',['record_id','patient_id','trial_id','text_path'],['text_path']),('Trials',['trial_id','inclusion_criteria','exclusion_criteria'],['inclusion_criteria','exclusion_criteria'])],[])}
        ts,resources=specs[key];c['tables']=[table(*t) for t in ts];c['environment']={'requirement':'required' if resources else 'none','resources':resources}
        c['audit_status']='local_definition';c['notes']=['依据本仓查询协议描述逻辑输入，非原论文执行字段；字段与资料应按对应公开数据导出绑定。']
        return c

    def run(self):
        contracts=[]
        imported={r['query_id']:r for r in map(json.loads,(ROOT/'query/input_contracts.jsonl').read_text().splitlines()) if r['query_id'].startswith('swb/')}
        for q in self.queries:
            if q['query_id'] in imported:
                contracts.append(imported[q['query_id']]);continue
            prefix=q['query_id'].split('/')[0]
            handler={'sembench':self.sembench,'tag-bench':self.tag,'uda-bench':self.uda,'local-derived':self.derived,'8-17':self.supplied}.get(prefix)
            if prefix=='7-30':handler={'FDABench':self.fda_contract,'LongDA':self.longda_contract,'DABstep':self.dabstep,'KramaBench':self.krama,'DAB':self.dab}[q['query_id'].split('/')[1]]
            contract=handler(q)
            if contract['audit_status']=='version_mismatch':contract['environment']['requirement']='unspecified'
            contracts.append(contract)
        (ROOT/'query/input_contracts.jsonl').write_text(''.join(json.dumps(c,ensure_ascii=False)+'\n' for c in contracts))
        summary=InputContracts(ROOT,{q['query_id'] for q in self.queries}).export(ROOT,self.queries)
        print('Wrote',len(contracts),'per-query contracts',summary['states'])

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--upstream',type=Path,required=True)
    ContractAudit(parser.parse_args().upstream).run()
