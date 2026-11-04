/** Shared locale state for the catalog and React canvas. Source documents stay verbatim. */
class AtlasLocale {
  constructor(){
    this.language='zh';try{this.language=localStorage.getItem('semrel-language')==='en'?'en':'zh';}catch{}
    this.originals=new WeakMap();
    this.content=window.SEMREL_CONTENT_EN;
    this.queryZh=window.SEMREL_QUERY_ZH||{};
    this.contentKeys=Object.keys(this.content).sort((a,b)=>b.length-a.length);
    this.messages={
      '切换分组':'Switch group','NLP 任务':'NLP tasks','Sem-operator 问题':'Sem-operator questions',
      '原始 JSON':'Original JSON','原始查询':'Original query','计划来源':'Plan origin','离线快照，非实时编译':'Offline snapshot, not live-compiled','无法读取本地计划服务':'Unable to read the local plan service','请启动 python3 scripts/serve.py 并刷新。原始 JSON、环境与输入仍可查看。':'Start python3 scripts/serve.py and reload. Original JSON, environment and inputs remain available.','计划图暂不可用；原始 JSON、环境与输入可独立查看。':'Plan unavailable; original JSON, environment and inputs can be viewed independently.',
      '任务定义':'Task definition','查询分析':'Query analysis',
      '参考计划':'Reference plan','参考任务':'reference tasks','未建立可编译 DAG':'No compilable DAG','来源文件中的参考计划／分析；尚未核验为原论文 DAG 或执行结果。':'Reference plan / analysis from supplied files; not verified as a paper-original DAG or execution result.',
      '环境与输入':'Environment & inputs','查询定义 / 实现':'Query definition / implementation',
      '搜索查询':'Search queries','添加到分组':'Add to group','图例':'Legend','总览':'Overview','来源目录':'Sources','工作区导航':'Workspace navigation','查询目录':'Query catalog','收起查询目录':'Close catalog','查询列表':'Queries','搜索':'Search','查询名称、算子或关键词…':'Search queries, operators, keywords…','全部':'All','本地派生':'Derived','本地 EAL':'Local EAL','导入 EAL':'Import EAL','打开 .eal':'Open .eal','暂无导入文件。':'No imported files.','本次导入':'Imported','没有匹配的查询。':'No matching queries.','该标签下没有匹配查询。':'No matching queries in this category.',
      '逻辑计划':'Plan','EAL 源码':'EAL source','来源与依据':'Sources','查询视图':'Query views','重新加载':'Reload','重新编译':'Recompile','下载 .eal':'Download .eal','正在读取…':'Loading…','等待编译结果':'Waiting for compilation','读取失败':'Read failed','加载失败':'Load failed','计划清单不可用':'Plan catalog unavailable','请重新构建图册并刷新页面。服务会自动读取最新清单。':'Rebuild the atlas and refresh. The service reads the latest catalog automatically.','计划文件不可用':'Plan file unavailable','请检查 EAL 文件或重新构建图册，然后重新加载。':'Check the EAL file or rebuild the atlas, then reload.','编译器忙':'Compiler busy','请稍后点击重新加载。':'Click Reload again shortly.','无法生成计划图':'Unable to build plan','修正 EAL 后重新加载以显示计划图。':'Fix the EAL and reload to display the plan.','修正 EAL 后重新加载。':'Fix the EAL and reload.','可在 EAL 源码页查看文件内容，修正后重新加载。':'Check the EAL source, fix it, then reload.','正在构建依赖图…':'Building graph…','正在读取或文件不可用。':'Loading or file unavailable.',
      '结构化':'Relational','语义':'Semantic','输入':'Input','数据输入':'Data input','结构化算子':'Relational operator','语义算子':'Semantic operator','计划详情':'Plan details','箭头从输出指向输入。仅编译与展示，不执行查询。':'Edges connect outputs to inputs. This view compiles plans without executing queries.',
      '查询计划':'Queries','逻辑节点':'Plan nodes','语义节点':'Semantic nodes','算子类型':'Operator types','来源':'Sources','数据与文件':'Files & resources','全部 EAL':'All EAL','数据模型':'Data model','EAL 说明':'EAL guide','Benchmark 收录核对':'Benchmark coverage','索引':'Index','分析':'Analysis','结构化与语义混合查询的逻辑计划目录。':'A catalog of relational and semantic query plans.','当前目录包含 benchmark 选例与本地派生任务。图册编译并展示 EAL，不执行查询；节点数量不代表模型调用次数。':'Benchmark examples and derived workloads. EAL is compiled for display, not executed; node counts are not model call counts.',
      '论文':'Paper','数据':'Data','协议':'Protocol','关联论文 / 协议':'Papers / protocols','数据来源':'Data sources','查询':'Queries','论文与统计':'Papers & statistics','关闭来源信息':'Close source details','统计范围：当前文件夹的目录查询；不代表原始数据行数或实际执行次数。':'Counts cover catalog queries in this folder, not source data rows or runtime executions.','来源资料对应图册原始记录；手动修改 EAL 后，来源并不会自动证明修改后的计划。':'References describe the catalog records and do not validate manual EAL changes.','本地导入文件未关联图册来源。文件内容仅提交到本机编译器，不写入查询目录。':'Imported files have no catalog references. They are compiled locally without being saved to the catalog.',
      '画布操作':'Canvas controls','放大':'Zoom in','缩小':'Zoom out','适配全图':'Fit view','横向布局':'Horizontal layout','纵向布局':'Vertical layout','重置布局':'Reset layout','聚焦输入输出':'Focus inputs and outputs','展开画布':'Expand canvas','收起画布':'Collapse canvas','正在自动布线…':'Routing…','这个 mission 没有调用节点。':'This mission has no call nodes.',
      '节点详情':'Node details','关闭节点详情':'Close node details','输出':'Output','无上游调用输入':'No upstream inputs','未绑定返回值':'Unbound return value','未被其他调用引用':'No downstream references','调用参数':'Arguments','文件未提供独立表达式参数。':'No separate expression parameters in this file.','目标与计划元数据':'Target and plan metadata','查看 EAL 源码':'View EAL source',
      '复制源码':'Copy source','源码已复制':'Source copied','无法访问剪贴板，请选择源码复制或下载文件。':'Clipboard unavailable. Select the source to copy or download the file.','该调用没有可定位的绑定，请按 ability 名称查找。':'No binding to locate. Search by ability name.','请选择不超过 1 MiB 的 .eal 文件。':'Choose an .eal file no larger than 1 MiB.','已导入；外部修改后请重新选择文件。':'Imported. Select the file again after external edits.','无法读取文件，请重新选择。':'Unable to read file. Select it again.'
    };
    this.applyLanguage();
  }
  queryTitle(query){return this.language==='en'&&query.original_query?query.original_query.text:this.t(query.title);}
  t(value){
    if(typeof value!=='string')return value;
    if(this.language==='zh'){const translated=this.queryZh[value.trim()];return translated?value.replace(value.trim(),translated):value;}
    const trimmed=value.trim();if(this.content[trimmed])return value.replace(trimmed,this.content[trimmed]);if(this.messages[trimmed])return value.replace(trimmed,this.messages[trimmed]);
    if(/[\u4e00-\u9fff]/.test(value))for(const key of this.contentKeys)if(value.includes(key))value=value.replaceAll(key,this.content[key]);
    return value.replace(/(\d+) 个语义算子/g,'$1 semantic operators').replace(/(\d+) 个节点/g,'$1 nodes').replace(/(\d+) 条/g,'$1 queries').replace(/\b1 queries\b/g,'1 query').replace(/\b1 semantic operators\b/g,'1 semantic operator').replace(/ 论文与统计$/,' papers and statistics').replace(/ 来源与统计$/,' sources and statistics');
  }
  applyLanguage(){document.documentElement.lang=this.language==='en'?'en':'zh-CN';}
  toggle(){this.language=this.language==='zh'?'en':'zh';try{localStorage.setItem('semrel-language',this.language);}catch{}this.applyLanguage();document.dispatchEvent(new Event('atlas-language-change'));}
  localize(root){
    if(!root)return;
    const walker=document.createTreeWalker(root,NodeFilter.SHOW_TEXT);let node;
    while((node=walker.nextNode())){if(node.parentElement.closest('pre,code,[data-verbatim]'))continue;let original=this.originals.get(node);if(original===undefined){original=node.nodeValue;this.originals.set(node,original);}node.nodeValue=this.t(original);}
    for(const el of [root,...root.querySelectorAll('[aria-label],[title],[placeholder]')]){
      if(el.closest('[data-verbatim]'))continue;
      let saved=this.originals.get(el);if(!saved){saved={};this.originals.set(el,saved);}
      for(const attr of ['aria-label','title','placeholder'])if(el.hasAttribute(attr)){saved[attr]??=el.getAttribute(attr);el.setAttribute(attr,this.t(saved[attr]));}
    }
  }
}
window.AtlasI18n=new AtlasLocale();
