# 工作负载

**数据集**（§4.1，p.4）：

| 任务 | 数据集 | 来源 | 划分 / 规模（原文所述） |
|---|---|---|---|
| 实体匹配 | Fodors-Zagats、Beer、iTunes-Amazon、Walmart-Amazon、DBLP-ACM、DBLP-Google、Amazon-Google（7 个） | Magellan 基准 | 使用提供的 train/dev/test 划分 |
| 数据填补 | Restaurant、Buy | IMP 论文 [73] | 原无划分，按 [41,73] 协议生成 |
| 错误检测 | Hospital、Adult | 数据清洗常用基准 | 同上；Adult 因预算随机抽 1K 行 |
| 模式匹配 | Synthea | OMAP 基准 | 原文未给规模 |
| 数据转换 | StackOverflow、Bing-QueryLogs | TDE 基准 | 原文未给规模 |

**指标**：ED、EM、模式匹配用 F1；DI、数据转换用 accuracy（§4.1，p.4）。

**消融负载**：只在 Beer、iTunes-Amazon、Walmart-Amazon 三个 EM 数据集上做，每个至多 200 个样本，k=10（Table 4，p.5）。随机示例实验用 3 个随机种子。

**样本单位**：EM 是记录对，ED/DI 是单元格。原文没有在 12 页正文中给出各数据集的记录数、正例比例或测试集大小，本笔记不补造这些数字。

阅读者分析：负载规模偏小，且每任务只选了少数被作者称为"具有挑战性"的数据集，因此结论代表性有限。

依据：§4.1、Tables 1–4，PDF pp.4–5。
