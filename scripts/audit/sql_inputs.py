"""Extract table/column lineage from source SQL; never execute benchmark SQL."""
import re
import sqlglot
from sqlglot import exp
from sqlglot.optimizer.scope import Scope, traverse_scope


def extract_sql(sql, dialect='bigquery'):
    sql = sql.replace('<<other_params>>', '')
    sql = re.sub(r'<<[^>]+>>', '0', sql)
    sql = re.sub(r"EXTERNAL_OBJECT_TRANSFORM\(TABLE\s+(`[^`]+`),\s*\['SIGNED_URL'\]\)", r"\1", sql, flags=re.I)
    roots = sqlglot.parse(sql, read=dialect)
    tables = {}
    for root in roots:
        if root is None:
            continue
        for scope in traverse_scope(root):
            def resolve(column, owner, seen=None):
                seen = set() if seen is None else seen
                key = (id(owner), column.sql())
                if key in seen:
                    return []
                seen = seen | {key}
                parts = [p.name for p in column.parts]
                sources = {k.lower(): v for k, v in owner.sources.items()}
                alias = parts[0].lower() if len(parts)>1 else ''
                if alias in sources:
                    source = sources[alias]; name = '.'.join(parts[1:])
                elif alias and owner.parent and alias in {k.lower() for k in owner.parent.sources}:
                    return resolve(column, owner.parent, seen)
                elif len(sources)==1:
                    source = next(iter(sources.values())); name = '.'.join(parts)
                else:
                    return []
                if isinstance(source, exp.Table):
                    name_table = '.'.join(p.name for p in source.parts)
                    return [(name_table, name)] if name_table else []
                if isinstance(source, Scope):
                    for selection in source.expression.selects:
                        if selection.alias_or_name.lower()==name.lower():
                            return [pair for col in selection.find_all(exp.Column) for pair in resolve(col,source,seen)]
                    for selection in source.expression.selects:
                        if selection.is_star:
                            return resolve(exp.column(name, table=selection.table if isinstance(selection,exp.Column) else None), source, seen)
                return []
            for source in scope.sources.values():
                if isinstance(source,exp.Table) and isinstance(source.this,exp.Identifier):
                    tables.setdefault('.'.join(p.name for p in source.parts), {})
            for col in scope.columns:
                semantic=False; parent=col.parent
                while parent and parent is not scope.expression:
                    if isinstance(parent,exp.Dot) and isinstance(parent.this,exp.Identifier) and parent.this.name.upper()=='AI':semantic=True
                    parent=parent.parent
                for table,name in resolve(col,scope):
                    columns=tables.setdefault(table,{})
                    columns[name]=columns.get(name,False) or semantic
    return [{'name':table,'columns':[{'name':name,'type':None} for name in columns],
             'passed_columns':[name for name,semantic in columns.items() if semantic],
             'row_unit':'record','scope':'used','path':None} for table,columns in tables.items()]
