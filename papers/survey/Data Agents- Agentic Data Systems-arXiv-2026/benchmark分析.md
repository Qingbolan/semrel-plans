# 评测与边界

**实验 1（DABStep 排行榜）**（Table III，p.11，节选）：

| 系统 | Easy | Hard |
|---|---|---|
| DATA AGENT（Qwen 3） | 94.44 | 50.79 |
| DS-PlaVer（Gemini 2.5-Pro） | 87.50 | 45.24 |
| Amity DA Agent v0.1 | 80.56 | 41.01 |
| Mphasis-IZI-Agents | 80.56 | 28.04 |
| Claude 4 Sonnet ReACT Baseline | 81.94 | 19.84 |
| Open Data Scientist | 84.72 | 16.40 |
| o1 Reasoning Prompt Baseline | 69.44 | 11.11 |

相对第二名提升 +6.94（easy）和 +5.55（hard）。

**实验 2（Spider 2.0-Lite 排行榜）**（Table IV，p.11，节选）：

| 方法 | 执行准确率 |
|---|---|
| DATA AGENT | 44.50 |
| ReForce + o3 | 37.84 |
| ReForce + Qwen3 | 35.60 |
| Autolink + DeepSeek-R1 | 34.92 |
| RSL-SQL + o3 / LinkAlign + DeepSeek-R1 | 33.09 |
| Spider-Agent + Claude-3.7-Sonnet | 28.52 |
| Spider-Agent + Claude-4-Sonnet | 27.79 |

**实验 3（消融）**（§6-B，Fig. 2，p.12）：分别去掉语义数据组织、反馈闭环、记忆管理。作者报告三者在两个基准上都有贡献：去掉语义组织在 Multiple Data Statistic 和 Multi-table 类上下降明显；去掉反馈在深推理类（复杂逻辑匹配、递归分析）上下降更多；去掉记忆在除最简单类以外都有影响。

**实验 4（时间与 token）**（§6-C，Tables V–VII，pp.12–13）：

| 基准 | DATA AGENT | 基线 | 加速 |
|---|---|---|---|
| DABStep 平均每查询 | 2.8 min | 6.5 min（Qwen3 ReACT） | 2.32× |
| Spider 2.0-Lite 平均每查询 | 5.1 min | 7.4 min（ReFoRCE） | 1.45× |

DABStep 输入 token 从 33.3k 降到 16.9k（简单查询）、从 178.5k 降到 27.6k（复杂逻辑匹配，约 6.5×）；Spider 2.0-Lite 各类输入 token 为 10.8k–20.4k，ReFoRCE 为 52.8k–88.4k。Fig. 3 显示 DATA AGENT 在几乎所有类别上迭代步数更少。

**边界**：
- 原文承认：更强的主动能力（自主检测事件、无提示发起任务）仍未解决；自我演化中的反馈与归因、安全更新、记忆质量与迁移都是开放问题（§6-B、§7）。
- 阅读者整理：DATA AGENT 用 Qwen 3，基线各用不同 LLM，比较的是系统 + 模型的组合，没有同骨干对照；基线数字是否重跑不清楚（只说采用排行榜上的公开配置）；两组时间/token 的基线不同，不能互相比较；没有报告美元成本或方差；Qwen 3 具体版本与代码未给出。
- 阅读者注：§6 把 Claude 系 Spider-Agent 写作“来自 Anthropic”，按通常的出处 Spider-Agent 是 Spider 2.0 基准作者提供的基线智能体，此处疑似表述有误（阅读者分析，未在本文中核实）。

依据：[arXiv 2609.24137v1](https://arxiv.org/html/2609.24137v1)，§6–7、Tables III–VII、Figs. 2–3，pp.11–13。
