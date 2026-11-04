"""Import supplied task evidence and lower its explicit logical dependencies."""
import csv
import hashlib
import json
import shutil
from reference_plans import lower_collections
from pathlib import Path


class CollectionImporter:
    def __init__(self, root):
        self.root = Path(root)
        self.tables = {name: self.read_rows(self.root / 'query' / f'{name}.jsonl')
                       for name in ('queries', 'nodes', 'edges', 'sources', 'query_sources', 'task_details', 'input_contracts', 'original_queries')}
        self.metadata = json.loads((self.root / 'config/catalog.json').read_text())
        for query in self.tables['queries']:
            query.setdefault('plan_format', 'logical_dag')
            query.setdefault('collection_label', '')
            query.setdefault('category_label', '')

    @staticmethod
    def read_rows(path):
        return [json.loads(line) for line in path.read_text().splitlines() if line.strip()] if path.exists() else []

    def write_json(self, path, value):
        path = self.root / path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')

    def snapshot(self, source, collection):
        relative = Path('query/imports') / collection / source.name
        destination = self.root / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, destination)
        digest = hashlib.sha256(destination.read_bytes()).hexdigest()
        source_id = 'import_' + hashlib.sha256(str(relative).encode()).hexdigest()[:16]
        self.tables['sources'].append(dict(source_id=source_id, location=relative.as_posix(),
            original_location=str(source.resolve()), source_type='task_definition' if collection == '8-17' else 'query_analysis', title=f'{collection} / {source.name}',
            version=f'Supplied snapshot; SHA256 {digest}', verification='Local source copied and hashed; paper attribution and results not independently verified.',
            checked_on='2026-10-13', publication_label='', publication_url=''))
        return source_id

    def reset(self, collection):
        ids = {q['query_id'] for q in self.tables['queries'] if q['benchmark_id'] == collection}
        for name in ('queries', 'nodes', 'edges', 'query_sources', 'task_details'):
            self.tables[name] = [r for r in self.tables[name] if r['query_id'] not in ids]
        self.tables['sources'] = [s for s in self.tables['sources'] if not s['location'].startswith(f'query/imports/{collection}/')]
        self.metadata['scenarios'] = [s for s in self.metadata['scenarios'] if not s.startswith(f'files/{collection}/')]

    def environment(self, collection, domain, source_id, directory=None):
        identity = f'{collection}/{domain}'
        inventory = []
        if directory:
            for file in sorted(directory.rglob('*')):
                if file.is_file() and not file.name.startswith('.'):
                    inventory.append({'path': file.relative_to(directory).as_posix(), 'bytes': file.stat().st_size})
            self.write_json(f'data/{identity}/inventory.json', inventory)
        self.write_json(f'data/{identity}/manifest.json', dict(dataset_id=identity,
            source_ids=[source_id], availability='local_external' if directory else 'not_provided',
            local_path=str(directory.resolve()) if directory else None, schema=None, record_count=None,
            version=None,
            verification='File inventory only; contents and gold not evaluated' if directory else 'Query analysis CSV only; original data not supplied',
            file_count=len(inventory) if directory else None,
            total_bytes=sum(f['bytes'] for f in inventory) if directory else None,
            inventory_path=f'data/{identity}/inventory.json' if directory else None))
        self.write_json(f'environment/{identity}/manifest.json', dict(environment_id=identity,
            dataset_id=identity, runtime_status='unconfigured', engine=None, model=None, hardware=None,
            execution_status='not_executed', record_batch_size=None, query_batch=None,
            model_batch_size=None, concurrency=None))
        return identity

    @staticmethod
    def bind_input(item, directory):
        aliases = {'CONTRACTEXHIBIT_corpus': '.', 'data/contract-exhibit': '.',
                   'complaints_csv': 'data/complaints.csv', 'recalls_jsonl': 'data/recalls.jsonl',
                   'investigation_reports_txt': 'data/investigation_reports'}
        relative = aliases.get(item['source_id'], item['source_id'])
        path = directory / relative.removesuffix('/*')
        exists = path.exists()
        schema = None
        if exists and path.is_file() and path.suffix == '.csv':
            with path.open(encoding='utf-8-sig', newline='') as f:
                schema = next(csv.reader(f), [])
        return {**item, 'local_path': str(path.resolve()), 'selector': relative,
                'binding_status': 'path_verified' if exists else 'missing', 'schema': schema,
                'record_count': None}

    def add(self, collection, domain, task_id, title, source_id, locator, origin, status, details):
        qid = f'{collection}/{domain}/{task_id}'
        self.tables['queries'].append(dict(query_id=qid, benchmark_id=collection,
            scenario_id=f'{collection}-{domain}', source_query_id=task_id, title=title,
            plan_origin=origin, plan_status_label=status, source_id=source_id, root_node_id=None,
            notes='Supplied reference only; not a paper-original DAG, execution trace or reproduced result.',
            display_order=len(self.tables['queries']), group_label=f'{collection} / {domain}',
            mixed_label='Not inferred from supplied annotations', environment_id=f'{collection}/{domain}',
            plan_format='reference_program', collection_label=collection, category_label=domain))
        self.tables['query_sources'].append(dict(query_id=qid, source_id=source_id, role='task_definition' if collection == '8-17' else 'analysis',
            locator=locator, attribution_note='Supplied local task/analysis record; original attribution and answers require separate verification.'))
        self.tables['task_details'].append({'query_id': qid, **details})

    def import_august(self, folder):
        collection = '8-17'
        self.reset(collection)
        domains = {'sec10k_queries.json': ('SEC10K', 'SEC'), 'contract_exhibit_queries.json': ('ContractExhibit', 'contract-exhibit'),
                   'asrs_queries.json': ('ASRS', 'asrs'), 'nhtsa_queries.json': ('NHTSA', 'nhtsa_vehicle_safety')}
        for filename, (domain, data_folder) in domains.items():
            file = folder / 'query' / filename
            source_id = self.snapshot(file, collection)
            directory = folder / 'data' / data_folder
            if not directory.is_dir():
                raise ValueError(f'Missing supplied dataset directory: {directory}')
            self.environment(collection, domain, source_id, directory)
            rows = json.loads(file.read_text())
            rows = rows['tasks'] if isinstance(rows, dict) else rows
            for index, row in enumerate(rows):
                self.add(collection, domain, str(row['task_id']), row['query'], source_id,
                    f'{filename}: task {row["task_id"]}; array index {index}', 'supplied_reference',
                    'Supplied reference plan · not execution-verified',
                    dict(inputs=[self.bind_input(i, directory) for i in row['inputs']],
                         reference_programs=row['reference_semantic_plan'], output=row.get('gold', {}).get('answer_schema'),
                         evaluation=row.get('evaluation'), gold=row.get('gold'), annotation=None,
                         original_record=row))
            self.scenario(collection, domain)

    def import_july(self, folder):
        collection = '7-30'
        self.reset(collection)
        self.snapshot(folder / 'summary.csv', collection)
        for file in sorted(folder.glob('*_per_query.csv')):
            with file.open(encoding='utf-8-sig', newline='') as stream:
                rows = list(csv.DictReader(stream))
            domain = rows[0]['benchmark']
            source_id = self.snapshot(file, collection)
            self.environment(collection, domain, source_id)
            for index, row in enumerate(rows):
                self.add(collection, domain, row['task_id'], row['query'], source_id,
                    f'{file.name}: CSV logical row {index + 2}', 'supplied_analysis',
                    'Supplied minimal-plan analysis · original data not supplied',
                    dict(inputs=[], reference_programs=[{'type': 'minimal_plan_analysis', 'program': row['minimal_plan']}],
                         output=None, evaluation=None, gold=None,
                         annotation={k: v for k, v in row.items() if k not in ('query', 'minimal_plan')}, original_record=row))
            self.scenario(collection, domain)

    def scenario(self, collection, domain):
        path = f'files/{collection}/{domain}/scenario.json'
        self.write_json(path, dict(id=f'{collection}-{domain}', name=f'{collection} / {domain}',
            query_ids=[q['query_id'] for q in self.tables['queries'] if q['environment_id'] == f'{collection}/{domain}']))
        self.metadata['scenarios'].append(path)

    def save(self):
        operators = {o["operator_type"] for o in json.loads((self.root / "config/operators.json").read_text())}
        lower_collections(self.tables, operators, self.root)
        for index, q in enumerate(self.tables['queries']):
            q['display_order'] = index
        for name, rows in self.tables.items():
            (self.root / 'query' / f'{name}.jsonl').write_text(''.join(json.dumps(row, ensure_ascii=False) + '\n' for row in rows))
        self.metadata['scope'] = 'Logical DAG catalog plus supplied 8-17 reference tasks and 7-30 query analyses; no execution or gold validation implied.'
        self.write_json('config/catalog.json', self.metadata)
