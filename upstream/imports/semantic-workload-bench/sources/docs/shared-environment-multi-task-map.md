# 同一数据湖的多个批处理任务：目标更新后的核验表

用户最新偏好：一个数据湖最好支持多个目标批处理任务。十五个独立数据湖的总目标保持不变；同湖语言、标注层、查询变体均不增加湖数。本表重新读取已构造private gold核对原生标签覆盖；新增任务视图尚未单独冻结/运行，不自动成为新合格workload。

## 已核验来源中的任务组合

| Query | 数据湖 数据1 | 数据湖 数据2 | private gold及数量 |
|---|---|---|---|
| SENTiVENT：从公司新闻构造事件类型/子类型索引，定位并购、用工与证券价格事件 | 同一冻结规范第3–6章，52页摘录 | 同282真实全文 | 6111事件；其中并购173、用工239、SecurityValue720；这些是同一类型抽取任务的三个查询，不算三个语义任务 |
| SENTiVENT：把事件论元归到正确角色与规范指称，建立公司—事件索引 | 同规范的角色定义和canonical reference规则 | 全文与给定事件触发词；此新增视图必须明确annotation-given事件，不提供论元gold | 13535带角色的canonical argument；不同于只抽事件类型 |
| SENTiVENT：标记事件是否被否定、是否带模态，供事实表述与预测表述分流 | 同规范模态/否定章节 | 全文与给定事件库存 | modality true721/false5390；negated true157/false5954。不是现实中“发生/未发生”的gold |
| GENIA-MK：把生物医学事件按研究信息性质归类，构造观察/分析/方法索引 | 同66页原protocol及其类别/组合约束 | 968摘要与明确给定的基础事件图 | 35587事件；KT Observation12308、Analysis6366、Method923等 |
| GENIA-MK：区分当前研究与其他研究的事件来源，防止把被引用发现归给本研究 | 同protocol的跨句来源与嵌套传播规则 | 同摘要上下文及基础事件图 | Source Current35054、Other533；不能只靠当前事件句分类 |
| GENIA-MK：标记确信程度、否定与强度，输出高强度可靠观察清单 | 同protocol关于certainty、polarity、manner的差异及传播 | 同完整必要输入 | CL L1=725/L2=2166/L3=32696；Negative2199；Manner High1349/Low303；原联合筛选selected1000 |

UDRP/WIPO目前只确认原决策任务；没有独立要素级gold依据前，不补造“恶意/混淆/合法利益”三个任务来凑数。MAVEN多关系层、UMR句子/文档图是多任务潜力，但尚未通过来源资格缺口，不移入上表合格来源。

| 类python的DAG | 具体数值/状态 |
|---|---|
| `events=sem_map(news, event_schema); filter(events,type in query_types)` | SENTiVENT 282文档→6111事件；多个type筛选只是一个语义节点的不同消费查询 |
| `arguments=sem_map(news,given_events,role_and_reference_rules); groupby(company)` | 同湖13535原生论元标签；新增given_events公开视图尚未单独构造 |
| `status=sem_map(news,given_events,modality_negation_rules); partition(status)` | 同湖6111事件双属性；与角色/类型任务分开评价 |
| `kind=sem_map(abstract,given_graph,KT_rules); groupby(kind)` | GENIA35587事件、968独立摘要，不能算35587篇论文 |
| `provenance=sem_map(abstract,given_graph,source_rules); filter(Source=='Other')` | 533目标事件，不能当533篇论文 |
| `attributes=sem_map(abstract,given_graph,epistemic_rules); filter(original_joint_predicate)` | 1000 selected为确定性组合gold；不是1000额外人工decision |

| 预期关键语义算子交LOTUS结果 | 预期LOTUS过程 | 预期Data Agent结果 | 预期Data Agent过程，用==标注探索== | 预期operator结构 |
|---|---|---|---|---|
| SENTiVENT的AAL原例应将The company/AAL归到American Airlines Group Inc. AAL相应指称span；详见round60实际源核验 | 同规范、同全文的固定指称检索与角色映射；给定事件条件对齐 | 同一gold目标，未预设优势 | ==定位前文全名；核代词与公司简称指向；区分事件角色==→canonical论元 | 文档指称索引→角色约束→canonical span→公司聚合；未提取 |
| GENIA既有高强度观察例，五字段及selected目标见round53；更细任务分别投影同一人工标签 | 固定规范检索/传播规则及同资源批缓存，按任务输出属性 | 同一字段目标，未预设更好 | ==读跨句研究来源；区分强度与不确定性；按嵌套结构检查传播==→字段 | 共享事件结构索引→来源/确信/强度三个可分支模块→约束检查→清单 |

多个任务带来两个不同研究单位：单一任务内跨文档摊销，以及同湖跨任务资源复用。当前原目标要求前者；后者可作为新增实验轴，不能把合并多个任务轨迹说成一次示范。每任务分别冻结task、允许资源和private gold视图；若给定目标以外的人工标注，必须在所有比较臂同等提供并披露。

本次只重新统计原生gold，没有模型调用或能力结论。具体计数脚本与收据位于artifact/evidence/shared-environment-audit-20260908-v68/multitask_audit.py和multitask-counts-private.json。SOURCE_VERIFIED_CONSTRUCTIBLE_DEVELOPMENT来源仍3/10，新增任务视图为NATIVE_GOLD_VERIFIED_VIEW_PENDING。

## CASIE：round70新增同湖任务

991真实新闻；Q1事件及角色论元抽取（8380events22471args）；Q2同事件realis分类（5201Actual2069Generic1109Other，1General无效源标签保留）。两类目标共享同一28页规范。Q1公开正文/私有gold开发视图已构造校验；Q2运行与评分契约待实现。不是两个独立数据湖。见[round70](shared-environment-search-2026-09-08-round70.md)。

## GUM：round74

已构造142文档文本/转录话语图任务（19271EDUs896secondary）；来源tokenization/版式/speaker明确给定，不含figure。不同relation投影不另算任务。实体/信息状态/共指第二任务已取得原生来源，构造尚未完成。见[round74](shared-environment-search-2026-09-08-round74.md)。

## AAEC：round77

397作文/6007成分/3781支持攻击关系/1486claim stance；联合结构视图已独立源核验。相对主立场For/Against是不同于关系support/attack的目标字段，但独立运行视图待建。语义类型扩展已下载，5边界冲突处理披露，尚未独立构造。不另算数据湖。见[round77](shared-environment-search-2026-09-08-round77.md)。


## UKP web discourse：round81

第7个来源构造开发候选。已构造889真实非空唯一正文P1/P2任务，456真433假，11477词同协议；§3.3.1包括中立的双边论据，不能简化为普通说服意图。第二Toulmin任务原生gold可取、视图未构造，零长度隐式Claim/低一致性pathos需分开，衍生关系不能算独立语义任务。原990与340结构集重叠279源ID；两个task仍同一lake。见[round81](shared-environment-search-2026-09-08-round81.md)。7/15仅SOURCE_VERIFIED_CONSTRUCTIBLE_DEVELOPMENT，不是实测环境增益或确认通过。
