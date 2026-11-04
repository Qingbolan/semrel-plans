"""Uniform task documents using the supplied 8-17 task schema."""
from copy import deepcopy
import json
import shutil


class TaskRecords:
    def __init__(self, catalog):
        self.catalog = catalog

    def create(self, query, nodes, edges):
        detail = self.catalog.details.get(query['query_id'], {})
        original = detail.get('original_record', {})
        if query['query_id'].startswith('8-17/'):
            return deepcopy(original)
        contract = query['input_contract']
        dataset = original.get('subset') or query['dataset']['dataset_id']
        inputs = []
        for table in contract['tables']:
            inputs.append({'source_id': table['name'], 'dataset': dataset,
                           'source_type': 'document' if table['row_unit'] == 'document' else 'table',
                           'role': 'primary', 'columns': deepcopy(table['columns']),
                           'semantic_columns': table['passed_columns'],
                           **{k:deepcopy(table[k]) for k in ('path','record_count','selection','selected_record_count') if k in table}})
        for resource in contract['environment']['resources']:
            inputs.append({'source_id': resource if isinstance(resource,str) else resource['name'],
                           'dataset': dataset, 'source_type': resource.get('source_type','document') if isinstance(resource,dict) else 'document', 'role': 'context',
                           **{k:deepcopy(resource[k]) for k in ('path','columns','record_count','selection','source_path','storage_encoding') if isinstance(resource,dict) and k in resource}})
        programs = deepcopy(detail.get('reference_programs', []))
        if not programs:
            children = {}
            for edge in edges:
                children.setdefault(edge['parent_id'], []).append(edge)
            lines=[];seen=set()
            def visit(nid):
                if nid in seen:return
                seen.add(nid)
                dependencies=sorted(children.get(nid,[]),key=lambda e:e['input_position'])
                for edge in dependencies:visit(edge['child_id'])
                n=nodes[nid]
                lines.append(f"{nid} = {n['operator_type']}({', '.join(e['child_id'] for e in dependencies)}) // {n['label']}")
            if nodes:
                parents={e['parent_id'] for e in edges}; children_ids={e['child_id'] for e in edges}
                root=next(iter(parents-children_ids),next(iter(nodes)))
                visit(root)
                programs=[{'type':'operator_dag','program':'\n'.join(lines)}]
        annotation = detail.get('annotation') or {}
        def number(value):
            return int(value) if value is not None and str(value).isdigit() else None
        semantic = sum(self.catalog.families[n['operator_type']]=='semantic' for n in nodes.values()) if nodes else number(annotation.get('semop_count'))
        relational = sum(self.catalog.families[n['operator_type']]=='relational' for n in nodes.values()) if nodes else None
        modalities=set()
        for table in contract['tables']:
            modalities.add('text' if table['row_unit'] in ['document','review'] else 'structured_table')
            for column in table['columns']:
                if column.get('type') in ['image','audio']:modalities.add(column['type'])
                elif column.get('type')=='string':modalities.add('text')
        for resource in contract['environment']['resources']:
            if isinstance(resource, dict):
                for column in resource.get('columns', []):
                    if column.get('type') in ['image', 'audio']:modalities.add(column['type'])
        output=contract.get('output')
        schema=output if isinstance(output,dict) else None
        return {'task_id':query['query_id'], 'datasets':[dataset],
                'query':query['original_query']['text'],
                'tags':{'data_modality':sorted(modalities), 'analytical_objective':None,
                        'n_rel_ops':relational, 'n_sem_ops':semantic,
                        'join_hops':sum(n['operator_type'] in ['JOIN','LEFT_JOIN','CROSS_JOIN','SEM_JOIN'] for n in nodes.values()) if nodes else None,
                        'operator_complexity':None,'plan_optimization_opportunity':[],
                        'output_type':schema.get('type') if schema else None},
                'inputs':inputs,'reference_semantic_plan':programs,
                'gold':deepcopy(detail.get('gold')) or {'gold_answer':None,'answer_schema':schema},
                'evaluation':{**(deepcopy(detail.get('evaluation')) or {'primary_metric':None}),
                              **({'input_batching':deepcopy(contract['batching'])} if 'batching' in contract else {})}}

    @staticmethod
    def export(root, queries):
        directory=root/'dist/tasks'
        if directory.exists():shutil.rmtree(directory)  # fully generated; drop folders that were renamed
        directory.mkdir()
        records=[]
        for q in queries:
            path=directory/q['collection_name']/f"{q['display_number']}.json"
            path.parent.mkdir(parents=True,exist_ok=True)
            path.write_text(json.dumps(q['task_record'],ensure_ascii=False,indent=2)+'\n')
            q['task_path']=path.relative_to(root/'dist').as_posix()
            records.append(q['task_record'])
        (root/'exports/tasks.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in records))
