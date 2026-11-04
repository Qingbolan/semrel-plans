# 评测与边界

**基线**：专有方法 FM-Agent、MLE-STAR-Pro-1.5、MARS、MARS+、AIBuildAI；开源方法 AIDE、R&D-Agent、ML-Master、AIRA-Dojo、Leeroo、ML-Master 2.0。基线数值取自 MLE-Bench 排行榜或原论文，并非本文重跑（§4.1，PDF p.9）。

**指标**：奖牌率（总体及低/中/高）、金牌率、有效提交率、超过中位数比例（Med+）、Beat Ratio（平均超过的人类参赛者比例）（附录 D.2，PDF p.18）。

**主要结果（Table 1，mean±SEM，3 个种子，PDF p.10）**

| 方法 | 时间 | 总奖牌 | 低/中/高 | 有效 | Med+ | 金牌 |
|---|---|---|---|---|---|---|
| MLEvolve（Gemini-3.1-Pro） | 12h | 65.3±0.8 | 80.3/64.0/46.7 | 100.0 | 76.0 | 34.7 |
| AIBuildAI（Claude-Opus-4.6） | 24h | 63.1±0.4 | 77.3/61.4/46.7 | 100.0 | 71.1 | 25.8 |
| MARS+（Gemini-3-Pro） | 24h | 62.7±0.8 | 78.8/60.5/44.4 | 100.0 | 74.2 | 33.8 |

**消融（Table 3，Lite 22 任务）**：完整 81.82% 奖牌；去掉 Progressive MCGS 或 Retrospective Memory 均降至 68.18%，去掉自适应代码生成降至 72.73%。Table 5（9 任务）中去掉分支内演化使奖牌率从 66.67% 降至 33.33%。

**数学任务（Table 2）**：原文称 15 题中 11 题最好。阅读者按表格核对：Kissing number（592 vs 593）、第二自相关不等式（0.9054 vs 0.9627）、Minimum Overlap（0.380897 vs 0.380868）三题落后；方阵圆装箱与 SimpleTES 在其报告精度下相同；Heilbronn triangles、uncertainty inequality 的领先只在 1e-11 量级。

**阅读者分析的局限**：
- Table 1 跨方法的骨干 LLM、时间预算各不相同，无法把差距归因于框架本身；MLEvolve 用的 Gemini-3.1-Pro-preview 比多数基线更新。
- 消融与机制分析未说明种子数，9 任务子集上一项变化就是 11.1 个百分点。
- Figure 5 的"代表性任务"与 Vanilla MCTS 对比未给出任务清单与重复次数；数学任务未说明预算。
- 原文没有独立的局限性讨论，也未报告 API 成本或 token 消耗。
