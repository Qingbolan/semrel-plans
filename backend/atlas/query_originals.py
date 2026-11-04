"""Source text is independent of display translations and plan reconstructions."""
import ast
import csv
import hashlib
import json
import re
import tomllib
from pathlib import Path
from sql_source import query_text, sql_statements


def extract_text(path, selector):
    text=path.read_text()
    kind=selector['type']
    if kind=='text':return text
    if kind=='python_string':
        matches=[n.value for n in ast.walk(ast.parse(text)) if isinstance(n,ast.Constant) and isinstance(n.value,str) and n.lineno==selector['line'] and n.col_offset==selector['column']]
        if len(matches)!=1:raise ValueError('Python string selector is not unique')
        return matches[0]
    if kind=='jsonl_task':
        matches=[r for r in map(json.loads,text.splitlines()) if r[selector['id_field']]==selector['id']]
        if len(matches)!=1:raise ValueError('JSONL task selector is not unique')
        return matches[0][selector['field']]
    if kind=='toml':return tomllib.loads(text)['definition']['natural_language']
    if kind=='json_field':return json.loads(text)[selector['field']]
    if kind=='json_task':
        data=json.loads(text)
        if isinstance(data,dict):data=data['tasks']
        matches=[r for r in data if r[selector['id_field']]==selector['id']]
        if len(matches)!=1:raise ValueError('Source task identity is not unique')
        return matches[0][selector['field']]
    if kind=='csv_task':
        matches=[r for r in csv.DictReader(text.splitlines(keepends=True)) if r['task_id']==selector['id']]
        if len(matches)!=1:raise ValueError('Source CSV task identity is not unique')
        return matches[0]['query']
    if kind=='csv_row':
        matches=[r for r in csv.DictReader(text.lstrip('\ufeff').splitlines(keepends=True)) if r[selector['id_field']]==selector['id']]
        if len(matches)!=1:raise ValueError('Source CSV row identity is not unique')
        return matches[0][selector['field']]
    if kind=='comment_line':
        matches=[l[len(selector['prefix']):].strip() for l in text.splitlines() if l.startswith(selector['prefix'])]
        if len(matches)!=1:raise ValueError('Comment line selector is not unique')
        return matches[0]
    if kind=='python_return_item':
        source=text;tree=ast.parse(source)
        fn=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name==selector['function'])
        ret=next(n for n in ast.walk(fn) if isinstance(n,ast.Return) and isinstance(n.value,ast.Tuple) and len(n.value.elts)==3)
        return ast.get_source_segment(source,ret.value.elts[2].elts[selector['index']])
    if kind=='json_value':return json.loads(text)
    if kind=='python_query':
        fn=next(n for n in ast.parse(text).body if isinstance(n,ast.FunctionDef) and n.name==selector['function'])
        stmt=next(n for n in fn.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='query' for t in n.targets))
        return ast.literal_eval(stmt.value)
    if kind=='sql_statement':return sql_statements(text)[selector['index']]
    if kind=='sql_query':return query_text(sql_statements(text)[selector['index']])
    if kind=='sql_block':return re.findall(r'```sql\n(.*?)```',text,re.S)[selector['index']].rstrip('\n')
    if kind=='heading':return text.splitlines()[0].removeprefix('# ')
    raise ValueError('Unsupported source selector')


class QueryOriginals:
    def __init__(self, root, queries):
        self.records={r['query_id']:r for r in map(json.loads,(Path(root)/'query/original_queries.jsonl').read_text().splitlines())}
        if set(self.records)!={q['query_id'] for q in queries}:raise ValueError('Original query coverage mismatch')
        hashes={}
        for qid,r in self.records.items():
            path=Path(root)/r['source_path']
            if path not in hashes:hashes[path]=hashlib.sha256(path.read_bytes()).hexdigest()
            if hashes[path]!=r['source_sha256'] or hashlib.sha256(r['text'].encode()).hexdigest()!=r['text_sha256']:
                raise ValueError('Stale original query '+qid)
