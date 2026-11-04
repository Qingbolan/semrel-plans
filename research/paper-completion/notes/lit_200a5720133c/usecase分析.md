# 具体用例

论文贯穿全文的例子（§4.2、Figure 1、Figure 3）：

**问题**："中国央行与区域经济的关键金融指标（对外负债、政府存款、GDP）与上一年相比如何，能得到什么洞见？"

1. **规划/分解**：该问题涉及多个指标、时间比较和洞见，被判定需要分解为子问题，如"过去一年政府存款趋势如何？""区域经济 GDP 过去一年如何变化？""对央行负债过去一年如何变化？"
2. **检索**：对子问题同时生成关键词做向量检索，并由 Text-to-SQL 生成 `SELECT GovernmentSavings FROM ed_moneyauthoritybs;`。
3. **SQL 改写**：因结果过长，改写为 `SELECT Year, SUM(GovernmentSavings) AS TotalSavings FROM ed_moneyauthoritybs GROUP BY Year;`。
4. **报告生成**：结合子问题、改写后 SQL 及其结果生成分段报告，例如"政府存款从约 33,760 百万元增至 481,597 百万元""对央行负债从 1,224,980 百万元降至 609,655 百万元"，随后给出"财政审慎、流动性管理"等洞见与结论。

涉及的表包括 `ed_moneyauthoritybs`、`ed_newincreasingloan`、`ed_financialbalance`、`ed_chinafibalancesheetrmb` 等（Figure 3）。

阅读者分析：示例报告中"财政审慎""稳健前瞻的经济战略"等解释性结论无法由检索数据直接验证，论文的 Accuracy 指标也只对照参考报告打分，因此这类洞见的正确性未被独立检验。

依据：[arXiv:2503.13269v2](https://arxiv.org/abs/2503.13269)，§4.2、Figure 1，PDF pp.4–5；Figure 3，p.9。
