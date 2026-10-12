"""Tabular exports and SQL views built from canonical catalog tables."""
import csv
import json
import sqlite3

class StatisticsExporter:
    def __init__(self, catalog):
        self.catalog = catalog

    def export(self):
        root = self.catalog.root / 'exports'
        root.mkdir(exist_ok=True)
        tables = {**self.catalog.tables, 'operators': self.catalog.operators}
        database = root / 'catalog.sqlite'
        database.unlink(missing_ok=True)
        with sqlite3.connect(database) as db:
            for name, rows in tables.items():
                fields = list(rows[0])
                with (root / f'{name}.csv').open('w', newline='') as f:
                    writer = csv.DictWriter(f, fieldnames=fields)
                    writer.writeheader()
                    writer.writerows(rows)
                types = ['INTEGER' if isinstance(rows[0][k], int) else 'TEXT' for k in fields]
                definition = ', '.join(f'"{k}" {t}' for k, t in zip(fields, types))
                db.execute(f'CREATE TABLE {name} ({definition})')
                db.executemany(f'INSERT INTO {name} VALUES ({",".join("?" for _ in fields)})', [tuple(row[k] for k in fields) for row in rows])
            db.executescript('''
                CREATE UNIQUE INDEX query_pk ON queries(query_id);
                CREATE UNIQUE INDEX node_pk ON nodes(query_id,node_id);
                CREATE UNIQUE INDEX source_pk ON sources(source_id);
                CREATE UNIQUE INDEX operator_pk ON operators(operator_type);
                CREATE VIEW query_statistics AS
                SELECT q.query_id, q.benchmark_id, q.scenario_id, q.plan_origin,
                       COUNT(n.node_id) AS node_count,
                       SUM(o.family='semantic') AS semantic_node_count,
                       SUM(o.family='relational') AS relational_node_count,
                       SUM(o.family='input') AS input_node_count,
                       COUNT(DISTINCT n.operator_type) AS distinct_operator_types
                FROM queries q JOIN nodes n USING(query_id)
                JOIN operators o USING(operator_type) GROUP BY q.query_id;
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
            summary = {'queries': len(tables['queries']), 'nodes': len(tables['nodes']), 'edges': len(tables['edges']), 'sources': len(tables['sources']), 'operator_types': len(tables['operators']), 'benchmarks': dict(db.execute('SELECT benchmark_id,COUNT(*) FROM queries GROUP BY benchmark_id')), 'measurement': 'logical_plan_nodes; not runtime calls or independent benchmark counts'}
        (root / 'summary.json').write_text(json.dumps(summary, ensure_ascii=False, indent=2) + '\n')
