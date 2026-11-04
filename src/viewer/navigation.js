/** Source folders own their category filters; panel visibility is independent of selection. */
class CatalogNavigation {
  constructor(queries,onSelect,onOverall,onPapers,onCatalog){
    this.queries=queries;this.onSelect=onSelect;this.openGroup=null;this.active=null;this.selectedQuery=null;this.expanded=new Set();this.tags=new Map();this.term='';
    this.groupFilter='';try{this.groupFilter=localStorage.getItem('semrel-catalog-group')||'';}catch{}
    this.panel=document.querySelector('#catalog-panel');this.workspace=document.querySelector('#workspace');
    this.folders=new Map();this.sourcePopover=new SourcePopover();
    for(const q of queries){
      const parts=q.query_id.split('/');
      const source=q.collection_name;
      q.folder=source;q.tags=q.category_label?[q.category_label]:parts[0]==='sembench'?[parts[1]]:parts[0]==='uda-bench'?parts.slice(2,-1):parts[0]==='local-derived'?['本地派生']:['BIRD'];
      if(!this.folders.has(source))this.folders.set(source,[]);this.folders.get(source).push(q);
    }
    document.querySelector('#scene-rail').innerHTML=[['overall','overview','Overall','总览'],['catalog','folder','来源目录','来源目录'],['papers','document','Paper','Paper']].map(([page,icon,label,title])=>`<button data-page="${page}" aria-label="${label}" title="${title}" ${page==='catalog'?'aria-controls="catalog-panel"':''}>${AtlasIcons.render(icon)}</button>`).join('');
    document.querySelector('#catalog-title').onchange=e=>{this.groupFilter=e.target.value;try{localStorage.setItem('semrel-catalog-group',this.groupFilter);}catch{}this.update();this.render();};
    document.querySelector('#close-catalog').innerHTML=AtlasIcons.render('close');
    document.querySelector('#close-catalog').title='收起查询目录';
    document.querySelector('[data-page=overall]').onclick=onOverall;
    document.querySelector('[data-page=catalog]').onclick=()=>{onCatalog();this.toggle('catalog');};
    document.querySelector('[data-page=papers]').onclick=onPapers;
    const language=document.createElement('button');language.id='language-toggle';language.innerHTML=AtlasIcons.render('language');document.querySelector('#scene-rail').append(language);
    language.onclick=()=>AtlasI18n.toggle();
    const migration=document.createElement('button');migration.title='浏览器数据迁移';migration.setAttribute('aria-label','浏览器数据迁移');migration.innerHTML=AtlasIcons.render('download');migration.onclick=()=>{location.href='/migration.html';};document.querySelector('#scene-rail').append(migration);
    this.updateLanguage=()=>{const label=AtlasI18n.language==='zh'?'Switch to English':'切换到中文';language.title=label;language.setAttribute('aria-label',label);};this.updateLanguage();
    document.querySelector('#close-catalog').onclick=()=>this.close();
    const search=document.querySelector('#search'),searchToggle=document.querySelector('#toggle-catalog-search');
    searchToggle.innerHTML=AtlasIcons.render('search');
    const setSearchOpen=open=>{search.hidden=!open;searchToggle.setAttribute('aria-expanded',String(open));(open?search:searchToggle).focus();};
    searchToggle.onclick=()=>setSearchOpen(search.hidden);
    search.onkeydown=e=>{if(e.key==='Escape'){e.stopPropagation();setSearchOpen(false);}};
    search.oninput=e=>{this.term=e.target.value.toLowerCase().trim();searchToggle.classList.toggle('has-value',!!this.term);this.render();};
    this.panel.addEventListener('keydown',e=>{if(e.key==='Escape')this.close();});
    document.addEventListener('atlas-groups-change',()=>{this.update();this.render();});
    this.update();this.render();
  }
  toggle(group){this.openGroup=this.openGroup===group?null:group;this.update();}
  close(){this.openGroup=null;this.update();}
  setActive(q){this.active=q;if(q&&typeof q==='object'){this.selectedQuery=q;this.expanded.add(q.folder);}this.render();this.update();}
  openFolder(name){this.groupFilter='';try{localStorage.setItem('semrel-catalog-group','');}catch{}this.expanded.add(name);this.openGroup='catalog';this.update();this.render();}
  update(){
    this.sourcePopover.close();
    this.panel.hidden=this.openGroup===null;this.panel.classList.toggle('imports-only',this.openGroup==='本地 EAL');this.workspace.classList.toggle('catalog-open',this.openGroup!==null);
    const selector=document.querySelector('#catalog-title'),groups=SemRelPapers.catalogGroups();
    if(!groups.some(g=>g.id===this.groupFilter))this.groupFilter='';
    selector.replaceChildren();
    for(const group of [{id:'',name:AtlasI18n.t('来源目录')},...groups]){const option=document.createElement('option');option.value=group.id;option.textContent=AtlasI18n.t(group.name);option.selected=group.id===this.groupFilter;selector.append(option);}
    selector.title=AtlasI18n.t('切换分组');
    for(const b of document.querySelectorAll('#scene-rail [data-page]')){const page=b.dataset.page;b.setAttribute('aria-current',((page==='overall'&&this.active==='Overall')||(page==='papers'&&this.active==='Paper'))?'page':'false');if(page==='catalog')b.setAttribute('aria-expanded',String(this.openGroup===(page==='catalog'?'catalog':'本地 EAL')));}
    AtlasI18n.localize(this.panel);
  }
  render(){
    this.sourcePopover.close();
    const root=document.querySelector('#list');root.replaceChildren();
    const make=(tag,text,cls)=>{const el=document.createElement(tag);if(text)el.textContent=text;if(cls)el.className=cls;return el;};
    let folderCount=0;
    for(const [name,sourceItems] of this.folders){
      const items=this.groupFilter?sourceItems.filter(q=>SemRelPapers.queryGroups(q).some(g=>g.id===this.groupFilter)):sourceItems;
      if(!items.length)continue;
      const matching=items.filter(q=>[q.title,q.original_query?.text||'',AtlasI18n.queryZh[q.title]||'',AtlasI18n.content[q.title]||'',q.id,String(q.display_number),...q.tags,q.note,AtlasI18n.content[q.note]||'',...(q.eal?.ops||[]).map(n=>AtlasI18n.content[n.label]||n.label),...(q.reference_programs||[]).map(p=>p.program)].join(' ').toLowerCase().includes(this.term));if(!matching.length)continue;
      const section=make('section',null,'source-folder');const expanded=this.term||this.expanded.has(name);
      const heading=make('button',null,'folder-heading');heading.setAttribute('aria-expanded',String(!!expanded));heading.innerHTML=SemRelPapers.sourceIcon(items);heading.append(make('span',name),make('small',String(items.length)));heading.onclick=()=>{this.expanded.has(name)?this.expanded.delete(name):this.expanded.add(name);this.render();};const row=make('div',null,'folder-row');row.append(heading);this.sourcePopover.attach(row,name,items);section.append(row);
      if(expanded){
        const tags=make('div',null,'folder-tags');for(const tag of ['全部',...new Set(items.flatMap(q=>q.tags))]){const b=make('button',tag);b.setAttribute('aria-pressed',String((this.tags.get(name)||'全部')===tag));b.onclick=()=>{this.tags.set(name,tag);this.render();};tags.append(b);}section.append(tags);
        const filtered=matching.filter(q=>!this.tags.get(name)||this.tags.get(name)==='全部'||q.tags.includes(this.tags.get(name)));
        for(const q of filtered){const b=make('button',null,'item'+(this.selectedQuery===q?' active':''));b.setAttribute('aria-current',this.selectedQuery===q?'page':'false');const title=make('strong',null,'query-title');const groups=SemRelPapers.queryGroups(q);if(groups.length)title.insertAdjacentHTML('beforeend',SemRelPapers.groupDots(groups));b.setAttribute('data-verbatim','');title.append(make('span',AtlasI18n.queryTitle(q)));b.title=AtlasI18n.queryTitle(q)+(groups.length?' · '+groups.map(g=>g.name).join(' · '):'');b.append(make('small',String(q.display_number)),title);b.onclick=()=>this.onSelect(q);section.append(b);}
        if(!filtered.length)section.append(make('p','该标签下没有匹配查询。','empty'));
      }root.append(section);folderCount++;
    }
    if(!folderCount)root.append(make('p','没有匹配的查询。','empty'));
    AtlasI18n.localize(root);
  }
}
