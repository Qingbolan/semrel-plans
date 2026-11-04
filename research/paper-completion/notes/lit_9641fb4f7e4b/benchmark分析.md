# 评测与边界

基线（§5.1，PDF p.8）：IO、CoT、CoT SC（5 个答案）、MultiPersona Debate、Self-Refine（最多 3 轮）、MedPrompt（3 个答案 5 次投票），以及自动方法 ADAS。

主要结果（Table 1，GPT-4o-mini 执行，3 次平均，PDF p.8）：

| 方法 | HotpotQA | DROP | HumanEval | MBPP | GSM8K | MATH | Avg |
|---|---|---|---|---|---|---|---|
| CoT SC | 68.9 | 78.8 | 91.6 | 73.6 | 92.7 | 50.4 | 76.0 |
| ADAS | 64.5 | 76.6 | 82.4 | 53.4 | 90.8 | 35.4 | 67.2 |
| AFlow | 73.5 | 80.6 | 94.7 | 83.4 | 93.5 | 56.2 | 80.3 |

原文称 AFlow 比手工方法平均高 5.7%，比自动方法高 19.5%。阅读者核算：80.3/76.0≈1.057，80.3/67.2≈1.195，因此这两个数字是相对提升，绝对差分别为 4.3 和 13.1 个百分点。

迁移（Table 2，HumanEval）：用 GPT-4o-mini 搜得的工作流，在 GPT-4o 上 96.2、Claude-3.5-sonnet 上 95.4；用 DeepSeek 搜得的工作流在 GPT-4o-mini 上只有 90.8，说明不同模型适合不同工作流。

成本（App. D，PDF p.30）：在 DeepSeek 上执行 AFlow(GPT-4o-mini) 工作流，HumanEval 得分 0.9390，花费 $0.0291，原文称以 GPT-4o IO（0.9389，$0.6371）4.55% 的成本达到同等水平。

消融：GSM8K 去掉算子后仍有 93.1%（Fig. 5(A)）。

局限：只验证了有数值反馈的推理任务；成本前沿只针对 HumanEval；未报告多次搜索之间的方差。
