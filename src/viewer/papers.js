import {marked} from 'marked';
import DOMPurify from 'dompurify';
import { PaperGroups } from './paper-groups.js';
import { mountPaperEditor } from './paper-editor.jsx';

const groupStore=new PaperGroups();
groupStore.seed(window.SEMREL_QUERY_GROUPS);
export function catalogGroups(){return groupStore.state.groups;}
const sections=[['overview','概览','Overview'],['coverage','收录核对','Coverage'],['queries','查询清单','Queries'],['research','研究记录','Research notes'],['motivation','出发点','Motivation'],['usecase','具体用例','Use case'],['problem','研究问题','Problem'],['novelty','贡献与评价','Contributions'],['benchmark','基准评测','Benchmark'],['workload','工作负载','Workload'],['environment','环境与输入','Environment & inputs']];
const escape=value=>String(value).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));

/** Owns paper selection, filtering, and document rendering; never changes query state. */
export class PaperLibrary {
  constructor(records,onNavigate,inspectors){
    this.inspectors=inspectors;
    this.records=records;this.onNavigate=onNavigate;this.selected=records.find(p=>p.title.startsWith('SemBench'))||records[0];this.section='motivation';this.term='';this.venue='';this.activeTool=null;this.expanded=true;this.active=false;
    this.panel=document.querySelector('#paper-panel');this.groups=groupStore;this.groupFilter='';this.domain='';this.category='';
  }
  label(zh,en){return window.AtlasI18n.language==='en'?en:zh;}
  open(id,section='motivation'){
    this.selected=this.records.find(p=>p.id===id||(p.source_ids||[]).includes(id))||this.selected;this.section=(section==='environment'||(section==='usecase'?!!this.selected.usecase:!!this.selected.sections[section]))?section:'overview';
    this.active=true;this.updatePanel();this.render();this.revealSelected();
  }
  updatePanel(){
    const visible=this.active&&this.expanded;
    this.panel.hidden=!visible;document.querySelector('#workspace').classList.toggle('papers-open',visible);
    const button=document.querySelector('[data-page="papers"]');button.setAttribute('aria-controls','paper-panel');button.setAttribute('aria-expanded',String(visible));
  }
  hidePanel(){this.expanded=false;this.updatePanel();}
  disposeEditor(){this.unmountEditor?.();this.unmountEditor=null;}
  deactivate(){this.active=false;this.updatePanel();}
  togglePanel(){this.expanded=!this.expanded;this.updatePanel();this.revealSelected();}
  revealSelected(){const cell=this.panel.querySelector('[data-paper="'+this.selected.id+'"]');if(!this.panel.hidden&&cell){const a=cell.getBoundingClientRect(),b=this.panel.getBoundingClientRect();if(a.top<b.top||a.bottom>b.bottom)this.panel.scrollTop+=a.top-b.top-80;}}

  renderList(){
    const searchLabel=this.label('搜索论文与用例','Search papers and use cases'),filterLabel=this.label('筛选发表来源','Filter publication venue');
    this.panel.innerHTML=`<div class="sidebar-title paper-toolbar"><span>Paper <small>${this.records.length}</small></span><div class="paper-tools"><button data-tool="search" title="${searchLabel}" aria-label="${searchLabel}" aria-expanded="${this.activeTool==='search'}" aria-controls="paper-search" class="${this.term?'has-value':''}">${AtlasIcons.render('search')}</button><button data-tool="filter" title="${filterLabel}" aria-label="${filterLabel}" aria-expanded="${this.activeTool==='filter'}" aria-controls="paper-venue" class="${this.venue?'has-value':''}">${AtlasIcons.render('filter')}</button><button class="paper-close" title="${this.label('收起论文目录','Close papers')}" aria-label="${this.label('收起论文目录','Close papers')}">${AtlasIcons.render('close')}</button></div></div><input id="paper-search" ${this.activeTool==='search'?'':'hidden'} type="search" aria-label="${searchLabel}" value="${escape(this.term)}" placeholder="${this.label('标题、问题、数据集…','Title, problem, dataset…')}"><select id="paper-category-filter" ${this.activeTool==='filter'?'':'hidden'} aria-label="${this.label('论文类别','Paper category')}"><option value="">${this.label('全部类别','All categories')}</option>${categories(this.records).map(c=>`<option value="${escape(c.key)}" ${this.category===c.key?'selected':''}>${escape(this.label(c.zh,c.en))}</option>`).join('')}</select><select id="paper-venue" ${this.activeTool==='filter'?'':'hidden'} aria-label="${this.label('发表来源','Publication venue')}"><option value="">${this.label('全部发表来源','All venues')}</option>${[...new Set(this.records.map(p=>p.venue))].sort().map(v=>`<option ${v===this.venue?'selected':''}>${escape(v)}</option>`).join('')}</select><select id="paper-group-filter" ${this.activeTool==='filter'?'':'hidden'} aria-label="${this.label('自定义分组','Custom groups')}"><option value="">${this.label('全部分组','All groups')}</option>${this.groups.state.groups.map(g=>`<option value="${escape(g.id)}" ${this.groupFilter===g.id?'selected':''}>${escape(g.name)}</option>`).join('')}</select><select id="paper-domain-filter" ${this.activeTool==='filter'?'':'hidden'} aria-label="${this.label('研究方向','Research area')}"><option value="">${this.label('全部研究方向','All research areas')}</option>${[...new Set(this.records.flatMap(p=>p.literature_domains||[]))].sort().map(d=>`<option value="${escape(d)}" ${this.domain===d?'selected':''}>${escape(d)}</option>`).join('')}</select><nav class="paper-list" aria-label="Paper"></nav>`;
    this.panel.querySelector('.paper-close').onclick=()=>this.hidePanel();
    this.panel.querySelectorAll('[data-tool]').forEach(button=>button.onclick=()=>{
      this.activeTool=this.activeTool===button.dataset.tool?null:button.dataset.tool;this.renderList();
      this.panel.querySelector(this.activeTool?this.activeTool==='search'?'#paper-search':'#paper-venue':`[data-tool="${button.dataset.tool}"]`).focus();
    });
    this.panel.querySelector('#paper-search').oninput=e=>{this.term=e.target.value;this.panel.querySelector('[data-tool="search"]').classList.toggle('has-value',!!this.term);this.renderItems();};
    this.panel.querySelector('#paper-venue').onchange=e=>{this.venue=e.target.value;this.panel.querySelector('[data-tool="filter"]').classList.toggle('has-value',!!this.venue);this.renderItems();};
    this.panel.querySelector('#paper-category-filter').onchange=e=>{this.category=e.target.value;this.renderItems();};
    this.panel.querySelector('#paper-group-filter').onchange=e=>{this.groupFilter=e.target.value;this.renderItems();};
    this.panel.querySelector('#paper-domain-filter').onchange=e=>{this.domain=e.target.value;this.renderItems();};
    this.panel.onkeydown=e=>{if(e.key==='Escape'&&this.activeTool){const tool=this.activeTool;this.activeTool=null;this.renderList();this.panel.querySelector(`[data-tool="${tool}"]`).focus();}};
    this.renderItems();
  }
  renderItems(){
    const term=this.term.toLowerCase().trim();const items=this.records.filter(p=>(!this.category||p.category.key===this.category)&&(!this.domain||(p.literature_domains||[]).includes(this.domain))&&(!this.venue||p.venue===this.venue)&&(!this.groupFilter||this.groups.groupsFor(p.id).some(g=>g.id===this.groupFilter))&&[p.title,p.venue,p.year,...Object.values(p.sections)].join(' ').toLowerCase().includes(term));
    const root=this.panel.querySelector('.paper-list');
    root.innerHTML=categories(items).map(c=>{const members=items.filter(p=>p.category.key===c.key);return `<section class="paper-category" aria-label="${escape(this.label(c.zh,c.en))}"><h3>${escape(this.label(c.zh,c.en))} <small>${members.length}</small></h3>${members.map(p=>{
      const groups=this.groups.groupsFor(p.id);const tip=p.title+(groups.length?'\n'+groups.map(g=>g.name).join(' · '):'');
      return `<div class="paper-row"><button class="paper-item" title="${escape(tip)}" data-paper="${p.id}" aria-current="${this.selected.id===p.id?'page':'false'}"><small class="paper-kind-line">${kindIcon(p)}${escape(p.venue)}${p.year==='0'?'':p.year}<i class="paper-group-dots" aria-label="${escape(groups.map(g=>g.name).join(', '))}">${groups.slice(0,3).map(g=>`<i style="background:${g.color}" title="${escape(g.name)}"></i>`).join('')}</i></small><span>${escape(p.title)}</span></button><button class="paper-group-edit" data-group-paper="${p.id}" aria-label="${this.label('编辑分组','Edit groups')}" title="${this.label('编辑分组','Edit groups')}">${AtlasIcons.render('folder')}</button></div>`;
    }).join('')}</section>`;}).join('')||`<p class="empty">${this.label('没有匹配的论文','No matching papers')}</p>`;
    root.querySelectorAll('[data-paper]').forEach(b=>b.onclick=()=>this.onNavigate(b.dataset.paper,'motivation'));
    root.querySelectorAll('[data-group-paper]').forEach(b=>b.onclick=()=>this.groups.edit(this.records.find(p=>p.id===b.dataset.groupPaper),this.label.bind(this),()=>{if(!this.groups.state.groups.some(g=>g.id===this.groupFilter))this.groupFilter='';this.renderList();this.revealSelected();}));
  }
  markdown(source,paper){
    const container=document.createElement('div');container.innerHTML=DOMPurify.sanitize(marked.parse(source));
    for(const a of container.querySelectorAll('a')){
      const href=a.getAttribute('href')||'';
      if(href.startsWith('#')||/^query\/imports\//.test(href)){continue;}
      if(/^https?:\/\//i.test(href)){a.target='_blank';a.rel='noopener noreferrer';continue;}
      let decoded;try{decoded=decodeURIComponent(href);}catch{decoded=href;}
      const section=Object.entries({overview:'README.md',motivation:'出发点分析.md',usecase:'usecase分析.md',problem:'解决的问题分析.md',novelty:'Novelty分析.md',benchmark:'benchmark分析.md',workload:'workload分析.md'}).find(([,file])=>decoded===file);
      if(section){a.href=`#paper/${paper.id}/${section[0]}`;continue;}
      // PDFs remain in the source repository; use a recorded public URL when available.
      if(/\.pdf$/i.test(decoded)&&paper.url){a.href=paper.url;a.target='_blank';a.rel='noopener noreferrer';}
      else a.replaceWith(document.createTextNode(a.textContent));
    }
    container.querySelectorAll('img').forEach(el=>el.remove());
    return container.innerHTML;
  }
  relatedQueries(){
    const ids=new Set(this.selected.source_ids||[]);
    return window.SEMREL_PLANS.filter(q=>q.provenance.some(ref=>ref.role==='paper'&&ids.has(ref.source_id)));
  }
  renderEvidence(){
    const queries=this.relatedQueries();
    const links=queries.map(q=>`<details><summary>${escape(q.group)} / ${escape(q.display_number)} · ${escape(AtlasI18n.queryTitle(q))}</summary><p><a href="#${encodeURIComponent(q.query_id)}?view=environment">${this.label('打开查询详情','Open query details')} →</a></p>${this.inspectors.environment(q)}</details>`).join('');
    return queries.length?links:`<p class="empty">${this.label('尚未关联逐查询数据记录。','No query records are linked yet.')}</p>`;
  }

  render(){
    this.disposeEditor();this.renderList();const p=this.selected,root=document.querySelector('#detail');
    if(!p){root.innerHTML='<h1>Paper</h1>';return;}
    const content=this.section==='usecase'?p.usecase||p.sections.workload:p.sections[this.section];
    root.innerHTML=`<article class="paper-reading" data-section="${this.section}"><div class="paper-heading"><span class="badge paper-kind-line">${kindIcon(p)}${escape(p.venue)}${p.year==='0'?'':p.year}</span><span class="paper-links">${p.url?`<a href="${escape(p.url)}" target="_blank" rel="noopener noreferrer">${AtlasIcons.render('document')} ${this.label('原文','Paper')} ↗</a>`:''}${(p.repositories||[]).filter(r=>/^https?:\/\//.test(r.url)&&r.url!==p.url).map(r=>`<a href="${escape(r.url)}" target="_blank" rel="noopener noreferrer" title="${escape(r.commit||r.link_source)}">${AtlasIcons.render('folder')} ${this.label('代码仓库','Repository')} ↗</a>`).join('')}</span></div><h1>${escape(p.title)}</h1><nav class="tabs paper-tabs" aria-label="${this.label('阅读方面','Reading aspects')}">${sections.filter(([id])=>id==='environment'||(id==='usecase'?!!p.usecase:!!p.sections[id])).map(([id,zh,en])=>`<button data-section="${id}" aria-current="${this.section===id?'page':'false'}">${this.label(zh,en)}</button>`).join('')}</nav><section class="paper-editor" data-verbatim></section></article>`;
    if(this.section==='environment'){
      const panel=root.querySelector('.paper-editor');panel.innerHTML=`<p class="empty">${this.label('正在读取查询详情…','Loading query details…')}</p>`;
      Promise.all(this.relatedQueries().map(q=>window.SemRelDetails.load(q)||q)).then(()=>{if(this.selected===p&&this.section==='environment')panel.innerHTML=this.renderEvidence();},error=>{panel.textContent=error.message;});
    }
    else this.unmountEditor=mountPaperEditor(root.querySelector('.paper-editor'),{paper:p.id,section:this.section,html:this.markdown(content||'',p),label:this.label.bind(this)});
    root.querySelectorAll('.paper-tabs button[data-section]').forEach(b=>b.onclick=()=>this.onNavigate(p.id,b.dataset.section));
  }
}

/** Categories present in the given papers, in taxonomy order. */
function categories(papers){return [...new Map(papers.map(p=>[p.category.key,p.category])).values()].sort((a,b)=>a.order-b.order);}

/** Source IDs are the canonical relationship between query provenance and papers. */
export function sourceHref(ref){
  const paper=window.SEMREL_PAPERS.find(p=>p.source_ids?.includes(ref.source_id));
  if(!paper)throw new Error(`Missing paper for source ${ref.source_id}`);
  return `#paper/${paper.id}/overview`;
}

export function kindIcon(paper){
  const names={benchmark:'Benchmark',research:'Research',survey:'Survey / Perspective'};
  return `<span class="paper-kind" role="img" aria-label="${names[paper.kind]}" title="${names[paper.kind]}">${AtlasIcons.render(paper.kind)}</span>`;
}

export function sourceIcon(items){
  const ids=new Set(items.flatMap(q=>q.provenance.filter(r=>r.role==='paper').map(r=>r.source_id)));
  const paper=window.SEMREL_PAPERS.find(p=>p.source_ids?.some(id=>ids.has(id)));
  return paper?kindIcon(paper):`<span class="paper-kind" role="img" aria-label="Research · Protocol" title="Research · Protocol">${AtlasIcons.render('research')}</span>`;
}

export function queryGroups(query){
  const sourceIds=new Set((query.provenance||[]).filter(r=>r.role==='paper').map(r=>r.source_id));
  const papers=window.SEMREL_PAPERS.filter(p=>p.source_ids?.some(id=>sourceIds.has(id)));
  return [...new Map([query.query_id,...papers.map(p=>p.id)].flatMap(id=>groupStore.groupsFor(id)).map(g=>[g.id,g])).values()];
}
export function groupDots(groups){
  return `<i class="paper-group-dots" title="${escape(groups.map(g=>g.name).join(' · '))}" aria-label="${escape(groups.map(g=>g.name).join(', '))}">${groups.slice(0,3).map(g=>`<i style="background:${g.color}"></i>`).join('')}</i>`;
}

export function editQueryGroups(query){
  groupStore.edit({id:query.query_id||'import:'+query.id,title:AtlasI18n.queryTitle(query)},(zh,en)=>window.AtlasI18n.language==='en'?en:zh,()=>{});
}
