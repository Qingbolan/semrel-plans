# 增量196：AMR长规范与《小王子》公开镜像

已下载[AMR原论文](https://aclanthology.org/W13-2322.pdf)158383bytes，完整[规范作者仓库](https://github.com/amrisi/amr-guidelines)commit `3e1daf8483385fa9386b1c38092209ebd2349c7b`，3tracked files；amr.md97766bytes、14404词。它是持续更新规范，并依赖OntoNotes谓词/角色及另一个AMR Dictionary；不能仅下载amr.md就声称完整词义/角色资源已齐。

官方amr.isi.edu首页与v3.0语料入口本机DNS失败。实际从[公开镜像文件](https://github.com/flipz357/AMR-World/blob/main/data/reference_amrs/amr-bank-struct-v3.0.txt)下载689852bytes；这不是本轮官方字节核验。原件data/shared-environment-audit-20260908-v196，下载收据（含失败）、完整规范repo清单、audit.json在artifact/evidence/shared-environment-audit-20260908-v196。尚未下载完整镜像仓库，不把单文件说成完整数据作者仓库；完整下载的是规范作者仓库。

实际按id/snt注释和空行分块：1562blocks、1562unique IDs、0缺snt，307blocks含字面`:polarity -`。未运行PENMAN解析器，307不是已验证语义分类gold数量。头部声明release v3.0、2018-01-25生成，并保留ISI annotator等元信息；不是据此独立验证全部人工来源和官方字节一致。

输入为已有文学作品的句子，内容是虚构故事；不是LLM临时合成句子，也不是真实保险/医疗决策。1562句共享AMR规范但只来自1部作品，不能报1562独立文档。章节、同情节及翻译版本隔离要另审，跨语言同源版本不能凑多个独立湖。

具体lpp_1943.5描述蛇吞食猎物且不咀嚼；native图将`:polarity -`挂在chew-01节点上，swallow-01没有该否定边。下游若检索“明确否定的行为”，需要保留否定范围而不是把整句所有事件都标为负。此例来自本次镜像实际读取；它单独只涉及短否定规则，不能代表整部复杂规范必要性。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold |
|---|---|---|---|---|
| 逐句抽取规范AMR图，再形成事件/参与者索引 | 1562镜像句子，每句有snt及graph；1部作品 | 14404词AMR规范；OntoNotes角色库及AMR Dictionary未齐 | 公开上下文，graph与annotator元数据隔离 | 原生图，版本/解析/角色绑定待核 |
| 图抽取→否定范围→否定行为清单 | 同句输入 | negation章节及框架语义 | 上游预测AMR，不能给gold图却称端到端 | lpp_1943.5：chew-01负，swallow-01未带负极性 |
| 图抽取→重入/共享论元→事件关系索引 | 同句和上下文 | reentrancy、控制结构、角色规范 | 上游预测事件/角色 | 同人工图派生目标，非独立下游事实标注 |

| 类python的DAG | 具体数值 | 边界 |
|---|---|---|
| `scan(sentences).sem_map(parse_amr,E).explode_events()` | 1562句/1部作品 | 完整必要词典、源版本尚未建立 |
| `events.filter(polarity_is_negative).project(predicate)` | 307图块字面出现负极性；例chew-01 | 上游parse是关键语义步骤；下游filter可普通程序执行 |
| `graphs.sem_map(resolve_roles,E).join_shared_arguments()` | 全图结构计数/评分未执行 | 不将另加多任务计为独立湖 |

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
|---|---|---|---|---|
| 否定挂chew-01，不扩散到所有事件；实际未知 | 完整同规范及词典固定解析→图检查→程序filter，可共享词典检索 | 同目标，不预设优势 | ==查否定范围规则、谓词角色定义== → 生成图 → 公开检查 | `AMRParser(schema_version, frame_lookup, scope_resolver, validator)` |
| 规范中的重入及论元结构；实际未知 | 固定检索/分步解析，允许同资源缓存 | 同结构，实际未知 | ==查控制/共指规则及词义== → 绑定节点 → 校验 | `RoleBinder + ReentrancyResolver` |

未运行任何模型或评分，==为可观察环境查阅。固定程序/CodingAgent/E-only编译均可直接编译规范，不将图复杂自动归因于Agent优势。许可未确认，不将规范或镜像公开等同于文本自由再分发。当前保持11/15开发可构造，AMR待官方源可追溯性、完整词典与框架版本、图解析及必要E范围验证。
