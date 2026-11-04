# Increment82 — E3C：长时间协议与人工层已下载核验，暂不新增资格

当前7/15，E3C为SOURCE_DOWNLOADED_AND_AUDITED。原始人工病例层、多字段gold与长共享规则有直接证据；尚未构造公开视图，不能称合格第8湖。

已下载原论文[CLiC-it2020](https://aclanthology.org/2020.clicit-1.30.pdf)223071bytes/7页、[2021项目论文](https://ceur-ws.org/Vol-2968/paper5.pdf)466032bytes/4页，完整[作者仓库](https://github.com/hltfbk/E3C-Corpus)commit8196181eacd5d65828d324dcc63970c503aff5e9，ZIP237517555bytes/51426entries/51361Git blobs。ZIP CRC、完整tree与每个blob的Git SHA1均通过；没有执行作者代码。ZIP SHA256846b92a19e632d2200dd48ee6f9f3701d15e772c92a0676a2cd979eb7b5cb18a。

[官方数据页](https://e3c.fbk.eu/data)的时间指南下载实际是40页、版本2.0.0 November2021，708208bytes，SHA25633dd3f8b40ef0b87e8b47087526d050c64d93e8ce7c0b507610024f07b3fadb1；网站链接文字仍写v1.2。完整仓库附带的THYME_ANNOTATION_GUIDELINES_v1.2.pdf为39页/11686词，SHA256d9480f8bc0e32ce022f1a7220db32120c8007e5d2a0caf04831dc5afd75e00df。后续从后者绑定数据，不能默默换新版。实体指南19页/5081词，两来源bytes一致，SHA256e2f997790133a3f16795f5e0676ac07133cc5ec130c10e20789e3057c4ac87a2。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold |
|---|---|---|---|---|
| 按E3C协议建立病例事件时间/事实性索引，区分已陈述、否定、假设及发生时间 | 人工layer1：English84/French81/Italian86/Spanish81/Basque90，共422源文档 | 随库39页v1.2时间与事实性规则 | 原生正文及经审计的必要日期/语境元数据；如只预测属性须明确given-event条件 | 25259EVENT，每事件原生docTimeRel、polarity、contextualModality等 |
| 将检验数值归到对应检查事件，构造结果表 | 同一人工病例层 | v1.2 RML及PERTAINS-TO规则 | 原文、必要事件及数值span；给定部分须所有方法一致 | 2863RML、3128 RMLPERTAINSTOLink；关系引用有目标，不代表每条已验证来源语义 |
| 临床实体识别/规范化（同湖第二类潜力） | 同422文档 | 19页实体指南 | 规范化要求额外UMLS版本，尚未取得 | 6475CLINENTITY；不能把gold的entityID/xtra词条作为公开检索库 |

仅layer1为本文人工gold统计。layer2为半自动、layer3未标注；不能按仓库体量声称所有病例都有人工标签。422是文件数，258文件有DOI、177不同DOI；81西班牙文件共享的是SPACCC整个语料DOI，不能当同一病例也不能自动证明81独立病例。意大利2文件共享文章DOI。西班牙源可能与已查CodiEsp/SPACCC重叠；跨湖独立性仍待审计，五语言不算五个lake。

| 类python的DAG | 具体数值 | 下游gold/边界 |
|---|---|---|
| `scan(cases).sem_map(event_attributes,E).explode().filter(polarity=='NEG').project(event)` | English84文档4885EVENT | NEG456/POS4429；不是456独立病人，也不是确认患者没有疾病 |
| `events.sem_map(contextual_modality,E).groupby(modality).count()` | 同4885英语事件 | ACTUAL4678、HYPOTHETICAL-OTHER74、HEDGED87、GENERIC40、HYPOTHETICAL-IF6 |
| `cases.sem_map(temporal_graph,E).explode_edges().filter(role=='BEFORE')` | 英语4350 EVENTTLINKLink | BEFORE1218、CONTAINS1791、OVERLAP728、SIMULTANEOUS389、BEGINS-ON151、ENDS-ON73；TIMEX关系另计，不能遗漏或混合 |
| `cases.sem_map(test_result_links,E).explode().project(test,value)` | 英语480RML、541PERTAINS链接 | 尚未验证完整source-owner-link图与值归属，未构造运行视图 |

原生实例EN100017中，history[51:58]为ACTUAL/BEFORE/NEG；presented[59:68]为ACTUAL/BEFORE/POS。这说明ACTUAL不能简单等同“临床事实肯定发生”，必须联合polarity解释。此处记录的是作者标注，不提供临床诊疗建议或替代诊断。

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
|---|---|---|---|---|
| 目标history为ACTUAL/BEFORE/NEG，presented为ACTUAL/BEFORE/POS；实际预测未知 | 固定sem_map接收完整病例、同一适用E；若给定event库存需显式对齐信息条件；属性与筛选分开 | 同一原生字段目标，未预言优势 | ==核对polarity与contextualModality的独立定义、docTimeRel的时间锚==→读上下文→输出属性→下游投影 | `event_inventory→context_features→protocol_attribute_rules→schema_validation→projection`，真实轨迹提取未做 |
| 目标恢复原生结果—检查链接；具体数值例子待下一轮源owner验证 | 固定全输入链接抽取，允许固定工具/检索 | 同目标、无实测结果 | ==按RML定义区分值与检查，核对PERTAINS方向和跨句指向==→产生链接 | `detect_measurements→resolve_test_reference→emit_typed_link→validate_endpoints`；不能从当前gold索引取答案 |

实际验证覆盖：全部422XMI正文非空检查、custom span UTF16范围、target引用存在，0错误；没有独立surface字段，不能称精确span文本被第二来源确认；尚未验证所有slot owner、许可/元数据冲突、语言特定规则和跨源重叠。意大利86文件共172METADATA，需查为何双份，不能任取日期作为可靠输入。README声明清理了非病例句子及图表引用，需检查任务必要信息是否随之缺失。

本轮脚本与收据在`artifact/evidence/shared-environment-audit-20260908-v82/`，完整下载在data同后缀。额外2023章节作者站点下载遇TLS issuer验证失败，未关闭TLS；两篇原始论文已取得。无模型/prompt/tokens/费用、无默认执行与评分结果。后续优先核对v1.2规则到实际属性绑定、元数据时间语义、源病例/语言独立性与public-only构造。
