import re,json,pathlib,urllib.request,concurrent.futures,html
root=pathlib.Path(__file__).parent
s=(root/'evidence/sjtu.md').read_text(); entries={}
for heading in ['## 🏆 Benchmarks','## 📊 Data Analysis','## 🔬 Data Science']:
 start=s.index(heading);end=s.find('\n## ',start+5)
 block=s[start:end if end!=-1 else None]
 if heading.startswith('## 🏆'):block=block.split('### Benchmarks for Tabular Data')[0]
 for line in block.splitlines():
  m=re.search(r'https?://(?:www\.)?arxiv.org/(?:pdf|abs)/(\d{4}\.\d+)',line)
  if m:entries[m[1]]=heading[5:]
for id in ['2410.05080','2407.01725','2506.06541','2609.24137','2411.07763','2506.23719','2608.03451','2509.25084','2311.17541','2310.03302','2405.15793','2402.10890']:
 entries[id]='data agent and benchmark'

def fetch(item):
 id,topic=item; url='https://arxiv.org/abs/'+id
 try:
  raw=urllib.request.urlopen(url,timeout=25).read().decode();
  def meta(k):
   m=re.search(r'<meta name="'+k+r'" content="(.*?)"',raw,re.S);return html.unescape(m[1]) if m else ''
  title=meta('citation_title');date=meta('citation_date')
  if not title:raise ValueError('no citation metadata')
  (root/'evidence'/('abs-'+id+'.html')).write_text(raw)
  return {'title':title,'url':url,'year':int(date[:4]),'venue':'arXiv','topic':topic,'reading_status':'metadata_only','evidence':[url],'review_folder':None,'source_date':date,'discovery_source':'https://github.com/SJTU-DMTai/Awesome-Data-Agent-Papers','metadata_verified':True}
 except Exception as e:return {'url':url,'error':str(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as ex:result=list(ex.map(fetch,entries.items()))
(root/'catalog.json').write_text(json.dumps([r for r in result if 'title'in r],ensure_ascii=False,indent=2)+'\n')
(root/'unresolved.json').write_text(json.dumps([r for r in result if 'error'in r],indent=2)+'\n')
print('verified',sum('title'in r for r in result),'unresolved',sum('error'in r for r in result))
