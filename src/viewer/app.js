const queries = window.SEMREL_PLANS;
const esc = s => String(s).replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const $ = s => document.querySelector(s);
const offline = location.protocol==='file:';

let current=queries[0],view='graph',screen='query';
const imports=[];
const reader=new EalDocument(render);
const papers=new SemRelPapers.PaperLibrary(window.SEMREL_PAPERS,(id,section)=>showPapers(id,section));
const navigation=new CatalogNavigation(queries,q=>select(q,true,false),()=>showOverall(),()=>togglePapers(),()=>papers.deactivate());
function provenance(q) {
  if(q.imported) return '<div class="empty">本地导入文件未关联图册来源。文件内容仅提交到本机编译器，不写入查询目录。</div>';
  const roles={paper:'论文',dataset:'数据',protocol:'协议'};
  return q.provenance.map(ref=>`<section class="provenance-source">${ref.role==='paper'&&ref.publication_label?`<a class="badge" href="${esc(ref.publication_url)}" target="_blank" rel="noopener">${esc(ref.publication_label)}</a>`:`<span class="badge">${roles[ref.role]}</span>`}<div><h3><a href="${esc(ref.role==='paper'?SemRelPapers.sourceHref(ref):ref.location)}" ${ref.role==='paper'?'':'target="_blank" rel="noopener"'}>${esc(ref.title)} ${ref.role==='paper'?'→':'↗'}</a></h3><p>${esc(ref.version)} · ${esc(ref.locator)}</p><p>${esc(ref.attribution_note)}</p></div></section>`).join('');
}
let disposeGraph = null;
function render() {
  if(screen==='overall'){renderOverall();return;}
  if(screen==='papers'){papers.render();return;}
  papers.disposeEditor();
  disposeGraph?.();
  disposeGraph = null;
  const q=current,s=reader.state,ready=s.status==='ready',model=s.graph;
  $('#detail').innerHTML=`<div class="detail-heading"><div class="eyebrow">${esc(q.group)} / ${esc(q.id)}</div><div class="document-actions query-group-action"><button id="query-group" title="添加到分组" aria-label="添加到分组">${AtlasIcons.render('folder')}<span>添加到分组</span></button></div></div><h2>${esc(q.title)}</h2><div class="metadata"><span>${ready?model.nodes.length+' 个节点':'等待编译结果'}</span><span>${ready?model.nodes.filter(n=>n.family==='semantic').length+' 个语义算子':esc(q.status)}</span></div>${s.status==='loading'?'<div class="read-status" role="status">正在读取…</div>':''}<div class="tabs" role="tablist" aria-label="查询视图">${[['graph','逻辑计划'],['eal','EAL 源码'],['sources','来源与依据']].map(([id,label])=>`<button id="tab-${id}" role="tab" aria-selected="${view===id}" aria-controls="panel" data-view="${id}" tabindex="${view===id?0:-1}">${label}</button>`).join('')}</div>${s.error?'<div class="compile-error" role="alert"><strong>无法生成计划图</strong><pre>'+esc(s.error)+'</pre><p>可在 EAL 源码页查看文件内容，修正后重新加载。</p></div>':''}<section id="panel" role="tabpanel" aria-labelledby="tab-${view}" tabindex="0"></section>`;
  if(view==='graph') $('#panel').innerHTML=ready?`<div id="graph-root"></div>${q.note?'<div class="note">'+esc(q.note)+'</div>':''}`:`<div class="empty">${s.status==='loading'?'正在构建依赖图…':'修正 EAL 后重新加载以显示计划图。'}</div>`;
  if(view==='eal') $('#panel').innerHTML=`<div class="eal-code-surface"><div class="code-actions"><span>eal</span><button id="copy" aria-label="复制源码" title="复制源码" ${s.source?'':'disabled'}>${AtlasIcons.render('copy')}</button></div><pre class="code" tabindex="0" aria-label="EAL 源码"><code class="language-eal">${EalCode.highlight(s.source||'正在读取或文件不可用。')}</code></pre></div><div id="copy-status" role="status"></div>`;
  if(view==='sources') $('#panel').innerHTML=provenance(q);
  $('#query-group').onclick=()=>SemRelPapers.editQueryGroups(q);
  document.querySelectorAll('[data-view]').forEach(b=>{b.onclick=()=>{view=b.dataset.view;render();$(`#tab-${view}`).focus();};b.onkeydown=e=>{const ids=['graph','eal','sources'];if(['ArrowLeft','ArrowRight','Home','End'].includes(e.key)){e.preventDefault();view=ids[e.key==='Home'?0:e.key==='End'?2:(ids.indexOf(view)+(e.key==='ArrowRight'?1:2))%3];render();$(`#tab-${view}`).focus();}};});
  AtlasI18n.localize($('#detail'));
  if(view==='graph' && ready) disposeGraph = SemRelGraph.mount($('#graph-root'), model, locateSource);
  if($('#copy')) $('#copy').onclick=async()=>{try{await navigator.clipboard.writeText(s.source);$('#copy-status').textContent=AtlasI18n.t('源码已复制');}catch{$('#copy-status').textContent=AtlasI18n.t('无法访问剪贴板，请选择源码复制或下载文件。');}};
}
function locateSource(node) {
  const source=reader.state.source;
  view='eal';render();
  const lines=source.split('\n');
  const index=node.binding?lines.findIndex(line=>line.includes('let '+node.binding+' =')):-1;
  if(index<0){$('#copy-status').textContent=AtlasI18n.t('该调用没有可定位的绑定，请按 ability 名称查找。');return;}
  $('.code code').innerHTML=EalCode.highlight(source,index);
  $('#source-target').scrollIntoView({block:'center'});
}
function select(q,updateHash=true,closeCatalog=true) {
  screen='query';papers.deactivate();
  current=q;
  if(closeCatalog)navigation.close();
  navigation.setActive(q);
  if(updateHash&&!q.imported)history.replaceState(null,'','#'+encodeURIComponent(q.query_id));
  list();reader.load(q);
  if(closeCatalog) $('#detail').focus({preventScroll:true});
}
function list() {
  navigation.render();
  $('#imports').innerHTML=imports.length?imports.map((q,i)=>`<button class="item ${q===current?'active':''}" data-import="${i}"><small>本次导入</small><strong>${esc(q.title)}</strong></button>`).join(''):'<div class="empty">暂无导入文件。</div>'; 
  $('#imports').insertAdjacentHTML('afterbegin','<button data-action="import-eal" class="import-button">打开 .eal</button>');
  AtlasI18n.localize($('#imports'));
  document.querySelectorAll('[data-import]').forEach(b=>b.onclick=()=>select(imports[Number(b.dataset.import)]));
}
let importRevision=0;
async function importFile(file) {
  const revision=++importRevision;
  if(!file)return;
  if(!file.name.toLowerCase().endsWith('.eal')||file.size>1024*1024){navigation.openGroup='本地 EAL';navigation.update();list();$('#import-status').textContent=AtlasI18n.t('请选择不超过 1 MiB 的 .eal 文件。');return;}
  try {const source=await file.text();if(revision!==importRevision)return;const q={imported:true,importedSource:source,title:file.name,id:file.name.replace(/\.eal$/i,''),group:'本地 EAL',status:'导入文件',note:''};imports.push(q);$('#import-status').textContent=AtlasI18n.t('已导入；外部修改后请重新选择文件。');select(q);}catch{$('#import-status').textContent=AtlasI18n.t('无法读取文件，请重新选择。');}
}
document.addEventListener('click',event=>{if(event.target.closest('[data-action="import-eal"]'))$('#eal-file').click();});
$('#eal-file').onchange=e=>{importFile(e.target.files[0]);e.target.value='';};
for(const event of ['dragover','drop'])document.addEventListener(event,e=>{e.preventDefault();if(event==='drop')importFile(e.dataTransfer.files[0]);});
function showOverall(updateHash=true){
  screen='overall';papers.deactivate();navigation.close();navigation.setActive('Overall');
  if(updateHash)history.replaceState(null,'','#overall');
  renderOverall();
}
function renderOverall(){
  papers.disposeEditor();
  disposeGraph?.();disposeGraph=null;
  const groups=[...navigation.folders.keys()];
  const nodeCount=queries.reduce((sum,q)=>sum+q.eal.nodes,0);
  const operatorCount=new Set(queries.flatMap(q=>q.eal.snapshot.graph.nodes.map(n=>n.ability))).size;
  $('#detail').innerHTML=`<section class="overall"><h1>Overall</h1><p class="overall-lead">结构化与语义混合查询的逻辑计划目录。</p><div class="overall-stats">${[[queries.length,'查询计划','document'],[nodeCount,'逻辑节点','nodes'],[operatorCount,'算子类型','overview']].map(args=>AtlasIcons.stat(...args)).join('')}</div><div class="scene-index">${groups.map(g=>`<button data-overall-group="${esc(g)}"><span>${esc(g)}</span><span>${navigation.folders.get(g).length} 条 <b>↗</b></span></button>`).join('')}</div><div class="resource-links"><a href="exports/catalog.sqlite" download>${AtlasIcons.render('database')}SQLite</a><a href="docs/data-model.md">${AtlasIcons.render('database')}数据模型</a><a href="docs/eal.md">${AtlasIcons.render('document')}EAL 说明</a></div></section>`;
  AtlasI18n.localize($('#detail'));
  document.querySelectorAll('[data-overall-group]').forEach(button=>button.onclick=()=>{
    const group=button.dataset.overallGroup;
    navigation.openFolder(group);select(navigation.folders.get(group)[0],true,false);
  });
}
function togglePapers(){
  if(screen==='papers'&&papers.active){papers.togglePanel();return;}
  papers.expanded=true;showPapers(papers.selected.id,papers.section);
}
function showPapers(id,section='usecase',updateHash=true){
  screen='papers';disposeGraph?.();disposeGraph=null;navigation.close();navigation.setActive('Paper');papers.open(id,section);
  if(updateHash)history.replaceState(null,'',`#paper/${papers.selected.id}/${papers.section}`);
  $('#detail').scrollTop=0;
}
function restore(){
  let q;
  try{const h=decodeURIComponent(location.hash.slice(1));if(h==='papers'||h.startsWith('paper/')){const [,id,section]=h.split('/');showPapers(id,section||'usecase',false);return;}if(!h||h==='overall'){showOverall(false);return;}q=queries.find(q=>q.query_id===h||q.group+'|'+q.id===h);}catch{}
  if(q)select(q,false);else showOverall(false);
}
window.addEventListener('hashchange',restore);list();restore();

document.addEventListener('atlas-language-change',()=>{navigation.sourcePopover.close();navigation.render();render();AtlasI18n.localize($('#catalog-panel'));AtlasI18n.localize($('#scene-rail'));navigation.updateLanguage();});
AtlasI18n.localize($('#catalog-panel'));AtlasI18n.localize($('#scene-rail'));navigation.updateLanguage();
