# 评测与边界

指标：执行准确率 EX（预测 SQL 与金标准 SQL 执行结果相同的比例，§5.1）。

BIRD dev（Table 2，p.8）：

| 方法 | 推理模型 | 零样本 | All |
|---|---|---|---|
| CHASE-SQL | Gemini-1.5-Pro（选择用微调的 Gemini-1.5-Flash） | 否 | 73.0 |
| XiYan-SQL | 未知 | 否 | 73.3 |
| RSL-SQL | GPT-4o | 是 | 67.2 |
| MCS-SQL | GPT-4 | 是 | 64.4 |
| Alpha-SQL | Qwen2.5-Coder-7B / 14B / 32B | 是 | 66.8 / 68.7 / 69.7 |

32B 版按难度为 74.5 / 64.0 / 57.2。Spider dev（Table 3）：14B 版 87.0，与 SuperSQL（GPT-4）持平，高于 SFT CodeS-15B 的 84.9（正文称“提升 2.1%”）。

**SDS 上与基线 LLM 对比（Table 4，p.9，EX %）**：

| 模型 | 直接提示 | + Alpha-SQL |
|---|---|---|
| Qwen2.5-Coder-7B | 47.6 | 64.6（+17.0） |
| Phi-4 | 43.5 | 60.0（+16.5） |
| GPT-4o | 53.7 | — |
| Gemini-1.5-Pro | 56.2 | — |
| Gemini-2.0-Flash-Thinking-Exp | 60.8 | — |
| DeepSeek-V3 / DeepSeek-R1 | 51.2 / 50.3 | — |

**消融（Table 5，SDS）**：去掉 SQL 修正 −1.8，去掉 schema 选择 −1.5，去掉列值识别 −0.4。

**rollout 数（Fig.5）**：rollout 从 4 增加到 24，上界准确率和最终准确率都上升。

阅读者分析与局限：
- 原文没有局限性章节，也没有报告推理成本（LLM 调用次数、token、时延）；24 次 rollout、每个动作采样 3 次、每次奖励再采样 5 条并执行，成本很可能远高于单次提示的基线，比较并非等预算。
- “超过最佳 GPT-4o 零样本方法 2.5%”是 69.7 对 67.2 的百分点差；基线数字多引自原论文，而非同环境重跑。
- 消融和基线 LLM 对比只在 147 题上进行，未报告方差。
- 未在 BIRD test 或 Spider 2.0 等更新的基准上评测。

依据：[arXiv:2502.17248v2（ICML 2025，PMLR 267），21 页](https://arxiv.org/abs/2502.17248)，§5、Tables 2–5、Fig.5，PDF pp.7–9。
