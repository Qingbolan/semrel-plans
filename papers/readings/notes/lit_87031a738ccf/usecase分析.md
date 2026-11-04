# 具体用例

Figure 1 的示例：用户提出"通过互动分析找出 Salesforce 中的'僵尸'商机"。

1. **DE-Arch**：agent 写设计文档，例如定义 `fct_opportunity_health` 表，来源为 `int_opportunities_with_age`、`int_activities_per_deal`，列 `opportunity_health_score` 按优先规则打分（30 天内 ≥5 次活动→90；30 天无活动→10；在某阶段停留 >90 天→25；否则 60）。
2. **DE-Impl**：按规格写 staging / intermediate / marts 三层 SQL，构建 DE-DAG。
3. **DE-Evol**：在新需求下修 3 个 SQL、新增 4 个 SQL（如 `fct_sales_velocity.sql`、`fct_funnel_conversion.sql`）。
4. **DA**：在语义层上用 Python/SQL 分析，产出报告，如"Q3 管线价值的 40% 来自 30 天以上无活动的'不健康'商机"，并配图。

App. D 的 DE-Evol 错误案例（Figure 15）说明级联失败：staging 层同一 `account_id` 有多条 `is_most_recent = true`，intermediate 层 join 后 A001 的 spend 被重复计算（20,000 而非 10,000），marts 层公司总支出变为 35,000（正确 25,000）。

阅读者分析：这个例子说明 DAComp 关心的是多表、多层的业务语义正确性，以及上游小错误对下游指标的放大——在评测上就是 CS 与 CFS 的差异。Figure 1 的"40%"是示意报告文本，不是论文的实验结果。

依据：[arXiv:2512.04324v1](https://arxiv.org/abs/2512.04324)，Figure 1，PDF p.2；App. D、Figure 15，p.34。
