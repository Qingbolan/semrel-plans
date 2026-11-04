# 第65增量：MAVEN家族完整来源与真实批量核验

合格仍3/10。MAVEN、MAVEN-ERE、MAVEN-Arg共享文档，只算一个潜在数据湖，不把不同标注层拆成多个。原论文和完整作者仓库均取得；本轮没有以论文总数替代可访问gold数。

| 来源 | 原论文实下载 | 仓库commit | 完整ZIP bytes/条目 | Git blob逐个验证 |
|---|---|---|---|---:|
| [MAVEN](https://aclanthology.org/2020.emnlp-main.129/) | 20页616398bytes | 71151f6da53bc9df9d6c5718dc81a2e1489651bf | 18470943/74 | 59 |
| [MAVEN-ERE](https://arxiv.org/abs/2211.07342) | 16页567186bytes | ac81a9711a69f43f55bfbc50b3bb573fd11c64b0 | 104866/58 | 45 |
| [MAVEN-Arg](https://arxiv.org/abs/2311.09105) | 20页798307bytes | b2672448a933510c815f45322ced6226a3ffef9e | 9945/4 | 3 |

仓库均THU-KEG名下，与表中名称对应；递归tree未截断，全部blob校验通过。ERE作者数据ZIP19635238bytes/4条目；Arg作者数据ZIP33611154bytes/6条目，全部CRC通过。下载来自各仓库README的清华云链接；未运行作者程序。原始MAVEN单独数据包尚未下载，本轮实际数据审计仅ERE/Arg，不声称三套原始语料均已下载。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold |
|---|---|---|---|---|
| 在给定事件触发词与实体候选的条件下，为全文事件填充论元，形成事件参与者/地点/损失索引 | MAVEN-Arg论文称14655词、162事件类型、612角色的完整定义；**完整规范未在发布包发现** | 源Wikipedia派生文本及事件；若触发词/实体簇作为输入，须显式annotation-given | 可用实体指称与非实体原文span | 公开train2913篇190479论元；valid710篇46458；test857篇无公开论元gold |
| 根据统一关系规范，为给定全文事件/时间节点构造事件图，供时间线、因果前置条件查询 | ERE README明确链接[RED规范](https://github.com/timjogorman/RicherEventDescription/blob/master/guidelines.md)，取得196547bytes/29541词 | MAVEN-ERE原论文§2及README给出删改规则，不能直接继承全部RED | train2913/valid710篇；TIMEX/event输入与目标关系须明确拆分 | 人工标注/复核产生的关系；时间关系由人工排好的端点顺序推导，并非每一对独立人工直接判断 |
| 实例：Action of 20 October 1793中accident | Arg论文Table7 Incident规则：Participant合并难以区分的Agent/Patient；Loss可与Participant重叠 | 文中事故导致一人受伤，发生于Crescent舰上 | 触发词accident [1206,1214) | Participant=a single man[1179,1191)，Loss=a single man wounded[1179,1199)，Location=aboard `` Crescent ''[1215,1236)，Content=[]；此例直接出现在论文，只作开发解释 |

| 类python的DAG | 具体数值/当前状态 |
|---|---|
| `docs=scan(train+valid)` | ERE/Arg各3623篇，逐split ID交集分别2913/710/857，不能当两份独立湖 |
| `args=sem_map(doc,given_events,given_entities,role_schema)` | Arg公开80479事件/87771事件mention；236937论元=94922实体引用+142015文本span；跨度与引用检查0错误 |
| `event_graph=sem_map(doc,given_nodes,relation_protocol)` | ERE公开84285事件簇/91719mention、20827TIMEX；核心共指若作为目标不可同时提供gold簇 |
| `timeline=project(event_graph.temporal)` | train792445条、valid188928条；仅计发布的六种正关系，不擅自把缺边作为已审查FALSE |
| `causes=project(event_graph.causal)` | CAUSE8420、PRECONDITION37594；subevent12019；全部发布关系端点引用闭合 |
| `index=groupby(event).collect(arguments_or_edges)` | 固定下游图/索引可定义，但完整公开输入与评分契约尚未构造、无模型执行 |

| 预期关键语义算子交LOTUS结果 | 预期LOTUS过程 | 预期Data Agent结果 | 预期Data Agent过程，用==标注探索== | 预期operator结构 |
|---|---|---|---|---|
| Incident例应输出Participant/Location/Loss三个role及重叠span；Content空 | 同规则、全文和给定上游节点的固定sem_map；允许按事件类型固定检索角色定义 | 同一目标，未预设Agent更准 | ==查Incident将Agent/Patient合并的规则；核一人受伤同时是Participant及Loss；核原文位置==→论元 | 事件类型→角色定义检索→实体/非实体选择→重叠角色保留→跨度校验→索引；未学习或运行 |
| ERE需输出符合冻结关系语义的图，不能指定尚未实测准确率 | 固定事件对分类、时间端点约束、图一致性检查；允许同资源缓存 | 同样目标，未预设优势 | ==查RED适用规则及MAVEN删改；区分时间包含与事件部分关系；证据不明确时按冻结未知语义处理==→图 | 规范编译→事件/时间节点上下文→关系候选→规则检查→图输出；未知/缺边评分尚未冻结 |

两个具体缺口：

1. **Arg规范缺失已实证。** 完整repo只有README/.gitignore/evaluate.py，数据ZIP只有三JSONL与Mac元数据。论文Appendix A.1称完整schema随数据发布，实际没有；[issue #3](https://github.com/THU-KEG/MAVEN-Argument/issues/3)提出同一问题，本轮API读取0回复。未联系作者。不能自行从gold归纳612角色定义后称独立环境。论文解释界面只给当前事件对应规则；即使规范补齐，也须检验简单按type检索是否足够。
2. **ERE规范适用范围未冻结。** RED包含大量事件标注、模态、时间、因果、共指及边界例，不是29541词都为当前关系任务必要。MAVEN限定TIMEX类别、六种时间关系及方向、两种简化因果关系，并用时间端点排序推关系；这些改动必须显式纳入E，核对缺边/跨时间轴语义。当前仅取得链接文件的字节哈希，未锁RED commit及完成适用章节审计。

原例正文还含UNK替换，现有跨度检查不能证明Wikipedia原始信息无损；本轮输入只能称作者发布文本。不能用与测试共享的gold簇/参数做隐式先验。test中events字段缺失按0计数只表示隐藏结构，不表示零事件。没有public快照、实体近重复/规范例排除、独立确认、模型准确率或收益。许可仍须区分仓库代码与Wikipedia派生数据，本轮未全面核验再分发条件。

证据目录artifact/evidence/shared-environment-audit-20260908-v65含下载URL/SHA256、Git验证、全量audit.py与audit-private.json；原资产位于data同名v65。新工程测试0，无模型/作者代码执行；prompt/种子/预算/缓存/确认split不适用。下一步优先ERE适用规范、真实具体关系及可构造的public/gold边界，仍只算同一个MAVEN湖。
