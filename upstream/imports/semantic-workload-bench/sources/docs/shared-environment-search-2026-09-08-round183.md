# 增量183：PCC范围语义纠正与标签版本差异

上一轮有有效进展，本轮继续核验，仍10/15，PCC未升格。主数据、原论文和手册复用181；本轮另下载[pyMMAX2原论文](https://aclanthology.org/2020.law-1.16.pdf)和[完整作者仓库](https://github.com/nlpAThits/pyMMAX2)，commit `751f0e295f30430076d601e832a4def25b518e92`、11 tracked files。原件`data/shared-environment-audit-20260908-v183/`，逐文件bytes/SHA256在`artifact/evidence/shared-environment-audit-20260908-v183/downloads.json`。

## 已解决：四处词号缺口不是跨度错误

作者Basedata.interpolate_span（pyMMAX2.py:2154）从DCELEMENTS按顺序收集首末ID之间实际存在的节点，不生成整数ID范围。本轮用AST只提取这个无依赖方法，实际执行4个已观察案例；不是完整Java/MMAX运行，也没有修改上游代码。maz-17953的word191..194输出191、192、194；其余三例同样成功。因此撤销把这些词号缺口视为跨度失败的可能推断。182记录保留，解释以本轮为准。

## 新证据：手册与发布标签不一致

手册印刷第18页明确未采用Disjunction，将其并入Conjunction；实际10篇共20条parent边仍标disjunction。其余已观察非span关系均找到同名定义标题（大小写不敏感），这只是清单检查，不是所有实例符合定义证明。span是结构标记，本就不应按语义关系标题查找。

具体10篇名单、边ID及四个范围probe完整输出在`probe.json`。例如maz-19012的11→30与group28→30均为disjunction。不能一边提供现行手册、一边把原生disjunction当唯一正确答案，更不能默默将20条重命名后仍称原生gold。可以未来显式定义版本转换或开发排除，但需先审计其余差异。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold |
|---|---|---|---|---|
| 每篇解析共指关系并输出前件清单 | 176篇真实评论，原词序/ID | PCC手册PM/SM/群组与指代规则 | 作者MMAX范围解释器属于公开格式工具 | 原MMAX前件；1悬空group目标、190空前件语义仍待查 |
| 每篇解析RST结构并统计关系 | 原生EDU及全文 | 手册第10章及第18页适配说明 | 标题独立规则；固定图检查 | 5102原生边中20 disjunction与提供的手册不一致 |

| 类python的DAG | 具体数值/例子 | 边界 |
|---|---|---|
| `scan(docs).decode_spans().sem_map(antecedent,E).project(edges)` | word191..194解码3个实际词节点191/192/194；4例作者方法probe成功 | decode_spans是确定程序，不能计作Agent语义优势 |
| `scan(docs).sem_map(rst,E).explode(edges).aggregate()` | maz-19012两条源边是disjunction；E要求归入Conjunction | 未决定映射，尚不可直接给该例报唯一规范gold |

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
|---|---|---|---|---|
| 共指例目标仍Sie→secondary markable_2；实际未知 | 同一个固定范围解码器→固定检索/sem_map；前件引用检查 | 相同目标，实际未知 | ==核对跨层候选与PM/SM规则== → 输出前件 → 引用检查 | `AntecedentResolver(E_version, decoded_spans, layer_rules, budget)` |
| disjunction例尚无冻结的一致评分目标 | 提供规范版本后执行sem_map；先解决gold契约 | 同样不能预设正确输出 | ==发现规范/标签版本冲突== → 报研究侧待决；不可读私有gold后自行改答案 | `RSTParser(frozen_inventory, title_policy, graph_rules)`，版本待冻结 |

表为待测设计；无LOTUS/Agent实验、无轨迹提取、无E必要性证据。固定程序、E-only编译和Coding Agent均须同资源。下一步是PCC手册示例全文重叠与可构造范围决策，不把修复数据格式等同于证明研究方法。
