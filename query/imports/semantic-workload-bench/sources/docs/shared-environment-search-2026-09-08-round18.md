# 第十八增量：CIViC，真实专家策展批量与长规范

本轮结论：**保留为优先补证候选，未计入严格合格数。** 原始规范论文、61页补充材料、当前完整官方仓库和完整月度证据TSV均已下载。批量与人工标签成立；规范版本绑定、全部原始文献输入以及必要规则复杂度仍未完成验证。不能把61页含截图的材料直接称为61页必要推理。

来源：[Danos et al. 2019原论文](https://link.springer.com/article/10.1186/s13073-019-0687-x)、[61页补充SOP](https://media.springernature.com/original/springer-static/esm/art%3A10.1186%2Fs13073-019-0687-x/MediaObjects/13073_2019_687_MOESM1_ESM.pdf)、[官方仓库](https://github.com/griffithlab/civic-v2)、[官方开放数据登记](https://registry.opendata.aws/civic/)、[2026-09-01完整TSV](https://civic-aws-opendata.s3.us-west-2.amazonaws.com/ClinicalEvidenceSummaries/date=01-Sep-2026/ClinicalEvidenceSummaries.tsv)。规范CC BY 4.0、策展数据CC0；源文献许可单独核验。

本地原资产：`data/shared-environment-audit-20260908-v18/`。原论文12页/1,837,865 bytes；补充61页/7,404,803 bytes；仓库ZIP15,973,317 bytes，commit `da062f9e7d773a34184210fd8b20c704d95ca61c`，5,561个blob逐个Git哈希匹配，tree未截断。该仓库是当前官方v2源码，不冒充2019论文当时的软件版本。TSV4,118,431 bytes。来源收据和审计在`artifact/evidence/shared-environment-audit-20260908-v18/`。

## 实际数据与任务

4,906个独立evidence_id，全部accepted，其中157个flagged。4,884行PubMed来源、2,239个独立PMID；ASCO19、ASH3。Predictive共有2,869行；限定PubMed且非flagged得到2,805行、1,339个PMID、2,772个(profile,disease,therapy,therapy_interaction,PMID)查询键。因此一个查询可能有多个证据标签，不能静默去重成一个单标签。

| Query | 数据湖 数据1：共享E | 数据湖 数据2：批量x | 数据湖 数据3：实际源证据 | 私有gold，不给模型 |
|---|---|---|---|---|
| 按CIViC规范逐项提取治疗证据的level、direction、significance，然后筛选支持Reduced Sensitivity的查询 | 2019原论文12页+补充SOP61页，含Table S6比较情境、S7意义定义、证据等级及评分说明 | 非flagged/PubMed/Predictive的2,772个查询键；只公开profile、disease、therapy、interaction及citation定位 | 1,339篇独立文献需要补齐；本轮只下载PMID18955451 XML摘要，不能声称全文湖就绪 | 2,805条accepted结构化证据；direction/significance/level/rating/statement全部隔离 |
| 开发例：KIT exon 9 mutation，GIST，imatinib，PMID18955451 | S6区分同治疗下不同变异、同变异下不同治疗；较低敏感性不等于耐药 | EID2477仅为私有回连ID，开发曝光，不进入确认集 | [原研究摘要](https://pubmed.ncbi.nlm.nih.gov/18955451/)报告exon11和exon9的反应率71.7% vs44.4%；exon9在800mg与400mg下67% vs17%。本轮未下载其全文 | Predictive / Supports / B / Reduced Sensitivity，rating2；不是预测值 |

**具体依赖E的证据**：补充Table S7给出概括定义，Table S6进一步限制比较情境。只比较同一变异不同剂量，不能据此直接贴Reduced Sensitivity；本例同时存在跨变异比较，需从论文分离两种比较。Gold的statement主要描述剂量，因此不能把statement当唯一输入，也不能把它当充分的独立理由证明。已有accepted标签是策展参考标准，不是临床真理。

| 类python的DAG | 具体数值/边界 | 下游输出 |
|---|---|---|
| `scan(tsv).where(Predictive & PubMed & ~flagged)`（构造侧） | 2,805条证据；当前gold筛选定义任务人群，属于annotation-defined队列 | 不声称对所有未策展文献的发现召回率 |
| `group_by(profile,disease,therapy,interaction,pmid)` | 2,772查询、1,339文献；同论文与相关profile须分组隔离 | 每query的gold为集合 |
| `papers.join(queries).sem_map(curate_under_E)` | 批量源论文未齐，因此尚不可运行完整默认路径 | level/direction/significance集合及源证据 |
| `sem_filter(any(Supports & ReducedSensitivity)).project(query_id).count()` | 16条证据的significance为Reduced Sensitivity；尚非Supports去重后count | 必须从完整预测生成清单，不能将16硬编码为答案 |
| `score(private_sets, frozen_outputs)` | 开发例1条；未运行模型；无准确率或成本值 | 集合匹配、清单P/R、ABSTAIN、完整摊销成本 |

## 方法表：全为预期，非已运行结果

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
|---|---|---|---|---|
| 公平目标为本例`{B, Supports, Reduced Sensitivity}`；可能正确，不能预写其必错 | 固定sem_map读取同样的E、query、论文；固定检索/分段抽取也应允许。抽出跨变异及跨剂量比较，按S6赋值；sem_filter形成清单 | 同一目标集合；是否改善及其成本未知 | ==定位S6/S7并核对比较对象== → ==读取论文各组人群、剂量和终点，分离两种比较== → 引用证据并返回标签；缺证据ABSTAIN。这里描述可观察动作，不要求私人思维链 | `CurationOperator(E_hash, version, schema)`：检索规范→抽取`Comparison(variant,disease,therapy,dose,endpoint,groups)`→规则适用性检查→标签集合→来源/ABSTAIN。不得写死KIT、PMID或本例答案 |
| E-only编译器可能直接正确，也可能与轨迹提取相同 | 先从SOP编译比较情境规则，复用到整个batch；共享文献只解析一次 | Agent未必需要逐行探索 | ==仅在证据缺口/比较冲突时补查允许的公开材料==；固定程序可用同一工具 | 必须比较E-only、Coding Agent、固定检索、批Agent、单轨迹提取；不把“能编译规范”当成轨迹必要性证据 |

尚缺：2019规范和2026标签的冻结版本匹配（现代标签包含Oncogenic）；规范内示例与评测记录重叠审计；完整公开文献及表格、许可；精确实体/论文/试验分组；相同query多标签的任务消歧；规则有效范围、E消融与强固定基线。长SOP中界面截图和无关任务章节必须单列。**这是一份可追溯候选，不是已经满足全部硬门槛的第1个湖。**
