# benchmark

- **被测系统**：原生 CLI——Codex CLI v2.3.1（GPT-5.5 及 xhigh）、Claude Code v2.1.150（Opus-4.7、Opus-4.6、Sonnet-4.6），默认配置；框架——OpenHands v1.7（GPT-5.5、Opus-4.7、Kimi-K2.6、DeepSeek-V4-Pro）、Mini-SWE-Agent v2.0.0（GPT-5.5），温度 0。

**主结果（Table 4，%）**：

| 系统 | 模型 | DA | EA | Hard DA | Hard EA | $/题 |
|---|---|---|---|---|---|---|
| Codex CLI | GPT-5.5 (xhigh) | 75.0 | 60.5 | 57.0 | 42.9 | ~1.42 |
| Codex CLI | GPT-5.5 | 74.9 | 60.3 | 61.4 | 47.9 | ~1.39 |
| Claude Code | Opus-4.7 | 77.3 | 51.9 | 61.4 | 45.4 | 0.22 |
| Claude Code | Opus-4.6 | 71.3 | 47.8 | 68.4 | 45.4 | 0.20 |
| Claude Code | Sonnet-4.6 | 77.9 | 53.8 | 61.4 | 42.9 | 0.11 |
| Mini-SWE-Agent | GPT-5.5 | **83.0** | **61.1** | 67.5 | **49.6** | ~0.39 |
| OpenHands | GPT-5.5 | 82.1 | 59.7 | 63.2 | 44.5 | ~0.65 |
| OpenHands | Opus-4.7 | 72.0 | 49.3 | 59.6 | 38.7 | ~1.17 |
| OpenHands | Kimi-K2.6 | 71.5 | 43.8 | 59.6 | 37.0 | ~0.41 |
| OpenHands | DeepSeek-V4-Pro | 75.9 | 49.0 | 58.8 | 36.1 | ~0.15 |

- **成本**：Claude Code Sonnet-4.6 平均 81,714 token、14.7 轮；Codex CLI GPT-5.5 380,558 token、6.8 轮（Claude Code 按内置计费，其余按 OpenRouter 价格估算，表中以 ~ 标记）。
- **Oracle 消融（§6.1、Fig.5，CoDA-Hard）**：给出目标文件路径后，Claude Code（Sonnet-4.6）45.4→73.1，OpenHands（GPT-5.5）44.5→68.9；oracle 下平均仍只有 71.0%。
- **环境因素（Fig.4，OpenHands GPT-5.5，前 30 社区）**：文件数与准确率 Spearman ρ=−0.271（p=0.148，不显著）；SNR ρ=0.466（p<0.01）；数据量 ρ=−0.461（p<0.01），超过 8GB 的若干社区接近 0。
- **错误归因（Fig.7，人工分析 200 个失败样本）**：GPT-5.5 代码生成 44.0%、数据发现 33.0%、执行错误 6.5%；Kimi-K2.6 数据发现 40.7%、代码生成 34.7%、执行错误 12.6%。
- **局限（附录 H）**：Kaggle 偏重 EDA 与预测建模，不代表 ETL 或实时分析；Kaggle 数据比真实仓库更干净；单用户笔记本流程；公开数据可能出现在训练语料中（污染风险）。
- **阅读者分析**：(1) oracle 消融中 Claude Code Sonnet-4.6 的 Community 基数 45.4 与 Table 4 中其 Hard EA 42.9 不一致（45.4 是 Opus-4.7/4.6 的数值），原文未解释；(2) DA 要求使用文件集合与目标完全相等，多读一个文件也算失败，口径严格；(3) 600 秒超时与 4GB 内存在 GB 级社区上可能本身就是失败原因，与"数据量造成瓶颈"的结论相互纠缠；(4) 原文未说明重复运行次数，也未报告方差。

依据：[arXiv:2606.15300v1，37 页](https://arxiv.org/abs/2606.15300)，§5–6、Table 4、Figs.4–7，附录 E、H，PDF pp.6–9、27、37。
