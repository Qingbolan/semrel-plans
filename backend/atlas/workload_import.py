"""Import a local research project's query atlas and linked literature without rewriting source text."""
from collections import defaultdict
from copy import deepcopy
import ast
import hashlib
import json
from pathlib import Path
import re
import shutil
from urllib.parse import urlsplit, urlunsplit
from uda_source import UdaSourceCatalog
from reference_plans import dag_mixed_label

COLLECTION = 'semantic-workload-bench'
PREFIX = 'swb/'

def digest(value):
    return hashlib.sha256(value).hexdigest()

def sql_columns(sql):
    """Columns an SQL query reads, by table (aliases resolved; UDA's 'Med_drug' qualifier means table 'drug').
    Unqualified columns are listed under ''. Needs sqlglot (backend/scripts/audit/requirements.txt); empty if unparsable."""
    columns=defaultdict(list)
    try:
        import sqlglot
        from sqlglot import exp
        tree=sqlglot.parse_one(sql)
    except Exception:  # QUEST writes values unquoted ('team = Los Angeles Lakers'): select list and comparison left sides
        select=re.search(r'SELECT\s+(.*?)\s+FROM\b',sql,re.I|re.S)
        names=[c.strip() for c in select.group(1).split(',')] if select else []
        names+=re.findall(r'(?:WHERE|AND|OR|\()\s*(\w+)\s*(?:=|!=|<>|<=|>=|<|>|\bLIKE\b|\bIN\b)',sql,re.I)
        columns['']=list(dict.fromkeys(n for n in names if re.fullmatch(r'\w+',n)))
        return columns
    aliases={t.alias_or_name.lower():t.name.lower() for t in tree.find_all(exp.Table)}
    # 'setting = urban': QUEST leaves values unquoted, so a column on the right of a column comparison is a value
    values=set()
    for c in tree.find_all(exp.EQ,exp.NEQ,exp.GT,exp.GTE,exp.LT,exp.LTE):
        right=list(c.expression.find_all(exp.Column))
        if isinstance(c.this,exp.Column) and right and not any(r.table for r in right):  # 'type = quarter-based': unquoted value
            values.update(id(r) for r in right)
    for c in tree.find_all(exp.Column):
        if id(c) in values:continue
        table=aliases.get(c.table.lower(),c.table.lower()) if c.table else ''
        table=re.sub(r'^med_','',table)
        if c.name not in columns[table]:columns[table].append(c.name)
    return columns

UNSPECIFIED_LOOKUP='；检索实现尚未指定'

def workload_label(op,detail,scan_table,columns,record_id=''):
    """Readable node text for the supplied plans: no provenance jargon in labels; extraction steps name their fields;
    helper identifiers (sem_map_relevance_rank) read as words."""
    identifier=re.fullmatch(r'([a-z][a-z0-9_]*)('+UNSPECIFIED_LOOKUP+')?',detail)
    if op in ('SMap','Transform','Lookup') and identifier:
        return op+' '+re.sub(r'^(sem_map|retrieve)_','',identifier.group(1)).replace('_',' ')
    if op=='Filter' and '（HTS为显式前缀；其他按原契约）' in detail:  # template clause that only applies to the HTS task
        return op+' '+detail.replace('（HTS为显式前缀；其他按原契约）','（HTS 编码按显式前缀匹配）' if record_id.startswith('hscodecomp') else '')
    if op=='Unnest' and re.fullmatch(r'[a-z_]+(/[a-z_]+)+',detail):return 'Unnest 检索结果'  # pandas call chain in the source
    if op=='Scan':return 'Scan '+re.sub(r'\s*(对应)?原始文档集合$','（文档）',detail)
    if op=='SExtract':
        fields=re.sub(r'^逻辑补出的原文抽取；','',detail)
        if scan_table is not None and (columns.get(scan_table) or (fields.startswith('原文→') and columns.get(''))):
            needed=[f.strip() for f in fields.split(',')] if not fields.startswith('原文→') else []
            needed+=[c for c in columns.get(scan_table,[])+(columns.get('',[]) if fields.startswith('原文→') else []) if c not in needed]
            fields=', '.join(needed)
        return 'SExtract '+fields
    return op+' '+re.sub(r'\s{2,}',' ',detail)

def rows(path):
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]

def canonical_url(url):
    url=url.strip('<>').split('#')[0].rstrip('/')
    url=re.sub(r'(arxiv.org)/(pdf|html)/',r'\1/abs/',url)
    url=re.sub(r'(arxiv.org/abs/[^?]+?)(?:v\d+)?(?:\.pdf)?$',r'\1',url)
    if 'aclanthology.org/' in url or 'nature.com/articles/' in url:url=url.removesuffix('.pdf')
    return url.replace('http://','https://',1)

class WorkloadProjectImporter:
    def __init__(self, root, source):
        self.root=Path(root); self.source=Path(source)
        self.base=Path('upstream/imports')/COLLECTION
        self.tables={n:rows(self.root/'catalog'/f'{n}.jsonl') for n in ('queries','nodes','edges','sources','query_sources','task_details','input_contracts','original_queries')}
        self.metadata=json.loads((self.root/'config/catalog.json').read_text())
        self.types=json.loads((self.root/'config/paper-types.json').read_text())
        self.registry=json.loads((self.root/'config/workload-registry.json').read_text())
        self.environment_ids={p.parent.relative_to(self.root/'environment').as_posix().lower():p.parent.relative_to(self.root/'environment').as_posix() for p in (self.root/'environment').rglob('manifest.json')}
        self.files={}; self.paper_documents=defaultdict(set); self.paper_links={};self.coverage=[]

    def write(self, relative, value):
        path=self.root/relative;path.parent.mkdir(parents=True,exist_ok=True)
        path.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')
        return relative.as_posix() if isinstance(relative,Path) else relative

    def snapshot(self,path):
        path=Path(path)
        if path in self.files:return self.files[path]['path']
        try:relative=path.relative_to(self.source)
        except ValueError:relative=Path('external')/digest(str(path).encode())[:12]/path.name
        target=self.base/'sources'/relative
        (self.root/target).parent.mkdir(parents=True,exist_ok=True)
        shutil.copyfile(path,self.root/target)
        self.files[path]={'path':target.as_posix(),'original_path':str(path),'sha256':digest(path.read_bytes())}
        return target.as_posix()

    def add_source(self,location,title,kind='task_definition'):
        sid='swb_'+digest(location.encode())[:16]
        if not any(s['source_id']==sid for s in self.tables['sources']):
            self.tables['sources'].append(dict(source_id=sid,location=location,title=title,source_type=kind,version='Local project snapshot',verification='Source-linked project record',checked_on='2026-10-13',publication_label='',publication_url=location if kind=='paper' else ''))
        return sid

    def reference(self,qid,sid,role,locator):
        if not any(r['query_id']==qid and r['source_id']==sid and r['role']==role for r in self.tables['query_sources']):
            self.tables['query_sources'].append(dict(query_id=qid,source_id=sid,role=role,locator=locator,attribution_note='Imported from the supplied semantic-workload-bench project.'))

    def import_literature(self):
        existing={canonical_url(s['location']):s['source_id'] for s in self.tables['sources'] if s['source_type']=='paper'}
        # Existing reading-note papers must share the same source identity on import.
        survey=json.loads((self.root/'papers/survey/manifest.json').read_text())
        for entry in survey:
            p=self.root/'Survey'/entry['folder']/'README.md'
            urls=re.findall(r'\]\((https?://[^\s)]+)\)',p.read_text())
            if urls:
                url=canonical_url(urls[0])
                if url not in existing:existing[url]=self.add_source(url,entry['folder'].rsplit('-',2)[0],'paper')
        documents=sorted(set(self.source.glob('*.md'))|set((self.source/'docs').rglob('*.md'))|set((self.source/'workloads').rglob('*.md'))|set((self.source/'environments').rglob('*.md')))
        generic=re.compile(r'^(?:原文|论文|原论文|项目原论文|paper|original paper|原始论文|作者论文|完整论文|论文PDF|PDF)$',re.I)
        for path in documents:
            local=self.snapshot(path);text=path.read_text();heading=next((s.lstrip('# ').strip() for s in text.splitlines() if s.startswith('#')) ,path.stem)
            links=re.findall(r'\[([^\]]+)\]\((https?://[^\s)]+)\)',text)
            linked={u for _,u in links}
            for url in re.findall(r'https?://[a-zA-Z0-9./_?=&%~:#@+;-]+',text):
                if url not in linked and re.search(r'arxiv.org/(?:abs|pdf|html)/|aclanthology.org/|doi.org/|nature.com/articles/|vldb.org/pvldb/',url):links.append(('Original paper',url.rstrip('.;:')))
            for arxiv_id in re.findall(r'arXiv[:\s]?(\d{4}\.\d{4,5})',text,re.I):links.append(('Original paper','https://arxiv.org/abs/'+arxiv_id))
            for label,url in links:
                academic=re.search(r'arxiv.org/(?:abs|pdf|html)/|aclanthology.org/[^/\s]+|doi.org/(?!10.5281|10.6084)|vldb.org/pvldb|proceedings.mlr|openreview.net/(?:forum|pdf)|dl.acm.org/doi|(?:papers|proceedings).neurips|nature.com/articles|pubmed.ncbi|pmc.ncbi',url)
                explicit=re.search(r'论文|\bpaper\b',label,re.I) or ('原论文['+label+']') in text
                if not (academic or explicit) or re.search(r'指南|手册|规范|仓库|评审|搜索|列表|征稿|截止',label):continue
                url=canonical_url(url)
                title=(heading+' — '+label) if generic.fullmatch(label.strip()) else label
                sid=existing.get(url)
                if sid is None:sid=self.add_source(url,title,'paper');existing[url]=sid
                self.paper_documents[sid].add(local);self.paper_links[url]=sid
                self.types.setdefault(sid,'research')
        for url,entry in self.registry['papers'].items():
            sid=existing.get(canonical_url(url)) or self.add_source(url,entry['title'],'paper')
            existing[canonical_url(url)]=sid
            self.paper_links[canonical_url(url)]=sid
            for document in entry['evidence']:
                self.paper_documents[sid].add(self.snapshot(self.source/document))
            self.types.setdefault(sid,'research')
        for sid,docs in self.paper_documents.items():
            source=next(s for s in self.tables['sources'] if s['source_id']==sid)
            if not sid.startswith('swb_'):continue
            candidates=[]
            for doc in docs:
                text=(self.root/doc).read_text()
                identity=re.search(r'身份：([^，；\n]+)',text)
                if identity:candidates.append((0,identity.group(1)))
                heading=next((line.lstrip('# ').strip() for line in text.splitlines() if line.startswith('#')),'')
                heading=re.sub(r'^(?:第[^：:]+|Increment\d+|增量\d+)[：:— –]*','',heading).strip()
                if heading and not re.search(r'log|报告|索引|交付|总结|契约',heading,re.I):candidates.append((1 if '/workloads/' in doc else 2,heading))
            if candidates and ('— Original paper' in source['title'] or '— 原论文' in source['title'] or '— 论文' in source['title']):source['title']=min(candidates)[1]
        metadata_path=self.root/self.base/'paper-metadata.json'
        if metadata_path.exists():
            for entry in json.loads(metadata_path.read_text()):
                if entry['status']!='metadata_found':continue
                source=next((s for s in self.tables['sources'] if s['source_id']==entry['source_id']),None)
                if source and source['source_id'].startswith('swb_'):
                    source['title']=entry['title']
                    source['publication_label']=' '.join(filter(None,[entry.get('venue'),entry.get('date')]))
        # Curated identities take precedence over inferred document headings and HTML metadata.
        for url,entry in self.registry['papers'].items():
            sid=self.paper_links[canonical_url(url)]
            source=next(source for source in self.tables['sources'] if source['source_id']==sid)
            source['title']=entry['title']
            if entry.get('publication_label'):source['publication_label']=entry['publication_label']
        for url,title in json.loads((self.root/'config/paper-identities.json').read_text())['titles'].items():
            for source in self.tables['sources']:
                if source['source_type']=='paper' and canonical_url(source['location'])==canonical_url(url):source['title']=title
        self.documents=documents
        self.paper_records=[]
        for sid,docs in self.paper_documents.items():
            s=next(s for s in self.tables['sources'] if s['source_id']==sid)
            self.paper_records.append({'source_id':sid,'url':s['location'],'documents':sorted(docs)})

    def paper_ids(self, record):
        assignment=self.registry['queries'][record['id']]
        return [self.paper_links[canonical_url(url)] for url in assignment['paper_urls']]

    def medical_contract(self, record, source_path):
        query=int(record['id'].rsplit('/Q',1)[1])
        modalities={1:['SymptomsText'],2:['LungAudio'],3:['XrayImage'],4:['SymptomsText'],5:['LungAudio','XrayImage'],6:['SymptomsText','XrayImage','LungAudio'],7:['SymptomsText','XrayImage','SkinCancer','LungAudio'],8:['SkinCancer'],9:['SkinCancer','XrayImage'],10:['SymptomsText']}[query]
        schema={'Patient':[('patient_id','string'),('age','integer'),('gender','string'),('smoking_history','string'),('did_family_have_cancer','boolean')],'SymptomsText':[('patient_id','string'),('symptom_id','string'),('symptom','string')],'XrayImage':[('patient_id','string'),('xray_id','string'),('xray_image','image')],'SkinCancer':[('patient_id','string'),('skin_image_id','string'),('skin_image','image')],'LungAudio':[('patient_id','string'),('audio_id','string'),('location','string'),('filtration_type','string'),('audio','audio')]}
        semantic={'Patient':[],'SymptomsText':['symptom'],'XrayImage':['xray_image'],'SkinCancer':['skin_image'],'LungAudio':['audio']}
        names=(['Patient'] if query!=10 else [])+modalities
        tables=[{'name':name,'columns':[{'name':column,'type':kind} for column,kind in schema[name]],'passed_columns':semantic[name],'row_unit':'record','scope':'used'} for name in names]
        readme=Path(record['source']).parents[4]/'src/scenario/medical/README.md'
        evidence_path=self.snapshot(readme)
        return {'query_id':'','environment':{'requirement':'required' if query==10 else 'none','resources':[{'name':'Disease label list','kind':'classification_labels'}] if query==10 else []},'tables':tables,'output':None,'evidence':{'path':source_path,'locator':record['id'],'excerpt':record['query']},'supplementary_evidence':[{'path':evidence_path,'locator':'Schema and Query Summary'}],'notes':[],'audit_status':'source_definition'}

    def input_contract(self,record,source_path):
        if record['group']=='sembench-medical':return self.medical_contract(record,source_path)
        tables=[];resources=[];requirement='unspecified'
        for node in (record['graph'] or {}).get('nodes',[]):
            if node['op']!='Scan':continue
            name=node['detail']
            if 'frozen public lake' in name:
                resources.append({'name':name,'kind':'reference_corpus'});requirement='required';continue
            name=re.sub(r'\s*(?:对应原始文档集合|原始文档集合)$','',name)
            tables.append({'name':name,'columns':[],'passed_columns':None,'row_unit':'document' if record['group'].startswith(('uda-','quest-')) else 'record','scope':'used'})
        if record['group'].startswith('uda-'):
            from sql_inputs import extract_sql
            parsed=extract_sql(record['query'],'sqlite')
            tables=parsed['tables'] if isinstance(parsed,dict) else parsed
            for t in tables:
                t['row_unit']='document';t['passed_columns']=None
        if record['group']=='derived-five-lakes':
            lake=record['id'].split('-Q')[0];public=self.source/'data/shared-environment-five-lakes-v2'/lake/'public'
            for t in tables:
                p=public/'records.json'
                if p.exists():
                    data=json.loads(p.read_text());t['path']=str(p);t['record_count']=len(data)
                    if isinstance(data,list) and data and isinstance(data[0],dict):t['columns']=[{'name':k,'type':None} for k in data[0]]
            for resource in resources:resource['path']=str(public/'lake')
        if record['group']=='public-tasks':
            task=record['task_definition']
            for key in ('shared_environment','environment','resources','required_inputs','allowed_inputs'):
                value=task.get(key)
                if value:
                    for item in value if isinstance(value,list) else [value]:
                        resources.append({'name':str(item),'kind':key})
            if resources:requirement='required'
            parent=Path(record['source']).parent
            if record.get('domain')=='biodex':parent=self.source/'data/biodex-gap-pilot-v1/public'
            if record.get('domain')=='pathology':parent=self.source/'data/pathology-batch-v1/public'
            if parent.name=='public' or 'inspection' in parent.name:
                for path in sorted(parent.iterdir()):
                    if path.name in ('task.json','queries.json','manifest.json','gold.csv') or path.name.startswith('private'):continue
                    if re.search(r'environment|protocol|guideline|terminology|manual',path.name,re.I):
                        resources.append({'name':path.name,'kind':'reference_material','path':str(path)});requirement='required';continue
                    if not (path.is_dir() or path.suffix in ('.json','.jsonl','.csv','.sqlite','.db')):continue
                    table={'name':path.name,'path':str(path),'columns':[],'passed_columns':None,'row_unit':'document' if path.is_dir() else 'record','scope':'available'}
                    sample=next(iter(sorted(path.glob('*.json'))),None) if path.is_dir() else path
                    if sample and sample.suffix in ('.json','.jsonl') and sample.stat().st_size<10_000_000:
                        data=json.loads(sample.read_text()) if sample.suffix=='.json' else rows(sample)
                        if isinstance(data,list):
                            if not path.is_dir():table['record_count']=len(data)
                            data=data[0] if data else None
                        if isinstance(data,dict):table['columns']=[{'name':k,'type':None} for k in data]
                    tables.append(table)
        return dict(query_id='',environment={'requirement':requirement,'resources':resources},tables=tables,output=None,evidence={'path':source_path,'locator':record['id'],'excerpt':record['query']},notes=[],audit_status='project_source')

    def public_tasks(self):
        records=[]
        for path in sorted((self.source/'data').rglob('task.json')):
            if 'public' not in path.parts and 'inspection' not in str(path):continue
            data=json.loads(path.read_text());self.snapshot(path)
            fields=[k for k in ('request','question','query','instruction','predicate','task','optional_task') if isinstance(data.get(k),str)]
            for field in fields:
                relative=path.relative_to(self.source).as_posix()
                lake=data.get('dataset')
                domain=lake if lake else re.sub(r'-(?:v|check-v)\d+$','',relative.split('/')[1])
                records.append(dict(id='public-task/'+relative.removeprefix('data/').removesuffix('/task.json')+'/'+field,group='public-tasks',query=data[field],source=str(path),source_line=None,provenance='local_derived',status='source_definition',note='',composition='',graph=None,task_definition=data,domain=domain))
        # BioDEX's public task file contains only an identifier; its actual prompt is a source constant.
        path=self.source/'src/semantic_workload_bench/biodex_experiment.py'
        module=ast.parse(path.read_text())
        instruction=next(ast.literal_eval(n.value) for n in module.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='INSTRUCTION' for t in n.targets))
        records.append(dict(id='public-task/biodex/INSTRUCTION',group='public-tasks',query=instruction,source=str(path),source_line=15,provenance='local_derived',status='source_definition',note='',composition='',graph=None,task_definition={'instruction':instruction},domain='biodex'))
        path=self.source/'workloads/pathology-patches/workload-card.md'
        request=next(line for line in path.read_text().splitlines() if line.startswith('业务请求：'))
        records.append(dict(id='public-task/pathology/workload',group='public-tasks',query=request,source=str(path),source_line=None,provenance='local_derived',status='source_definition',note='',composition='',graph=None,task_definition={'request':request},domain='pathology'))
        return records

    def run(self):
        uda=UdaSourceCatalog(self.root,self.metadata['source_commits']['UDA-Bench'])
        atlas_path=self.source/'artifact/evidence/benchmark-query-plan-atlas-20261012/plans.json'
        atlas=json.loads(atlas_path.read_text())['records']
        uda.validate_records(atlas)
        uda_existing=uda.existing(self.tables['original_queries'])
        # Replace this import's own records; never remove pre-existing catalog entries.
        previous_scenarios=[p for p in self.metadata['scenarios'] if p.startswith('files/'+COLLECTION+'/')]
        previous_ids={q['query_id'] for q in self.tables['queries'] if q['query_id'].startswith(PREFIX)}
        # Keep each record's catalog position; other importers append after this one, so len() is not a free slot.
        previous_order={q['query_id']:q['display_order'] for q in self.tables['queries'] if q['query_id'] in previous_ids}
        next_order=max((q['display_order'] for q in self.tables['queries']),default=-1)+1
        previous_environments={q['environment_id'] for q in self.tables['queries'] if q['query_id'] in previous_ids}
        for name in ('queries','nodes','edges','task_details','input_contracts','original_queries'):
            self.tables[name]=[r for r in self.tables[name] if r['query_id'] not in previous_ids]
        self.tables['query_sources']=[r for r in self.tables['query_sources'] if r['query_id'] not in previous_ids and not r['source_id'].startswith('swb_')]
        self.metadata['scenarios']=[p for p in self.metadata['scenarios'] if not p.startswith('files/'+COLLECTION+'/')]
        self.import_literature()
        self.snapshot(atlas_path)
        self.snapshot(atlas_path.with_name('sources.json'))
        atlas_count=len(atlas)
        atlas+=self.public_tasks()
        originals={r['query_id']:r for r in self.tables['original_queries']}
        by_text=defaultdict(list)
        for q in self.tables['queries']:
            domain='sembench-'+q['scenario_id'] if q['benchmark_id']=='sembench' else 'uda-'+q['query_id'].split('/')[2].lower() if q['benchmark_id']=='uda-bench' else q['environment_id']
            by_text[(domain,' '.join(originals[q['query_id']]['text'].split()))].append(q['query_id'])
        operators={o['operator_type']:o for o in json.loads((self.root/'config/operators.json').read_text())}
        mapping={'Scan':'SCAN','SFilter':'SEM_FILTER','SMap':'SEM_MAP','SExtract':'SEM_MAP','SJoin':'SEM_JOIN','SLeftJoin':'SEM_LEFT_JOIN','SAggregate':'SEM_AGG','Aggregate':'AGGREGATE','AntiJoin':'ANTI_JOIN','Distinct':'DISTINCT','Filter':'FILTER','Intersect':'INTERSECT','Join':'JOIN','LeftJoin':'LEFT_JOIN','Limit':'LIMIT','Project':'PROJECT','Sort':'SORT','Union':'UNION_DISTINCT','Unnest':'UNNEST','Transform':'COMPUTE','PartitionTopK':'PARTITION_TOPK','ExternalSearch':'EXTERNAL_SEARCH','Lookup':'LOOKUP','ResultBundle':'RESULT_BUNDLE','Unresolved':'UNRESOLVED'}
        groups=defaultdict(list)
        if {r['id'] for r in atlas} != set(self.registry['queries']):
            raise ValueError('Every imported record requires an explicit source assignment')
        # Redundant versions of one task are folded into the version named by `superseded_by`; import kept versions first.
        superseded=[r for r in atlas if self.registry['queries'][r['id']].get('superseded_by')]
        atlas=[r for r in atlas if r not in superseded]+superseded
        for record in atlas:
            assignment=self.registry['queries'][record['id']]
            if assignment.get('superseded_by'):
                kept=next((c for c in self.coverage if c['source_query_id']==assignment['superseded_by'] and c['status']!='superseded'),None)
                if kept is None:raise ValueError('Superseded record must name an imported version: '+record['id'])
                original_path=self.snapshot(record['source']);sid=self.add_source(original_path,record['group']+' source')
                record_path=self.write(self.base/'records'/f"{digest(record['id'].encode())[:20]}.json",record)
                self.reference(kept['query_id'],sid,'task_definition',record['id'])
                self.reference(kept['query_id'],self.add_source(record_path,record['id'],'query_analysis'),'analysis',record['id'])
                self.coverage.append(dict(source_query_id=record['id'],query_id=kept['query_id'],status='superseded',superseded_by=assignment['superseded_by'],record_path=record_path,source_path=original_path,assignment=assignment))
                continue
            original_path=self.snapshot(record['source']); sid=self.add_source(original_path,record['group']+' source')
            uda_record=uda.records.get(record['id'])
            if uda_record:
                original_path=uda_record['path']
                sid=self.add_source(uda_record['url'],record['group']+' SQL source','query_code')
                source=next(s for s in self.tables['sources'] if s['source_id']==sid)
                source.update(version=uda.manifest['commit'],verification='SQL file verified against pinned repository archive',checked_on=uda.manifest['checked_on'])
            record_path=self.write(self.base/'records'/f"{digest(record['id'].encode())[:20]}.json",record)
            analysis_sid=self.add_source(record_path,record['id'],'query_analysis')
            domain=record['id'] if record['group']=='public-tasks' else record['id'].split('-Q')[0] if record['group']=='derived-five-lakes' else record['group']
            text_key=(domain,' '.join(record['query'].split()))
            matches=([uda_existing[record['id']]] if record['id'] in uda_existing else []) if uda_record else by_text[text_key]
            # UDA preserves every source occurrence; other project records retain text linking.
            if matches:
                qid=matches[0];status='linked_existing'
            else:
                qid=PREFIX+record['id'];status='added'
                if any(q['query_id']==qid for q in self.tables['queries']):raise ValueError('Import identity collision '+qid)
                group=record['group'];collection=assignment['collection'];category=assignment['category']
                # Public-task categories are workspace paths; they key environments but are not readable labels.
                label=('Derived tasks' if assignment['query_kind']=='derived_task' else 'Repository queries') if group=='public-tasks' else category
                group_key=re.sub(r'[^a-z0-9]+','-',collection.lower()).strip('-')+'/'+re.sub(r'[^a-z0-9]+','-',category.lower()).strip('-')
                scenario='swb-'+group_key;identity=self.environment_ids.get(group_key.lower(),group_key)
                graph=record['graph'] or {'nodes':[],'edges':[],'root':None}
                columns=sql_columns(record['query']) if re.match(r'\s*SELECT\b',record['query'],re.I) else {}
                ops={n['id']:n for n in graph['nodes']}
                scan_of={parent:ops[child]['detail'].split()[0].lower() for child,parent in graph['edges'] if ops[child]['op']=='Scan'}
                for n in graph['nodes']:
                    op=mapping[n['op']];operators.setdefault(op,{'operator_type':op,'family':'relational'})
                    node_label=workload_label(n['op'],n['detail'],scan_of.get(n['id']),columns,record['id'])
                    self.tables['nodes'].append(dict(query_id=qid,node_id=n['id'],operator_type=op,label=node_label))
                positions=defaultdict(int)
                for child,parent in graph['edges']:
                    self.tables['edges'].append(dict(query_id=qid,parent_id=parent,child_id=child,input_position=positions[parent]));positions[parent]+=1
                if qid not in previous_order:previous_order[qid]=next_order;next_order+=1
                self.tables['queries'].append(dict(query_id=qid,benchmark_id=re.sub(r'[^a-z0-9]+','-',assignment['benchmark'].lower()).strip('-'),scenario_id=scenario,source_query_id=record['id'],title=assignment.get('title') or record['query'],plan_origin='derived_workload' if assignment['query_kind']=='derived_task' else 'source_reconstruction',plan_status_label='',source_id=sid,root_node_id=graph['root'],notes=' '.join(filter(None,[assignment.get('note',''),'Lookup 步骤只说明需要检索，检索实现尚未指定。' if any(UNSPECIFIED_LOOKUP in n['detail'] for n in graph['nodes']) else ''])),display_order=previous_order[qid],group_label=collection+' / '+label,mixed_label=dag_mixed_label([mapping[n['op']] for n in graph['nodes']],{k:v['family'] for k,v in operators.items()}),environment_id=identity,plan_format='logical_dag' if record['graph'] else 'reference_program',collection_label=collection,category_label=label))
                contract=self.input_contract(record,original_path);contract['query_id']=qid;self.tables['input_contracts'].append(contract)
                self.tables['original_queries'].append(dict(query_id=qid,text=record['query'],kind='sql' if group.startswith(('uda-','quest-')) else 'local_definition' if assignment['query_kind'] in ('derived_task','code_example') else 'natural_language',verification='supplied_project_record',source_path=record_path,selector={'type':'json_field','field':'query'},source_sha256=digest((self.root/record_path).read_bytes()),text_sha256=digest(record['query'].encode()),upstream_comparison=None))
                self.tables['task_details'].append(dict(query_id=qid,original_record=deepcopy(record),inputs=[],reference_programs=[{'type':'task_definition' if record.get('task_definition') else 'source_graph','program':json.dumps(record.get('task_definition') or graph,ensure_ascii=False,indent=2)}],output=None,evaluation=None,gold=None,annotation=None))
                groups[group_key].append(qid);by_text[text_key].append(qid)
                if not (self.root/'environment'/identity/'manifest.json').exists():
                    self.write(Path('data')/identity/'manifest.json',dict(dataset_id=identity,source_ids=[sid],availability='source_definition',local_path=None,schema=None,record_count=None,version='Imported project snapshot',file_count=None,total_bytes=None,inventory_path=None,verification='Source definitions retained'))
                    self.write(Path('environment')/identity/'manifest.json',dict(environment_id=identity,dataset_id=identity,runtime_status='unconfigured',engine=None,model=None,hardware=None,execution_status='not_executed',record_batch_size=None,query_batch=None,model_batch_size=None,concurrency=None))
            if uda_record:
                self.tables['original_queries']=[r for r in self.tables['original_queries'] if r['query_id']!=qid]
                self.tables['original_queries'].append(uda.original(record['id'],qid))
                query=next(q for q in self.tables['queries'] if q['query_id']==qid)
                query['source_id']=sid
                query['source_query_id']=record['id']
            self.reference(qid,sid,'task_definition',record['id']);self.reference(qid,analysis_sid,'analysis',record['id'])
            for pid in self.paper_ids(record):
                self.reference(qid,pid,'paper',record['id'])
                ref=next(r for r in self.tables['query_sources'] if r['query_id']==qid and r['source_id']==pid and r['role']=='paper')
                ref['relationship']=assignment['paper_relation']
                ref['attribution_note']={'query_source':'Query from the named benchmark repository.','dataset_origin':'Dataset paper; the task definition is derived in the supplied project.','system_implementation':'Implementation example from the system repository.'}[assignment['paper_relation']]
                ref['evidence_paths']=[self.snapshot(self.source/path) for path in assignment['evidence']]

            self.coverage.append(dict(source_query_id=record['id'],query_id=qid,status=status,record_path=record_path,source_path=original_path,assignment=assignment))
        uda_coverage=uda.coverage(self.coverage)
        for group,qids in groups.items():
            path=Path('files')/COLLECTION/group/'scenario.json'
            self.write(path,{'id':'swb-'+group,'name':group,'query_ids':qids});self.metadata['scenarios'].append(path.as_posix())
        first={}
        for q in self.tables['queries']:  # UDA repeats some SQL at two query sites; say so instead of showing twin titles
            if q['benchmark_id']=='uda-bench' and q['query_id'].startswith(PREFIX):
                key=' '.join(q['title'].split())
                if key in first:q['notes']=' '.join(filter(None,[q['notes'],f"与 {first[key]} 的 SQL 相同（上游重复）。"]))
                else:first[key]=q['query_id'].split('/',2)[2]
        for name,records in self.tables.items():(self.root/'catalog'/f'{name}.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in records))
        self.write('config/catalog.json',self.metadata);self.write('config/paper-types.json',self.types);self.write('config/operators.json',list(operators.values()))
        self.write(self.base/'literature.json',self.paper_records)
        report={'project':str(self.source),'atlas_records':atlas_count,'public_task_records':len(atlas)-atlas_count,'total_source_records':len(atlas),'added_queries':sum(r['status']=='added' for r in self.coverage),'linked_queries':sum(r['status']=='linked_existing' for r in self.coverage),'superseded_queries':sum(r['status']=='superseded' for r in self.coverage),'literature_records':len(self.paper_records),'research_documents':len(self.documents),'queries':self.coverage,'files':list(self.files.values())}
        self.write('exports/semantic-workload-import.json',report)
        self.write('exports/uda-source-coverage.json',uda_coverage)
        # Remove only obsolete outputs owned by this importer after the new catalog is written.
        for path in previous_scenarios:
            if path not in self.metadata['scenarios']:(self.root/path).unlink(missing_ok=True)
        used_environments={q['environment_id'] for q in self.tables['queries']}
        for directory in ('data','environment'):
            for identity in previous_environments-used_environments:
                (self.root/directory/identity/'manifest.json').unlink(missing_ok=True)
            for path in (self.root/directory/COLLECTION).glob('**/manifest.json'):
                if path.parent.relative_to(self.root/directory).as_posix() not in used_environments:path.unlink()
        for path in (self.root/'data').glob('**/manifest.json'):
            manifest=json.loads(path.read_text())
            if manifest.get('version')=='Imported project snapshot' and manifest['dataset_id'] not in used_environments:
                path.unlink()
                (self.root/'environment'/manifest['dataset_id']/'manifest.json').unlink(missing_ok=True)
        for path in (self.root/'dist/tasks'/COLLECTION).glob('*.json'):path.unlink()

        return {k:v for k,v in report.items() if k not in ('queries','files')}
