# benchmark

**被测系统**（§6.1，PDF pp.7–8）：harness = DA-Agent（80 步上限、15 步历史窗口、1 分钟单步超时）、Smolagents（40 步、5 分钟单步超时）、Claude Code、CodeX（每任务 60 分钟）；LLM = Qwen3.5-397B-A17B、Kimi-K2.5、Claude Sonnet 4.6，默认温度；12 种组合全交叉。硬件：128GB 内存、3.1GHz CPU 的 Linux 服务器，Docker 隔离。

**总分**（Table 4，PDF p.9，Pass@1，%）：
| | Qwen3.5 | Kimi-K2.5 | Claude 4.6 |
|---|---|---|---|
| Smolagents | 47.1 | 43.8 | 46.7 |
| DA-Agent | 44.4 | 44.8 | 46.1 |
| Claude Code | 40.9 | 44.3 | 46.6 |
| CodeX | 39.9 | **48.8** | 31.6 |

没有任何 harness 在所有领域最优；Real Estate 普遍最难（8.1–25.0）。

**代价**（Table 5，PDF p.10）：CodeX（Kimi）平均 40.2 步、1,091.2K tokens、$0.19/任务，成功步比例最低 59.5%；Smolagents（Claude 4.6）$1.66/任务最贵。

**技能与失败分析**（§6.3–6.4，Figs 7–9，PDF pp.10–12）：数据格式处理与跨阶段技能得分较高；最低分技能为 Data Alignment & Merging、Histogram Creation、Text Processing；数据分析类贡献最多失败；超出全局限制的任务 <0.6%，放宽步数/超时（抽样至多 10 个失败任务）并不显著提分。

**局限与不一致**（阅读者分析）：单次 Pass@1、无方差；技能级评分由 LLM 判定，未报告人工一致性；文中称 “Claude Code (Kimi-K2.5) 43.3”，与 Table 4 的 44.3 不符；Finding 1 的 harness 排序（CodeX > Smolagents > Claude Code > DA-Agent）与各 harness 最佳组合的分数（48.8 > 47.1 > 46.6 > 46.1）一致，但按三个 LLM 平均则 CodeX 最低（约 40.1），解读时需区分口径。原文无独立 limitations 节。

依据：[arXiv:2607.01647v1，14 页](https://arxiv.org/abs/2607.01647)，§6，Tables 4–5、Figs 6–9，PDF pp.7–12。
