import json,re,urllib.request,urllib.parse,pathlib,concurrent.futures,subprocess
root=pathlib.Path(__file__).parent
records=[x for x in json.load(open(root.parent/'surveys/catalog.json')) if x.get('reading_status')=='discovered']
(root/'publisher-evidence').mkdir(exist_ok=True)
def run(pair):
 i,p=pair;u=p['url'];r={'original_url':u,'discovered_title':p['title']}
 try:
  m=re.search(r'(10\.\d{4,9}/[^?]+)',u)
  if m:
   doi=m[1];api='https://api.crossref.org/works/'+urllib.parse.quote(doi,safe='');raw=urllib.request.urlopen(api,timeout=30).read();d=json.loads(raw)['message'];(root/'publisher-evidence'/f'{i}.json').write_bytes(raw)
   r.update(title=d['title'][0],url='https://doi.org/'+doi,year=d.get('published',d.get('created',{}))['date-parts'][0][0],venue='; '.join(d.get('container-title',[])),reading_status='metadata_only',evidence=[api],metadata_verified=True)
  elif u.endswith('.pdf'):
   if u.startswith('http://'):u=u.replace('http://','https://',1)
   raw=urllib.request.urlopen(u,timeout=30).read();f=root/'publisher-evidence'/f'{i}.pdf';f.write_bytes(raw);t=f.with_suffix('.txt');subprocess.run(['pdftotext','-f','1','-l','1','-layout',str(f),str(t)],check=True,capture_output=True)
   r.update(pdf_text=t.read_text(),local_evidence=str(t),url=u)
  else:
   r['pending']='publisher lookup required'
 except Exception as e:r['error']=str(e)
 return r
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as e:results=list(e.map(run,enumerate(records)))
(root/'publisher-work.json').write_text(json.dumps(results,ensure_ascii=False,indent=2))
for i,x in enumerate(results):
 if x.get('reading_status'):print(i,'DOI',x['title'],'|',x['year'],'|',x['venue'])
 elif x.get('pdf_text'):print(i,'PDF',x['pdf_text'][:650], '\nEND',x['pdf_text'][-1600:])
 else:print(i,'PENDING',x)
