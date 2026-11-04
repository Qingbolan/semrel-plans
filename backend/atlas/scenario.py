"""Normalized catalog with referential integrity and graph validation."""
from pathlib import Path
from collections import defaultdict
import json
from input_contracts import InputContracts
from task_records import TaskRecords
from query_originals import QueryOriginals
from collection_folders import CollectionFolders

class Catalog:
    TABLES = ('queries', 'nodes', 'edges', 'sources', 'query_sources', 'task_details')

    def __init__(self, root: Path):
        self.root = root
        self.content_en = json.loads((root / 'config/content-en.json').read_text())
        self.metadata = json.loads((root / 'config/catalog.json').read_text())
        self.tables = {name: [json.loads(line) for line in (root / f'catalog/{name}.jsonl').read_text().splitlines() if line.strip()] for name in self.TABLES}
        self.operators = json.loads((root / 'config/operators.json').read_text())
        self.families = {op['operator_type']: op['family'] for op in self.operators}
        self.environments = self.load_manifests('environment', 'environment_id', {q['environment_id'] for q in self.tables['queries']})
        self.datasets = self.load_manifests('data', 'dataset_id', {e['dataset_id'] for e in self.environments.values()})
        self.details = {d['query_id']: d for d in self.tables['task_details']}
        self.input_contracts = InputContracts(root, {q["query_id"] for q in self.tables["queries"]})
        self.original_queries = QueryOriginals(root, self.tables["queries"])
        self.folders = CollectionFolders(root)
        self.validate()

    def load_manifests(self, directory, key, identities):
        records = {}
        for identity in sorted(identities):
            path = (self.root / directory / identity / 'manifest.json').resolve()
            if not path.is_relative_to((self.root / directory).resolve()):
                raise ValueError('Manifest path escapes catalog directory')
            record = json.loads(path.read_text())
            if record[key] != identity or identity in records:
                raise ValueError('Invalid manifest identity')
            records[identity] = record
        return records

    @staticmethod
    def unique(rows, fields):
        keys = [tuple(row[f] for f in fields) for row in rows]
        if len(keys) != len(set(keys)):
            raise ValueError(f'Duplicate key: {fields}')

    def graph(self, query_id):
        nodes = {n['node_id']: n for n in self.tables['nodes'] if n['query_id'] == query_id}
        children = defaultdict(list)
        for edge in self.tables['edges']:
            if edge['query_id'] == query_id:
                children[edge['parent_id']].append(edge)
        for edges in children.values():
            edges.sort(key=lambda e: e['input_position'])
        return nodes, children

    def validate(self):
        t = self.tables
        self.unique(t['queries'], ['query_id'])
        self.unique(t['queries'], ['display_order'])
        self.unique(t['nodes'], ['query_id', 'node_id'])
        self.unique(t['edges'], ['query_id', 'parent_id', 'input_position'])
        self.unique(t['sources'], ['source_id'])
        self.unique(t['query_sources'], ['query_id', 'source_id', 'role'])
        self.unique(t['task_details'], ['query_id'])
        self.unique(self.operators, ['operator_type'])
        allowed_origins = {'source_reconstruction', 'baseline_reconstruction', 'end_to_end_interpretation', 'proposed_missing_sql', 'intent_sql_mismatch', 'derived_workload', 'supplied_reference', 'supplied_analysis'}
        for q in t['queries']:
            if q['plan_origin'] not in allowed_origins:
                raise ValueError('Unknown plan_origin')
            if q['environment_id'] not in self.environments:
                raise ValueError('Missing environment')
        for env in self.environments.values():
            if env['dataset_id'] not in self.datasets:
                raise ValueError('Missing dataset')
        source_ids = {s['source_id'] for s in t['sources']}
        for dataset in self.datasets.values():
            if not set(dataset['source_ids']) <= source_ids:
                raise ValueError('Unknown dataset source')
        if any(op['family'] not in {'input', 'semantic', 'relational'} for op in self.operators):
            raise ValueError('Unknown operator family')
        for edge in t['edges']:
            if type(edge['input_position']) is not int or edge['input_position'] < 0:
                raise ValueError('Input position must be a nonnegative integer')
        qids = {q['query_id'] for q in t['queries']}
        if any(d['query_id'] not in qids for d in t['task_details']):
            raise ValueError('Orphan task details')
        sources = {s['source_id'] for s in t['sources']}
        for ref in t['query_sources']:
            if ref['query_id'] not in qids or ref['source_id'] not in sources:
                raise ValueError('Dangling provenance reference')
            if ref['role'] not in {'paper', 'dataset', 'protocol', 'task_definition', 'analysis'} or not ref['attribution_note']:
                raise ValueError('Invalid provenance role or attribution')
        for qid in qids:
            refs = [ref for ref in t['query_sources'] if ref['query_id'] == qid]
            if not any(ref['role'] in {'paper', 'protocol', 'task_definition', 'analysis'} for ref in refs):
                raise ValueError('Missing paper or protocol provenance')
            if not any(ref['role'] == 'dataset' for ref in refs) and not any(ref['role'] in {'protocol', 'task_definition', 'analysis'} for ref in refs):
                raise ValueError('Missing dataset provenance')
        for source in t['sources']:
            loc = source['location']
            if not loc.startswith('https://') and not (self.root / loc).is_file():
                raise ValueError(f'Missing source: {loc}')
        for row in t['nodes'] + t['edges']:
            if row['query_id'] not in qids:
                raise ValueError('Orphan query reference')
        for node in t['nodes']:
            if node['operator_type'] not in self.families or not node['label']:
                raise ValueError('Unknown operator or empty label')
        for q in t['queries']:
            if q['source_id'] not in sources:
                raise ValueError('Unknown source')
            nodes, children = self.graph(q['query_id'])
            if q['plan_format'] == 'reference_program':
                if nodes or children or q['root_node_id'] is not None or q['query_id'] not in self.details:
                    raise ValueError('Reference task must have details and no fabricated graph')
                continue
            if q['plan_format'] != 'logical_dag':
                raise ValueError('Unknown plan format')
            for parent, edges in children.items():
                if parent not in nodes or any(e['child_id'] not in nodes for e in edges):
                    raise ValueError('Dangling graph edge')
                if [e['input_position'] for e in edges] != list(range(len(edges))):
                    raise ValueError('Input positions must be contiguous from zero')
            seen, active = set(), set()
            def visit(nid):
                if nid in active:
                    raise ValueError('Cycle in plan')
                if nid not in nodes:
                    raise ValueError('Missing root or child')
                if nid in seen:
                    return
                active.add(nid)
                for e in children[nid]:
                    visit(e['child_id'])
                active.remove(nid)
                seen.add(nid)
            visit(q['root_node_id'])
            if seen != set(nodes):
                raise ValueError('Unreachable nodes')
        indexed = []
        for path in self.metadata['scenarios']:
            scenario = json.loads((self.root / path).read_text())
            expected = {q['query_id'] for q in t['queries'] if q['scenario_id'] == scenario['id']}
            if set(scenario['query_ids']) != expected:
                raise ValueError('Scenario index mismatch')
            indexed.extend(scenario['query_ids'])
        if len(indexed) != len(set(indexed)) or set(indexed) != qids:
            raise ValueError('Scenario coverage mismatch')
        return len(qids)

    @property
    def queries(self):
        """Presentation projection only; never used for statistical counting."""
        sources = {s['source_id']: s for s in self.tables['sources']}
        result = []
        collection_counts = defaultdict(int)
        tasks = TaskRecords(self)
        for q in sorted(self.tables['queries'], key=lambda q: (self.folders.rank(q), q['display_order'])):
            nodes, children = self.graph(q['query_id'])
            def tree(nid):
                node = nodes[nid]
                family = self.families[node['operator_type']]
                return {'label': node['label'], 'kind': 'scan' if family == 'input' else family, 'children': [tree(e['child_id']) for e in children[nid]]}
            result.append({'id': q['source_query_id'], 'query_id': q['query_id'], 'group': q['group_label'], 'title': q['title'], 'status': q['plan_status_label'], 'mixed': q['mixed_label'], 'note': q['notes'], 'source': sources[q['source_id']]['location'], 'provenance': [{**sources[ref['source_id']], **ref} for ref in self.tables['query_sources'] if ref['query_id'] == q['query_id']], 'tree': tree(q['root_node_id']) if q['root_node_id'] else None})
            collection_name, tag = self.folders.place(q, self.details.get(q['query_id']))
            collection_counts[collection_name] += 1
            result[-1]['collection_name'] = collection_name
            result[-1]['display_number'] = collection_counts[collection_name]
            if tag is not None:
                result[-1]['group'] = collection_name + ' / ' + tag
            environment = self.environments[q['environment_id']]
            result[-1].update({
                'plan_origin': q['plan_origin'],
                'plan_format': q['plan_format'],
                'collection_label': q['collection_label'],
                'category_label': q['category_label'] if tag is None else tag,
                'environment': environment,
                'dataset': self.datasets[environment['dataset_id']],
                'inputs': [{'node_id': n['node_id'], 'operator_type': n['operator_type'], 'description': self.content_en.get(n['label'], n['label']), 'binding_status': 'logical_only'} for n in nodes.values() if self.families[n['operator_type']] == 'input'],
                'output': nodes[q['root_node_id']]['label'] if q['root_node_id'] else None,
            })
            if q['query_id'] in self.details:
                result[-1].update({k: v for k, v in self.details[q['query_id']].items() if k not in ('query_id', 'original_record')})
            result[-1]['input_contract'] = self.input_contracts.project(result[-1])
            result[-1]['original_query'] = self.original_queries.records[q['query_id']]
            result[-1]['task_record'] = tasks.create(result[-1], nodes, [edge for es in children.values() for edge in es])
        return result
