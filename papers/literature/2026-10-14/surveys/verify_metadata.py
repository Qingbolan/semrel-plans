"""Resolve discovery citations against primary arXiv metadata; retain failures explicitly."""
import concurrent.futures,html,json,re,urllib.request
from pathlib import Path
ROOT=Path(__file__).parent
rows=[]; section=''
for line in (ROOT/'discovery-list.md').read_text().splitlines():
 if line.startswith('#'): section=line.lstrip('# ').strip()
 m=re.match(r'- \[(.+?)\]\((https?://[^)]+)\) - \*(.+?)\*',line)
 if not m:continue
 title,url,label=m.groups(); year=re.search(r'20\d{2}',label)
 rows.append(dict(title=title,url=url,year=year.group() if year else '0',venue=label,topic=section,reading_status='discovered',evidence=['https://github.com/HKUSTDial/awesome-data-agents'],review_folder=None))
rows.append(dict(title='A Survey of Data Agents: Emerging Paradigm or Overstated Hype?',url='https://arxiv.org/abs/2510.23587',year='2025',venue='arXiv',topic='Surveys',reading_status='discovered',evidence=['https://github.com/HKUSTDial/awesome-data-agents'],review_folder=None))
def verify(row):
 match=re.search(r'arxiv.org/(?:abs|pdf|html)/(\d{4}\.\d{4,5})',row['url'])
 if not match:return row
 url='https://arxiv.org/abs/'+match.group(1)
 try:
  raw=urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=25).read().decode()
  title=re.search(r'<meta\s+name="citation_title"\s+content="([^"]+)"',raw)
  if not title:raise ValueError('missing citation title')
  row['discovered_title']=row['title'];row['title']=html.unescape(title.group(1));row['url']=url
  row['reading_status']='metadata_verified';row['evidence'].append(url)
  date=re.search(r'<meta\s+name="citation_date"\s+content="([^"]+)"',raw)
  if date:row['year']=date.group(1)[:4]
  row['venue']='arXiv';row['metadata_file']='metadata/'+match.group(1)+'.html'
  (ROOT/'metadata').mkdir(exist_ok=True);(ROOT/row['metadata_file']).write_text(raw)
 except Exception as e: row['verification_error']=str(e)
 return row
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:rows=list(pool.map(verify,rows))
(ROOT/'catalog.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
from collections import Counter
print(len(rows),dict(Counter(r['reading_status'] for r in rows)))
