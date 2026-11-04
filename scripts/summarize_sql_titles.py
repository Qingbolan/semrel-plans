"""Chinese one-line summaries for queries whose title is their SQL text (UDA-Bench, QUEST).

The English UI keeps the SQL; the Chinese UI shows the summary from config/translations/queries-zh.json.
Requires sqlglot (scripts/audit/requirements.txt). Re-run after the titles change.
"""
import hashlib
import json
from pathlib import Path
import re

import sqlglot
from sqlglot import exp

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / 'config/translations/queries-zh.json'
AGG = {'avg': '平均', 'sum': '总和', 'min': '最小值', 'max': '最大值', 'count': '计数'}


def where_text(sql):
    """The WHERE clause as written (QUEST values are unquoted, so re-rendered SQL would split 'quarter-based')."""
    masked = re.sub(r"'[^']*'", lambda m: 'x' * len(m.group()), sql)  # find clause ends outside quoted values
    start = re.search(r'\bWHERE\s+', masked, re.I)
    if not start:
        return ''
    end = re.search(r'\bGROUP\s+BY\b|\bORDER\s+BY\b|\bLIMIT\b|;', masked[start.end():], re.I)
    return short(sql[start.end():start.end() + end.start() if end else len(sql)])


def summary(sql):
    if not re.search(r'\bFROM\s+\w+', sql, re.I) or re.search(r'\bFROM\s+\w+\s*(?:>=|<=|!=|<>|=|<|>)', sql, re.I):
        return '源 SQL 缺少表名或 WHERE，未能解析'  # e.g. QUEST LCR/25: 'FROM hearing_year >= 2006 AND …'
    try:
        tree = sqlglot.parse_one(sql)
    except sqlglot.errors.ParseError:
        tree = None
    where = where_text(sql)
    if not isinstance(tree, exp.Select):  # QUEST leaves values unquoted; fall back to the clauses as text
        table = re.search(r'\bFROM\s+(\w+)', sql, re.I).group(1)
        select = re.search(r'SELECT\s+(.*?)\s+FROM', sql, re.I | re.S)
        columns = '、'.join(c.strip() for c in select.group(1).split(',')) if select else '?'
        return f'{table}：列出 {columns}' + (f'（{where}）' if where else '')
    tables = list(dict.fromkeys(t.name for t in tree.find_all(exp.Table)))
    parts = []
    group = tree.args.get('group')
    if group:
        parts.append('按 ' + '、'.join(g.sql() for g in group.expressions) + ' 分组')
    aggs = []
    for a in tree.find_all(exp.AggFunc):
        name = a.key.lower()
        target = a.this.sql() if a.this is not None and not isinstance(a.this, exp.Star) else ''
        aggs.append(f"{target} {AGG.get(name, name.upper())}".strip())
    plain = [p.alias_or_name for p in tree.expressions if not p.find(exp.AggFunc)]
    if aggs:
        parts.append('求 ' + '、'.join(dict.fromkeys(aggs)))
    elif plain:
        parts.append('列出 ' + '、'.join(plain))
    text = '⋈'.join(tables) + '：' + '，'.join(parts)
    if where:
        text += f'（{where}）'
    if tree.args.get('order') is not None:
        text += '，排序' + ('取前 ' + tree.args['limit'].expression.sql() if tree.args.get('limit') is not None else '')
    return text


def short(condition, limit=70):
    """Whole predicates only: cut between AND/OR, never inside a quoted value."""
    condition = re.sub(r'\s+', ' ', condition).strip()
    if len(condition) <= limit:
        return condition
    pieces = re.split(r"\s+(AND|OR)\s+(?=(?:[^']*'[^']*')*[^']*$)", condition, flags=re.I)
    kept = pieces[0]
    for i in range(1, len(pieces) - 1, 2):
        if len(kept) + len(pieces[i + 1]) + 5 > limit:
            break
        kept += f' {pieces[i]} {pieces[i + 1]}'
    return kept + (' …' if kept != condition else '')


if __name__ == '__main__':
    records = json.loads(OUTPUT.read_text())
    count = 0
    for line in (ROOT / 'query/queries.jsonl').read_text().splitlines():
        q = json.loads(line)
        if q['benchmark_id'] not in ('uda-bench', 'quest') or not re.match(r'\s*SELECT\b', q['title'], re.I):
            continue
        records[q['query_id']] = dict(source=q['title'], zh=summary(q['title']), source_sha256=hashlib.sha256(q['title'].encode()).hexdigest())
        count += 1
    OUTPUT.write_text(json.dumps(records, ensure_ascii=False, indent=2) + '\n')
    print(f'Summarized {count} SQL titles')
