"""Lossless logical-plan lowering to EAL ability calls (not executable SQL)."""
import json
from pathlib import Path
from urllib.parse import quote
from zipfile import ZipFile, ZIP_DEFLATED


class EalExporter:
    """Owns node bindings, ordered input ports, and portable export artifacts."""

    def __init__(self, catalog):
        self.catalog = catalog

    def render(self, query):
        nodes, children = self.catalog.graph(query['query_id'])
        bindings = {nid: f'n{i:03d}' for i, nid in enumerate(sorted(nodes))}
        emitted = set()
        lines = ['// Logical-plan representation; requires SemRel operator abilities.',
                 '// Labels are preserved, not parsed into executable predicates.',
                 '// input_0, input_1, ... preserve the source input positions.',
                 f'mission {json.dumps(query["query_id"], ensure_ascii=False)} {{']
        def visit(nid):
            if nid in emitted:
                return
            for edge in children[nid]:
                visit(edge['child_id'])
            node = nodes[nid]
            args = {'query_id': query['query_id'], 'node_id': nid,
                    'operator_type': node['operator_type'],
                    'family': self.catalog.families[node['operator_type']],
                    'label': node['label'], 'plan_origin': query['plan_origin']}
            lines.append(f'  let {bindings[nid]} = call "semrel.{node["operator_type"].lower()}" on "semrel-worker" with {{')
            fields = [f'    {k} = {json.dumps(v, ensure_ascii=False)}' for k, v in args.items()]
            fields.extend(f'    input_{e["input_position"]} = {bindings[e["child_id"]]}.output' for e in children[nid])
            lines.append(',\n'.join(fields))
            lines.extend(['  } on_failure abort', ''])
            emitted.add(nid)
        visit(query['root_node_id'])
        lines.extend([f'  emit "result" kind answer value {bindings[query["root_node_id"]]}.output', '}', ''])
        return '\n'.join(lines)

    def export(self):
        directory = self.catalog.root / 'exports/eal'
        directory.mkdir(parents=True, exist_ok=True)
        result = {}
        for query in self.catalog.tables['queries']:
            filename = quote(query['query_id'], safe='') + '.eal'
            source = self.render(query)
            (directory / filename).write_text(source, encoding='utf-8')
            nodes, _ = self.catalog.graph(query['query_id'])
            result[query['query_id']] = {'source': source, 'path': 'exports/eal/' + filename,
                'status': 'logical-plan', 'nodes': len(nodes),
                'semantic': sum(self.catalog.families[n['operator_type']] == 'semantic' for n in nodes.values())}
        manifest = [{'query_id': qid, **{k: v for k, v in entry.items() if k != 'source'}} for qid, entry in result.items()]
        (directory / 'manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
        with ZipFile(self.catalog.root / 'exports/eal.zip', 'w', ZIP_DEFLATED) as archive:
            for entry in result.values():
                archive.write(self.catalog.root / entry['path'], Path(entry['path']).name)
            archive.write(directory / 'manifest.json', 'manifest.json')
        return result
