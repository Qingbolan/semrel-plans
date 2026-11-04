# 增量153：SitEnt 原论文、完整仓库与49页手册已下载；原生50,009片段并非全有可评分gold

本轮新增来源，不与历史候选重复。状态为 `SOURCE_ACQUIRED_NATIVE_AUDITED_SCOPE_PENDING`，仍8/15。长E与真实批量已获得直接证据；当前XML/论文范围、上位标签、缺失gold、指南样例污染仍待收口，不将其列为已满足全部要求的第9个。

## 下载及来源

- [作者完整仓库](https://github.com/annefried/sitent/tree/28d64abfe53a22122488b39976075edffcb18b92)，commit `28d64abfe53a22122488b39976075edffcb18b92`。ZIP965,100,691 bytes、1767成员，CRC全通过；SHA256 `0f4e483593ece758e296d32a03e4d904191e812bf843618c05359c7e1efe79bc`。含模型和派生特征，下载完整不意味着全部可给被测模型。
- [原ACL2016论文](https://aclanthology.org/P16-1166.pdf)，172654 bytes，SHA256 `abc7d3d98a13e713770ad494714d373ce2a7ec7ab19771a53c165dbedcc3d644`。
- [原标注论文LAW2014](https://aclanthology.org/W14-4921.pdf)，169497 bytes，SHA256 `38a3adb8ba83ccd1bfa1c14c5bbf5e6cd7ce0ed5839ef25e009076ae83abcdbf`。
- [正式手册v1.1](https://www.coli.uni-saarland.de/projects/sitent/files/sitent_manual_v1.1.pdf)，1105309 bytes，SHA256 `228ddf1cdf238c6d1dc7de9cb525db27cecd62d698030968b58d2ee8c1ecd0f7`。49 PDF页、pdftotext空白分词15367词，与完整仓库附带手册逐字节相同。末尾有德语附录与参考文献，不能全算英语任务必要规则。README明确绑定此版与本仓库标注。

原件在 `data/shared-environment-audit-20260908-v153/`。下载收据、可重跑acquire.py/audit.py、audit.json、span-errors.json、documents.json和examples.json在 `artifact/evidence/shared-environment-audit-20260908-v153/`。`private-native-rows.json`含原生gold，仅用于构造审计，不能挂载运行器。尚无正式public/private快照。

## 核验结果与任务边界

1. 实读367个XML及配对原文本，50,009个segment、ID无重复、完整文本哈希无重复。47,098片段逐字符匹配原文offset；其余2911片段仅空白不同，全部50,009在空白规范化后匹配。无越界/归一化失败。原文不改写，构造时应保留原文偏移与XML文本规范化规则。
2. SE-type分布：STATE18337、EVENT9688、GENERIC_SENTENCE7582、GENERALIZING_SENTENCE1466、REPORT1617、QUESTION1056、IMPERATIVE1046；七类共40,792。另432 GENERAL_STATIVE、48 SPEECH_ACT为上位标签；970 CANNOT_DECIDE、7767缺字段。不能把后两种当FALSE或模型ABSTAIN，不能将上位标签擅自压成子类。
3. 其他已决字段：mainReferentGenericity39690（含143 EXPLETIVE），habituality39282，mainVerbAspectualClass39796。它们不是额外独立文本；跨字段交集、各自标注规范和评分仍需冻结。自动生成的mainVerb/mainReferent span明确不是人工gold，不将其冒充可靠上游定位。
4. 官方split为285 train/82 test文件，表中segment总数40940，与论文MASC30333+Wikipedia10607一致；当前XML总数50009。按全片段比341文档数量不同；即使只计有seType字段仍41文档不同。七类已决数40792也不等于40940。数量差异不是数据无效的证明，但还不能称恢复了论文评测集。保留本次XML范围，不暗中改成论文数字。
5. 论文说明MASC/Wikipedia由三位具基本语言学训练的标注员独立标注，以多数票构造gold。仓库同时保存个人标签与gold。本轮未重算多数票，未声称与每位标注一致。类别统计不是独立正确率证明。
6. 手册§4.3.2–4.3.4对否定、未来/情态、条件句给出细粒度规则及泛指/习惯性例外。已渲染检查PDF37页（印刷36页）。这证明E含会改变任务语义的具体规范；尚未证明长E相对短规则摘要存在实测收益。E-only编译完全是合理强基线。
7. 根目录Apache-2.0覆盖范围与原MASC/Wikipedia文本权利需分别核对；不能把代码license当所有原文无条件商业许可。指南样例与文档近重复/来源重叠还未排除。

## 用户要求的三张表

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold / 当前范围 |
| --- | --- | --- | --- | --- |
| 为语料检索构造“实际事件叙述”片段清单，再按文档统计 | 367真实原文本，来自MASC/Wikipedia | 49页绑定版SitEnt手册；英语任务不强行挂德语附录 | 原始segment ID和begin/end作为显式给定上游切分；上下文全文可读 | 七类已决40792，EVENT9688；缺失/未决/上位标签单独登记，不能宣称全篇事件数 |
| 区分种类泛指与特定个体的习惯性行为，用于建立两类检索索引 | 同批文本与片段 | §4.1.1主指称泛指、§4.1.3习惯性、§4.2.3 general statives | 同一文档上下文，用于解析代词与重复行为 | GENERIC_SENTENCE7582、GENERALIZING_SENTENCE1466；这是同任务的下游视图，不新增数据湖 |
| 单独评估词汇体及习惯性标注，用于语料的体貌分布统计 | 同批片段，不提供人工属性 | 分别绑定§4.1.2/§4.1.3与coercion规则 | 自动解析器若用，所有方法同样可用，不能视为gold | aspect已决39796、habituality已决39282；独立字段可评分但范围交集待核验 |

具体原生例子 `blog_Anti-Terrorist.txt_16`：片段描述美国自9/11后未遭受一次成功的大型袭击。原生gold为 `STATE / NON-GENERIC / STATIC / DYNAMIC`。这里 **DYNAMIC是词汇体，STATE是整个片段的SE type**，二者不矛盾；否定使特定事件的实际发生不成立。真实文档共104片段：47STATE、4EVENT、23GENERIC_SENTENCE、4GENERALIZING_SENTENCE、4QUESTION，另19缺失与3未决。不能把这22条自动当负例。

| 类python的DAG | 具体数值 / 原生实例 | 上下游核验与边界 |
| --- | --- | --- |
| `scan(raw_text).join(given_segments)` | 367文本→50009片段；50009归一化offset匹配 | 原文+上游切分可公开；原标签私有。给定切分任务，不是端到端分句能力 |
| `segments.sem_map(label_situation,E,document_context)` | 例16目标`STATE`且词汇体`DYNAMIC` | 必须分开返回字段；全量仅40792七类已决可做当前7类评分视图 |
| `labels.filter(seType=='EVENT').project(doc,id).groupby(doc).count()` | 已决视图全库9688；例文已决EVENT4 | 只称“已决评估范围内”的计数；不能拿4作原文所有实际事件gold |
| `segments.sem_map(label_aspect_and_habit,E).groupby(doc,aspect,habit).count()` | 例16`DYNAMIC/STATIC` | 原始两字段分别有39796/39282已决；不能把缺失字段补零或推测交集 |

以下仅为预期目标和执行设计，未执行LOTUS或Data Agent，没有准确率、成本或优势预测。

| 预期关键语意算子直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期关键语意算子直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索步骤== | 预期产生的operator结构 |
| --- | --- | --- | --- | --- |
| 例16应输出STATE，EVENT过滤不选中；实际未测 | 固定sem_map读取同规范与上下文，区分词汇体和派生SE类型；确定性filter/count | 相同目标，不能预言更准确 | ==查§4.3.2否定及泛指例外，确认主指称范围==→输出字段与条款证据→固定过滤 | `ContextResolver -> AspectClassifier -> SECoercion -> TypedOutput`；算子是否需要这些内部步骤要由真实轨迹决定 |
| 例16词汇体DYNAMIC、习惯性STATIC | 同资源固定多字段抽取；固定检索/缓存允许；两个字段分别评分 | 相同目标 | ==核对词汇体与整句静态性的差别，阅读适用定义==→输出两字段 | 共享`RuleIndex`与字段约束；不拿SE type机械替代词汇体 |
| 两类泛指索引应区分种类断言与个体习惯，未测具体错例 | 固定全文/检索程序同样读取泛指、习惯性、例外规则；允许批共享预处理 | 同样不自动获得正确性 | ==定位冲突定义，结合前后文判定referent==→输出带证据类型 | 可参数化任务/类别与上下文范围，ABSTAIN不当FALSE；须与无轨迹E-only编译、Coding Agent比较 |

## 本轮结论与下一步

下载、E版本绑定、真实文本—片段偏移核验已完成。未补成“第9个可行”：下一增量先核对XML与原实验XMI范围、上位类/未决语义和指南示例污染，再冻结具体评估关系。即使构造闭合，仍需短摘要/完整E消融来验证长环境必要性；不能以49页证明重复推理成本或单轨迹提取必要性。没有模型调用、模型费用、快照、正式scorer运行、测试套件或commit。
