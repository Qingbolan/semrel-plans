# 评测与边界

**实验 1（自动标注，Table 2，PDF p.7）**：所有模型的 FCR 与 Overall Accuracy 均未超过 80%。

| 模型 | FCR | Overall Acc |
|---|---|---|
| DeepSeek-V3 | 69.65 | 77.43 |
| GPT-4 | 73.28 | 77.23 |
| o1-mini | 64.99 | 76.45 |
| Cleverlaw | 78.43 | 61.79 |
| Law-Justice | 3.87 | 39.32 |

作者据此认为纯 LLM 标注不能替代人工，PPP 人机协作是必要的，并选 DeepSeek-V3 为标注助手（§5，PDF p.7）。

**实验 2（推理任务，标准输入 vs 人工设计 CoT，Table 3，PDF p.9）**：

| 模型 | Std IRAC | Std LLM | H-CoT IRAC | H-CoT LLM |
|---|---|---|---|---|
| o1-mini | 72.49 | 69.69 | 70.08 | 55.51 |
| DeepSeek-R1 | 65.81 | 94.82 | 58.61 | 62.71 |
| QwQ-32B | 65.74 | 93.70 | 55.54 | 59.90 |
| GPT-4o | 66.06 | 68.47 | 71.78 | 88.98 |
| Lawyer-LLM | 45.86 | 27.65 | 52.56 | 65.15 |

人工 CoT 提升了全部 4 个法律模型和大多数通用模型，但使 Qwen2.5-72B、DeepSeek-V3 及多数推理模型下降，QwQ-32B 的 LLM Score 降 33.80、IRAC Recall 降 10.20（§5，PDF p.8）。

**实验 3（指标效度）**：IRAC Recall 与 LLM Score 的 Pearson 相关在两种输入下分别为 0.85 和 0.83（p<0.001）；380 条输出的专家评级与 DeepSeek-R1 评级一致率 87.96%（Figure 2、§5，PDF pp.7–8）。one-shot 只带来有限提升（Figure 3，PDF p.9）。

**实验 4（自拟 CoT，Figure 4，PDF p.10）**：在 DeepSeek-V3、QwQ-32B、DeepSeek-R1 上，自拟 CoT 的 IRAC Recall/LLM Score 为 65.71/80.19、65.34/92.56、65.85/94.65，均高于人工 CoT。

阅读者分析：把 Figure 4 与 Table 3 的标准输入对比，三个模型自拟 CoT 与标准输入几乎相同（如 QwQ-32B 标准输入 65.74/93.70，自拟 CoT 略低），所以证据支持"自拟 CoT 避免了人工 CoT 的损害"，而非"自拟 CoT 明显提升推理"；摘要中"consistently improve"的说法偏强（阅读者分析）。

阅读者分析：LLM Score 的评委 DeepSeek-R1 同时是被测模型，可能存在自评偏好；单次推理、无方差报告；没有独立局限章节，仅覆盖内幕交易一个罪名/违法类型。
