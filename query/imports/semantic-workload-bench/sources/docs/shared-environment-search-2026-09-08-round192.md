# 增量192：MPQA原始论文与清理版本边界

仍11/15开发可构造来源，本轮不新增。继191继续补源：下载[2005原始标注论文](https://people.cs.pitt.edu/~wiebe/pubs/papers/lre05.pdf)，361851bytes、50PDF页、提取17563词；下载[2024清理及模型论文](https://aclanthology.org/2024.lrec-main.1093.pdf)，640293bytes、15页；完整克隆其[作者仓库](https://github.com/theSaeed/opinion-mining-using-llms)，commit `541e6c8e7f6f77b82e8de670d777e4db4d6a376f`、39tracked files。原件data/shared-environment-audit-20260908-v192；逐文件SHA256/下载错误/patch清单在artifact/evidence/shared-environment-audit-20260908-v192。Wilson学位论文此次连接超时，未取得，未伪记下载成功。

50页原论文讨论标注方案、例子、统计、训练与一致性；它的§6.1和参考文献仍另引Wiebe2002技术报告TR-02-101完整说明。不能将50页全部作为此任务的必要规范长度。2024仓库要求自行下载MPQA2.0，未包含database.mpqa.2.0原文；191包为1.2，不能给2.0清理脚本当匹配源。本轮仅阅读，不安装、不运行、不应用patch。

清理研究论文§2.2明确有修正与删除：175条跨度/21文档修正、1文档58条排字修正、5文档5个agent跨度去撇号、2文档133条不可匹配标注删除，以及206条特殊字符处理。这些是论文作者报告，不是本次重跑结果。本次直接核仓库patch：33文件块，其中31个man_anns文件，另包括doclist等；不将patch文件数与论文各类“文档数”相加或强行对齐。一个可核差异：20011024/21.21.31-27111的agent id25，从1016:1017改1015:1016，nested-source=w,putin,putin不变。另20020203/20.46.36-9539存在删除119行的hunk，里面包含结构行，不能把119行说成119个独立gold意见。

这说明使用cleaned数据需要独立版本契约与重新核验；不能用原版gold评分清理版输入，也不能让Agent读取这些当前样本patch来“修正答案”。版本1.2/2.0/3.0及2024清理版仍是同一湖谱系，不增加独立湖数。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold |
|---|---|---|---|---|
| 新闻→主观表达/持有者→可归属意见清单 | 191已得535份LRE1.2标注及GATE token；原始文本映射待核 | 新得50页原始研究论文；完整规范另引、未得 | 2024清理仓库用于构造审计，不给模型答案patch | 只能选定同版本gold；禁止把2.0清理gold混入1.2 |
| 表达→类型/极性/强度→汇总 | 191例complaining850:861 | 上下文极性与强度规范，必要长篇幅待证 | 同文档公开上下文，未冻结 | 原生negative/medium；不据此预设模型成功 |

| 类python的DAG | 具体数值 | 边界 |
|---|---|---|
| `scan(versioned_docs).sem_map(extract,E).explode().sem_map(attributes,E)` | 191实际535文档；本轮39仓库文件 | 仓库文件不是批处理items，未新增可执行快照 |
| `construct(raw, source_lock).validate_offsets().seal(public,private)` | patch33文件块，31man_anns | 这是构造DAG，不是被测语意算子；本轮未应用patch |

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
|---|---|---|---|---|
| 冻结文本版本上的表达/来源/属性；实际未知 | 同一E与上下文上固定调用→schema/跨度检查 | 同一目标；实际未知 | ==核公开E版本，查直接主观表达与报道、嵌套来源== → 抽取 → 检查 | `OpinionExtractor(version, rules, source_graph, validator)` |
| 不应输出某条patch作为推理结果 | 构造完成后不接触当前gold修正表 | 同样不能读取patch取答案 | ==检查公开跨度是否落在文本范围==，仅公开输入验证 | `validate_public_offsets`；不含私有修正表 |

方法均未执行；==表示可观察环境查阅，不记录私人思维链。E-only编译、CodingAgent、固定检索与批量Agent必须共享同资源与工具；不要预设单轨迹提取优于直接编译规范。许可方面，本次下载不建立原新闻再分发授权；保留原件在忽略目录。

下一步转查其他独立来源，MPQA保留完整规范、原始正文及版本绑定缺口；不能用反复格式审计替代第12–15个实际来源。
