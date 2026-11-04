# 评测与边界

指标：Pass@1，即操作区域全部单元格匹配（§5.1，pp.8–9）。

**实验 1（SpreadsheetBench 主结果，Table 1，p.8）**：Qwen3-4B-Thinking-2507 的逐步消融如下。

| 配置 | Pass@1 |
|---|---|
| 原始模型 | 12.0 |
| + 表格原生 harness | 15.6 |
| + 完整工具 | 19.3 |
| + RL（Spreadsheet-RL） | 23.4 |

同环境的其他开源模型：Qwen3-4B-Instruct-2507 9.3、Qwen3-4B 11.0、Qwen3-14B 15.0、Qwen3-8B 15.9、Qwen3-32B 17.6。闭源结果直接引用他人报告（运行环境分别是 OSX+LibreOffice 或 Windows+Excel）：

| 系统 | Pass@1 |
|---|---|
| GPT-4o | 16.8 / 18.4 |
| o3 | 23.3 |
| ChatGPT agent | 35.3 |
| Claude Files Opus 4.1 | 42.9 |
| ChatGPT agent with .xlsx | 45.5 |
| Copilot Agent Mode | 57.7 |

**实验 2（Domain-Spreadsheet，Table 2，p.8）**：

| 领域 | 任务数 | Base | RL |
|---|---|---|---|
| Finance-B | 597 | 15.6 | 29.3 |
| Finance-I | 388 | 7.7 | 16.2 |
| Finance-A | 135 | 8.1 | 19.3 |
| Supply Chain | 180 | 1.1 | 5.0 |
| HR | 185 | 0.5 | 3.2 |
| Sales | 86 | 1.2 | 5.8 |
| Real Estate | 89 | 1.1 | 1.1 |
| Overall | 1,660 | 8.4 | 17.2 |

**实验 3（训练动态，Fig.4，§5.2）**：训练奖励约 0.21→0.33；平均响应长度约 16k→11k；平均轮数约 20→11。训练 60 步，4×H100 约 40 小时（A.14）。

边界：只训练了 4B 模型，未报告更大稠密模型或 MoE（A.1）；SheetAgent 未作为基线，因公开实现在作者环境中几乎为 0（A.2）。阅读者分析：所谓"超过 o3"是把本文 Excel 环境下的 23.4 与他人在 OSX/LibreOffice 下报告的 23.3 比较，环境不同、差距仅 0.1 点，不能视为可比结论；未报告多次运行方差。
