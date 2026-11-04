# 第52增量：CGBench任务参数及COL6A1独立机制背景

本轮补一个可定位的输入缺口，不新增合格湖。复用第15–20轮已下载原论文、完整作者仓库和全部246作者数据文件、63页SOP9；来源/哈希见第20轮，不重复计湖。

## 新核验

`audit_params.py`重新读取检查包615查询：gene、disease、moi、pmid、paper_path均无空项；MOI为AR308、AD233、XL22、UD7、SD10、MT35。非空不证明值语义正确，不能把UD等缩写自行猜为某种机制。审计脚本起初将PMID当裸数字匹配，实际格式为`PubMed:26438297`；已修正，恢复同论文AD/AR两个查询，未改原数据。

此前例子只用论文找不到人类显性机制。本轮找到[GeneReviews：Collagen VI-Related Dystrophies](https://www.ncbi.nlm.nih.gov/books/NBK1503/?report=printable)，页面明确最后更新2021-03-11；“Mechanism of disease causation”区分显性负效应变异与隐性功能缺失变异，指出杂合缺失不支持单倍剂量不足机制。它提供了独立于当前CGBench gold的背景依据，但这是科学综述，不能单独规定专家应打几分。

网页工具实际读取该章节；本地PDF和printable HTML请求均HTTP403，失败收据保存。**没有取得章节本地原文件，也没有把本次摘要挂入public包冒充原始文献。** 原论文/作者仓库已在前轮取得，不受此次辅助文献下载失败影响。

## 三表

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold |
|---|---|---|---|---|
| 按SOP9为gene/disease/MOI/paper输出实验性证据类别和分值，再按类别汇总 | 官方63页SOP9 | 615查询/568论文，参数完整；COL6A1的AD与AR查询指向相同犬模型论文 | 本轮定位GeneReviews2021机制章节；尚未本地冻结，不称已供模型执行 | 已有773条专家选定证据；COL6A1同篇AD1分、AR2分 |

| 类python的DAG | 具体数值/行为 | 证据边界 |
|---|---|---|
| `scan(615).join(papers).join(background_by_target)` | 当前参数缺失0；新增背景仅定位COL6A1这一个目标族 | 背景检索应按公开gene/disease选，不能按当前gold理由挑全部资源 |
| `sem_map(experimental_evidence_set, SOP9, target, paper, background)` | 同一篇犬隐性null模型，AD/AR参考1/2 | GeneReviews支持机制不同；不能从机制不同逻辑必然推得减1分 |
| `groupby(category).aggregate(scores)` | 保留每查询的类别/分数；本轮未计算预测 | 专家选定集合非穷尽科学证据；不能把未标证据直接判false，也不能替代最终gene-disease有效性评分 |

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent 的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
|---|---|---|---|---|
| 发布参考AD1/AR2；未执行，精确分数无法由此次背景核验保证 | 固定提取模型扰动及表型，检索与Agent相同背景，条件化机制匹配，再按SOP打分 | 同一参考，无提升预设 | ==确认MOI；核犬模型null作用；查询人类显性负效应及隐性功能缺失背景；对照SOP检查评分依据==→输出类别、分数、证据 | `PaperExperimentCache + TargetMechanismLookup + SOPScoring + UncertaintyGate`；缓存实验事实，评分必须依目标参数；没有真实执行/提取成果 |

## 对后续构造的影响

这一背景缺口有公开解决路径，不应再笼统写成“没有机制来源”。但还需取得可冻结原文、系统化覆盖其他目标的背景、处理跨论文证据和curator选择范围。本轮不根据已见gold补专用评分分支，不把原测试例变成新确认样本。

模型/作者代码执行0、新工程测试0；实际执行参数审计和下载尝试，均已终止，无活动进程。合格仍1/10，目标继续。
