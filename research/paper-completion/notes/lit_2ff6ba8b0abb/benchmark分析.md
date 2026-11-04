# 评测与边界

基线（§5.1.2）：多数投票、LLM-as-a-judge（DeepSeek-V3.2）、自奖励（Qwen3-235B-A22B-Instruct）；判别式 PRM：Math-Shepherd-PRM-7B、Qwen2.5-Math-PRM-7B/72B、ReasonFlux-PRM-7B；生成式 PRM：ThinkPRM-14B、GenPRM-32B。

Best-of-N 主结果（Table 2，N=16）：

| 验证器 | ScienceAgentBench SR | DABStep Avg |
|---|---|---|
| 多数投票 | 23.08 | 38.00 |
| 自奖励（235B） | 24.36 | 39.77 |
| GenPRM-32B | 20.51 | 34.22 |
| Qwen2.5-Math-PRM-72B | 20.51 | 29.11 |
| DataPRM（4B） | 25.64 | 40.89 |

N=4 时 DataPRM 的 SR（24.36）与多数投票持平。Qwen2.5-Math-PRM-72B 随 N 从 8 增到 16 由 31.33% 降到 29.11%；Beam Search 下 DataPRM 35.33→38.00→38.89%（Fig.4）。

**消融（Table 3，DABStep Avg，N=16）**：

| 变体 | Avg |
|---|---|
| CoT | 38.89 |
| 单轮代码 + 环境 | 39.77 |
| 多轮、无环境 | 38.89 |
| 多轮 + 环境 | 39.77 |
| 完整 DataPRM | 40.89 |

**过滤策略（Table 4）**：不过滤在 N=16 最好（40.89），作者解读为多样性比纯度更重要。

**推理成本（Table 5）**：

| 验证器 | 平均 token | 平均轮数 | 工具调用 | 时间（秒） |
|---|---|---|---|---|
| DataPRM | 21,455.78 | 2.57 | 0.87 | 24.66（并行环境 3.30） |
| GenPRM | 7,061.25 | 1.00 | — | 14.86 |
| 自奖励 | 25,282.51 | 3.32 | 0.63 | 194.95 |

**RL（Fig.5a、§5.4）**：过程奖励在 DABench 78.73%、TableBench 64.84%，优于 SFT 和仅结果奖励；仅结果奖励约 200 步后熵塌缩至约 0.12，过程奖励保持约 0.18。

边界：作者承认只覆盖推理与可视化类分析，未涵盖模型训练等工程任务，且 DataPRM 只用 SFT 训练、依赖高质量轨迹数据（Limitations）。阅读者分析：多数差距在 1–2 个百分点，ScienceAgentBench 仅 78 题（1 题约 1.28 个百分点），未报告方差或多次运行；摘要中的“提升 7.21% / 11.28%”在正文未明确对比基准；RL 评测依赖 LLM 评判。

依据：[arXiv 2604.24198v2，12 页](https://arxiv.org/pdf/2604.24198v2)，§5.1–5.4、Tables 2–5、Figs.4–5、Limitations，PDF pp.6–9。
