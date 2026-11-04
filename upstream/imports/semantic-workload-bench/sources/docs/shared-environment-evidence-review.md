# 共享环境批处理语义任务证据审查

> **本次严格目标入口：** [A–H严格审计](shared-environment-strict-index.md)。本页的“限定Strong”和排名使用较宽的历史结构口径，不代表满足静态不足、语义执行家族和20条闭合证据要求；不得计入当前15项目标。


公开数据确实存在真实案件反复适用同一政策的批处理结构。当前最直接的证据来自UDRP域名争议裁决：共享政策和解释体系、真实案件、正式决定同时存在。这个结论不等于已经证明Data Agent优于固定检索程序，也不等于已经观察到可从执行轨迹学习的中间复用层。

此前12项登记是来源可核验、可构造的开发候选，不能视为12项Strong fit。本文件详细展开十三项，另三项见医学/保险复核；最终16项限定结论、评分及完整证据索引统一见[调研交付](shared-environment-delivery.md)。没有找到15项Strong fit，不降低标准补齐数量。

## 入场审计

| 数据湖 / Benchmark | 论文 | Repository | Shared Environment E | E规模/类型 | Batch Records | N | Fixed Query | Gold | Gold类型 | Environment Necessity | 是否天然Batch | 是否公开可下载 | Verdict |
|---|---|---|---|---|---|---:|---|---|---|---|---|---|---|
| UDRP，限定回顾性救济预测 | [原论文](https://astrolavos.gatech.edu/articles/Manuscript_UDRP_final.pdf) | [完整作者归档](https://doi.org/10.5281/zenodo.16954717) | UDRP政策、细则及WIPO Overview3.0 | 官方共享解释环境152页 | 单域名案件的程序、记载事实和双方主张 | 1572 | 对给定记载材料按同一规则判断是否获得救济 | 1513获救济、59驳回 | 正式裁决，经程序提取粗标签 | **任务定义与实际引用支持**：1543案分析引用同一Overview；不是E消融结果 | 是，真实争议审理反复适用规则 | 已下载论文、完整归档、E和案文 | ✅ Strong fit，限回顾性任务；不是原始诉状预测或部署验证 |
| FrameNet1.7 | [原论文](https://aclanthology.org/P98-1013.pdf) | [完整发布包](https://raw.githubusercontent.com/nltk/nltk_data/gh-pages/packages/corpora/framenet_v17.zip) | 手册、框架/角色定义及关系 | 129页手册；清理后366949定义词 | 指定target的源文本 | 28113 targets / 101标注文档 | target→frame→角色结构 | frame及59074条角色 | 人工标注 | 框架/跨度约定依赖规范；**长规范相对短schema的必要性未确认** | 是，词典/语料人工标注 | 已下载完整包与论文；公开视图已核 | △ Partial fit |
| DrugProt | [原论文](https://upcommons.upc.edu/bitstreams/4a4e2dc2-df18-4bcd-893a-ffeadc9bf2b3/download) | [官方语料](https://zenodo.org/records/5119892)、[评分库](https://github.com/tonifuc3m/drugprot-evaluation-library) | 关系规范和13类发布范围 | 33页、9292词规范 | 给定实体的真实摘要 | 2168摘要 | 抽取化学物—蛋白关系，再生成证据清单 | 13452关系 | 人工关系标注 | 有方向、证据和粒度约定；**完整E相对短规则的作用未确认** | 是，科学文献关系标注 | 已下载论文、语料、作者库并构造 | △ Partial fit |
| AnnoCTR | [原论文](https://aclanthology.org/2024.lrec-main.103.pdf) | [作者库](https://github.com/boschresearch/anno-ctr-lrec-coling-2024) | 冻结ATT&CK定义和标注指南 | 官方URL实体1266项、112331定义词；指南939词 | 给定提及及真实CTR | 120报告；5626 MITRE链接行 | 提及→实体集合 | 专家链接URL | 人工标注导出，含重复和多目标 | 一部分可从报告表格/技术名得到；**其余E必要性未确认** | 是，CTI报告标注；不等于实际告警处置 | 已下载完整6617文件仓库及论文 | △ Partial fit，18缺KG链接等边界未闭合 |

Strong fit只评价上述明确范围的workload结构。UDRP输入已由裁决文书作者选择和概括，不能推断其等价于裁决前全部证据。前部可能泄漏结论的执行公告已按统一公开规则处理，但语义泄漏、来源选择偏差、主体隔离和全部粗标签复核仍是实验限制。[来源与构造证据](shared-environment-search-2026-09-08-round26.md)

## UDRP：真实实例与固定DAG

真实例为D2024-0001。公开输入记载域名`decathlonag2r.com`于2023-11-27注册，曾用于自称官方的Decathlon/AG2R车队网站，随后变为空白页；2024-01被投诉后，注册人提出有偿出售。商标注册时间在其前。正式决定为Transfer，任务粗标签为`RELIEF_GRANTED`。这些来自实际公开视图和独立保存的裁决，非构造案例。[正式源案件](https://www.wipo.int/amc/en/domains/search/text.jsp?case=D2024-0001)

共同E中三要件要求相似性、无权利或合法利益，以及恶意注册和使用。当前空白页不会单独决定第三要件；应结合被动持有规则及案件事实。逐案引用的专家分析只供评测侧审计，不交给运行器。[WIPO Overview3.0](https://www.wipo.int/amc/en/docs/2023_overview3.pdf)

| Query | 数据湖数据1 | 数据湖数据2 | 数据湖数据3 | 数据湖数据4 | Gold Output |
|---|---|---|---|---|---|
| 按UDRP批量判断救济 | 冻结environment.pdf | D2024-0001的§1–§5文本 | 域名/商标/注册时间等归属明确的事实 | 双方主张与程序背景 | RELIEF_GRANTED；正式Transfer |
| 生成获救济投诉清单及总数 | 同E | 全1572个案件 | 上述判断输出 | 无额外必需资源 | 源清单1513项；此为同语义任务的聚合，不算第二个独立任务 |

| 类Python DAG | 具体输入值示例 | 中间结果示例 | Gold |
|---|---|---|---|
| `cases.scan().join(public_text)` | case_e10c6ed72502db06d572 | 文本及ID，普通读取/连接 | 无新的中间人工gold |
| `facts = sem_map(attribute_facts,text)` | 注册2023-11-27、此前商标、仿冒网站与出售提议 | 时间线及事实/主张归属；语义步骤 | 示例可检查事实出处，尚无全批独立事实标签 |
| `rules = retrieve(E,facts)` | 仿冒使用后空白页 | 三要件、合法利益、被动持有的相关规则；检索与路由 | 规则检索不使用本案专家分析 |
| `decision = sem_map(apply_rules,facts,rules)` | 上述事实+规则 | 三要件/例外判断为预计内部结构；未实测 | **RELIEF_GRANTED**，关键可评分语义结果 |
| `decisions.filter(granted).project(id).count()` | 冻结decision列表 | 普通选择、投影、计数 | 全批gold count=1513 |

中间结构是方法设计，不能因为最终决定有gold，就声称每个内部要件都有独立gold。

### 四路执行推演

| 方法 | 预期结果 | 预期执行过程 |
|---|---|---|
| **LOTUS：只把关键semantic operator交给LOTUS** | 本例目标RELIEF_GRANTED；正确率未知。事实归属与例外遗漏可能影响结果 | DB扫描与文本读取→共享固定规则索引→固定事实抽取流程→将`apply_rules`交给传统sem_map→DB筛选/计数。完整E和同样检索工具可用 |
| **LOTUS：整个semantic task直接执行** | 同目标；多次调用可能传播事实抽取误差，不能预言弱于Agent | 固定DAG：sem_map事实与时间线→规则检索→sem_map三要件及例外→确定性状态校验→清单/计数。允许共享缓存、分支及批处理，不强迫每行重新读全文 |
| **Data Agent：只把关键semantic operator交给Agent** | 同目标；可能更完整检查例外，也可能多花成本而不改善 | 外层DB计划固定；给`apply_rules`提供案件和E工具；Agent查相关规则并判断，返回类型化决定/ABSTAIN；其余步骤普通执行 |
| **Data Agent：完整执行任务** | 同目标；尚无实际轨迹或优势证据 | 读取批任务→==检查共享政策结构并建立索引==→逐案提取归属与时间线→==定位适用要件及例外==→==核对空白页是否仍可能构成恶意使用==→生成决定→确定性汇总。索引可跨案保留，个案事实须重新检查 |
| **预期产生的operator structure** | 设计，非已学习产物 | `AttributedFacts`、`RegistrationTimeline`、`RelevantRuleSet(E_version)`、`UDRPReliefDecision`、`ABSTAIN`；可形成按例外类型路由的片段，但不能用当前gold编写路由 |

### 三层复用及十问

| 复用层 | 可复用内容 | 仍须逐案执行 | 最强直接对照 |
|---|---|---|---|
| Environment-only `f(E)` | 三要件、规则索引、举证责任、例外树、版本校验 | 事实是否触发规则 | 仅E编译器；可以在没有轨迹时生成大量结构 |
| Per-record `f(x,E)` | 归属抽取、时间比较、要件检查和输出schema | 事实判断、缺证据及相互矛盾的主张 | 固定检索程序、Coding Agent生成批程序 |
| Group-specific `f_g(x,E)` | 仿冒网站、被动持有、善意第三方使用等案件可能共享规则分支 | 是否属于该族、族内例外和时间事实 | 固定规则路由与缓存；必须作为同资源对照 |

| 问题 | 回答 |
|---|---|
| 1 固定q？ | 从给定记载材料判断按UDRP应否获得救济 |
| 2 共享E？ | 同版政策、细则和Overview，不为每案换环境 |
| 3 E多复杂？ | 152页共享解释材料，含证明责任、时间条件与例外；不是每案全读152页 |
| 4 records？ | 裁决文书§1–§5中记载事实、程序和双方主张；非原始诉状 |
| 5 N？ | 当前开发构造1572案，主体与近重复隔离未完成 |
| 6 gold？ | 正式Transfer/取消或驳回的粗救济结果；程序提取，8案抽查一致非全量复核 |
| 7 x为何不足？ | 仿冒、空白页等事实到救济的规范标准由E定义；1543案原分析引用同一Overview提供实际使用证据。模型可能记住规则，不代表其从未依赖规则体系 |
| 8 Agent探索什么？ | 适用章节、注册/商标时间关系、合法利益及恶意使用例外 |
| 9 哪些计算复用？ | 规则索引和路由可共享；事实归属与要件判断程序复用；具体族内分支可能重复 |
| 10 为何不是普通RAG/缓存？ | **目前没有证据排除固定RAG/编译器已足够。** 数据证明真实规则应用，不证明新执行复用机制必要 |

`1 << K << N`目前只是可检验假说：有多个法律事实类型为分组提供现实理由，但尚无轨迹统计证明K的数量、稳定性、覆盖率或新增复用价值。必须报告路由学习/验证开销，并比较同族固定程序。常量“获救济”也因1513/1572的偏斜而不可省略。

## AnnoCTR：新边界证据

相同提及和前后文可以对应多个官方目标。例如`executed macros were`在一篇报告中同时对应T1059与T1204；`SOAP`在另一篇报告中同时对应T1555与T1071。现有导出不能无条件压成单标签；集合是否表达合法多技术标注仍需与源标注过程核对。这两个例子不是已运行的Agent结果。[原件与上下文审计](shared-environment-search-2026-09-08-round215.md)

| 复用层 | AnnoCTR候选结构 | 当前证据边界 |
|---|---|---|
| E-only | 定义索引、别名表、类型约束 | 已有1266官方实体定义；固定RAG直接覆盖大量工作 |
| 每条程序 | 候选召回→上下文消歧→实体集合 | 可能是普通实体链接，不自动构成Agent必要性 |
| 分组复用 | 协议通信、宏执行、凭据行为可能重复选用相邻定义 | 未测重复路由、K或因果收益；类别标签频数不是执行结构频数 |

## 科学标注与事件抽取：四项进一步审查

以下四项有实际共享规范、人工标注和稳定批任务，但没有直接实验排除短规范、固定检索或已学习的分类器足以完成任务。因此当前均为Partial fit。这个评级不否认来源可构造，也不把尚未验证的环境必要性写成反证。

| 数据湖 / Benchmark | 论文 | Repository | Shared Environment E | E规模/类型 | Batch Records | N | Fixed Query | Gold | Gold类型 | Environment Necessity | 是否天然Batch | 是否公开可下载 | Verdict |
|---|---|---|---|---|---|---:|---|---|---|---|---|---|---|
| GENIA Meta-Knowledge | [原论文](https://doi.org/10.1186/1471-2105-12-393) | [完整官方包](https://www.nactem.ac.uk/meta-knowledge/Meta-knowledge_GENIA_corpus.zip) | 元知识protocol、属性适用与传播规则 | 包内66页；规则主要在13–48页，后部含UI | 给定事件图中的事件及完整摘要 | 35587事件 / 968摘要 | 事件→五维元知识→高强度当前证据清单 | 五维属性；派生选中1000事件 | 两层分离的人工标注 | 传播/跨句来源由规范定义；完整规则相对短版增益未确认 | 是，文献事件元知识标注 | 原论文、完整2036成员发布包及开发视图已核 | △ Partial fit |
| SENTiVENT | [原论文](https://doi.org/10.1007/s10579-021-09562-4) | [完整数据](https://huggingface.co/datasets/GillesJacobs/sentivent/tree/6a9e8f9fc11ba7db3d8dffe3e5df9e7b062e6441)、[指南源码](https://github.com/GillesJ/sentivent-event-annotation-guidelines) | 事件、参数、canonical reference规范 | 原69页中52页规范正文，124321字符 | 完整商业新闻 | 282篇 | 全文→事件及canonical参数 | 6111事件、13535参数 | 人工原始XMI与发布JSON对齐 | §4.3决定参数跨度；与普通指称解析/短schema相比的E增益未确认 | 是，新闻事件整理 | 原论文、完整作者数据/指南库已下载 | △ Partial fit |
| CASIE | [原论文](https://ebiquity.umbc.edu/get/a/publication/1312.pdf) | [作者库](https://github.com/Ebiquity/CASIE/tree/2c8beef56d48e8de6599891c6a5e0e5f0d82e20c) | 五类事件、角色、realis约定 | 作者论文28个相关页、5529词；非178页全文 | 完整网络安全新闻 | 991篇 | 事件及角色抽取；可另评realis | 8380事件、22471参数；realis有1个无效源标签 | 基础人工标注，排除自动CAPEC/子类 | 角色/窗口规则有用；五类任务可能被短schema覆盖 | 是，事件语料标注；非告警处置 | 完整作者库、论文及规范来源已下载 | △ Partial fit |
| STREUSLE/SNACS | [原论文](https://aclanthology.org/P18-1018.pdf) | [作者库](https://github.com/nert-nlp/streusle) | SNACS v2.6关系与构式规则 | 114页、34662词；包括参考和例子 | 给定语义目标及完整评论 | 5476目标 / 720评论 | 目标→role/function二元组 | 5476对，1837对不同 | 人工标签，官方评分及错误探针已核 | 角色/词汇作用区分依赖约定；完整指南增益未测 | 是，评论语义标注；非保险审批 | 原论文、完整77文件库、绑定指南已下载 | △ Partial fit |

### Query及实例

| Query | 数据湖数据1 | 数据湖数据2 | 数据湖数据3 | 数据湖数据4 | Gold Output |
|---|---|---|---|---|---|
| GENIA元知识 | 完整摘要 | 给定E19事件及Theme/Cause图 | 66页protocol | 摘要其他句用于Source判断 | Fas mRNA约10倍诱导例：Observation/L3/Positive/High/Current |
| GENIA筛当前高强度肯定事件 | 上述五维预测 | 固定字段条件 | document/event ID | 无额外输入 | 本例true；全开发集1000项；不是独立实验数量 |
| SENTiVENT事件及canonical参数 | aal00完整新闻 | §4.3指称规范 | 参数角色定义 | 公开不提供原共指链 | “The company”[266:277]对应明确公司[90:122] |
| CASIE事件及角色 | 2075新闻正文 | 五类事件定义 | 合法参数角色 | span坐标规范 | access[323:329]→Databreach；敏感数据→Compromised-Data |
| CASIE事件realis | 相同全文和事件输入契约 | Actual/Generic/Other定义 | 事件上下文 | 上游预测事件；给定gold事件须另列诊断 | 上例Other，不入Actual清单 |
| SNACS角色/作用 | reviews-003418-0003的My | 完整评论/目标token1 | SocialRel与Gestalt定义 | 所有格与合法标签约束 | SocialRel/Gestalt；应入差异清单 |

上述实例均来自已检查的真实数据，属于开发暴露；完整原件和构造/评分收据分别见[GENIA53](shared-environment-search-2026-09-08-round53.md)、[SENTiVENT60](shared-environment-search-2026-09-08-round60.md)、[CASIE70](shared-environment-search-2026-09-08-round70.md)、[STREUSLE171](shared-environment-search-2026-09-08-round171.md)。

### 固定DAG与关键可评分节点

| 类Python DAG | 具体输入值示例 | 中间结果示例 | Gold |
|---|---|---|---|
| `papers.scan().join(given_events).sem_map(meta,E).filter(criteria).groupby(paper)` | GENIA E19、10倍诱导 | 五维标签是**依赖E的语义节点**；join/filter/groupby为普通算子 | 五维人工标签；selected=true |
| `news.scan().sem_map(events_and_canonical_roles,E).explode().filter(SecurityValue)` | SENTiVENT The company与前文明示公司 | 事件发现、角色分派、指称解析为语义计算；规范决定返回canonical跨度 | 同湖6111事件、13535参数；SecurityValue720项 |
| `news.scan().sem_map(events_roles,E).explode().sem_map(realis,E).filter(Actual)` | CASIE access及敏感数据 | 两个可分别检验的语义输出，抽取错误必须计入端到端质量 | Databreach/Other；不入Actual清单 |
| `reviews.join(targets).sem_map(role_function,E).filter(role!=function)` | SNACS My token1 | 语义输出SocialRel/Gestalt；字段比较无需LLM | 差异清单包含本例；全批1837 |

### 四路推演：GENIA

| 方法 | 预期结果 | 预期执行过程 |
|---|---|---|
| LOTUS关键算子 | E19目标五维标签及true，未实测 | 普通DB连接给定图→固定上下文/规范检索→sem_map五维→确定性筛选；不把人工事件图算模型成果 |
| LOTUS整个语义任务 | 同目标；默认标签偏斜可能使简单程序很强 | 按摘要批量读取事件图→固定传播/适用规则→联合标注→范围校验→清单。允许一次编译规则与图遍历程序 |
| Agent关键算子 | 同目标；收益未知 | 在元知识节点内访问完整摘要、给定图和规范→返回五字段；外层DB计划不变 |
| Agent完整任务 | 同目标；未有轨迹或成本数据 | ==建立KT与其他维度适用表==→按摘要读取图→==核嵌套事件范围和跨句Source==→标五维→确定性筛选/汇总 |
| operator structure | 候选设计 | `KTResolver`、`DimensionApplicability`、`EventScopePropagation`、`SourceResolver`。多数规则可由E-only编译，不自动证明单轨迹有增量 |

### 四路推演：SENTiVENT

| 方法 | 预期结果 | 预期执行过程 |
|---|---|---|
| LOTUS关键算子 | canonical跨度[90:122]为目标，未实测 | DB提供全文→固定事件候选/规范检索→把canonical参数解析交给sem_map→span校验 |
| LOTUS整个语义任务 | 同事件/角色目标；误差来源为漏事件、角色和指称 | 固定事件抽取→角色分派→指称解析→factuality→JSON校验→类型过滤。固定程序可完整处理跨句上下文 |
| Agent关键算子 | 同目标，无优势预设 | 在角色解析节点查规范并读取前文；返回canonical span，其他算子照常运行 |
| Agent完整任务 | 同目标；多步不必然更好 | ==按事件类型查角色和跨度规则==→定位trigger→==读取前文并按§4.3确认明确指称==→检查否定/确定性→输出/聚合 |
| operator structure | 候选设计 | `EventSchemaDispatcher → RoleMapper → CanonicalReferenceResolver → SpanValidator`；schema分派可静态恢复 |

### 四路推演：CASIE

| 方法 | 预期结果 | 预期执行过程 |
|---|---|---|
| LOTUS关键算子 | access→Other为目标，未实测 | 固定事件/角色流程→realis sem_map→确定性Actual筛选 |
| LOTUS整个语义任务 | 同样目标，可能受五类短schema基线挑战 | 同E全文→事件及论元抽取→realis分类→校验与汇总；不给自动CAPEC结果 |
| Agent关键算子 | 同目标 | 在realis节点查定义与正文范围，返回合法枚举/ABSTAIN |
| Agent完整任务 | 同目标；无成本收益证据 | ==查事件定义及合法角色==→提取→==核具体发生、一般描述或不确定范围==→输出→筛选 |
| operator structure | 候选设计 | `TypedEventExtractor + RoleConstraintCheck + RealisClassifier`；原General标签不能硬并入其他类 |

### 四路推演：SNACS

| 方法 | 预期结果 | 预期执行过程 |
|---|---|---|
| LOTUS关键算子 | My→SocialRel/Gestalt目标，未实测 | DB连接给定目标→固定构式/定义检索→二元sem_map→合法对校验 |
| LOTUS整个语义任务 | 同目标；可能普通条件分类已足够 | 评论→固定目标上下文→关系与作用联合映射→约束检查→差异清单；省去不必要的Agent聚合 |
| Agent关键算子 | 同目标 | 仅在二元映射中使用规范查阅工具，返回role/function |
| Agent完整任务 | 同目标；未观察到执行族 | ==查所有格构式与SocialRel/Gestalt==→==核role专用约束==→输出→普通字段比较和groupby |
| operator structure | 候选设计 | `ConstructionRouter + PairLabeler + LegalityValidator`；约束库属于E-only复用，不能当轨迹提取成果 |

### 三层复用对照

| 湖 | Environment-only | Per-record program | Group-specific候选 | 实证边界与最强反例基线 |
|---|---|---|---|---|
| GENIA | 属性schema、适用/传播表 | 事件图遍历、局部范围与来源判断 | 嵌套调节、推测分析、既有事实引用等分支 | 有规则动机，无K/轨迹统计；固定图程序+短规范或E-only编译可能足够 |
| SENTiVENT | 类型/角色及canonical约定 | 事件识别、参数/指称解析 | 证券变化、交易/雇佣等事件族 | 类型族不是已证执行族；固定schema分派+成熟指称解析可能胜出 |
| CASIE | 五类schema、窗口与realis规则 | 抽取、角色和realis映射 | 泄漏/钓鱼/漏洞/补丁等流程 | 仅五类可能过于简单；固定多阶段程序是必须比较的对照 |
| SNACS | 关系层级、合法role/function对、构式索引 | 语境映射到二元标签 | 所有格、路径/地点、施事/工具等构式 | 可能就是固定分类器分支；未知是否满足1≪K≪N及净收益 |

### 十问逐项核对

| 问题 | GENIA | SENTiVENT | CASIE | SNACS |
|---|---|---|---|---|
| 1 固定q | 标五维事件元知识 | 提取事件及canonical参数 | 提取事件/角色，可附realis | 标场景role和词汇function |
| 2 共享E | 同版元知识protocol | 同版事件规范 | 同版事件schema/规则 | SNACS2.6指南 |
| 3 复杂规模 | 66页，含UI非全必要 | 52页规则正文 | 28页5529词 | 114页34662词非全必要 |
| 4 x | 给定事件+完整摘要/图 | 一篇完整新闻 | 一篇完整新闻 | 给定target+评论 |
| 5 N | 35587事件/968摘要 | 282篇 | 991篇 | 5476目标/720评论 |
| 6 y | 五个人工属性 | trigger、角色、canonical spans | 类型/角色/realis；后者1无效值 | 人工role/function对 |
| 7 x单独为何不足 | 标签、传播和适用约定来自E；长E不可替代性未证 | canonical边界由E约定；短规则充分性未测 | 类型角色约束由E规定；可能短schema足够 | 双层角色约定由E规定；长指南增益未测 |
| 8 探索 | KT、范围、嵌套、来源 | 类别、角色、前文指称 | 类型、参数窗口、realis | 构式、关系定义、合法组合 |
| 9 复用 | 属性适用及图分支 | schema和指称解析程序 | 类型分派与角色校验 | 构式分派与合法对检查 |
| 10 非普通RAG/分类/缓存证据 | 尚无排除固定程序的证据 | 尚无；必须与完整上下文固定流程比较 | 尚无，五类schema尤其易静态实现 | 尚无，条件分类是强对照 |

四项均不提供轨迹复用收益的现成证据。它们适合检验并可能否定该假设，不应先把预期operator结构视为研究结论。

## 论证和话语结构：五项进一步审查

这些来源把真实文本转换为协议定义的结构，适合研究图构建和论证分析。它们尚未证明完整长规范不可由短规则替代，更没有证明必须让Agent逐记录探索环境。话语关系的多种过滤是同一构图任务的投影，不能算新增独立湖。

| 数据湖 / Benchmark | 论文 | Repository | Shared Environment E | E规模/类型 | Batch Records | N | Fixed Query | Gold | Gold类型 | Environment Necessity | 是否天然Batch | 是否公开可下载 | Verdict |
|---|---|---|---|---|---|---:|---|---|---|---|---|---|---|
| GUM/eRST | [GUM论文](https://gucorpling.org/amir/pdf/GUM_paper_prepub.pdf)、[eRST论文](https://aclanthology.org/2025.cl-1.3.pdf) | [完整作者库](https://github.com/amir-zeldes/gum/tree/22fdf87f9c71c96bcc771461d06e689b1f90020d) | GUM话语规范、结构图及RST分段参考 | GUM页面约6396词含UI；参考分段8634词；不能把论文全文计E | 真实文本/转录，给定token及源speaker/版式 | 142文档 | 构建主树/次边并查询关系 | 19271 EDU、17890 group、896次边 | 人工话语结构；其他自动层不作gold | speaker与分段约定有明确作用；长E增益未测 | 是，持续语料标注 | 原论文、完整6843 blobs库及资源已下 | △ Partial fit |
| AAEC | [原论文](https://aclanthology.org/J17-3005.pdf) | [官方发布](https://tudatalib.ulb.tu-darmstadt.de/items/9177c48c-8bd5-4881-9cb4-0632b5941464) | 成分/边界、关系与stance规范 | 31页11171词 | 完整作文与原prompt | 397篇 | 构造论证图与claim stance | 6007成分、3781关系、1486 stance | 人工BRAT | 边界与stance约定依赖E；短schema是否足够未知 | 是，作文论证标注 | 原论文、完整官方包/扩展库已下 | △ Partial fit |
| UKP web discourse | [原论文](https://aclanthology.org/J17-1004.pdf) | [作者库](https://github.com/UKPLab/emnlp2015-ih-ig)、[官方包](https://tudatalib.ulb.tu-darmstadt.de/items/d4a7ac0c-e7a8-466a-855a-917e42a24342) | P1/P2规则及历史争议例 | 11477词相关段，不借Toulmin章节凑长度 | 正文/title/topic | 889唯一非空文档 | 是否进入后续论证分析 | 456 P1、433 P2 | 人工多数票 | 无总体立场的双边论据也P1；该例外或可短规则表达 | 是，协议筛选真实帖子 | 已取得原论文、完整库/发布及开发视图 | △ Partial fit |
| PersianRST | [原论文](https://arxiv.org/pdf/2106.13833) | [作者库](https://github.com/hadiveisi/PersianRST) | 87页参考手册+论文波斯语适配 | 26235词；给定EDU不借分句配价材料 | 给定人工EDU的真实新闻 | 146篇 / 5643 EDU | 构造RST关系与依附 | 11097原生边，其中3641 span | 人工RS3 | 标签/核规则依赖约定；适配偏好未完全形式化，E充分性仍有缺口 | 是，新闻话语标注 | 原论文、完整152文件库/手册已下 | △ Partial fit |
| PCC | [原论文](https://aclanthology.org/2020.lrec-1.133.pdf) | [完整官方2.2包](https://angcl.ling.uni-potsdam.de/resources/pcc2.2.zip) | PCC手册RST章及标题约定 | RST约40页；非全书234页 | 给定EDU的真实评论 | 141篇 / 2410 EDU | 构建RST并生成理由清单 | 4065边，其中1498 span | 人工RST；摘要另有人工标注 | 标题/关系约定明确；版本冲突文档已排；长E及RST对摘要增益未测 | 是，评论标注 | 完整源、论文、手册及摘要作者库已下 | △ Partial fit |

### Query与具体数据

| Query | 数据湖数据1 | 数据湖数据2 | 数据湖数据3 | 数据湖数据4 | Gold Output |
|---|---|---|---|---|---|
| GUM构造eRST图 | 142篇token化文本/转录 | 5993个公开结构元素及speaker字段 | 同版话语规范与分段规则 | 无当前EDU/关系标签 | 主树与896次边；归因投影1283、证据565、条件284 |
| AAEC论证图 | essay001完整文本 | 写作prompt | shell language与组件/关系规则 | span坐标契约 | T4[716:851]支持T3[591:714]；T3为Claim/For |
| AAEC反主立场claim清单 | 同397作文 | 上游预测论证图 | stance规则 | 不把题目观点当作者观点 | 274 Against；不是217 attacks关系的同义项 |
| UKP筛选 | 源1025与1220的正文/title/topic | §3.3.1例外与P1/P2协议 | 历史规范争议例 | 不含当前多数票标签 | 1025 false；1220 true；全批456 true |
| PersianRST图构建 | etemad001全文的原波斯语EDU | 参考定义+适配 | EDU顺序 | 人工分句显式给定 | EDU2→EDU1/explanation，结构边另列 |
| PCC理由图 | maz-19372的EDU7/8与完整评论 | Reason/Evidence/Justify规则 | 标题独立约定 | 给定分句 | 8→7/reason |
| PCC摘要排序，待对齐 | 同141篇全文/句子 | 预测RST图 | 短摘要排序说明 | [独立摘要标签](https://github.com/fhewett/pcc-summaries) | 每文3句排序，尚未证明图是必要输入 |

GUM旧示例GUM_news_sensitive尚未确认属于142篇选择范围，故不把它当本视图实测例。其他具体例的原文/源标签已在对应卡片实际检查： [GUM74](shared-environment-search-2026-09-08-round74.md)、[AAEC77](shared-environment-search-2026-09-08-round77.md)、[UKP81](shared-environment-search-2026-09-08-round81.md)、[PersianRST180](shared-environment-search-2026-09-08-round180.md)、[PCC184](shared-environment-search-2026-09-08-round184.md)。上述表述不是模型预测。

### DAG和可评分边界

| 类Python DAG | 具体输入值示例 | 中间结果示例 | Gold |
|---|---|---|---|
| `docs.scan().sem_map(parse_erst,E,source_structure).explode(edges).filter(relation)` | GUM转录的speaker/token/布局 | 分段、主树及次边是语义输出；结构检查/过滤为普通程序 | EDU和图可对照源gold；不同relation过滤不算新任务 |
| `essays.join(prompts).sem_map(argument_graph,E).explode(relations).filter(attacks)` | AAEC T4对T3 | 论证关系支持而非反驳；普通filter不选该边 | supports；全批attacks217 |
| `docs.sem_filter(P1_under_protocol,E).project(id).count()` | UKP1025/1220 | 正文是否符合协议为关键语义节点 | false/true，count456 |
| `given_edus.groupby(doc).sem_map(parse_rst,E).explode(edges).filter(explanation)` | Persian etemad001 | 依附与关系标签；人工EDU不是模型抽取成果 | 2→1/explanation |
| `given_edus.groupby(doc).sem_map(parse_rst,E).filter(reason)` | PCC maz-19372 | 保留独立标题，判断正文关系 | 8→7/reason |
| `docs.join(predicted_rst).sem_map(rank_sentences).topk(3)` | 同PCC全文+预测图 | 排名语义节点；topk为普通操作 | 独立摘要排序；无图摘要对照不可省略 |

### 三层复用与最强直接对照

| 湖 | Environment-only | Per-record program | Group-specific候选及仍须逐条处理 | 主要风险 / 最强baseline |
|---|---|---|---|---|
| GUM | 分段、attachment、关系规则和图约束 | 按源speaker/结构构图 | 同speaker应答、归因、列表可能走不同分支；具体边仍需文本判断 | 固定解析流程可直接利用相同结构；源转录信息不是Agent感知增益 |
| AAEC | 组件/关系schema、shell排除规则 | 边界→成分→边→stance | 让步反驳、理由链、隐含主张可能共享程序 | 少类型论证parser或短schema+固定流程可能足够 |
| UKP | P1/P2和双边论据例外、示例索引 | 整篇协议分类 | 双边论述、单纯推荐资料、立场加理由等族；主题相关性需逐篇判断 | 短规则编译最可能消除长E成本；K可能太小 |
| PersianRST | 粗关系及核/卫星约定 | 给定EDU的依附/关系推断 | 解释、并列、背景等结构模板 | 适配优先级不完整；固定RST模型/规则检索是强对照 |
| PCC | 标题独立、关系区分及结构校验 | RST构图，可另做摘要 | 理由链、转折、论据层级可能复用；排序仍需全文 | 直接全文摘要可能不需RST；不能用独立摘要gold证明中间图价值 |

所有族均为语料/规范提供的动机，不是实际轨迹聚类结果。这里没有测得K，也没有证明族路由优于E-only生成的固定分支。对Partial任务可以据此设计实验，不能据此提高入场级别。

### 十问逐项核对

| 问题 | GUM | AAEC | UKP web | PersianRST | PCC |
|---|---|---|---|---|---|
| 1 固定q | 全文构造eRST图 | 作文构造论证图/stance | P1/P2协议筛选 | 给定EDU构造RST | 给定EDU构造RST |
| 2 E | GUM规范+分段参考 | 作者论证规范 | P1/P2规范与争议例 | 参考手册+波斯适配 | PCC RST章 |
| 3 规模 | 6396词网页含UI+8634词分段 | 31页11171词 | 11477词相关段 | 87页26235词 | 约40页RST章 |
| 4 x | token/结构/speaker文本 | 全作文和prompt | 正文/title/topic | 原始EDU文本及顺序 | 原始EDU含标题 |
| 5 N | 142文档 | 397作文 | 889文档 | 146新闻 | 141评论 |
| 6 y | EDU、主图及次边 | 成分/边/stance | 人工多数票P1/P2 | 原生依附及关系 | 原生RST；摘要另层待对齐 |
| 7 x不足原因 | 分段/attachment规范约定；长E仍未证 | 边界/stance约定；长E仍未证 | 特定P1语义区别普通说服性；或可短规则表达 | 核/关系约定；适配尚有未形式化部分 | 标题/关系约定；完整E必要性未证 |
| 8 Agent探索 | speaker条件及attachment规则 | shell、角色、主立场 | 双边论据例外与主题 | 关系定义和核选择 | Reason/Evidence及标题 |
| 9 复用 | 图约束、结构分支 | 组件schema、论证链流程 | 例外路由/规则索引 | 关系分派与结构校验 | 关系边界与标题处理 |
| 10 排除普通RAG等？ | 没有，需强固定parser | 没有，需固定论证pipeline | 没有，短分类规则尤强 | 没有，固定RST强对照 | 没有，尤其直接摘要可能足够 |

原料许可也不相同：AAEC/UKP有研究与再分发限制，PersianRST为非商业，PCC语料CC BY-NC-SA与手册权利分开，GUM按源处理。已公开可下载不等于可以重新发布整个组合包。

## FrameNet与DrugProt：补齐真实实例和四路比较

这两项仍为Partial。以下实际输入在本轮再次打开核对：[FrameNet公开文档](../data/shared-environment-audit-20260908-v201/view/public/documents.jsonl)、[DrugProt doc_0000](../data/shared-environment-audit-20260908-v130/inspection-v1/public/records/doc_0000.json)。源gold只用于本研究审计，不能给被测系统。此前全量源一致性与评分诊断分别见[FrameNet验证](../artifact/evidence/shared-environment-audit-20260908-v201/verification.json)、[DrugProt诊断](../artifact/evidence/shared-environment-audit-20260908-v131/checks.json)，不是LLM结果。

FrameNet真实句子为“Your contribution to Goodwill will mean more than you may know .”。给定target为`contribution[5:17]`，源gold为Giving，Donor=`Your[0:4]`，Recipient=`to Goodwill[18:29]`。不能把介词删掉只返回Goodwill，也不能补出源gold没有标注的Theme。同句know的Content=DNI，不等于模型未完成。

DrugProt真实摘要说明human type 12 RDH将dihydrotestosterone还原为androstanediol。给定T1是产物androstanediol，T9是该蛋白；源gold仅`(T1,T9,PRODUCT-OF)`。给定3个化学实体和10个基因实体，产生30个候选对；不能因为正文提到底物，就擅自增加未给定实体的关系。这里是给定实体的文献整理，不是临床治疗判断。

| Query | 数据湖数据1 | 数据湖数据2 | 数据湖数据3 | 数据湖数据4 | Gold Output |
|---|---|---|---|---|---|
| FrameNet目标框架及角色抽取 | 28113条target跨度 | 101篇有目标标注文档及完整句上下文 | 1221框架/角色定义、13631词汇单元定义 | 同版129页手册、关系和语义类型 | 示例Giving；Donor/Recipient跨度；全批59074角色 |
| Giving清单 | 同一target关系 | 预测frame | 同环境 | 普通过滤/计数 | 57条；同任务下游不增加湖数 |
| 隐式角色类型统计 | 同一target和上下文 | 预测角色 | DNI/INI/CNI/INC源约定 | 保留原rank/itype | 8272隐式角色；不是8272独立文档 |
| DrugProt关系证据索引 | 2168摘要全文 | 61730给定实体及跨度 | 33页9292词规范 | 13种发布关系范围 | 13452关系；145个多标签对 |
| 产物 / 抑制证据清单 | 上述预测关系 | 实体提及ID | 文献ID | 普通类型过滤 | PRODUCT-OF 807条；INHIBITOR 4420条 |

| 类Python DAG | 具体输入值示例 | 中间结果示例 | Gold |
|---|---|---|---|
| `targets.join(sentences).sem_map(resolve_frame,E)` | contribution[5:17] | 给定目标的语义消歧 | Giving |
| `targets.join(predicted_frames).sem_map(extract_roles,E).explode()` | 该句和预测Giving | 按角色规则判断跨度，不给gold frame | Donor[0:4]、Recipient[18:29] |
| `frames.filter(name=='Giving').project(id).count()` | 全28113个预测 | 普通关系操作 | 57个正确ID，而非仅count相同 |
| `docs.join(entities).sem_map(extract_relations,E).explode()` | doc_0000，3×10候选对 | 产物与底物方向、证据有效性为语义判断 | (T1,T9,PRODUCT-OF) |
| `relations.filter(type=='PRODUCT-OF').project(doc,arg1,arg2)` | 全批预测关系 | 普通filter/project | 807条具体关系 |

join、explode、过滤和计数为普通算子；frame、角色、关系推断为依赖规范的语义算子。端到端角色评测使用预测frame；给gold frame仅可作为单独标注的oracle诊断。

### FrameNet四路推演

| 方法 | 预期结果 / 风险 | 预期执行过程 |
|---|---|---|
| LOTUS关键operator | 目标Giving及原角色跨度，实际未测；可能漏介词或隐式角色 | 普通target/context join→固定候选和规则检索→语义节点判定→结构校验→普通聚合 |
| LOTUS完整任务 | 可与Agent相同或更好，不能从E长度预言失败 | 一次建立E索引→固定frame消歧→角色映射→保留rank及itype→清单统计；允许同工具补读 |
| Agent关键operator | 同gold目标；更宽检索是否改善未测 | 固定外层→==检查contribution候选词义及Giving定义==→==核角色跨度规则==→返回结构化结果 |
| Agent完整任务 | 目标完整28113条结果；预算、覆盖及错误传播未测 | ==核同版词典和手册==→共享索引→逐target==查候选区别及角色约束==→==必要时补读文档消解省略==→输出并聚合 |
| 可能的operator | 未从轨迹提取 | `FrameResolver(E_digest) → RoleMapper(frame_schema) → LayerValidator`；null类别独立于ABSTAIN |

### DrugProt四路推演

| 方法 | 预期结果 / 风险 | 预期执行过程 |
|---|---|---|
| LOTUS关键operator | 示例目标PRODUCT-OF，实际未测；可能反向或把共现当关系 | 普通实体候选生成→固定规范检索→关系语义调用→ID/类型校验→普通过滤 |
| LOTUS完整任务 | 目标13452条关系集合；允许多标签，不假定比Agent差 | 一次解析13类契约→逐摘要关系抽取→给定实体allowlist与集合校验→证据清单/聚合 |
| Agent关键operator | 同目标；无法凭探索补造缺失给定实体 | 固定外层→==查PRODUCT-OF方向和证据规则==→==对照摘要产物/底物表述==→输出原实体ID关系 |
| Agent完整任务 | 是否降低方向、间接调节等错误未测 | ==检查规范版本、13类范围和多标签约定==→逐篇==定位候选关系证据==→==核直接/间接、否定和方向条款==→输出全部关系及状态→普通过滤 |
| 可能的operator | 未从轨迹提取 | `EvidenceLocator → RelationSetMapper → GivenEntityValidator`，每文集合输出，允许多标签和显式ABSTAIN |

上述“核”指可观察的文档查阅/证据校验，不是私人思维链。所有方法应获得相同必要输入、公开工具、缓存及预算条件；不能强制Agent每条重读全部E，也不能禁止静态流程索引规则。

### 三层复用及十问

| 湖 | Environment-only | Per-record | Group-specific假设 | 能否排除更简单方法 |
|---|---|---|---|---|
| FrameNet | 词义候选索引、frame/role约束图、跨度规范 | 消歧、逐句角色映射、结构校验 | 同frame角色布局、同省略类型的检查程序；实际文本跨度仍逐条处理 | 不能。E-only编译器可能恢复同样路由；796种gold frame不是测得的K |
| DrugProt | 13类方向/定义、实体与多标签契约 | 每篇找证据、判关系、检查引用 | 代谢产物、抑制、间接调节等证据检查族 | 不能。13标签不是13种已观察执行程序；短schema+固定抽取可能足够 |

| 问题 | FrameNet | DrugProt |
|---|---|---|
| 1 固定q | 给定target预测框架与角色结构 | 给定实体提取化学物—蛋白关系集合 |
| 2 E | 同版词典、角色/关系定义和手册 | 关系标注规范及发布类别范围 |
| 3 规模 | 129页手册、366949清理定义词 | 33页9292词、13种关系 |
| 4 x | 给定target及源文档文本 | 摘要全文及给定实体跨度 |
| 5 N | 28113targets，101个有目标文档 | 2168摘要；关系不是独立样本 |
| 6 y | 人工frame、角色跨度/rank/隐式类型 | 人工实体ID关系集合 |
| 7 为何x不足 | 规范决定框架、边界和省略类别；完整E必要性未确认 | 规范决定方向/粒度/多标签；完整E必要性未确认 |
| 8 探索 | 候选frame、角色约束、跨度与省略规则 | 产品/底物、直接/间接证据和方向规则 |
| 9 复用 | 索引、schema及角色检查程序；族复用待测 | 规则索引、证据模式和关系检查程序；族复用待测 |
| 10 超越普通RAG/分类？ | 未证明；固定检索+结构化语义标注是强基线 | 未证明；短schema条件关系抽取是强基线 |

## 后续排名的计分契约

采用7项各0—4分的证据评分，再以权重`(0.15,0.10,0.15,0.25,0.10,0.15,0.10)`加权：E复杂度、批量、gold质量、E必要性、语义算子潜力、复用潜力、真实性。总分范围0—4。未确认项目填“未确认”，不把未知当0，也不填一个看似精确的总分。计分权重是分析约定，不是实验结果。

E必要性未确认的候选不能因其他项高而升为Strong。复用潜力分须区分来源动机、实际轨迹重复与独立摊销收益；当前没有任何本报告候选达到后两级证据。[16项评分与五个验证对象](shared-environment-ranking.md)已给出各维度、未知区间、真实实例和最强基线；它包括[医学与保险复核](shared-environment-domain-recheck219.md)的3项。这个验证顺序不是五个合格workload排名，也不是全部历史来源的最终清点。

## 当前核心判断

**真实共享环境批任务存在。** UDRP的重复规则适用有直接来源依据；科学标注和知识库链接则提供不同程度的候选，但部分可能退化为短规则条件分类或普通RAG。

**比环境预处理和逐记录程序更有价值的中间复用层尚未被证明。** 规则例外和相邻概念提供分组理由，未提供学习后优于环境编译、固定路由、Coding Agent的证据。下一阶段应同时保留这个否定可能，避免先建机制再挑任务。

## 来源与核验材料

1. [UDRP原论文](https://astrolavos.gatech.edu/articles/Manuscript_UDRP_final.pdf)、[作者归档](https://doi.org/10.5281/zenodo.16954717)、[官方环境](https://www.wipo.int/amc/en/docs/2023_overview3.pdf)；[26轮构造与限制](shared-environment-search-2026-09-08-round26.md)。
2. [FrameNet原论文](https://aclanthology.org/P98-1013.pdf)、[完整1.7包](https://raw.githubusercontent.com/nltk/nltk_data/gh-pages/packages/corpora/framenet_v17.zip)；[201轮逐项源核验](shared-environment-search-2026-09-08-round201.md)。
3. [DrugProt原论文](https://upcommons.upc.edu/bitstreams/4a4e2dc2-df18-4bcd-893a-ffeadc9bf2b3/download)、[官方语料](https://zenodo.org/records/5119892)；[131轮评分与边界](shared-environment-search-2026-09-08-round131.md)。
4. [AnnoCTR论文](https://aclanthology.org/2024.lrec-main.103.pdf)、[官方仓库](https://github.com/boschresearch/anno-ctr-lrec-coling-2024)；[213](shared-environment-search-2026-09-08-round213.md)、[214](shared-environment-search-2026-09-08-round214.md)、[215](shared-environment-search-2026-09-08-round215.md)轮原文/实体/字段审计。
