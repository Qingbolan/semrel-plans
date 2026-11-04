# Increment99 — BioRED：真实关系gold已核验，长E资格暂不成立

当前仍7/15。本轮没有新增合格湖；BioRED作为中等长度规范的关系抽取候选保留，不混入严格合格清单。来源：[原论文预印本](https://arxiv.org/abs/2204.04263)、[作者仓库](https://github.com/ncbi/BioRED)、[官方16页规范](https://ftp.ncbi.nlm.nih.gov/pub/lu/BioRED/BioRED_Annotation_Guideline.pdf)。这不是医疗纳入/保险决策，而是按统一规范维护文献关系知识库的sem_map任务。

已实际下载原论文23页799524bytes；完整入口repo commit39e36f926eeb38d29fa212545adde8ebde62cd37，2160bytes/2ZIP成员（只有README）；另下载其直接链接的完整作者源代码tar340480bytes/160成员及数据ZIP2191684bytes/10成员，完整解包，ZIP全CRC通过。没有把只有README的repo称为完整算法实现。模型权重是单独外部发布，未下载，未执行作者代码。指南305545bytes/16页。精确URL和SHA256见downloads.json。

数据原生Train400/Dev100/Test100，600独立PMID。实体提及分别13351/3533/3535，共20419；关系4178/1162/1163，共6503；Novel2838/835/859，共4532，背景No1971。逐实体原文跨度检查0错误，关系端点到实体ID检查0缺失；600篇BioC JSON与PubTator关系多重集合全部一致。它们是三种序列化格式，不是三个数据湖。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold |
|---|---|---|---|---|
| 为600篇摘要建立文档级实体关系表，并区分新发现与背景 | 原始标题＋摘要，600篇；全文不属于关系任务允许证据 | 统一BioRED规范16页，全文约5287词，其中关系对/类型章节约2514词 | 可选择给定人工实体跨度/ID的关系抽取子任务，必须明确annotation-given；端到端实体归一化还需外部词库 | 6503条关系，8类；4532 Novel、1971 No。不能把未标注任意实体对直接当世界事实FALSE |
| 具体：PMID15824163是否仍应收录BRAF—melanoma关系，是否是本篇新发现？ | 标题No Evidence…；摘要先报告既有阳性关联，随后报告本研究未发现显著关联 | 规范明确：即使本篇结论不显著，也标注此前报告的关联；novelty区分背景与本篇结果 | Gene673=BRAF；Disease D008545=melanoma | 原生唯一关系Association、No。该篇被规范直接引用，只作开发讲解，不能进独立确认 |
| 具体：PMID25119790提取药物、肾毒性及其新颖性 | curcumin预防maleate诱导肾损伤的摘要 | 治疗映射Negative_Correlation，诱发映射Positive_Correlation；与新颖性分开判断 | D003474=curcumin，C030272=maleate，D007674=肾病 | curcumin—肾病 Negative/Novel；maleate—肾病 Positive/No；curcumin—maleate Negative/Novel。同为指南引用示例 |

| 类python的DAG | 具体数值 | 下游gold/验证边界 |
|---|---|---|
| `abstracts.join(given_entities).sem_map(extract_relations,E).explode()` | 600篇→原生6503条关系；8类 | 预测边集合对private原生关系评分；实体输入给定与端到端分开 |
| `relations.sem_map(classify_novelty,E,abstract).filter(novel).groupby(pair)` | 6503条中4532 Novel | 仅在给定gold关系的诊断臂中6503是已知输入规模；端到端不得向模型泄漏gold候选集合 |
| `paper15824163.sem_map(relations).filter(novel).count()` | 应抽取1条背景关联；过滤后0条新发现 | 原生gold实读；非模型运行结果 |
| `paper25119790.sem_map(relations)` | 全文档原生17条关系；上表展示其中3条 | 17不是全文所有可能医学关系；遵循标注世界 |

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
|---|---|---|---|---|
| PMID15824163目标输出Association/No，实际未测 | 同资源E＋完整摘要＋给定实体，固定sem_map抽取并判novelty，再筛Novel | 相同目标，不能预设Agent会更准确 | ==查明“否定结论不删除既往关联”的例外及novelty规则==→区分既往证据和本篇结论→输出背景关系 | `load_rule_index→collect_document_evidence→resolve_relation_scope→map_type→classify_novelty→validate_schema`；拟议结构，未从轨迹学出 |
| PMID25119790三条展示关系应分别Negative/Novel、Positive/No、Negative/Novel | 固定类型映射＋语义证据判读；允许共享索引缓存和固定复核 | 同样三条目标 | ==读取治疗/诱发映射及背景/新发现定义==→抽取不同实体对证据→分别判断类型和新颖性 | 共享类型表＋证据角色分支＋新颖性节点；不是把三条答案写入operator |

必要性边界：规则确实改变输出，例如“本研究无显著关联”不等于删除背景关联。但这仅证明条件语义有用，不证明长环境探索/一次轨迹提取必要。实际关系规则约2514词；novelty规则更短。若给定实体，不能把实体归一化全部指南与外部词库大小算作关系任务的必要成本。16页本身不是自动排除标准，但当前没有证明它达到目标所需的复杂共享环境，也不能靠追加通用医疗手册补长。

规范文本检出49个与数据匹配的PMID（正则7–8位数字，包含直接示例）；尚未做完整OCR/改写近重复审计，不能将其余551篇直接称独立干净。数据取自BC5CDR、NCBI Disease、tmVar、GNormPlus、NLM-Gene等已有语料，后续需跨湖PMID/文本隔离；BioRED-BC8扩展也不是新的独立湖。本轮没有构造public/private可运行快照、没有确认集、未跑LOTUS或Agent，不能报告准确率/成本优势。作者原论文的模型结果不等于本仓库复现。

独立脚本及收据：artifact/evidence/shared-environment-audit-20260908-v99/audit.py、audit.json、examples.json、downloads.json。原件在data/shared-environment-audit-20260908-v99/。开放可下载不自动证明摘要、代码与规范具有相同再分发权，许可尚未完整核验。后续若继续，应先证明适用E复杂性并解决示例/来源重叠；不优先启动模型实验。强对照应含E-only规则编译、Coding Agent及共享缓存整批Agent，不能强迫LOTUS每行重读PDF制造收益。
