"""Tabular exports and SQL views built from canonical catalog tables."""
from contextlib import closing
import csv
import json
import sqlite3

class StatisticsExporter:
    def __init__(self, catalog):
        self.catalog = catalog

    def export(self):
        root = self.catalog.root / 'exports'
        root.mkdir(exist_ok=True)
        tables = {**self.catalog.tables, 'operators': self.catalog.operators,
                  'environments': list(self.catalog.environments.values()),
                  'datasets': list(self.catalog.datasets.values())}
        database = root / 'catalog.sqlite'
        database.unlink(missing_ok=True)
        with closing(sqlite3.connect(database)) as db, db:
            for name, rows in tables.items():
                rows = [{key: json.dumps(value, ensure_ascii=False) if isinstance(value, (list, dict)) else value
                         for key, value in row.items()} for row in rows]
                fields = list(dict.fromkeys(key for row in rows for key in row))
                rows = [{key: row.get(key) for key in fields} for row in rows]
                with (root / f'{name}.csv').open('w', newline='') as f:
                    writer = csv.DictWriter(f, fieldnames=fields)
                    writer.writeheader()
                    writer.writerows(rows)
                types = ['INTEGER' if any(isinstance(row[k], int) for row in rows) else 'TEXT' for k in fields]
                definition = ', '.join(f'"{k}" {t}' for k, t in zip(fields, types))
                db.execute(f'CREATE TABLE {name} ({definition})')
                db.executemany(f'INSERT INTO {name} VALUES ({",".join("?" for _ in fields)})', [tuple(row[k] for k in fields) for row in rows])
            db.executescript('''
                CREATE UNIQUE INDEX query_pk ON queries(query_id);
                CREATE UNIQUE INDEX node_pk ON nodes(query_id,node_id);
                CREATE UNIQUE INDEX source_pk ON sources(source_id);
                CREATE UNIQUE INDEX operator_pk ON operators(operator_type);
                CREATE VIEW query_statistics AS
                SELECT q.query_id, q.benchmark_id, q.scenario_id, q.plan_origin, q.plan_format,
                       CASE WHEN q.plan_format='logical_dag' THEN COUNT(n.node_id) END AS node_count,
                       CASE WHEN q.plan_format='logical_dag' THEN SUM(o.family='semantic') END AS semantic_node_count,
                       CASE WHEN q.plan_format='logical_dag' THEN SUM(o.family='relational') END AS relational_node_count,
                       CASE WHEN q.plan_format='logical_dag' THEN SUM(o.family='input') END AS input_node_count,
                       CASE WHEN q.plan_format='logical_dag' THEN COUNT(DISTINCT n.operator_type) END AS distinct_operator_types
                FROM queries q LEFT JOIN nodes n USING(query_id)
                LEFT JOIN operators o USING(operator_type) GROUP BY q.query_id;
                CREATE VIEW operator_statistics AS
                SELECT q.benchmark_id,n.operator_type,o.family,
                       COUNT(*) AS node_count,COUNT(DISTINCT n.query_id) AS query_count
                FROM nodes n JOIN queries q USING(query_id)
                JOIN operators o USING(operator_type)
                GROUP BY q.benchmark_id,n.operator_type;
            ''')
            for view in ('query_statistics', 'operator_statistics'):
                cursor = db.execute(f'SELECT * FROM {view} ORDER BY 1,2')
                with (root / f'{view}.csv').open('w', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow([c[0] for c in cursor.description])
                    writer.writerows(cursor)
            summary = {'queries': len(tables['queries']), 'logical_dags': sum(q['plan_format'] == 'logical_dag' for q in tables['queries']), 'reference_tasks': len(tables['task_details']), 'nodes': len(tables['nodes']), 'edges': len(tables['edges']), 'sources': len(tables['sources']), 'operator_types': len(tables['operators']), 'benchmarks': dict(db.execute('SELECT benchmark_id,COUNT(*) FROM queries GROUP BY benchmark_id')), 'measurement': 'Logical nodes count only normalized DAGs; reference programs are not counted as executed operators.'}
        (root / 'summary.json').write_text(json.dumps(summary, ensure_ascii=False, indent=2) + '\n')
