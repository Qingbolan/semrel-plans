import json,re,urllib.request,urllib.parse,pathlib,concurrent.futures
root=pathlib.Path(__file__).parent;rows=json.load(open(root/'publisher-work.json'))
def run(pair):
 i,r=pair
 if r.get('reading_status') or r.get('pdf_text'):return None
 try:
  u='https://api.crossref.org/works?rows=2&query.title='+urllib.parse.quote(r['discovered_title']);raw=urllib.request.urlopen(u,timeout=35).read();d=json.loads(raw)['message']['items'];(root/'publisher-evidence'/f'{i}-search.json').write_bytes(raw)
  return {'index':i,'original':r['discovered_title'],'candidates':[{'title':x.get('title',[''])[0],'doi':x['DOI'],'year':x.get('published',{}).get('date-parts',[[None]])[0][0],'venue':x.get('container-title',[])} for x in d]}
 except Exception as e:return {'index':i,'error':str(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:res=[r for r in ex.map(run,enumerate(rows)) if r]
(root/'publisher-search.json').write_text(json.dumps(res,ensure_ascii=False,indent=2));print(json.dumps(res,ensure_ascii=False,indent=2))
