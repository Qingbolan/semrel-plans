/** Source folders own their category filters; panel visibility is independent of selection. */
class CatalogNavigation {
  constructor(queries,onSelect,onOverall,onPapers,onCatalog){
    this.queries=queries;this.onSelect=onSelect;this.openGroup=null;this.active=null;this.selectedQuery=null;this.expanded=new Set();this.tags=new Map();this.term='';
    this.panel=document.querySelector('#catalog-panel');this.workspace=document.querySelector('#workspace');
    this.folders=new Map();this.sourcePopover=new SourcePopover();
    for(const q of queries){
      const parts=q.query_id.split('/');
      const source=parts[0]==='local-derived'?parts[2]:({'sembench':'SemBench','tag-bench':'TAG-Bench','uda-bench':'UDA-Bench'}[parts[0]]||parts[0]);
      q.folder=source;q.tags=parts[0]==='sembench'?[parts[1]]:parts[0]==='uda-bench'?parts.slice(2,-1):parts[0]==='local-derived'?['本地派生']:['BIRD'];
      if(!this.folders.has(source))this.folders.set(source,[]);this.folders.get(source).push(q);
    }
    document.querySelector('#scene-rail').innerHTML=[['overall','overview','Overall','总览'],['catalog','folder','来源目录','来源目录'],['papers','document','Paper','Paper']].map(([page,icon,label,title])=>`<button data-page="${page}" aria-label="${label}" title="${title}" ${page==='catalog'?'aria-controls="catalog-panel"':''}>${AtlasIcons.render(icon)}</button>`).join('');
    document.querySelector('#close-catalog').innerHTML=AtlasIcons.render('close');
    document.querySelector('#close-catalog').title='收起查询目录';
    document.querySelector('[data-page=overall]').onclick=onOverall;
    document.querySelector('[data-page=catalog]').onclick=()=>{onCatalog();this.toggle('catalog');};
    document.querySelector('[data-page=papers]').onclick=onPapers;
    const language=document.createElement('button');language.id='language-toggle';language.innerHTML=AtlasIcons.render('language');document.querySelector('#scene-rail').append(language);
    language.onclick=()=>AtlasI18n.toggle();
    this.updateLanguage=()=>{const label=AtlasI18n.language==='zh'?'Switch to English':'切换到中文';language.title=label;language.setAttribute('aria-label',label);};this.updateLanguage();
    document.querySelector('#close-catalog').onclick=()=>this.close();
    const search=document.querySelector('#search'),searchToggle=document.querySelector('#toggle-catalog-search');
    searchToggle.innerHTML=AtlasIcons.render('search');
    const setSearchOpen=open=>{search.hidden=!open;searchToggle.setAttribute('aria-expanded',String(open));(open?search:searchToggle).focus();};
    searchToggle.onclick=()=>setSearchOpen(search.hidden);
    search.onkeydown=e=>{if(e.key==='Escape'){e.stopPropagation();setSearchOpen(false);}};
    search.oninput=e=>{this.term=e.target.value.toLowerCase().trim();searchToggle.classList.toggle('has-value',!!this.term);this.render();};
    this.panel.addEventListener('keydown',e=>{if(e.key==='Escape')this.close();});
    document.addEventListener('atlas-groups-change',()=>this.render());
    this.update();this.render();
  }
  toggle(group){this.openGroup=this.openGroup===group?null:group;this.update();}
  close(){this.openGroup=null;this.update();}
  setActive(q){this.active=q;if(q&&typeof q==='object'){this.selectedQuery=q;this.expanded.add(q.folder);}this.render();this.update();}
  openFolder(name){this.expanded.add(name);this.openGroup='catalog';this.update();this.render();}
  update(){
    this.sourcePopover.close();
    this.panel.hidden=this.openGroup===null;this.panel.classList.toggle('imports-only',this.openGroup==='本地 EAL');this.workspace.classList.toggle('catalog-open',this.openGroup!==null);
    document.querySelector('#catalog-title').textContent=this.openGroup==='本地 EAL'?'本地 EAL':'来源目录';
    for(const b of document.querySelectorAll('#scene-rail [data-page]')){const page=b.dataset.page;b.setAttribute('aria-current',((page==='overall'&&this.active==='Overall')||(page==='papers'&&this.active==='Paper'))?'page':'false');if(page==='catalog')b.setAttribute('aria-expanded',String(this.openGroup===(page==='catalog'?'catalog':'本地 EAL')));}
    AtlasI18n.localize(this.panel);
  }
  render(){
    this.sourcePopover.close();
    const root=document.querySelector('#list');root.replaceChildren();
    const make=(tag,text,cls)=>{const el=document.createElement(tag);if(text)el.textContent=text;if(cls)el.className=cls;return el;};
    for(const [name,items] of this.folders){
      const matching=items.filter(q=>[q.title,AtlasI18n.content[q.title]||'',q.id,...q.tags,q.note,AtlasI18n.content[q.note]||'',...q.eal.snapshot.graph.nodes.map(n=>AtlasI18n.content[n.label]||n.label),q.eal.snapshot.source].join(' ').toLowerCase().includes(this.term));if(!matching.length)continue;
      const section=make('section',null,'source-folder');const expanded=this.term||this.expanded.has(name);
      const heading=make('button',null,'folder-heading');heading.setAttribute('aria-expanded',String(!!expanded));heading.innerHTML=SemRelPapers.sourceIcon(items);heading.append(make('span',name),make('small',String(items.length)));heading.onclick=()=>{this.expanded.has(name)?this.expanded.delete(name):this.expanded.add(name);this.render();};const row=make('div',null,'folder-row');row.append(heading);this.sourcePopover.attach(row,name,items);section.append(row);
      if(expanded){
        const tags=make('div',null,'folder-tags');for(const tag of ['全部',...new Set(items.flatMap(q=>q.tags))]){const b=make('button',tag);b.setAttribute('aria-pressed',String((this.tags.get(name)||'全部')===tag));b.onclick=()=>{this.tags.set(name,tag);this.render();};tags.append(b);}section.append(tags);
        const filtered=matching.filter(q=>!this.tags.get(name)||this.tags.get(name)==='全部'||q.tags.includes(this.tags.get(name)));
        for(const q of filtered){const b=make('button',null,'item'+(this.selectedQuery===q?' active':''));b.setAttribute('aria-current',this.selectedQuery===q?'page':'false');const title=make('strong',null,'query-title');const groups=SemRelPapers.queryGroups(q);if(groups.length)title.insertAdjacentHTML('beforeend',SemRelPapers.groupDots(groups));title.append(make('span',q.title));b.title=q.title+(groups.length?' · '+groups.map(g=>g.name).join(' · '):'');b.append(make('small',q.id),title);b.onclick=()=>this.onSelect(q);section.append(b);}
        if(!filtered.length)section.append(make('p','该标签下没有匹配查询。','empty'));
      }root.append(section);
    }
    if(!root.children.length)root.append(make('p','没有匹配的查询。','empty'));
    AtlasI18n.localize(root);
  }
}
