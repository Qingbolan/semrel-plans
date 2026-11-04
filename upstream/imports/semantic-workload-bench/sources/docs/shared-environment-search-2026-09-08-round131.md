# 第131轮：DrugProt开发构造资格与独立评分

按现有七湖相同的SOURCE_VERIFIED_CONSTRUCTIBLE_DEVELOPMENT标准登记DrugProt为第8个来源可构造候选。不是科学VALIDATED，不表示已有8个通过长环境消融的benchmark。15个完整目标未完成；复杂E相对短规则、E-only编译、固定程序的收益与方法必要性仍未测。

## 资格依据与边界

128轮已下载原24页论文、完整官方语料及评分仓库，129轮原论文Figure3核对13类发布范围，130轮33页规范完整OCR后开发排除并构造2168摘要61730给定实体13452关系，独立验证2173资产的hash/字段/sourceparity。原生来源具有人类关系gold，共享规范有证据充分性、分支/粒度、方向及多标签约定。任务是给定实体的文献关系抽取，不是实际临床决策，也不是端到端NER。

与CHEMDNER重叠的2069篇及资源示例相关文档已从本快照排除；不再将ChemProt计为独立湖。OCR/exact-match排除不证明无语义近重复或训练污染。现阶段只有开发候选资格，无独立确认或模型执行。

## 当前快照具体例

`doc_0000`共有13实体，其中3化学提及、10基因提及，候选笛卡尔积30对。原文表述human type12 RDH将dihydrotestosterone还原成androstanediol。给定实体T1 androstanediol[466:480]、T9 human type12 RDH[417:434]；独立gold仅一条(T1,T9,PRODUCT-OF)。该例来自保留快照而不是被排除的FAQ例。解释限定给定实体候选：不能因未给定底物实体而添加超出任务输入的SUBSTRATE边。本轮查看此例是开发曝光。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold |
| --- | --- | --- | --- | --- |
| 建立文献中的化合物—蛋白代谢产物证据索引 | 2168篇原文 | 61730给定实体 | 33页关系规范+13类发布范围 | doc_0000：androstanediol→human type12 RDH为PRODUCT-OF，给定30对中1条gold |
| 建立文献抑制证据清单 | 同批文档与实体 | 同规范的直接/间接证据和粒度规则 | 固定抽取→类型过滤→文档计数 | 4420条INHIBITOR；不是临床禁忌gold |

| 类python的DAG | 具体数值 | 下游gold |
| --- | --- | --- |
| `records.sem_map(extract_relations,entities,E).explode()` | 2168记录→13452gold关系、145多标签对 | 独立按(record_id,type,arg1,arg2)集合评分 |
| `.filter(type=='PRODUCT-OF').project(record_id,arg1,arg2)` | 全量807条；doc_0000有1条 | 产物清单，保留实体提及级身份 |
| `.filter(type=='INHIBITOR').groupby(record_id).count()` | 全量4420条 | 清单和计数；属于同算子不同下游视图，不另计湖 |

| 预期关键语意算子直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期关键语意算子直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索步骤== | 预期产生的operator结构 |
| --- | --- | --- | --- | --- |
| 未执行；doc_0000目标1条PRODUCT-OF | 同E、原文、给定实体→固定关系提取→类型/引用校验→下游过滤 | 未执行；同样目标，不预设更高准确率 | ==查PRODUCT-OF的化学→蛋白方向==→==核对产物与底物、共现与证据的区别==→输出关系 | `DrugProteinRelations(text,entities,E_version)`允许多标签，给定实体allowlist；ABSTAIN显式输出，公共检索与缓存所有臂同等可用 |

## 独立评分实现与诊断

artifact/evidence/shared-environment-audit-20260908-v131/score.py为本研究快照的RelationEvaluator；不修改作者源码。以每文档关系集合计TP/FP/FN，报micro precision/recall/F1、coverage、全量文档exact accuracy、各类型计数。拒绝缺失/额外/重复记录、重复关系、未知引用/类型及非法ABSTAIN组合。ABSTAIN不能携带关系，计coverage失败且gold关系全为FN；即使空gold文档ABSTAIN也不算文档正确。

check.py实跑：全量gold自比较TP13452/F1=1，仅oracle工程诊断；全ABSTAIN FN13452/文档accuracy0；原作者函数跨文档反例在本实现TP0/FP1/FN1。5类非法输入拒绝通过。保存checks.json；没有把oracle结果写成模型表现。验证为3组评分诊断+5组拒绝检查，未运行仓库单元测试套件。无默认模型运行、无已提取operator、无成本测量。

复跑`python3 artifact/evidence/shared-environment-audit-20260908-v131/check.py`。下一步继续新独立湖检索；DrugProt长E实验作为明确欠账保留，不用反复静态检查冒充实测资源增益。

来源与完整下载收据见128轮，构造与独立parity见130轮。[原论文](https://upcommons.upc.edu/bitstreams/4a4e2dc2-df18-4bcd-893a-ffeadc9bf2b3/download)、[官方语料](https://zenodo.org/records/5119892)、[原作者仓库](https://github.com/tonifuc3m/drugprot-evaluation-library)。
