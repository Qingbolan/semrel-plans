import urllib.request,json,re,concurrent.futures
from pathlib import Path
from html import unescape
ROOT=Path(__file__).parent
IDS=['2407.11418','2405.14696','2410.12189','2505.14661','2507.06515','2308.03424','2603.11622','2604.09944','2402.17882','2409.00847','2407.09522','2610.08089','2608.06677','2606.07923','2405.04674','2510.08489','2304.00472','2403.05821','2511.19830','2512.05399','2504.01157','2304.09433','2512.02289','2511.01716']
def fetch(i):
 u='https://arxiv.org/abs/'+i
 try:
  html=urllib.request.urlopen(u,timeout=45).read().decode()
  fields={}
  for name in ['citation_title','citation_date','citation_pdf_url','citation_arxiv_id']:
   m=re.search(r'<meta name="'+name+r'" content="([^"]*)"',html)
   if m:fields[name]=unescape(m.group(1))
  m=re.search(r'<blockquote class="abstract[^>]*>(.*?)</blockquote>',html,re.S)
  fields['abstract']=re.sub(r'\s+',' ',unescape(re.sub('<[^>]*>',' ',m.group(1)))).strip() if m else ''
  fields.update(url=u,id=i)
  return fields
 except Exception as e:return dict(id=i,url=u,error=str(e))
results=list(concurrent.futures.ThreadPoolExecutor(max_workers=5).map(fetch,IDS))
(ROOT/'metadata.json').write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n')
for r in results:print(r['id'],r.get('citation_title',r.get('error')),r.get('citation_date',''))
