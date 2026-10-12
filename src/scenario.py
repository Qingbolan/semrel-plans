"""Normalized catalog with referential integrity and graph validation."""
from pathlib import Path
from collections import defaultdict
import json

class Catalog:
    TABLES = ('queries', 'nodes', 'edges', 'sources', 'query_sources')

    def __init__(self, root: Path):
        self.root = root
        self.metadata = json.loads((root / 'config/catalog.json').read_text())
        self.tables = {name: [json.loads(line) for line in (root / f'data/{name}.jsonl').read_text().splitlines() if line.strip()] for name in self.TABLES}
        self.operators = json.loads((root / 'config/operators.json').read_text())
        self.families = {op['operator_type']: op['family'] for op in self.operators}
        self.validate()

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
        self.unique(self.operators, ['operator_type'])
        allowed_origins = {'source_reconstruction', 'baseline_reconstruction', 'end_to_end_interpretation', 'proposed_missing_sql', 'intent_sql_mismatch', 'derived_workload'}
        for q in t['queries']:
            if q['plan_origin'] not in allowed_origins:
                raise ValueError('Unknown plan_origin')
        if any(op['family'] not in {'input', 'semantic', 'relational'} for op in self.operators):
            raise ValueError('Unknown operator family')
        for edge in t['edges']:
            if type(edge['input_position']) is not int or edge['input_position'] < 0:
                raise ValueError('Input position must be a nonnegative integer')
        qids = {q['query_id'] for q in t['queries']}
        sources = {s['source_id'] for s in t['sources']}
        for ref in t['query_sources']:
            if ref['query_id'] not in qids or ref['source_id'] not in sources:
                raise ValueError('Dangling provenance reference')
            if ref['role'] not in {'paper', 'dataset', 'protocol'} or not ref['attribution_note']:
                raise ValueError('Invalid provenance role or attribution')
        for qid in qids:
            refs = [ref for ref in t['query_sources'] if ref['query_id'] == qid]
            if not any(ref['role'] in {'paper', 'protocol'} for ref in refs):
                raise ValueError('Missing paper or protocol provenance')
            if not any(ref['role'] == 'dataset' for ref in refs) and not any(ref['role'] == 'protocol' for ref in refs):
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
        for q in sorted(self.tables['queries'], key=lambda q: q['display_order']):
            nodes, children = self.graph(q['query_id'])
            def tree(nid):
                node = nodes[nid]
                family = self.families[node['operator_type']]
                return {'label': node['label'], 'kind': 'scan' if family == 'input' else family, 'children': [tree(e['child_id']) for e in children[nid]]}
            result.append({'id': q['source_query_id'], 'query_id': q['query_id'], 'group': q['group_label'], 'title': q['title'], 'status': q['plan_status_label'], 'mixed': q['mixed_label'], 'note': q['notes'], 'source': sources[q['source_id']]['location'], 'provenance': [{**sources[ref['source_id']], **ref} for ref in self.tables['query_sources'] if ref['query_id'] == q['query_id']], 'tree': tree(q['root_node_id'])})
        return result
