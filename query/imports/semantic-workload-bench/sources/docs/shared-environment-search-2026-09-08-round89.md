# Increment89 — PHAEDRA共指与缺值核验

仍7/15，本候选不新增计数。本轮复用已完整下载的[原论文](https://link.springer.com/article/10.1186/s13321-018-0290-y)、[作者完整发布包](https://www.nactem.ac.uk/PHAEDRA/PHAEDRA_corpus.tar.gz)及[59页指南](https://www.nactem.ac.uk/PHAEDRA/PHAEDRA_Annotation_Guidelines.pdf)，精确来源字节与SHA256见v88/downloads.json。不是仅根据论文摘要判断。

全597摘要复核：标准ID无重复，1171关系和614属性的目标引用均存在；关系分为Subject_Disorder647、is_equivalent305、Coreference219。官网Coreference212与发布包219不同，保留版本差异。结构引用有效不等于语义正确。

上一轮17个直接参数基数疑点中，7个沿原生Coreference关系解析后有至少两个不同目标；4个仅有一个复数药物类别实体，6个缺必要角色或使用非该类型角色名。指南印刷页31–32明确允许多目标共指及共指链；印刷页8允许药物类别实体，但不能由此推定一个类别span自动满足DDI两个参与者要求。原生图不改写，解析后的药物投影是派生视图，不替代原图gold。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold |
|---|---|---|---|---|
| 为每篇摘要建立药物效应图，并把跨句指代归并到具体药物 | 597完整真实摘要 | 59页15264词作者实体/事件/共指协议；必要任务范围仍待裁定 | PMID15685264中these drugs的上下文，不能只给事件句 | 3189事件8229参数；其中219条共指关系 |
| 查询PMID15685264的E10组合中涉及哪些药物 | 原文中的Carbamazepine、Oxybutynin、Dantrolene和these drugs | 共指多目标规则 | 本轮给出的E10仅为审计示例；正式端到端输入不提供目标图 | E10→T44；T44经R4/R5/R6连接T21/T20/T19 |
| 提取效应强度并生成高强度事件清单 | 同摘要全文 | Manner规则与默认值 | 不能公开当前gold Manner_cue | High53、Low46；3个显式Manner无值，不能算Neutral |

| 类python的DAG | 具体数值 | 下游gold |
|---|---|---|
| `docs.sem_map(extract_graph,E).explode(events).join(predicted_coreference).project(drug_set)` | 597摘要→3189原生事件；219共指边 | 示例E10有1个直接参数，解析后3药物；1与3属于不同计数层级 |
| `flagged.resolve_coreference().audit(minimum_roles)` | 17→7可由共指解释＋4复数类别待查＋6角色疑点 | 此为gold侧数据质检，不是被测系统输出或准确率 |
| `events.sem_map(manner,E).filter(value=='High')` | 原始102个Manner行=53High＋46Low＋3无值 | 明确无值保留未解决标注状态；不能默默补默认值或让系统弃权获得正确分 |

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
|---|---|---|---|---|
| 目标E10药物集合为Carbamazepine、Oxybutynin、Dantrolene；未运行 | 同完整摘要＋同协议固定sem_map提取图与共指，再确定性展开；允许共享检索/缓存 | 同集合；没有实测优势 | ==定位协议的多目标共指与跨句链规则==→识别these drugs对应实体→输出原生图及派生集合 | `extract_mentions→extract_events_and_coref→cycle_safe_resolution→drug_projection`；目前只是设计，非已学习算子 |
| 对显式无值Manner，评测侧应识别标注缺口；模型仍按公开原文预测 | 固定规则区分缺少属性行与存在属性但缺值；清洗仅在私有评测侧 | 同样不能获得当前gold缺值信息 | ==核对Manner默认值及线索作用域==→预测；评分端独立处理已冻结缺口 | `cue_scope→manner_prediction`；不把当前gold缺口写入运行时分支 |

三个无值实例：11033836/A1→E1带significant线索；9876809/A2→E2带potentially serious线索；15840734/A4→E8未直接连接Manner线索。它们不能仅凭线索由研究者重标为High，也不能因格式中无值当作Neutral。完整原始事件/参数位于audit.json。

方法比较必须加入同E的固定程序、E-only规则编译和批处理Agent。共指需要跨句上下文是具体用例，但不证明每条都需重读59页，也不证明单轨迹提取优于直接从E生成程序。

本轮脚本和收据：artifact/evidence/shared-environment-audit-20260908-v89/audit.py、audit.json。未构造public快照，未跑模型。后续：任务必要E范围、短规则充分性、指南/论文示例泄漏、跨语料重叠、剩余角色缺口及public/private构造；在这些完成前保持候选状态。
