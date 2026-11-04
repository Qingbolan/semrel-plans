"""Integrate independently reviewed literature snapshots, preserving original queries."""
import hashlib
import json
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'backend' / 'atlas'))
from workload_import import canonical_url

BASE = ROOT / 'research/2026-10-14'
FILES = ['README.md','出发点分析.md','解决的问题分析.md','Novelty分析.md','workload分析.md','usecase分析.md','benchmark分析.md']


def main():
    identities = json.loads((ROOT/'config/paper-identities.json').read_text())
    def identity(url):
        url = canonical_url(url).replace('https://www.arxiv.org/', 'https://arxiv.org/')
        return identities['aliases'].get(url, url)
    manifest = json.loads((ROOT/'papers/survey/manifest.json').read_text())
    types = json.loads((ROOT/'config/paper-types.json').read_text())
    existing = {}
    for entry in manifest:
        text = (ROOT/'Survey'/entry['folder']/'README.md').read_text()
        urls = re.findall(r'\]\((https?://[^\s)]+)\)', text)
        if urls: existing[identity(urls[0])] = entry
    verification = {r['original_url']: r for r in json.loads((BASE/'data-agents/publisher-verification.json').read_text())}
    merged = {}
    rank = {'discovered':0,'metadata_verified':1,'metadata_only':1,'abstract_only':2,'full_text_reviewed':3,'full_text':3}
    for source in sorted(BASE.glob('*/catalog.json')):
        entries = json.loads(source.read_text())
        if isinstance(entries, dict): entries = entries.get('papers', entries.get('entries', []))
        for raw in entries:
            row = dict(raw)
            if row['url'] in verification:
                row.update(verification[row['url']])
            row['venue'] = re.sub(r'\s*20\d{2}\s*$', '', row['venue']).strip()
            key = identity(row['url'])
            topic = row.pop('topic', source.parent.name)
            row['topics'] = [topic] if isinstance(topic,str) else topic
            row['catalog_sources'] = [source.relative_to(ROOT).as_posix()]
            row['domains'] = [{'semantic':'Semantic operators','data-agents':'Data agents','agent-query':'Agent query systems','surveys':'Related data systems'}[source.parent.name]]
            row['evidence'] = row.get('evidence', [])
            if isinstance(row['evidence'],str):row['evidence']=[row['evidence']]
            review = row.get('review_folder')
            if review:
                path = Path(review)
                if not path.is_absolute():
                    path = next((p for p in [source.parent/path, ROOT/path, source.parent/'reviews'/path] if p.is_dir()), source.parent/path)
                if not all((path/f).exists() for f in FILES):raise ValueError(f'Incomplete review: {path}')
                entry = existing.get(key) or next((e for e in manifest if e['folder'] == path.name), None)
                folder = entry['folder'] if entry else path.name
                if not re.search(r'-[^-]+-\d{4}$',folder):raise ValueError(folder)
                target = ROOT/'Survey'/folder;target.mkdir(exist_ok=True)
                for filename in FILES:shutil.copyfile(path/filename,target/filename)
                if entry is None:
                    entry={'folder':folder};manifest.append(entry);existing[key]=entry
                entry.update(source=path.relative_to(ROOT).as_posix(),sha256={f:hashlib.sha256((target/f).read_bytes()).hexdigest() for f in FILES})
                row['review_folder']=target.relative_to(ROOT).as_posix()
                row['reading_status']='full_text_reviewed'
                # Fresh full reviews supersede earlier brief configuration summaries.
                for old_url in list(identities.get('reviews',{})):
                    if identity(old_url)==key:del identities['reviews'][old_url]
                types[hashlib.sha256(folder.encode()).hexdigest()[:12]]=row.get('kind','benchmark' if 'bench' in row['title'].lower() else 'research')
            previous=merged.get(key)
            if previous:
                topics=sorted(set(previous['topics']+row['topics']))
                evidence=previous['evidence']+[x for x in row['evidence'] if x not in previous['evidence']]
                catalogs=sorted(set(previous['catalog_sources']+row['catalog_sources']))
                domains=sorted(set(previous['domains']+row['domains']))
                if rank.get(row['reading_status'],0)>rank.get(previous['reading_status'],0):merged[key]=row
                merged[key].update(topics=topics,evidence=evidence,catalog_sources=catalogs,domains=domains)
            else:merged[key]=row
    labels={'discovered':'发现线索，待核对原文','metadata_verified':'已核对原始元数据','metadata_only':'已核对原始元数据','abstract_only':'已阅读摘要','full_text_reviewed':'本次已完成全文阅读与七项分析'}
    rows=sorted(merged.values(),key=lambda r:(-int(r['year']),r['title']))
    for row in rows:
        row['reading_status_label']=labels[row['reading_status']]
        types['lit_'+hashlib.sha256(identity(row['url']).encode()).hexdigest()[:12]]=row.get('kind','survey' if 'survey' in row['title'].lower() else 'benchmark' if 'bench' in row['title'].lower() else 'research')
    for path,value in [(ROOT/'config/literature-catalog.json',rows),(ROOT/'papers/survey/manifest.json',manifest),(ROOT/'config/paper-types.json',types),(ROOT/'config/paper-identities.json',identities)]:
        path.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')
    report=['# Data Agent 与 Semantic Operator 文献检索','', '检索截止：2026-10-14。覆盖数据分析与数据科学 agent、数据准备和发现、数据库 agent、语义算子、查询编译与优化、相关基准及综述。按原文 URL 与已有论文身份表去重；预印本和正式版仍可能存在尚未确认的对应关系。','', '检索使用主题词、系统名、作者综述与引用链。外部清单仅用于发现，已核对条目以原始 arXiv/出版社元数据为依据；无法取得原文的线索单列。清单不声称覆盖所有尚未检索到的工作。原始查询数据不由文献摘要生成。','']
    from collections import Counter
    counts=Counter(r['reading_status_label'] for r in rows)
    report+=['## 阅读范围','']+[f'- {k}：{v} 篇' for k,v in counts.items()]
    for status in ['full_text_reviewed','abstract_only','metadata_verified','metadata_only','discovered']:
        subset=[r for r in rows if r['reading_status']==status]
        if not subset:continue
        report+=['',f'## {labels[status]}','', '| 论文 | 年份 | 方向 | 阅读记录 |','|---|---|---|---|']
        for r in subset:
            review=f"[七项分析](../../{r['review_folder'].replace(' ', '%20')}/README.md)" if r.get('review_folder') else '—'
            report.append(f"| [{r['title'].replace('|','/').replace(chr(10),' ')}]({r['url']}) | {r['year']} | {', '.join(r['topics'])} | {review} |")
    (BASE/'README.md').write_text('\n'.join(report)+'\n')
    print(json.dumps(dict(total=len(rows),statuses=dict(counts),survey_folders=len(manifest)),ensure_ascii=False))

if __name__=='__main__':main()
