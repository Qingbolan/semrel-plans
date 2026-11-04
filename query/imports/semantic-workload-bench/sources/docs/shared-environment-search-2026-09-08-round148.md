# 第148轮：GFCC比例原则标注，新来源的论文与完整规则仓库核验

未qualified，仍8/15。此前147完成GIST多对一关系及原页求证，是实质进展。本轮转向新的独立法律来源，下载原论文和作者完整规则仓库；指南与原gold下载受Zenodo超时影响，不能将论文统计冒称本地全库实测。

[原论文 Classifying proportionality – identification of a legal argument](https://link.springer.com/article/10.1007/s10506-024-09415-9)，作者Lüders/Stohlmann，在线2024/卷期2025；[下载的德国国家图书馆PDF](https://d-nb.info/1385075120/34)1251793bytes，SHA256 `da0efdc60e6ea43c6732e389339097052beeb503c61b09ba4d663d90187be633`。完整[作者规则仓库](https://github.com/klueders/prop_rules)commit `355721de276002781a3425abbd7eaa8d3ea3ea41`，ZIP7312bytes、4members、CRC通过，SHA256 `a397729fc4e4a44b0008ac90968ce9d88730ac1ec9afedd9baa16ce434a560f1`。完整仓库只有README、规则Python和example.ipynb，不包含300份gold或神经模型训练流水线。原件data/shared-environment-audit-20260908-v148，收据artifact/evidence/shared-environment-audit-20260908-v148。

[正式数据发布](https://zenodo.org/records/10513684)列guidelines.zip、gold_data.zip、sent_data.csv和原标注。本次guideline直链/API metadata超时，另以API文件content端点请求guidelines.zip和sent_data.csv仍超时；收据downloads.json/alternate-downloads.json。没有成功取得原标注，未声称完整数据发布下载完成。代码仓库完整下载不等于原始数据全部取得。

## 对任务结构的具体发现

论文§4描述300真实判决/54929句，先标文本角色；仅245判决的24577个merits句接受比例原则多标签标注。55份无merits；其它角色不能默默当比例原则负例。Table2角色数量为facts25050、admissibility4717、overlap127、merits24577、signatures458，总和54929（论文值，未核原CSV）。

共享标注指南经历3轮变更，需绑定版本与每轮数据。论文§4.1说明指南只是原型定义，允许标注员凭法律训练识别不符合经典结构的实例，necessity定义很简短。这是共享E是否自足的重要缺口：不能仅因判决共5739印刷页，就声称共享指南很长。原指南未取得，页数/词数未知。

作者规则仓库将人工标注经验写为词面预筛和形态句法排除：关键词、至少两种比例步骤词、Übermaß；再过滤虚拟式、部分副词/形容词用法。它是已有手工经验编译基线，非单轨迹自动提取。check_entscheidung返回文档Boolean或Boolean+候选句DataFrame，表中是规则特征，并非每句最终标签完整预测。需另构造句子级适配，不能把文档Boolean拿来评多标签任务。代码依赖spaCy de_core_news_lg，未安装/执行模型。notebook两个存储True是历史程序输出，不是专家gold；不得拿它们作成功复现。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | gold状态 |
| --- | --- | --- | --- | --- |
| 从判决中找merits，再标出比例原则步骤，统计各步骤句数 | 论文描述300判决54929句，实际全库尚未下载 | 统一标注指南，3轮调整，当前未取得 | 完整上下文用于区分法院立场/他方意见、理由角色 | 论文Table1给BVerfGE68,272的10句样例标签；原CSV未核 |
| 按判决聚合是否使用比例原则 | 上游多标签句子结果 | 同一指南+聚合契约 | 作者已有手工规则可作对照 | 原生dec_agg_data.csv已定位未下载，不能报告聚合标签一致性 |

| 类python的DAG | 具体数值 | 上下游及边界 |
| --- | --- | --- |
| `decisions.sem_map(label_sections,E).explode().filter(role=='merits').sem_map(label_prop_steps,E)` | 论文样例10句：Aim3、Suitability1、Necessity2、Balancing5，共11个标签 | 第4句同时Suitability/Necessity，不能强制单分类；全库24577merits句仅论文统计 |
| `steps.groupby(decision).agg(any_prop,counts_by_type)` | 样例any=True、4个非空步骤类型 | 11标签不等于11句；10句是一个判决片段，不是10个独立案 |
| `rule_based.check_entscheidung(name,text,return_df=True)` | 作者代码输出Boolean+候选句特征，不含完整多标签序列 | 源码阅读，未运行。若使用需要明确与上游任务语义差异 |

以下均方法设计，模型未执行。样例为论文公开翻译并有德文附录；后续确认必须排除论文/代码例句。

| 预期关键语意算子直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期关键语意算子直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索步骤== | 预期产生的operator结构 |
| --- | --- | --- | --- | --- |
| 论文第4句目标集合{Suitability,Necessity}，输出未测 | 固定流程给完整段落与指南，先角色再多标签判定；允许检索/缓存 | 同样目标集合，无优势结论 | ==核对标签非互斥和merits限定==→==读取上下文确认法院自身论证==→输出两标签 | `SectionTagger -> ProportionalityStepTagger(E_version) -> per_decision_aggregate`；证据句ID与ABSTAIN分开 |
| 论文第5句目标Necessity | 识别是否讨论侵害更小的替代措施，而非只搜必要性词 | 同一目标Necessity | ==查指南的替代措施规则及邻句依赖==→标注并保留原句证据 | 共享规则、上下文窗口、可多标签结果；不能硬编码例句 |

原论文表1例子讨论建筑规划资格要求；第4句指出要求适合且必要，第5句讨论更少限制的替代办法，6–10句权衡职业活动限制。这是已发表标注例子，原生300案和长共享E尚未闭合，暂不进入用户要求的可行数据湖名单。本文论文说明专家训练可能补足指南，不能将未公开专家知识假定为已给E。

下一步优先选择不依赖当前超时Zenodo的独立作者数据来源。此候选保留，等可实际获取指南/gold再核验；没有联系作者、没有假定获授权使用未公开数据。论文CCBY4，仓库未见LICENSE文件，数据许可待原发布元信息核实。无数据构造快照、无模型/测试套件/正式评分/commit；只完成来源获取、源码和论文样例核验。
