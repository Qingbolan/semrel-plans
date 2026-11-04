# 增量215：AnnoCTR非明示ID切片与多目标契约

仍12/15。继续213已下载的[原论文](https://aclanthology.org/2024.lrec-main.103.pdf)和[完整作者仓库](https://github.com/boschresearch/anno-ctr-lrec-coling-2024)。本轮只做原生数据审计，不运行模型，不改变源标签。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold |
|---|---|---|---|---|
| 给定提及及报告→实体集合 | 全120篇中90篇未匹配显式T/TA编号 | 冻结ATT&CK定义库 | 给定提及及前后文 | 该切片3104行：TECHNIQUE1772、TACTIC506、TOOL31、GROUP276、MALWARE518、CON1；14行缺KG目标 |
| 行为描述→技术链接 | 同切片中的技术提及 | 同技术定义与指南 | 平台/动作/目的语境 | 尚未剔除直接技术名称或检查全部标签范围，不称E必要性已证实 |

| 类python的DAG | 具体数值 | 本轮边界 |
|---|---|---|
| `reports.filter(no_explicit_attack_id)` | 90/120篇 | 只按公开文本正则筛选，未读gold决定是否保留；不是无答案捷径证明 |
| `given_mentions.sem_map(link_set,E,report)` | 全量43组相同上下文有重复行，其中2组多个不同URL | 多目标可能是合法gold；不能自动选首个或当单标签冲突删除 |
| `links.explode().groupby(report).unique(url)` | 切片3104链接行 | 源行数不是独立提及数，须先明确实例/集合契约 |

具体切片例仍有“Standard Application Layer Protocols for communication between malware and command and control”→T1071。这篇无显式T编号，但提及已经近似技术名称；因此编号过滤只能减少查表捷径，不能证明剩余记录一定需要长环境推理。

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
|---|---|---|---|---|
| 该例{T1071}为记录目标，未实测 | 名称检索或固定定义检索→语义消歧→集合校验 | 同目标，未实测 | ==检查技术名称及定义、全文语境==→输出目标集合 | `EntityRetriever → SetLinker → SetValidator`；固定流程也能用名称检索 |
| 相同上下文可输出多个目标，具体规则待核 | 同资源固定候选排序/多标签决策 | 同契约，不保证优势 | ==核对候选是否同时成立==→集合输出 | 不强制单标签；未提取真实operator |

负例范围核验：完整带负例导出中TECHNIQUE行8494，包括3348个官方MITRE链接、5119个No Annotation、27个作者软件实体链接（Buer24、Redline stealer2、HallajPro1）。最后27个不能当官方技术ID，也不能自动当负例。仅因字段写TECHNIQUE就构造技术分类任务会混淆导出语义。

214剩余7个定位残差的mention字串均能在原报告中找到，说明尚不能判为缺失原文；有NBSP、前后文差异及两个截去首字母的mention（nsiders、elling）。仍需确认原标注与转换边界，未修改gold提及。原始64条上下文多次匹配与43组导出相同上下文重复是不同统计，不能混用。

证据[215审计](../artifact/evidence/shared-environment-audit-20260908-v215/)保存90篇选择规则、所有文档ID命中、14缺项和例子。没有构造确认split、公开视图、模型/成本或E必要性实测。下一步核作者导出语义与集合实例，判断可合法构造的具体任务；不把切片统计直接升级为合格湖。
