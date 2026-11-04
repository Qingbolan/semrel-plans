# 增量175：TDTB单侧论元的具体来源差异

复用173原件，仍9/15。本轮为实际新证据：不能凭派生表两侧非空，就认为原生人工标注也完整。未修复、删除或重标源数据。

具体开发例是`data/with_args/train/T00415.tsv`的连接词2696“ดังนั้น”，意义为`Contingency.Cause.Result`。原生最后一列只出现`arg1[2696]`，没有`arg2[2696]`。删除独立`_`空白token、其余token从1编号后，该连接词对应派生2360。这个映射本轮只检查具体例，没有声称全库token parity。

匹配到派生train.rels的同文档同意义行：unit1=2331–2359（29 tokens），unit2=2360–2454（95 tokens）。原生Arg1去除空白后有123 tokens，恰好等于派生unit1与unit2的并集减去连接词2360；它覆盖派生Arg2的94个内容token。原生Arg2为空。因此派生输出改变了原生两侧分配，不能称只是加连接词或重编号。

此例可能涉及修订标注或转换处理，但本轮没有找到说明其依据的转换代码/收据；不能断定哪版语义正确。173完整repo是公开的TSV及派生数据，没有Python转换源码。84个单侧病例不因此全部被判错，也不能一律用派生表覆盖。若将某版本定义为目标，必须明确来源、修订权威和评分单位。

机器可读证据：`artifact/evidence/shared-environment-audit-20260908-v175/probe.json`。源commit仍`226b2f898c7044345fcabec7d449f4d7da29b5d1`；全部原件哈希见173收据。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold / 状态 |
| --- | --- | --- | --- | --- |
| 抽取T00415连接词2696的论元 | 原生新闻token | PDTB3及Thai修改 | 原生人工指针；派生表仅作构造对照 | 原生Arg1包含123非空白tokens，Arg2为空；版本差异未决 |
| 生成该例因果关系行 | 同一段新闻 | Cause.Result方向规则 | 派生unit1=2331–2359、unit2=2360–2454 | 派生29/95两侧并非与原生边界等价；不当独立核验通过 |

| 类python的DAG | 具体数值 | 边界 |
| --- | --- | --- |
| `native_tokens.drop_space_marker().renumber(start=1)` | native2696→derived2360 | 具体例映射，未验证全局 |
| `compare(native_arg1, derived_arg1.union(derived_arg2))` | 并集124；原生123；差1个连接词 | 除连接词外，原生Arg1覆盖派生两侧 |
| `sem_map(argument_binding,E).project(causal_relation)` | 需要先冻结哪版论元gold有依据 | 不运行模型掩盖gold契约未决 |

下表是未执行方法预期。

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
| --- | --- | --- | --- | --- |
| 规范确定后应输出有方向的双论元；目前不能可靠指定此例评分答案 | 原文及同一规范上固定sem_map/检索 | 同一契约要求；不能以更像派生表证明更好 | ==检索Cause.Result和Arg2绑定规则，记录依据==→结构化输出 | `SenseLabeler → ArgumentBinder → RelationTuple` |
| 全量任务前须冻结源标注映射 | 构造侧审计和独立评分 | 相同要求 | ==构造阶段核对源/派生边界==，不允许被测Agent查看评测gold纠错 | 版本审计不算自动学得semantic operator |

本轮关闭“派生字段非空便足以解决单侧问题”的可能解释。TDTB保留候选，后续需正式修订说明、完整Thai规范及许可；下一轮转向新独立来源，避免围绕未解释的派生数据不断补假设。无下载、安装、LLM/模型/prompt实验/训练/种子/token预算/推理并发缓存、正式快照或commit；0测试套件测试。上一轮和本轮都提供改变下一步的新证据，目标保持活动。
