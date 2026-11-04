# 评测与边界

**基线**：ReAct（AgentBench 实现）、CodeAct、AWM_offline、ASI_offline（§4.1，PDF p.6）。

**实验 1（端到端，GPT-4o，Table 1，PDF p.6）**：

| 方法 | ALFWorld SR | ALFWorld 轮数 | WebArena SR | WebArena 轮数 |
|---|---|---|---|---|
| ReAct | 82.0 | 19.3 | 23.9 | 5.9 |
| CodeAct | 96.3 | 3.6 | 20.0 | 10.9 |
| AWM_offline | 54.5 | 11.3 | 21.2 | 5.9 |
| ASI_offline | 47.0 | 11.4 | 24.6 | 5.7 |
| SKILL-DISCO + ReAct | 92.4 | 8.8 | 29.1 | 5.1 |
| SKILL-DISCO + CodeAct | 99.3 | 3.2 | 22.9 | 8.5 |

**实验 2（跨模型迁移，Table 2，PDF p.7）**：

- ALFWorld 上，Qwen3.5-9B 从 54.5 升至 98.5；
- WebArena 上，Qwen3.5-4B 从 10.1 升至 18.7；
- GPT-4o-mini 在 WebArena 上持平，为 18.0。

**实验 3（技能使用情况，Table 3，PDF p.8）**：

- 技能数：SKILL-DISCO 为 5（ALFWorld）和 20（WebArena），ASI 为 110 和 146；
- 执行错误率：ALFWorld 从 75.3% 降至 0.0%，WebArena 从 33.9% 降至 21.5%。

**实验 4（消融，Tables 4、7，PDF pp.8、12）**：

- 去掉蒸馏（逐轨迹归纳 43 个技能）后，SR 降至 53.0；
- 去掉编译（只给自然语言流程）后，SR 为 97.0，但输入 token 从 8,468 增至 19,083。

**边界**：作者在 Limitations 中写明以下三点（PDF p.9）：只适用于程序性任务；效果依赖归纳模型的能力；需要成功轨迹。

阅读者补充以下几点（阅读者分析）：

- ALFWorld 评测集只有 134 题，99.3% 与 96.3% 的差距约为 4 题。
- WebArena 上 SKILL-DISCO + ReAct 的成本比 ReAct 高 5.5%（Table 5）。
- 没有给出多次运行或方差。
- 消融只在 ALFWorld 上做。
