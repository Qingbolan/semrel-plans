const queries = window.SEMREL_PLANS;
const esc = s => String(s).replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const $ = s => document.querySelector(s);
const offline = location.protocol==='file:';

let current=queries[0],view='graph',screen='query';
const imports=[];
const reader=new EalDocument(render);
const papers=new SemRelPapers.PaperLibrary(window.SEMREL_PAPERS,(id,section)=>showPapers(id,section),{environment:environmentDetails});
const analysis=new AnalysisView(queries,q=>select(q));
const navigation=new CatalogNavigation(queries,q=>select(q,true,false),()=>showOverall(),()=>togglePapers(),()=>papers.deactivate());
function provenance(q) {
  if(q.imported) return '<div class="empty">本地导入文件未关联图册来源。文件内容仅提交到本机编译器，不写入查询目录。</div>';
  const roles={paper:'论文',dataset:'数据',protocol:'协议',task_definition:'任务定义',analysis:'查询分析'};
  return `<p><a href="${esc(q.source)}" target="_blank" rel="noopener">${AtlasI18n.t('查询定义 / 实现')} ↗</a></p>`+q.provenance.map(ref=>`<section class="provenance-source">${ref.role==='paper'&&ref.publication_label?`<a class="badge" href="${esc(ref.publication_url)}" target="_blank" rel="noopener">${esc(ref.publication_label)}</a>`:`<span class="badge">${roles[ref.role]}</span>`}<div><h3><a href="${esc(ref.role==='paper'?SemRelPapers.sourceHref(ref):ref.location)}" ${ref.role==='paper'?'':'target="_blank" rel="noopener"'}>${esc(ref.title)} ${ref.role==='paper'?'→':'↗'}</a></h3><p>${esc(ref.version)} · ${esc(ref.locator)}</p><p>${esc(ref.attribution_note)}</p></div></section>`).join('');
}
function originalQuery(q) {
  const o=q.original_query;
  if(!o?.text||q.imported||o.text===AtlasI18n.queryTitle(q))return '';
  const code=['sql','local_sql','python_plan'].includes(o.kind);
  return `<figure class="original-query"><figcaption>${AtlasI18n.t('原始查询')} · ${esc(AnalysisLabels.tr(AnalysisLabels.kind[o.kind])||o.kind)}</figcaption>${code?`<pre data-verbatim>${esc(o.text)}</pre>`:`<blockquote data-verbatim>${esc(o.text)}</blockquote>`}</figure>`;
}
const detailPending=q=>!q.imported&&!q.detailLoaded;
const loadingDetail='<div class="read-status" role="status">正在读取…</div>';
function environmentDetails(q) { return detailPending(q)?loadingDetail:QueryInputs.render(q); }

function rawDetails(q) {
  const en=AtlasI18n.language==='en',t=(zh,english)=>en?english:zh;
  if(q.imported)return `<p>${t('此文件为导入的 EAL，没有关联原始 JSON。','This imported EAL has no associated JSON record.')}</p>`;
  if(detailPending(q))return loadingDetail;
  return `<p><a href="${esc(q.task_path)}" download>${t('下载 JSON','Download JSON')}</a></p><pre class="code" data-verbatim>${esc(JSON.stringify(q.task_record,null,2))}</pre>`;
}
const taskDefinitionOnly=q=>q.reference_programs?.length>0&&q.reference_programs.every(p=>p.type==='task_definition');
function referenceDetails(q) {
  const en=AtlasI18n.language==='en',t=(zh,english)=>en?english:zh;
  const section=(label,data)=>data===null||data===undefined?'':`<details><summary>${label}</summary><pre class="code" data-verbatim>${esc(JSON.stringify(data,null,2))}</pre></details>`;
  const definitionOnly=taskDefinitionOnly(q);
  return `<p>${definitionOnly?t('来源只提供了任务定义，没有逻辑计划；以下为原始任务定义文件。','The source supplies only a task definition, not a logical plan; the original task definition follows.'):t('以下保留提供文件中的参考描述；逻辑计划按其中的显式依赖转换，尚未执行验证。','Original supplied descriptions; logical plans preserve their explicit dependencies and have not been execution-verified.')}</p>`
    +q.reference_programs.map(p=>`<h3>${p.type==='task_definition'?t('任务定义','Task definition'):esc(p.type)}</h3><pre class="code" data-verbatim>${esc(p.program)}</pre>`).join('')
    +section(t('分析依据、置信度与上游定位（原记录）','Analysis, confidence and upstream locator (as supplied)'),q.annotation)
    +section(t('提供的参考答案（尚未独立验证）','Supplied gold (not independently verified)'),q.gold)
    +section(t('提供的评估规则','Supplied evaluation'),q.evaluation);
}
function planError(state) {
  const descriptions = {
    read:['无法读取本地计划服务','请启动 python3 backend/scripts/serve.py 并刷新。原始 JSON、环境与输入仍可查看。'],
    catalog:['计划清单不可用','请重新构建图册并刷新页面。服务会自动读取最新清单。'],
    file:['计划文件不可用','请检查 EAL 文件或重新构建图册，然后重新加载。'],
    busy:['编译器忙','请稍后点击重新加载。'],
    compile:['无法生成计划图','可在 EAL 源码页查看文件内容，修正后重新加载。'],
  };
  const [title,hint]=descriptions[state.errorKind]||descriptions.read;
  return `<div class="compile-error" role="alert"><strong>${AtlasI18n.t(title)}</strong><pre>${esc(state.error)}</pre><p>${AtlasI18n.t(hint)}</p></div>`;
}
let disposeGraph = null;
function render() {
  if(screen==='overall'){renderOverall();return;}
  if(screen==='papers'){papers.render();return;}
  papers.disposeEditor();
  disposeGraph?.();
  disposeGraph = null;
  const q=current,s=reader.state,ready=s.status==='ready',model=s.graph;
  const reference=q.plan_format==='reference_program';
  const tabs=reference?[['graph',taskDefinitionOnly(q)?'任务定义':'参考计划'],['raw','原始 JSON'],['environment','环境与输入'],['sources','来源与依据']]:[['graph','逻辑计划'],['eal','EAL 源码'],['raw','原始 JSON'],['environment','环境与输入'],['sources','来源与依据']];
  if(!reference && q.reference_programs?.length) tabs.splice(2,0,['reference','参考计划']);
  if(!tabs.some(([id])=>id===view))view='graph';
  $('#detail').innerHTML=`<div class="detail-heading"><div class="eyebrow">${esc(q.group)} / ${esc(q.display_number)}</div><div class="document-actions query-group-action">${!reference?`<button id="reload-plan" ${s.status==='loading'?'disabled':''}>重新加载</button>`:''}<button id="query-group" title="添加到分组" aria-label="添加到分组">${AtlasIcons.render('folder')}<span>添加到分组</span></button></div></div><h2 data-verbatim>${esc(AtlasI18n.queryTitle(q))}</h2>${originalQuery(q)}<div class="metadata">${q.imported?'':`<span class="origin-badge tier-${AnalysisLabels.tier(q.plan_origin)}" title="${esc(q.status||'')}">${esc(AnalysisLabels.origin_(q.plan_origin))}</span><span>${esc(AnalysisLabels.mixed(q.mixed))}</span>`}${offline&&!q.imported?'<span class="snapshot-badge">离线快照，非实时编译</span>':''}${reference?`<span>${AtlasI18n.t('未建立可编译 DAG')}</span>`:`<span>${ready?model.nodes.length+' 个节点':s.status==='error'?'加载失败':'等待编译结果'}</span>${ready?'<span>'+model.nodes.filter(n=>n.family==='semantic').length+' 个语义算子</span>':''}`}</div>${s.status==='loading'?'<div class="read-status" role="status">正在读取…</div>':''}<div class="tabs" role="tablist" aria-label="查询视图">${tabs.map(([id,label])=>`<button id="tab-${id}" role="tab" aria-selected="${view===id}" aria-controls="panel" data-view="${id}" tabindex="${view===id?0:-1}">${label}</button>`).join('')}</div>${s.error&&['graph','eal'].includes(view)?planError(s):''}<section id="panel" role="tabpanel" aria-labelledby="tab-${view}" tabindex="0"></section>`;
  if(view==='graph') $('#panel').innerHTML=reference?referenceDetails(q):ready?`<div id="graph-root"></div>${q.note?'<div class="note">'+esc(q.note)+'</div>':''}`:`<div class="empty">${s.status==='loading'?'正在构建依赖图…':'计划图暂不可用；原始 JSON、环境与输入可独立查看。'}</div>`;
  if(view==='eal') $('#panel').innerHTML=`<div class="eal-code-surface"><div class="code-actions"><span>eal</span><button id="copy" aria-label="复制源码" title="复制源码" ${s.source?'':'disabled'}>${AtlasIcons.render('copy')}</button></div><pre class="code" tabindex="0" aria-label="EAL 源码"><code class="language-eal">${EalCode.highlight(s.source||'正在读取或文件不可用。')}</code></pre></div><div id="copy-status" role="status"></div>`;
  if(view==='reference') $('#panel').innerHTML=referenceDetails(q);
  if(view==='raw') $('#panel').innerHTML=rawDetails(q);
  if(view==='environment') $('#panel').innerHTML=environmentDetails(q);
  if(view==='sources') $('#panel').innerHTML=provenance(q);
  if($('#reload-plan')) $('#reload-plan').onclick=()=>reader.load(q);
  $('#query-group').onclick=()=>SemRelPapers.editQueryGroups(q);
  document.querySelectorAll('[data-view]').forEach(b=>{b.onclick=()=>{view=b.dataset.view;if(!q.imported)history.replaceState(null,'','#'+encodeURIComponent(q.query_id)+'?view='+view);render();$(`#tab-${view}`).focus();};b.onkeydown=e=>{const ids=tabs.map(([id])=>id);if(['ArrowLeft','ArrowRight','Home','End'].includes(e.key)){e.preventDefault();view=ids[e.key==='Home'?0:e.key==='End'?ids.length-1:(ids.indexOf(view)+(e.key==='ArrowRight'?1:ids.length-1))%ids.length];render();$(`#tab-${view}`).focus();}};});
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
  try {const source=await file.text();if(revision!==importRevision)return;const q={display_number:imports.length+1,imported:true,importedSource:source,title:file.name,id:file.name.replace(/\.eal$/i,''),group:'本地 EAL',status:'导入文件',note:''};imports.push(q);$('#import-status').textContent=AtlasI18n.t('已导入；外部修改后请重新选择文件。');select(q);}catch{$('#import-status').textContent=AtlasI18n.t('无法读取文件，请重新选择。');}
}
document.addEventListener('click',event=>{if(event.target.closest('[data-action="import-eal"]'))$('#eal-file').click();});
$('#eal-file').onchange=e=>{importFile(e.target.files[0]);e.target.value='';};
for(const event of ['dragover','drop'])document.addEventListener(event,e=>{e.preventDefault();if(event==='drop')importFile(e.dataTransfer.files[0]);});
let overallTab='index';
function showOverall(updateHash=true){
  screen='overall';papers.deactivate();navigation.close();navigation.setActive('Overall');
  if(updateHash)history.replaceState(null,'',overallTab==='analysis'?analysis.hash():'#overall');
  renderOverall();
}
function renderOverall(){
  papers.disposeEditor();
  disposeGraph?.();disposeGraph=null;
  const tabs=[['index','索引'],['analysis','分析']];
  $('#detail').innerHTML=`<div class="tabs overall-tabs" role="tablist" aria-label="Overall">${tabs.map(([id,label])=>`<button id="overall-tab-${id}" role="tab" aria-selected="${overallTab===id}" aria-controls="overall-panel" data-overall-tab="${id}" tabindex="${overallTab===id?0:-1}">${label}</button>`).join('')}</div><div id="overall-panel" role="tabpanel" aria-labelledby="overall-tab-${overallTab}"></div>`;
  if(overallTab==='analysis')analysis.render($('#overall-panel'));else renderIndex($('#overall-panel'));
  AtlasI18n.localize($('#detail').querySelector('.overall-tabs'));
  document.querySelectorAll('[data-overall-tab]').forEach(b=>{
    b.onclick=()=>{overallTab=b.dataset.overallTab;showOverall();$(`#overall-tab-${overallTab}`).focus();};
    b.onkeydown=e=>{if(['ArrowLeft','ArrowRight','Home','End'].includes(e.key)){e.preventDefault();overallTab=e.key==='Home'?'index':e.key==='End'?'analysis':overallTab==='index'?'analysis':'index';showOverall();$(`#overall-tab-${overallTab}`).focus();}};
  });
}
function renderIndex(root){
  const groups=[...navigation.folders.keys()];
  const nodeCount=queries.reduce((sum,q)=>sum+(q.eal?.nodes||0),0);
  const operatorCount=new Set(queries.flatMap(q=>q.eal?.ops.map(n=>n.ability)||[])).size;
  root.innerHTML=`<section class="overall"><h1>Overall</h1><p class="overall-lead">结构化与语义混合查询的逻辑计划目录。</p><div class="overall-stats">${[[queries.length,'查询计划','document'],[nodeCount,'逻辑节点','nodes'],[operatorCount,'算子类型','overview']].map(args=>AtlasIcons.stat(...args)).join('')}</div><div class="scene-index">${groups.map(g=>`<button data-overall-group="${esc(g)}"><span>${esc(g)}</span><span>${navigation.folders.get(g).length} 条 <b>↗</b></span></button>`).join('')}</div><div class="resource-links"><a href="exports/catalog.sqlite" download>${AtlasIcons.render('database')}SQLite</a><a href="docs/data-model.md">${AtlasIcons.render('database')}数据模型</a><a href="docs/eal.md">${AtlasIcons.render('document')}EAL 说明</a><a href="docs/benchmark-coverage.md">${AtlasIcons.render('document')}Benchmark 收录核对</a></div></section>`;
  AtlasI18n.localize(root);
  root.querySelectorAll('[data-overall-group]').forEach(button=>button.onclick=()=>{
    const group=button.dataset.overallGroup;
    navigation.openFolder(group);select(navigation.folders.get(group)[0],true,false);
  });
}
function togglePapers(){
  if(screen==='papers'&&papers.active){papers.togglePanel();return;}
  papers.expanded=true;showPapers(papers.selected.id,papers.section);
}
function showPapers(id,section='motivation',updateHash=true){
  screen='papers';disposeGraph?.();disposeGraph=null;navigation.close();navigation.setActive('Paper');papers.open(id,section);
  if(updateHash)history.replaceState(null,'',`#paper/${papers.selected.id}/${papers.section}`);
  $('#detail').scrollTop=0;
}
function restore(){
  let q;
  try{const [identity,search='']=location.hash.slice(1).split('?');const params=new URLSearchParams(search);if(params.get('view'))view=params.get('view');const h=decodeURIComponent(identity);if(h==='papers'||h.startsWith('paper/')){const [,id,section]=h.split('/');showPapers(id,section||'motivation',false);return;}if(!h||h==='overall'){analysis.readParams(params);overallTab=params.get('tab')==='analysis'||['q','source','origin','op'].some(k=>params.get(k))?'analysis':'index';showOverall(false);return;}q=queries.find(q=>q.query_id===h||q.group+'|'+q.id===h);}catch{}
  if(q)select(q,false);else showOverall(false);
}
window.addEventListener('hashchange',restore);list();restore();

document.addEventListener('atlas-language-change',()=>{navigation.sourcePopover.close();navigation.update();navigation.render();render();AtlasI18n.localize($('#catalog-panel'));AtlasI18n.localize($('#scene-rail'));navigation.updateLanguage();});
AtlasI18n.localize($('#catalog-panel'));AtlasI18n.localize($('#scene-rail'));navigation.updateLanguage();
