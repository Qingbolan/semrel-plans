# 评测与边界

**指标**：准确率（使用 Binder 的评估器，容许语义正确但字面不同的答案）；单实例端到端时间和按 DeepSeek 官方价格计算的 API 费用。

**实验 1（接入不同 TQA 方法，Table 2）**：AutoPrep 对 End2End、CoT、NL2Py、NL2SQL 均有提升；NL2SQL 在四种骨干上平均提升 12.22（WikiTQ）和 13.23（TabFact）。DeepSeek 下 NL2SQL 从 52.83→66.09、70.21→87.85。

**实验 2–3（与数据准备方法和 SOTA TQA 比较，Table 3，DeepSeek）**：

| 方法 | WikiTQ | TabFact |
|---|---|---|
| Off-Prep | 55.32 | 81.67 |
| ICL-Prep | 56.54 | 80.53 |
| Binder | 56.81 | 82.81 |
| AutoTQA*（500 条抽样） | 60.80 | 84.40 |
| ReAcTable | 64.13 | 85.71 |
| CoTable | 64.53 | 86.22 |
| AutoPrep | 66.09 | 87.85 |

论文称对 CoTable 平均高 3.05 / 1.96 个点（四种骨干平均）。

**实验 4–6**：成本仅高于 Off-Prep 与 ICL-Prep（Figure 7，无表格数值）；TableBench 上比第二名 ReAcTable 高 5.28；TransTQ 上加入 Transform 操作后为 68.88。Table 4 中第二名 AutoTQA 为 59.75，差值是 9.13，正文写 9.31（阅读者分析）。

**实验 7–9（消融，Table 5）**：CoC 比直接提示在 WikiTQ / TabFact / TableBench 上高 7.92 / 4.50 / 5.27；工具增强把代码错误率从 4.51% 降到 1.50%（WikiTQ）；去掉 Derive 在 WikiTQ 降 4.30，去掉 Normalize 在 TableBench 降 8.52。

**边界**：仅单表；不处理缺失值和重复；AutoTQA 为复现版且评测子集不同；84%/76% 错误归因的细节在技术报告中。

依据：§6.1–6.6、Tables 2–5、Figures 7–8，PDF pp.9–12；§8，PDF p.12。
