# Increment90 — PHAEDRA示例重叠与规范/标注分歧

仍7/15；PHAEDRA继续待核验，不以59页长度自动计入。原论文、完整作者数据发布及指南已经下载，见round88及其downloads.json。本轮读取全部597摘要、指南59页和论文33页提取文本；12词且至少65字符规范化匹配得到28篇与指南重叠，论文提取文本未命中。这是候选暴露清单，不是完整的泄漏排除证明；短例、图中文字及改写仍可能漏检。

原始来源：[论文](https://link.springer.com/article/10.1186/s13321-018-0290-y)、[完整发布包](https://www.nactem.ac.uk/PHAEDRA/PHAEDRA_corpus.tar.gz)、[指南](https://www.nactem.ac.uk/PHAEDRA/PHAEDRA_Annotation_Guidelines.pdf)。本轮未重复下载已有相同字节。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold |
|---|---|---|---|---|
| 根据完整摘要建立药物效应及跨句指代图 | 597真实摘要 | 同59页作者协议 | 原文症状、药物和患者上下文 | 3189事件及219Coreference边；原生gold与协议一致性还未完全成立 |
| 检查PMID16132305中的symptomatology指向哪些症状 | rhinorrhea、poor feeding、decreased activity level | 指南PDF第33页直接展示此文并说明应连接这些症状 | 同页标红symptomatology/improved和标蓝三个症状；已视觉核对 | 发布中T24为Disorder 624:638，没有以T24为端点的共指边，也没有improved事件 |
| 在不含E中已见原文的后续批上评测 | 597候选减28长片段重叠=569候选 | 完整E保留，不能按测试结果删规则 | 尚无公开快照/冻结split | 569不是已确认清洁、合格或独立测试数量 |

| 类python的DAG | 具体数值 | 下游gold |
|---|---|---|
| `docs.sem_map(event_and_coref_graph,E).project(drug_effect_index)` | 原始597摘要/3189事件 | 需先明确规范/原生标注分歧如何处理，不能默默添加边 |
| `source_docs.join(E_examples).mark_development_exposed()` | 28篇长片段命中；位置及匹配内容逐项保存在audit.json | 本行是构造侧质检，不是被测语义任务，也不计模型能力 |
| `mentions.sem_map(resolve_referents,E).explode().join(events)` | 示例指南明确3个症状目标；发布T24相关Coreference为0 | 0表示此发布无该边，不能声称语言事实“没有指代” |

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
|---|---|---|---|---|
| 若以指南例子为目标，应输出三个症状；但不能当作原生gold的正确输出 | 同E与完整原文固定sem_map，按距离、语义和作用范围解析 | 相同规范目标；未运行，不预设优于固定实现 | ==检索共指规则，核对指称可越过最近句==→绑定三个症状→输出 | `mention_detection→bounded_context_resolution→event_role_join`，当前仅设计 |
| 对未暴露的后续文档，真实输出未知 | 固定流程可共享规则摘要/检索/缓存；E-only编译必须作为对照 | 真实输出未知 | ==检查事件角色、跨句规则与异常输入==→输出图 | 不允许把当前私有gold分歧或具体ID编进运行时operator |

具体发布原文已核对：T17=rhinorrhea[371:381]，T18=poor feeding[383:395]，T19=decreased activity level[401:425]；T24=symptomatology[624:638]。原生R3/R7/R8是患者指代T23/T28/T8→T14，不能误认为症状指代。现有E5是resolved[714:722]，也不是指南标出的improved。这个差异不靠补边或删除单个错例消除，需冻结任务采用哪套语义及覆盖边界。

跨源PMID审计：PHAEDRA597与GENIA-MK原始1000、MLEE262、IPF150各自交集为0。第一次通用*.txt文件名检测对GENIA(XML)与MLEE(PMID-前缀)得到0来源ID，未当作无重叠证据；按已观察到的各自格式修正后得到上述真实数量。这里只证明这三个集合的PMID交集，不证明患者独立、近重复隔离或与ADE/DDI/PK来源独立。

产物：artifact/evidence/shared-environment-audit-20260908-v90/audit.py、audit.json；视觉检查图data/shared-environment-audit-20260908-v90/guideline-page33.png。没有运行模型、作者代码或构造公开快照。下一步保留此分歧，检查其余示例和规范覆盖；不把候选数冒充已经求证的15个。
