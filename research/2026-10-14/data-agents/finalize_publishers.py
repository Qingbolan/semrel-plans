import json,re,pathlib,html
root=pathlib.Path(__file__).parent;work=json.load(open(root/'publisher-work.json'));original=[x for x in json.load(open(root.parent/'surveys/catalog.json')) if x.get('reading_status')=='discovered'];out=[]
search={x['index']:x for x in json.load(open(root/'publisher-search.json'))}
for i,w in enumerate(work):
 p=original[i];r={'original_url':w['original_url'],'title':p['title'],'url':w.get('url',w['original_url']),'year':int(p['year']),'venue':p['venue'],'reading_status':'metadata_only','evidence':[],'metadata_verified':True}
 if w.get('reading_status'):
  r.update({k:w[k] for k in ['title','url','year','venue','evidence']})
 elif w.get('pdf_text') or (root/'publisher-evidence'/f'{i}.txt').exists():
  r['evidence']=[r['url']];r['verification_method']='PDF first-page title and publication reference'
  r['local_evidence']=str(root/'publisher-evidence'/f'{i}.txt')
 elif i in [10,12,32,33]:
  d=search[i]['candidates'][0];r.update(title=d['title'],url='https://doi.org/'+d['doi'],year=d['year'],venue='; '.join(d['venue']),evidence=['https://api.crossref.org/works/'+d['doi']])
 elif (root/'publisher-evidence'/f'{i}-final.json').exists():
  d=json.load(open(root/'publisher-evidence'/f'{i}-final.json'));r.update(title=d['title'][0],url='https://doi.org/'+d['DOI'],year=d['published']['date-parts'][0][0],venue='; '.join(d['container-title']),evidence=['https://api.crossref.org/works/'+d['DOI']])
 elif i==26:
  r.update(url='https://doi.org/10.1109/ICDE60146.2024.00388',venue='ICDE',evidence=['https://ieeexplore.ieee.org/document/10597732/'])
 elif i==35:
  r.update(url='https://doi.org/10.1109/TVCG.2025.3579956',venue='IEEE Transactions on Visualization and Computer Graphics',evidence=['https://repository.kaust.edu.sa/bitstreams/6391d3df-415d-4f76-b1e3-55c79d00eac8/download'])
 elif i==41:
  r.update(url='https://www.researchgate.net/publication/392594876_Large_Language_Models_for_Data_Science_A_Survey',venue='Preprint',evidence=['https://www.researchgate.net/publication/392594876_Large_Language_Models_for_Data_Science_A_Survey'],verification_note='Author-uploaded preprint dated June 2025; original ResearchGate DOI is not an arXiv identifier. Crossref does not resolve this DOI.')
 else:
  r.update(reading_status='discovered',metadata_verified=False,verification_error=w.get('error','not resolved'))
 r['title']=html.unescape(re.sub(r'\s+',' ',re.sub('<[^>]+>','',r['title']))).strip().replace('LLM-R 2 :','LLM-R2:')
 if i==0:r['verification_note']='Original URL incorrectly puts a Springer DOI under dl.acm.org; normalized to DOI resolver.'
 if i==18:r['verification_note']='Crossref records PACMMOD publication in 2025; discovery list uses SIGMOD 2026 presentation year.'
 if i==21:r['evidence'].append('https://www.cidrdb.org/cidr2024/program.html');r['verification_note']='PDF retains an unfilled ACM 2018 template. Year and venue verified from the official CIDR 2024 program, not that template.'
 if i in [14,33]:r['verification_note']='Journal issue publication is 2025; DOI contains 2024 early-publication year.'
 if i==45:r.update(year=2023,verification_note='Published online 2022; final journal issue 35(5), May 2023. Catalog uses issue year.');r['evidence'].append('https://dbgroup.cs.tsinghua.edu.cn/ligl/papers/DM4ML_Survey.pdf')
 if i==19:r['venue']='aiDM 2025';r['verification_note']='Verified actual SERAG first page; rejected similarly titled SEFRQO Crossref candidate.'
 if i==27:r['venue']='Sarcouncil Journal of Engineering and Computer Sciences'
 if i in [37,42]:r['venue']='IEEE Data Engineering Bulletin';r['verification_method']='Publisher PDF first-page title; March 2025 issue path';r['evidence']=[w['original_url']]
 out.append(r)
(root/'publisher-verification.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');print(len(out),'records;',sum(x['metadata_verified'] for x in out),'verified')
