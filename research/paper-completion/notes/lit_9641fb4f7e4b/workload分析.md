# 工作负载

六个公开基准，验证集与测试集按 1:4 划分（§5.1，PDF pp.7–8）：

| 领域 | 基准 | 使用规模 | 指标 |
|---|---|---|---|
| QA | HotpotQA | 随机 1,000 条 | F1 |
| QA | DROP | 随机 1,000 条 | F1 |
| Code | HumanEval | 全量 | pass@1 |
| Code | MBPP | 全量 | pass@1 |
| Math | GSM8K | 全量 | Solve rate |
| Math | MATH lv5* | 4 类题（组合与概率、数论、预代数、预微积分）难度 5 共 617 题 | Solve rate |

设置：优化器为 Claude-3.5-sonnet；执行器有 DeepSeek-V2.5（温度 1）、GPT-4o-mini-0718、Claude-3.5-sonnet-0620、GPT-4o-0513（温度 0）。AFlow 迭代 20 轮；ADAS 迭代 30 轮（优化器 Claude-3.5-sonnet，执行器 GPT-4o-mini）。Table 1 中的结果均为在划分后的测试集上执行 3 次的平均值（PDF p.8）。

阅读者分析：负载都是单条输入、有标准答案的推理/代码题，工作流需对整个数据集泛化。HotpotQA/DROP 只抽取了 1,000 条，具体被抽到哪些样本由随机种子决定，文中没有列出。
