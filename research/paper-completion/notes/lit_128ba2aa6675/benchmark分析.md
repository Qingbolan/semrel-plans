# 评测与边界

**基线**（§6.1.1，p.6）：Seq2Vis、Transformer、ncNet、RGVisNet、同骨干无 CoT 的 Llama3.1-8B-SFT、少样本通用 LLM（Llama3.1-8B、GPT-4o-mini、GPT-o1、GPT-o3、Gemini-2.5-Pro、Claude、DeepSeek-R1）、ChartGPT。

**指标**：Chart Acc、Axis Acc、SQL Acc（沿用 RGVisNet），新增执行级 Data Acc（执行结果一致）与 All Acc（图表、坐标轴、数据全对）。

**主要结果**（Table 1，p.6）：

| 方法 | Chart | Axis | SQL | Data | All |
|---|---|---|---|---|---|
| ncNet | 98.05 | 46.40 | 42.59 | 43.07 | 42.28 |
| RGVisNet | 97.21 | 48.34 | 53.61 | 53.96 | 51.70 |
| Llama3.1-8B-SFT | 83.83 | 77.05 | 52.10 | 62.52 | 59.37 |
| GPT-4o-mini | 91.31 | 87.16 | 52.35 | 75.07 | 70.37 |
| DeepSeek-R1 | 92.25 | 94.36 | 51.75 | 77.34 | 72.60 |
| ChartGPT | 97.34 | 94.85 | 69.21 | 73.84 | 73.03 |
| NL2VIS-CoT | 97.52 | 95.17 | 74.63 | 80.74 | 77.16 |

**消融**（Table 2，p.7）：去掉值采样 All 69.31（Data 72.11）；去掉约束 75.39；去掉 CoT 49.31；ChartGPT 步骤顺序 73.54。

**错误分析**（§6.1.3，p.7）：

- 按步骤：S1 错误 56 个，S2/S3/S4 分别为 183/202/253（含 S2 聚合函数错误 131、S3 GROUP BY 错误 191、S4 ORDER BY 错误 220）。
- 按图表类型的错误率：BAR 1.18%、PIE 2.97%、SCATTER 7.63%、LINE 9.83%。
- 95% 以上的折线/散点错误出现在多种图表都合理的情形，作者指出单一金标评测无法容纳多解。

**用户研究**（§6.3，pp.8–9）：32 人，6 个维度的 5 点 Likert；“精炼效率”负面评价 DeepVIS 9%，ncNet 50%、DeepSeek 38%、ChartGPT 47%。

**局限**（§7，p.9）：推理过程未纳入最终可视化或数据反馈；VQL 抽象限制了颜色、布局、标记大小等细粒度控制。

阅读者分析：正文列出的 Claude 为 3.5-Sonnet，而 Table 1 写作 Claude-3.7-Sonnet，原文不一致；所有数字无方差或显著性检验；测试集规模未在正文给出。

依据：[arXiv v2，11 页](https://arxiv.org/abs/2508.01700)，§6–§7，Tables 1–2、Fig.6，pp.6–9。
