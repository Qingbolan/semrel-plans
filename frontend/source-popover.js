/** One transient source card, shared by every folder and dismissed with its owner. */
class SourcePopover {
  constructor(){
    this.element=document.createElement('section');this.element.id='source-popover';this.element.className='source-popover';this.element.hidden=true;this.element.setAttribute('role','dialog');document.body.append(this.element);
    this.element.onpointerenter=()=>clearTimeout(this.timer);
    this.element.onpointerleave=()=>this.scheduleClose();
    this.element.onfocusin=()=>clearTimeout(this.timer);
    this.element.onfocusout=()=>this.scheduleClose();
    document.addEventListener('keydown',e=>{if(e.key==='Escape'&&!this.element.hidden){e.stopPropagation();const anchor=this.anchor;anchor?.querySelector('.folder-heading')?.focus();this.close();}},true);
    document.addEventListener('pointerdown',e=>{if(!this.element.contains(e.target)&&!this.anchor?.contains(e.target))this.close();});
    document.querySelector('#catalog-panel').addEventListener('scroll',()=>this.close());
    window.addEventListener('resize',()=>this.close());
  }
  scheduleClose(){clearTimeout(this.timer);this.timer=setTimeout(()=>{if(!this.element.contains(document.activeElement)&&!this.anchor?.contains(document.activeElement))this.close();},180);}
  close(){clearTimeout(this.timer);this.element.hidden=true;this.anchor=null;}
  attach(row,name,items){
    const button=row.querySelector('.folder-heading');
    row.onpointerenter=()=>this.show(row,name,items);row.onpointerleave=()=>this.scheduleClose();
    button.onfocus=()=>this.show(row,name,items);
    button.onkeydown=e=>{if(e.key==='ArrowRight'){e.preventDefault();this.show(row,name,items);this.element.querySelector('a')?.focus();}};
    row.onfocusout=()=>this.scheduleClose();
  }
  show(anchor,name,items){
    clearTimeout(this.timer);if(this.anchor===anchor&&!this.element.hidden)return;this.close();this.anchor=anchor;
    const make=(tag,text)=>{const el=document.createElement(tag);el.textContent=text;return el;};
    const card=this.element;card.replaceChildren();card.setAttribute('aria-label',name+' 来源与统计');
    const header=make('header','');header.append(make('strong',name));const close=make('button','×');close.setAttribute('aria-label','关闭来源信息');close.onclick=()=>this.close();header.append(close);card.append(header);
    const info=window.SEMREL_COLLECTIONS?.folders[name],lang=AtlasI18n.language==='en'?'en':'zh';
    if(info){const kind=make('span',window.SEMREL_COLLECTIONS.kinds[info.kind][lang]);kind.className='source-kind';kind.setAttribute('data-verbatim','');card.append(kind);const summary=make('p',info.summary[lang]);summary.className='source-summary';summary.setAttribute('data-verbatim','');card.append(summary);}
    const stats=make('div','');stats.className='source-stats';
    const nodes=items.flatMap(q=>q.eal?.ops||[]);
    stats.innerHTML=[[items.length,'查询','document'],[nodes.length,'逻辑节点','nodes'],[nodes.filter(n=>n.family==='semantic').length,'语义节点','semantic'],[new Set(nodes.map(n=>n.ability)).size,'算子类型','overview']].map(args=>AtlasIcons.stat(...args)).join('');card.append(stats);
    const origins=new Map();for(const q of items)origins.set(q.plan_origin,(origins.get(q.plan_origin)||0)+1);
    const origin=make('p','');origin.className='source-origins';origin.innerHTML=`<span>${esc(AtlasI18n.t('计划来源'))}</span>${[...origins].sort((a,b)=>b[1]-a[1]).map(([o,n])=>`<span class="origin-badge tier-${AnalysisLabels.tier(o)}">${esc(AnalysisLabels.origin_(o))} ${n}</span>`).join('')}`;card.append(origin);
    const refs=[...new Map(items.flatMap(q=>q.provenance).map(r=>[r.role+'|'+r.location,r])).values()];
    const linked=new Set(refs.filter(r=>r.role==='paper').map(r=>window.SEMREL_PAPERS.find(p=>p.source_ids?.includes(r.source_id))?.id));
    const extra=(info?.papers||[]).filter(id=>!linked.has(id)).map(id=>window.SEMREL_PAPERS.find(p=>p.id===id)).filter(Boolean);
    for(const [roles,label] of [[['paper','protocol'],'关联论文 / 协议'],[['dataset'],'数据来源']]){
      card.append(make('h3',label));const list=make('ul','');
      if(roles.includes('paper'))for(const paper of extra){const li=make('li','');const link=make('a',paper.title);link.title=paper.title;link.href=`#paper/${paper.id}/overview`;link.onclick=()=>this.close();li.append(link);list.append(li);}
      for(const ref of refs.filter(r=>roles.includes(r.role))){const li=make('li','');const link=make('a',ref.title);link.title=ref.title;if(ref.role==='paper'){link.href=SemRelPapers.sourceHref(ref);link.onclick=()=>this.close();}else{link.href=ref.location;link.target='_blank';link.rel='noopener';}if(ref.role==='paper'&&ref.publication_label){const badge=make('span',ref.publication_label);badge.className='publication-badge';li.className='paper-reference';li.append(badge);}li.append(link);list.append(li);}card.append(list);
    }
    AtlasI18n.localize(card);
    card.hidden=false;
    const rect=anchor.getBoundingClientRect();const width=Math.min(380,innerWidth-24);card.style.width=width+'px';card.style.left=Math.max(12,Math.min(rect.right+8,innerWidth-width-12))+'px';card.style.top=Math.max(12,Math.min(rect.top,innerHeight-card.offsetHeight-12))+'px';
  }
}
