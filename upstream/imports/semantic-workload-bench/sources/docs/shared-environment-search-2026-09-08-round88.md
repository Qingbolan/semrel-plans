# Increment88 — PHAEDRA完整来源与59页指南

仍7/15，本候选待语义/构造核验。[原论文](https://link.springer.com/article/10.1186/s13321-018-0290-y)PDF9837171bytes/33页、[官方完整发布包](https://www.nactem.ac.uk/PHAEDRA/PHAEDRA_corpus.tar.gz)680545bytes/1798成员、[原指南](https://www.nactem.ac.uk/PHAEDRA/PHAEDRA_Annotation_Guidelines.pdf)1236850bytes/59页/15264词全部下载并完整解包。精确SHA256在artifact/evidence/shared-environment-audit-20260908-v88/downloads.json。此为作者完整数据发布，不是第三方数据摘要；包内无独立Git版本，按下载字节锁定。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold |
|---|---|---|---|---|
| 构建药物—不良作用—患者/疾病索引 | 597真实MEDLINE摘要：train359/dev120/test118 | 同59页实体、事件、作用属性、关系和共指协议 | 完整正文及必要共指上下文；公开字段尚未构造 | 3189事件、8229参数、1171关系；17572 span混含实体/触发词/线索 |
| 筛选推测/否定/高强度药物效应 | 同全文与给定事件图条件需明确 | 三属性及默认值规则 | 不公开当前目标has_cue或属性 | Speculated454、Negated58、Manner High53/Low46，另3条Manner缺值待查 |
| 识别跨句药物与患者指称 | 同正文 | 事件参与者条件与Coreferring_mention规则 | 不能把共指gold作为感知工具 | 原生共指关系可用，但关系类型/覆盖独立计数未完成 |

作者README明确实体规范化为自动链接；11233条N行不作为人工规范化gold。注释为CC BY-SA4.0，源摘要版权须单独处理。既有ADE/DDI/PK等语料参与选文，不能与这些同源扩展各计一个独立lake；本轮跨湖PMID检查未完成。

| 类python的DAG | 具体数值 | 下游gold |
|---|---|---|
| `abstracts.sem_map(drug_effect_graph,E).explode().filter(type=='Adverse_effect').project(agent,affects,subject)` | 597→3189事件 | Adverse_effect1382；Potential_therapeutic_effect895、Combination574、DDI338另有原生gold |
| `events.sem_map(attributes,E).filter(Speculated).project(event_id)` | 454原始Speculated行 | 唯一性/默认值及作用对象待核对，不能先宣称454独立有效事件 |
| `mentions.sem_map(coref,E).join(event_arguments).groupby(drug)` | 1171总关系包含多个类型 | 未完成共指单独计数及端到端默认输入构造 |

具体原生PMID2924444：E1 Adverse_effect由due to触发，has_agent=L-thyroxine，affects=myocardial infarction；E2/E3同药物还连接coronary spasm和myocardial infarction。这是论文文本的药物效应标注，不是临床因果确认。

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
|---|---|---|---|---|
| 目标E1 has_agent=L-thyroxine/affects=myocardial infarction；未测 | 完整正文和同一规则的固定sem_map，可固定检索与共享缓存 | 同一gold目标，不预设优势 | ==核对Adverse_effect定义、最少agent条件与共指规则==→定位主体/效应→输出 | `entity_and_coreference_index→event_type→role_binding→validity_check`；未从轨迹提取 |
| 目标区分否定、推测、强度；实际输出未知 | 固定属性映射保留全部输出，按协议默认值评分 | 同目标 | ==检索Cue作用域与默认值规则==→输出三属性→清单 | `scope_resolution→attributes→projection`，缺值不自动补Neutral |

全597记录span切片及事件引用检查0错误。直接按照官网最少参与者条件检测，17事件被标记：有的Combination/DDI只连一个参与者，有的PTE缺agent或缺affects/subject。尚未解析参与者是否指向组合事件或多实体共指，不能一概认定17条是错误。Manner三条无值亦不静默修复。

官网统计3166事件与本发布实际3189不同，类型数也有差异；当前以实际字节计数，后续核对论文/发布版本。规则长度必须按任务缩小范围，不能为了三属性单独分类要求读完59页。优先联合事件图任务；是否确需复杂探索由公平的静态/E-only编译对照决定。

无模型运行、无成本或优势主张。脚本download.py/audit.py与收据artifact/evidence/shared-environment-audit-20260908-v88；原始data同后缀。后续做最少参与者的语义解析、缺失属性、示例泄漏及公开构造。
