# 静态语义实现质量差距：候选与复现计划

更新：2026-09-05。文献证据按下列版本保留；本轮另已构造CUAD/BioDEX各8条开发pilot并运行比较，见[本地入口](pilot-artifact-guide.md)及report.md。以下数字仍是论文报告，不是本地结果。

## 用户最新确认的研究顺序

先寻找真实重复批任务，实测传统 LOTUS 静态实现的关键步骤质量不足且影响下游；再确认同环境 Data Agent 能改善但成本高；最后从单次 Agent 轨迹自动提取算子，保留质量并降低后续批处理总成本。不能把目标放宽为“即使静态质量已经足够也只研究降成本”。这是要检验的假设，不能通过削弱baseline确保成立。

PCB保留为工程控制：固定算法已在本仓库24条探索记录全对。另已导入旧仓库100条[原生LOTUS实验收据](../artifact/evidence/pcb-native-lotus-20260905/provenance.json)：带模板LOTUS91%、工具Agent92%，改正9/退步8、p=1.0，固定程序100%；并非本仓库复跑，未同时证明明确Agent改善。两个真实纠错案例用于[历史经验开发](historical-experience.md)，不是新的确认样本。

## 优先级与证据级别

| 优先级 | 候选 | 已有依据 | 未建立的结论 |
|---|---|---|---|
| P0 | BioDEX反应识别/标准化 | DocETL论文直接比较LOTUS式map-search-filter，存在排名质量差距 | 当前版本复现、Agent优势、单轨迹提取、完整环境增益 |
| P1 | CUAD条款抽取 | DocETL论文比较LOTUS sem_map，报告抽取F1/召回差距 | 独立模型复现、单类别差距、Agent和环境增益 |
| P2 | LOCO逻辑装配 | LogicQA提供拆分检查问题的实证线索 | 没有LOTUS直接对照，不是已证实gap |
| control | DeepPCB孤立铜 | 本地固定程序可运行并正确完成小批 | 不能作为主优势案例 |

这轮优先复现长文任务的直接文献证据；不以文本结果替代原多模态研究范围。LOCO/MMAD仍作为后续视觉路线，ContractNLI、金融候选保留但不优先于直接LOTUS比较线索。

## 论文证据（冻结阅读版本）

[DocETL arXiv:2410.12189v3，2025-04-01版本](https://arxiv.org/html/2410.12189v3)，§5.1表2与§5.4表6：

| 任务/指标 | LOTUS | DocETL |
|---|---:|---:|
| CUAD Avg F1 | 0.393 | 0.477 |
| CUAD Avg Recall | 0.471 | 0.719 |
| BioDEX RP@5 | 0.213 | 0.281 |
| BioDEX RP@10 | 0.207 | 0.313 |

CUAD使用前50合同；BioDEX使用250论文。BioDEX列是作者复现的LOTUS流程，并非LOTUS原论文分数。F1和RP不是普通accuracy。

比较局限：BioDEX执行使用gpt-4o-mini，但DocETL优化器使用gpt-4o；两条流程排序方法不同、作者复现候选数49。CUAD使用宽松span Jaccard>0.15匹配，存在JSON解析重试披露。必须重新锁定设置和完整成本；这些结果不是同预算通用Data Agent成功的证据，更不是单轨迹实验。

## Baseline版本边界

[现行LOTUS官方概念文档](https://lotus-ai.readthedocs.io/en/stable/core_concepts.html)已区分LLM semantic operators和agentic semantic operators。传统静态baseline应锁定commit、具体调用/优化开关、prompt、输入、模型与取证计划，不能将现行整个LOTUS描述成不支持工具。

同时保留最新agentic实现（如适配可行）、DocETL、固定检索/工具程序、Coding Agent生成程序和批内复用Agent等强对照。先复现论文设置，再报告统一模型/预算设置；二者不混报。不得在运行前写一个未核验的LOTUS版本号。

## 下一次实际实验的进入门槛

1. 核验源数据release、划分、全文/标注与辅助术语的可达性和许可，冻结本地hash。未完成前状态仍为PLANNED。
2. 从源实体分组抽取20–30条开发pilot；不按预期模型错误选例。抽样只为开发，不足以支持正式差距。
3. 按原任务复现LOTUS式流程和DocETL对照，保存原输出、错误、重试、token及工具成本。
4. 在同资源同模型条件运行Agent，分别分析抽取、候选召回、术语核验、最终输出错误，并检验下游损失。
5. 仅当差距可复现且证据/预算混杂得到说明，才进入单示范提取及独立确认集；无差距则记录负结果。

不要只评分候选filter掩盖上游漏提取；不要将DocETL优化轨迹当作单次业务任务轨迹；不要将专家报告公开给Agent。

## 本轮本地筛选结果

[2026-09-05各8文档pilot](pilot-results-2026-09-05.md)：CUAD Agent主F1 0.5275，固定复核0.5318；BioDEX Agent RP@10 0.3589，固定两臂0.3643。两者未通过预定优势筛选。BioDEX还需先修正/核验任务与gold的事件范围；本轮不推进单轨迹提取，不用更换指标制造成功。历史论文表格仍保留为候选线索，不混成本地结果。
