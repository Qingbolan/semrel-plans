# 增量201：FrameNet完整发布 → 28,113条公开输入/私有gold开发视图

本轮把FrameNet登记为第12个 `SOURCE_VERIFIED_CONSTRUCTIBLE_DEVELOPMENT` 数据湖。它提供真实源文本上的人工语义标注，**不是保险审批或临床处置结果**。长环境必要性、LOTUS质量差距、Agent改善、单轨迹提取及独立确认都未验证。该限定与此前11项相同，不能把12个构造候选说成12个最终通过的benchmark。

原件已在增量198下载：[原论文](https://aclanthology.org/P98-1013.pdf)、[发布访问/API论文](https://aclanthology.org/D17-2001.pdf)、[完整FrameNet1.7发布ZIP](https://raw.githubusercontent.com/nltk/nltk_data/gh-pages/packages/corpora/framenet_v17.zip)。这是完整数据发布，不是声称克隆了一个不存在于本轮的作者Git仓库。ZIP为99,207,152 bytes、14,937成员，SHA256 `22f6aad6fb799ba4dbed0440714e1118442ad7d7345351de37428581284f471c`。使用包内2016-11-01版129页、约70,034词手册，不用当前网站变化后的规范替换它。原件路径为 `data/shared-environment-audit-20260908-v198/`；[此前原件收据](../artifact/evidence/shared-environment-audit-20260908-v198/)。

本轮实际生成 [开发视图](../data/shared-environment-audit-20260908-v201/view/)，公开侧为原文、指定target跨度、去实例环境及配套手册；私有侧为源gold和排除登记。构造脚本[build.py](../artifact/evidence/shared-environment-audit-20260908-v201/build.py)，独立逐条比对脚本[verify.py](../artifact/evidence/shared-environment-audit-20260908-v201/verify.py)，[构造收据](../artifact/evidence/shared-environment-audit-20260908-v201/construction.json)及[验证结果](../artifact/evidence/shared-environment-audit-20260908-v201/verification.json)。原始全文XML、LU实例目录及私有收据都不属于运行器资源；目录分离不等于OS沙箱。

## 实际数据与三个任务视图

| Query | 数据湖 数据1：候选输入 | 数据湖 数据2：共享词典 | 数据湖 数据3：共享协议 | private gold |
|---|---|---|---|---|
| Q1：逐target判定框架，再生成Giving目标清单和计数 | 28,113条target，来自101篇有目标标注文档；107篇原文共10,147句全部保留作上下文。只给文本和target跨度，不给gold lemma/LU/frame ID | 同版1,221框架、13,631词汇单元定义、109语义类型、2,070框架关系；无当前实例 | 129页配套手册和框架定义 | 28,113人工frame；涉及796种frame；其中Giving **57条** |
| Q2：逐target抽取所有角色，再生成角色—跨度关系表 | 与Q1相同；端到端版本消费Q1预测frame，不能偷偷给gold frame | 角色定义、coreType、requires/excludes、core sets和角色关系 | 跨度、非连续角色、次层标注等规则 | rank1 **58,335**，rank2 **739**，合计59,074条；其中50,802有显式跨度 |
| Q3：逐target识别隐式角色及源类型，再汇总隐式论元 | 与Q1相同；可作为Q2的投影，不重复计为新湖 | 同版角色定义及词义 | DNI/INI/CNI及源枚举INC；不把它们混为ABSTAIN | **8,272**隐式标签，分布在6,478个target：DNI3,455、INI3,226、CNI1,573、INC18 |

Q1与Q2是不同输出契约；Q3是Q2的可评分子视图，不宣称独立数据湖或独立监督来源。7个WikiTexts文件只选择性标注词项，不能将未标注位置当负例。给定target意味着目标发现成本不在本任务内。

| 类python的DAG | 具体数值 | 可核验输入/输出与边界 |
|---|---|---|
| `targets.join(sentences).sem_map(resolve_frame, E)` | 28,113 → 28,113 frame输出槽位 | source frame为私有gold；执行失败须保留ABSTAIN行 |
| `frames.filter(frame == "Giving").project(record_id).count()` | gold清单57条，gold count=57 | 外层过滤与计数固定，不把它本身称语义难点 |
| `targets.join(predicted_frames).sem_map(extract_roles, E).explode()` | gold59,074角色，其中739条rank2 | 关键语义步骤是角色跨度/类别；比较端到端结果和给定gold frame的明确oracle诊断 |
| `roles.filter(has_itype).groupby(itype).count()` | DNI3,455 / INI3,226 / CNI1,573 / INC18 | 确定性聚合；源隐式标签不是执行失败 |

## 一个实际句子如何进入不同方法

源文件 `ANC__110CYL067.xml`，原句ID4106339：

> Your contribution to Goodwill will mean more than you may know .

公开目标 `contribution` 的Python跨度 `[5:17]`。私有源annotation6556463：**Giving；Donor=[0:4]="Your"；Recipient=[18:29]="to Goodwill"**。不能把Recipient自动缩成实体名Goodwill。这里没有补造源gold未标出的Theme。

同句目标 `know` 的源annotation6556467为 **Awareness；Cognizer="you"；Content=DNI**。同句 `more` 还有rank2 Added_set，说明rank2不是可以直接丢弃的重复层。所有这些例子已经被本次研究查看，属于开发暴露。

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
|---|---|---|---|---|
| Q1目标输出Giving；**实际未运行** | 固定词典检索和缓存→传统`sem_map`按候选frame定义消歧→JSON frame。也应比较完整必要输入直接调用；不能因E长就预言错误 | 相同目标Giving；**实际未运行** | ==查contribution候选词义、Giving定义及相邻框架== → 按上下文选择 → 输出 | `CandidateRetriever → FrameResolver → FrameSchemaValidator`，索引可一次共享构建 |
| Q2目标输出Donor="Your"、Recipient="to Goodwill"；**实际未运行** | 固定检索Giving角色定义/跨度规则→`sem_map`→保留层级的角色JSON→确定性explode | 相同角色与跨度；**实际未运行** | ==查角色定义、介词短语边界规则和次层规则== → 抽取 → 检查跨度与schema | `RoleRuleIndex → SpanAndRoleMapper → LayerPreservingValidator`；不能只写死该例两个角色 |
| Q3针对know输出Content=DNI；**实际未运行** | 同资源固定隐式角色提示或Q2结果投影→枚举校验 | 相同目标；**实际未运行** | ==查省略论元类型及可访问的文档上下文== → 选择源类型 → 输出 | `NullInstantiationClassifier`；语义null与运行ABSTAIN独立 |

`==`只表示可观察查阅/检查步骤，不要求私人思维链。上述结构是待检验设计，不是已学习的算子。固定检索程序、Coding Agent、仅E生成算子、批Agent均可访问同一资源、缓存和公开工具。长词典本身不能证明逐行探索优于一次编译。

## 构造修正与本轮验证

- 将多词target跨度按位置排序后，发现**29**个多标注键，修正199的28；新增一组是相同多词跨度的存储顺序不同。8键跨frame，全部29键在此单答案开发视图中排除并原样登记。原28171带frame人工annotation减去58份，得到**28113**；未择优挑选答案。后续若需要多解任务，应另定契约。
- 原LU目录含当前全文人工实例，不挂载。字段allowlist保留定义/lexeme/类型/角色约束/关系，去`<ex>`例句、标注状态、作者/日期、来源header、sentenceCount、valence和实例。框架文件中的13,631个词汇单元登记不等于具有独立LU文件的13,572项，未混报。
- 导出环境定义共366,949 whitespace词，其中框架及角色定义241,598词；较200的364,543增加的是导入语义类型定义。与全部源句的八词精确匹配为0。这是表面泄漏检查，不证明未包装例子、改写或预训练污染不存在。
- 独立脚本重新打开原始XML，逐条验证**28,113**个frame、target、全部FE rank/跨度/itype一致；公开字段、ID集合与文件大小/SHA256/完整清单检查通过。偏移从源闭区间显式转成Python右开区间，未改字词。
- 此轮未运行LLM、LOTUS、官方scorer或提取器；没有确认划分，没有E/短规则消融，没有成本和准确率结论。只运行一次构造和一次全量独立导出验证，不把它们算模型测试。
- FrameNet要求署名和来源说明；源文本版权需另行遵守。不自行赋予整个发布包新许可证，不公开发布本地private材料。

复现验证：`python3 artifact/evidence/shared-environment-audit-20260908-v201/verify.py`。构造默认拒绝已有目标；复建需在脚本中明确设置一个新的目的目录，不能覆盖冻结视图。当前是一次研究检查脚本，不宣称已接入仓库统一CLI。

本轮进度：**12/15构造级开发候选**，严格环境必要性实验仍未完成。下一步转新来源；不继续用FrameNet的任务变体增加独立湖数。
