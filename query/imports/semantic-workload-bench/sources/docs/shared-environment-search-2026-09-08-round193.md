# 增量193：WLP/X-WLP真实协议与过程图

新查WLP谱系，不与其他湖合并，也不将其X-WLP子集另计一个湖。已下载两篇原论文与两个完整作者仓库：

- [WLP原论文](https://arxiv.org/pdf/1805.00195)：525295bytes；作者旧PDF入口404后改用其README链接的arXiv。
- [WLP仓库](https://github.com/chaitanya2334/WLP-Dataset)：commit `1f51ae6e620a5aa3590acf725713f430783f56d7`，1246tracked files。
- [X-WLP原论文](https://aclanthology.org/2021.eacl-main.187.pdf)：686375bytes。
- [X-WLP数据作者仓库](https://github.com/ronentk/textlabs-xwlp-data)：commit `db06ed1f27f9e9ef86a7324df5a0ee3607956db1`，1131tracked files；未下载另一个建模代码仓库。
- [X-WLP原始指南](https://textlabs.github.io/TextLabs/misc/Annotation_Instructions.pdf)：1618478bytes，22页、3501提取词。含界面/操作说明，不能把22页全部算必要领域规则。

原件data/shared-environment-audit-20260908-v193；逐文件commit/bytes/SHA256、下载失败与可复现audit.py/json见artifact/evidence/shared-environment-audit-20260908-v193。没有安装或执行上游代码。

## 本次原生观察及限制

WLP标准ann文件：train374/dev123/test125，共622协议，README限定句内动作、实体与关系。X-WLP是其中279份协议的过程级扩展；人工通过文本模拟器标注，起点有WLP实体及预载关系，不是279次真实实验执行记录。所需共享E为标注/过程图表示规范，各篇实验protocol自身是xi，不能把每篇不同protocol当共同E。

本次279PEG JSON均可解析，共15070nodes、15125links、1703个co_ref_of节点。279个graph.sentences都与对应txt.splitlines完全一致；此检查不证明每个节点offset正确，也未证明PEG与AMR全等。无重复节点ID、links端点缺失；但节点inputs/outputs中发现14处引用缺失，涉及12协议（完整列表audit.json，重复输入/输出各记一处）。这是结构一致性缺口，可能涉及转换残留，尚不直接断言人工判断错误。原件不修复，未删除文档构造“通过集”。

13类operation实际计数：transfer1301、temp_treat503、default469、mix346、spin282、create178、destroy170、remove168、measure149、wash146、time114、seal68、convert21。类型来自人工扩展/模拟器表示，不是实验成功率、合规性或生物安全判定gold。指南前部明确无警告不代表完美标注。

具体协议0的op_13：原文位置550:553为Add，native type=transfer_op，inputs={a:rg_7,site:loc_0}，outputs=[loc_0]；对应display_name分别为`PB3 Neutralization Buffe`和`tube`（前者源标签确实缺末尾r，未改）。step134是标注模拟器时步，不是实测实验持续时间。该协议还有另一节点悬空引用，因此仅作开发结构例，不列为已通过评测实例。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold |
|---|---|---|---|---|
| 将协议转换为带类型的操作清单 | 279原始协议txt；WLP622为母集 | 同一X-WLP指南＋原论文schema＋types目录；必要长E尚未证明 | 如采用给定WLP实体，明确作为上游输入且只给allowlist；不暴露PEG类型 | PEG13类operation及触发词，例op_13=transfer_op |
| 将各操作绑定输入、目标位置及输出，再形成流程图 | 同一协议上下文 | 各类操作槽位和状态语义 | 上游操作预测、可公开检查的图约束 | op_13 a=rg_7,site=loc_0,output=loc_0；其他节点含14处引用缺口 |
| 解析跨句物料共指，汇总物料轨迹 | 同一279协议与显式给定或预测实体 | 共指与时序依赖规则 | 不含gold边的上游实体表 | 1703 co_ref_of节点；无独立实验效果gold |

| 类python的DAG | 具体数值 | 边界 |
|---|---|---|
| `scan(protocols).sem_map(type_operations,E).explode()` | 279协议，13类操作 | xi为protocol；不得声称279篇不同protocol是共享E |
| `operations.sem_map(bind_arguments,E,doc).groupby(doc).assemble_graph()` | 15070总节点、15125links | 部分输入/输出悬空；不能直接称可运行实验程序 |
| `entities.sem_map(resolve_coreference,E,doc).join(operations).aggregate(material_paths)` | 1703共指节点 | 原生图派生下游gold，不是独立测量的实验结果 |

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
|---|---|---|---|---|
| op_13目标transfer及a/site绑定；实际未知 | 同规范、上下文、上游实体上固定类型→绑定→检查；可缓存schema | 同目标；实际未知 | ==查transfer槽位与输出规则，查先前tube指代== → 输出图节点 → 公共检查 | `OperationMapper(type_rules, slot_schema, context_resolver)` |
| 共指/物料流程图；不预设必然失败 | 固定文档级调用或固定检索流程，允许跨句上下文 | 同结构，实际未知 | ==查共指的时间依赖与物料状态== → 绑定 → 校验 | `EntityStateTracker + CoreferenceResolver` |
| 对悬空gold不能靠模型补出官方答案 | 先由构造侧解释表示缺口再冻结评分 | 同样不能读取private图找答案 | ==检查预测引用只指向公开实体== | `GraphValidator`；不可读取gold修复表 |

==仅为可观察规则查阅/工具动作。批内固定程序、CodingAgent、E-only编译和DataAgent均可共享规范和缓存，未运行任何方法，不填性能差距。来源图标注与模拟器约束混合；没有证据说明只有动态Agent能完成。

当前不计入合格，仍11/15开发可构造来源。优先补核指南中实际必要规则篇幅、槽位版本与14处悬空引用；不能仅以模拟器复杂或protocol长来满足长共享E。X-WLP仓库MIT文件已下载；WLP仓库无独立LICENSE文件，原协议内容权利需与代码/新标注权利分开核验，不据MIT概括整个谱系。
