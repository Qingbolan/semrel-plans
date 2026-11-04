# 第二十九增量：CGBench 同论文、不同任务参数的真实评分差异

**本轮新增环境依赖证据，仍不新增合格湖，累计1/10。** 复用已下载的原论文、完整作者仓库、全部246个作者数据文件及官方SOP9，不重复下载。来源及版本见[第20轮](shared-environment-search-2026-09-08-round20.md)：[原论文](https://arxiv.org/abs/2510.11985)、[作者仓库](https://github.com/owencqueen/cgbench) commit `db9f94152ca1872c8be8d8411040dcba2610b50b`、[数据](https://huggingface.co/datasets/owencqueen/cgbench_data) revision `6b017e57f18ccb1e6476260d9af4daa30508a523`、[官方SOP9](https://www.clinicalgenome.org/site/assets/files/5391/version_9_gene_curation_sop_final2.pdf)63页。

## 新证据及不能越过的边界

615查询/568论文中，28个PMID对应多个查询；14个PMID的查询之间存在类别或分值集合差异。这不是14个独立环境或人为修改规则的反事实实验：共享SOP9不变，gene/disease/MOI任务参数不同，有些差异还可能反映专家选择的证据项不同。不能仅凭这一统计证明长SOP必要。

最清楚的一对是PMID26438297：**同一COL6A1、同一collagen 6-related myopathy、同一篇论文，AD任务gold=1分，AR任务gold=2分**，类别均为非人动物模型。私有专家理由明确：双等位基因null模型与人类显性疾病的dominant-negative机制不一致。公开论文有犬家系和隐性遗传分析；本次全文字符串查找没有`dominant`，因此不能声称该篇论文已提供人类显性机制所需的全部知识。这个配对同时证明任务参数不能忽略，并定位了具体背景资源缺口。

第二对PMID34706494/HBB：AR beta-thalassemia任务gold为非人模型救援2分，AD dominant beta-thalassemia任务为模型证据0分，原因是模型剪接变异机制与目标显性疾病不同。这里类别也不同，不应伪装成只改变一个变量的精确反事实。

另一个重要字段审计：773条证据中Score748条、Review25条；Review包含17个0分及8个正分，而Score也含72个0分。**Review不能直接翻译成ABSTAIN或0分，Score也不等于有效正例。** 当前尚未核实Review的全部UI工作流含义，保留原字段而不自创标签映射。

本次对第20轮已提出的固定筛选条件做私有统计：263查询含非人动物模型类别，其中15查询存在该类别绝对分值>2的证据。15是发布标注上的参考数量，非模型预测、非全部科学证据的完备真值。不能把其余600自动解释为没有这种科学证据，只能说发布集合未标该条件；源标注穷尽性仍需核验。

## 三表

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | 私有gold |
|---|---|---|---|---|
| 按SOP9抽取每个gene/disease/MOI/paper的实验性证据集合，并筛选含高于默认2分的非人动物模型证据的查询 | 冻结官方63页SOP9；直接实验规则主要38–42页及附录例子，不能声称63页都必需 | 615查询及568篇全文文本 | 机制背景资源仍有具体欠账；不能直接公开gold专家理由填空 | 773专家证据；263查询含模型项，15符合发布集合中的>2条件 |
| PMID26438297：比较同一COL6A1疾病的AD/AR任务，验证算子是否读取MOI | 模型与目标疾病一致性的共享规则 | 完全相同论文，公开路径`papers/p_584d58062c4b43b02ed4.txt` | 犬隐性家系在论文内；人类显性机制背景尚未验证完整来源 | AD=模型1分；AR=模型2分；在>2筛选下两者均False |
| PMID34706494：HBB两个疾病/遗传方式任务 | 同SOP9的模型、救援及机制规则 | 同论文公开路径`papers/p_81862a4c714b33eadaef.txt` | 模型、疾病与遗传方式需一起核对 | AR=救援2分；AD=模型0分；不是“有动物实验就得2分” |

| 类python的DAG | 具体数值 | 评价边界 |
|---|---|---|
| `scan(queries).join(papers)` | 615查询/568全文 | 现有第20轮检查包，非新增独立数据湖 |
| `sem_map(evidence_set, E=SOP9, params=(gene,disease,moi))` | 773条发布证据，13类别 | 集合大小由输出决定，不能预喂gold类别 |
| `sem_filter(any(category==nonhuman_model and score>2))` | 发布集合参考15选中/600未标选中 | 不能当作穷尽科学证据的已证实二元gold |
| `project(id).count()` | 参考15，实际结果未知 | 同报中间类别/分数质量，防止聚合掩盖AD/AR错误 |
| `paired_context_audit(same_paper_queries)` | 28多查询PMID，14有类别/分值差异 | 开发诊断；按论文分组，不能跨示范/确认泄漏 |

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
|---|---|---|---|---|
| COL6A1例参考AD1/AR2，最终>2均False；实际未运行 | 同一SOP和全文，固定抽取扰动/表型/遗传方式，检索同样可用的机制背景，比较目标机制后评分；允许缓存论文抽取 | 同参考值，不预言更准确；背景不足允许ABSTAIN | ==读任务MOI==→==从论文确认犬模型为隐性null==→==查允许背景中的人类显性机制==→对照SOP输出类别、分值和证据；不能读当前专家注释 | `ExperimentalEvidenceOperator(E_hash, target_gene_disease_moi, paper_experiments, permitted_background, category_rules, scoring, abstain)`；共享论文缓存必须与目标参数条件化评分分开 |
| HBB例目标AR救援2/AD模型0 | 固定模型/救援类别判断与机制核对可能正确完成，无需强制Agent多轮 | 同目标，未生成真实轨迹 | ==区分表型相似与致病机制相同==→==核对救援针对的变异==→输出集合 | 不能把“Review→0”或“动物模型→2”编译为捷径；与E-only编译、固定工具、Coding Agent比较 |

脚本及私有开发诊断位于`artifact/evidence/shared-environment-audit-20260908-v29/`。该目录含gold理由/选中ID，不挂载到被测系统。没有新增公开输入，也未依gold筛选确认集或补充模型资源。

本轮仍未解决：长规则的必要范围、全文之外背景来源、发布证据集合是否穷尽、47查询跨论文引用缺口及确认划分。新的配对证据改善了判断依据，但不能仅因发现有差异的样本就宣布第二湖合格。无模型调用、无新下载、无作者代码执行、新增工程测试0；当前只做开发数据审计。
