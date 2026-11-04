# 评测与边界

**设置**（§4.1，pp.6–7）：主智能体最多 10 步，温度 0.1，每步最多 8,192 token；骨干模型为 Qwen3-Coder-30B-A3B、Gemini 2.5 Flash/Pro、Claude 4 Opus。KramaBench 与 DA-Code 用官方评测脚本，DSBench 用 Gemini-2.5-Pro 作为二值判分器。基线：DS-GRU（KramaBench 原基线，把所有文件放进提示并自我纠错）、RAG（E5-large 取 top-5 文件，其余流程相同）、主从式（点名调用同样的子智能体）。

**实验 1（端到端，Table 1，p.8）**：宏平均得分如下。

| 骨干 | DS-GRU | RAG | 主从 | 黑板 |
|---|---|---|---|---|
| Qwen3-Coder | 1.21% | 3.87% | 5.03% | 7.90% |
| Gemini 2.5 Flash | 4.32% | 14.52% | 14.49% | 16.54% |
| Gemini 2.5 Pro | 7.71% | 18.51% | 24.01% | 28.53% |
| Claude 4 Opus | 4.11% | 23.00% | 27.63% | 31.43% |

**实验 2（文件发现，Table 2，p.9，Gemini 2.5 Pro）**：宏平均 F1 为 RAG 0.247、主从 0.513、黑板 0.561；黑板在三个数据集上 recall/precision/F1 均最高。

**实验 3（补充分析，Figure 2，pp.9–10；附录 F）**：动作上限从 2 增到 10 性能上升；去掉 search agent 性能下降；50 题抽样中三者每题运行时间在 132.0–145.2 秒，黑板成本约为 RAG 的 2.3 倍、主从的 1.8 倍；数据湖越大相对主从的增益越大（DA-Code 145 文件 +70%，Astronomy 1556 文件 +211%）；对 Data Interpreter 与 AutoGen 在 KramaBench 6 个领域中 5 个占优。

**边界**：阅读者分析——绝对成功率仍低（最好 31.43%），DA-Code 上各方法多在 0–9%；"全数据集超越"并非每个骨干都成立，例如 Gemini Flash 的 DA-Code 黑板 0.55% 低于 RAG 2.75%，Claude 的 Environment 低于主从（阅读者分析）。消融与成本实验只用 Gemini 2.5 Pro 和 KramaBench 子集；没有报告方差或多次运行；DSBench 依赖 LLM 判分。

依据：§4，pp.6–10；附录 F 与 Table 4、Figures 18–23，pp.31–41。
