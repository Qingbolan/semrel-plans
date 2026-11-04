import concurrent.futures,hashlib,json,re,urllib.request
from html.parser import HTMLParser
from pathlib import Path
ROOT=Path(__file__).parent
class Metadata(HTMLParser):
 def __init__(self):super().__init__();self.values={}
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=='meta':self.values[a.get('name',a.get('property','')).lower()]=a.get('content','')
def verify(r):
 if r['reading_status']!='discovered':return r
 url=r['url']
 if 'aclanthology.org' in url:url=url.removesuffix('.pdf')+'/'
 if not any(d in url for d in ['aclanthology.org','dl.acm.org','link.springer.com']):return r
 try:
  raw=urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=20).read().decode();parser=Metadata();parser.feed(raw)
  title=parser.values.get('citation_title')
  if not title:raise ValueError('missing citation_title')
  r['discovered_title']=r['title'];r['title']=title;r['reading_status']='metadata_verified';r['evidence'].append(url)
  r['metadata_file']='metadata/'+hashlib.sha256(url.encode()).hexdigest()[:12]+'.html';(ROOT/r['metadata_file']).write_text(raw)
 except Exception as e:r['verification_error']=str(e)
 return r
rows=json.loads((ROOT/'catalog.json').read_text())
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as p:rows=list(p.map(verify,rows))
(ROOT/'catalog.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
from collections import Counter
print(Counter(r['reading_status'] for r in rows))
