# 评测与边界

**基线（§4.1，p.8；附录 B.3，p.18）**：前沿智能体 Claude Code CLI、Codex CLI；数据集搜索智能体 DatasetResearch；端到端 ML 智能体 ML-Master 2.0；数据中心训练框架 DataFlex。除注明外均以 GLM-5 为骨干；PostTrainBench 上的 Codex 数据来自原论文（GPT-5.2-Codex）；DataFlex 只适用于 PostTrainBench，并被提供 DataMaster 最佳节点的数据集；ML-Master 2.0 只在 MLE-Bench Lite 上评测。

**主结果（Table 1，p.8）**

| 系统 | MLE 奖牌率 | MLE 金牌率 | PTB 平均 | GPQA |
|---|---|---|---|---|
| 初始分数 | 35.91% | 22.73% | 8.47% | 18.75% |
| 人类参考 | – | – | 46.91% | 30.35% |
| Codex* | 22.73% | 18.18% | 18.46% | 29.54% |
| Claude Code | 36.36% | 22.12% | 11.47% | 14.29% |
| DatasetResearcher | 59.09% | 27.27% | 8.50% | 18.00% |
| DataFlex | – | – | 19.09% | 28.80% |
| ML-Master 2.0 | 40.91% | 27.27% | 15.69% | 18.57% |
| DataMaster | 68.18% | 45.45% | 31.17% | 31.02% |

**其他实验**：不同骨干（Fig.2）中 GLM-5、Claude-4.6-sonnet、Qwen3.5-plus 平均约 30%，GPT-5.4 为 14.64%（作者归因于每节点工具调用少，11.3 次对 GLM-5 的 40.7 次）；初始代码敏感性（Table 3，p.11）中 Full-code 从 45.45% 到 72.73%，Algo-only 从 35.91% 到 68.18%；成本（Table 4）。

**口径问题（阅读者核对）**：
- 摘要写“medal rate 提升 32.27%”，实为百分点（35.91→68.18），且对应 Table 3 的 Algo-only 设置。
- §1（p.2）称 PostTrainBench 平均分“比最强非人类基线高 +19.79 点”，但 Table 1 中最强非人类基线 DataFlex 为 19.09%，差值为 12.08（§4.2 也写 12.08），+19.79 与表格不符。
- Table 4 的平均工具调用（红 41.3 / 黑 39.6）与 Fig.5/正文（红 58.52 / 黑 43.63）不一致，可能统计口径不同（“per executed node”），原文未解释。
- 论文无独立局限性章节；结果基于单次运行，未报告方差。附录 D.1 承认搜索树存在分支集中偏差（leaf-classification 中 5 个分支大小为 23/6/3/2/2）。
