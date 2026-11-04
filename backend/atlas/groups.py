"""Default, non-exclusive query groups derived from explicit catalog evidence."""
import json


def query_groups(catalog):
    config = json.loads((catalog.root / 'config/query-groups.json').read_text())
    semantic_queries = {n['query_id'] for n in catalog.tables['nodes'] if catalog.families[n['operator_type']] == 'semantic'}
    memberships = {}
    for q in catalog.tables['queries']:
        groups = []
        if q['benchmark_id'] == 'local-derived' and q['source_query_id'].split('/')[0] in config['nlp_source_tasks']:
            groups.append('nlp-tasks')
        detail = catalog.details.get(q['query_id'], {})
        annotation = detail.get('annotation') or {}
        tags = detail.get('original_record', {}).get('tags') or {}
        if q['query_id'] in semantic_queries or int(annotation.get('semop_count', 0)) > 0 or int(tags.get('n_sem_ops', 0)) > 0:
            groups.append('sem-operator')
        if groups:
            memberships[q['query_id']] = groups
    return {'version': config['version'], 'groups': config['groups'], 'memberships': memberships}
