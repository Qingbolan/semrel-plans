# 严格 Shared-Environment 调研：当前统一入口

当前 **28项入场判定：0 Strong / 5 Partial / 23 Reject**。这不是28个可运行benchmark。适用用户附件A–H标准；objective SHA256 `772662d1b859594fccc47e9fe5c974195e5829e6b44e409de44e6f9c27123f69`。原要求允许不足15时如实分级，但下载与实质核验缺口仍须逐项披露，不因Reject而声称全部完成。

| 用户所需内容 | 当前入口 | 证据边界 |
|---|---|---|
| 全部候选入场、原论文/仓库下载及缺口 | [28项总表](shared-environment-strict-delivery.md)；各行进入完整卡片 | 完整代码库不等于全部外部数据；各资产是否取得分开记录 |
| 横向Query × 数据湖、类Python DAG、LOTUS/Agent预期、四类ρ | [当前五Partial四表](shared-environment-current-five.md) | 推演没有实际模型准确率；K和ρ比例未知 |
| 前五个真实输入、E短引、gold及依据 | [五例集中证据](shared-environment-top-five-examples.md) | 局部支持不等于20条必要且充分证据闭合 |
| 八维排名与固定baseline风险 | [当前五Partial比较](shared-environment-current-five.md) | 查证优先级，不是性能排名；未知D/K不填通过 |
| 逐要求完成情况 | [完成审计](shared-environment-completion-audit.md) | 未完成项明确列出；未宣称目标全部达成 |
| 唯一机器可读判定清单 | [状态JSON](shared-environment-strict-goal-status.json) | 以reviewed数组为计数来源 |

五Partial依次为HSCodeComp、CodiEsp、UDRP、AnnoCTR、STARD。共同缺口是C完整证据链、同资源强固定程序不足、语义执行家族K。AnnoCTR有3348技术链接但只有120独立报告；不能用链接数代替文档级独立样本数。UDRP多数类高不直接证明执行分支少；标签分布与执行家族分开。

[旧排名](shared-environment-strict-ranking.md)、日期轮次和旧“12可构造”等材料只用于追溯，不计入本次Strong。28项卡片保留阴性与未知；没有用缺数据、弱基线或仅词面分组制造Agent优势。


本轮续查最新状态：**29项，0 Strong / 5 Partial / 24 Reject**。新增[C3PA排除依据](shared-environment-c3pa-in-progress.md)；上文28项为此前交付。HuBMAP ARMS正在审查，未计入通过或已审数量。


## 当前核验增量 2026-09-15T00:16:45.184140+08:00

当前已审32项：0 Strong、5 Partial、27 Reject。新增 OmniCompliance、PrivaCI、AIReg-Bench 均未通过；HuBMAP仍在审不计入。旧28项/29项数字属于历史批次。最新逐项事实见 [状态账本](shared-environment-strict-goal-status.json)，AIReg证据见 [核验卡](shared-environment-strict-audit-aireg.md)。用户至少5 Strong目标未完成。


## 当前核验增量 2026-09-15T00:37:30.713412+08:00

已判定36项：0 Strong、5 Partial、31 Reject。RegOps、PRT、DSO、GUIDE新增排除；MDACE、HuBMAP、CORTEX、SecAlert等未完成来源/环境核验，不计入已判定数。数字以[状态JSON](shared-environment-strict-goal-status.json)及各卡为准；历史批次数字保留。GUIDE已全量下载并计数，[实证卡](shared-environment-strict-audit-guide.md)。至少5Strong目标未完成。
