# 评测与边界

**实验 1（InfiAgent-DABench，Table 1，ABQ %）**：

| 模型 | ReAct | AutoGen | Taskweaver | Data Interpreter（复现） | DatawiseAgent |
|---|---|---|---|---|---|
| GPT-4o mini | 80.08 | 70.04 | 76.65 | 67.70 | 82.88 |
| GPT-4o | 81.32 | 73.54 | 85.99 | 75.78 | 85.99 |
| Qwen2.5-72B | 75.88 | 70.04 | 74.71 | — | 81.71 |

Data Interpreter 原文报告 GPT-4o 上 94.93，作者在其设置下无法复现，该值未纳入 SOTA 比较。GPT-4o 上 DatawiseAgent 与 Taskweaver 持平，与摘要的“consistently SOTA”不完全一致（阅读者分析）。

**实验 2（MatplotBench，Table 2）**：GPT-4o 下得分 61.22，加 GPT-4o mini 视觉工具后 64.33；AutoGen 加视觉工具为 63.60。

**实验 3（DSBench 建模，Table 3）**：

| 系统 | 成功率 % | RPG |
|---|---|---|
| DatawiseAgent + GPT-4o | 98.64 | 53.18 |
| DatawiseAgent + GPT-4o mini | 98.64 | 46.61 |
| DatawiseAgent + Qwen2.5-72B | 91.89 | 42.90 |
| AutoGen + GPT-4 | 87.84 | 45.52 |
| Code Interpreter + GPT-4 | 54.05 | 26.14 |

AutoGen 与 Code Interpreter 的数值取自 DSBench 原文，不是在相同环境下重跑；Human 行（100 / 65.02）仅基于 22 个竞赛。

**实验 4（消融，GPT-4o mini，Table 5）**：完整系统成功率 98.64、RPG 46.61、ABQ 77.14；去掉规划为 77.03、38.35、70.86；去掉代码修复为 87.84、43.80、75.43。

**成本（Tables 6–7）**：DSBench 上 GPT-4o mini 版共 $2.13，AutoGen+GPT-4 为 $19.34。

**局限（原文）**：工具集成只测了一个视觉反馈工具，未评估人在环协作。

依据：§4.2–4.4、Tables 1–7、Limitations，PDF pp.6–8、12–13。
