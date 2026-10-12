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
    const stats=make('div','');stats.className='source-stats';
    const nodes=items.flatMap(q=>q.eal.snapshot.graph.nodes);
    stats.innerHTML=[[items.length,'查询','document'],[nodes.length,'逻辑节点','nodes'],[nodes.filter(n=>n.family==='semantic').length,'语义节点','semantic'],[new Set(nodes.map(n=>n.ability)).size,'算子类型','overview']].map(args=>AtlasIcons.stat(...args)).join('');card.append(stats);
    const refs=[...new Map(items.flatMap(q=>q.provenance).map(r=>[r.role+'|'+r.location,r])).values()];
    for(const [roles,label] of [[['paper','protocol'],'关联论文 / 协议'],[['dataset'],'数据来源']]){
      card.append(make('h3',label));const list=make('ul','');
      for(const ref of refs.filter(r=>roles.includes(r.role))){const li=make('li','');const link=make('a',ref.title);link.title=ref.title;if(ref.role==='paper'){link.href=SemRelPapers.sourceHref(ref);link.onclick=()=>this.close();}else{link.href=ref.location;link.target='_blank';link.rel='noopener';}if(ref.role==='paper'&&ref.publication_label){const badge=make('span',ref.publication_label);badge.className='publication-badge';li.className='paper-reference';li.append(badge);}li.append(link);list.append(li);}card.append(list);
    }
    AtlasI18n.localize(card);
    card.hidden=false;
    const rect=anchor.getBoundingClientRect();const width=Math.min(380,innerWidth-24);card.style.width=width+'px';card.style.left=Math.max(12,Math.min(rect.right+8,innerWidth-width-12))+'px';card.style.top=Math.max(12,Math.min(rect.top,innerHeight-card.offsetHeight-12))+'px';
  }
}
