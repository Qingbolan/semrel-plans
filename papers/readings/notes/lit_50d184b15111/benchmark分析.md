# 评测与边界

基线：GPT-4.1 直接整表提示、TableRAG、Table-LLaVA（本地 A100 40G）、Palimpzest 0.7.7（MinTime/MinCost 策略，可用 gpt-4.1、gpt-4.1-nano 等）、Lotus v1.1.0（gpt-4.1 为主模型、nano 为辅助）（§5.1.3、§5.2.1，PDF p.9）。

**实验 1（端到端时间与成本）**：Table 4，PDF p.10，按查询均值；Δ 列为 Nirvana 相对 Palimpzest/Lotus 中较优者的降幅，阅读者按表值核对 Movie Small 19.963s 对 Lotus 40.283s 即 ↓50.44%）：

| 数据集 | Nirvana Δ时间 | Nirvana Δ成本 |
|---|---|---|
| Movie S/M/L | ↓50.44% / 72.79% / 72.21% | ↓46.48% / 89.50% / 96.31% |
| Estate S/M/L | ↓23.84% / 23.34% / 10.16% | ↓18.16% / 65.90% / 73.37% |
| Game S/M/L | ↓84.46% / 80.80% / 80.12% | ↓97.96% / 97.48% / 97.72% |

Palimpzest 在 Game 上超过 5.5 小时。

**实验 2（结果质量）**：Table 5 答对比例：Nirvana 75.0% / 41.7% / 50.0%（Movie/Estate/Game）；Lotus 8.3% / 16.7% / 25.0%；Palimpzest 58.3% / 25.0% / –；GPT-4.1、Table-LLaVA、TableRAG 基本为 0 或无法运行。

**实验 3（消融与开销）**：LLM-as-a-judge 成功率 81.6%–90.0%、精确率 84.6%–95.6%、召回 91.6%–100%（Table 7）；q10/Estate 上逻辑优化花 9.8s 和 $0.0082，而 Palimpzest Cascades 近乎零开销（Table 6）；物理优化相对 Smart 优化时间约为 1/4（§5.4.4）；优化时间占总时间 50.7%/6.7%/42.7%（§5.5.1）。部分单算子查询中逻辑优化反而增加了时间和成本（§5.3.2）。

§5.3.4 称完整优化与“w/o all optim.”答对数相同，但 Table 5 中 Movie 为 75.0% 对 66.7%、Game 为 50.0% 对 41.7%，正文与表格不一致，此处保留表值。每数据集仅 12 题，质量差异的统计意义有限；未报告重复运行方差。（阅读者分析）
