# 评测与边界

参评模型共 26 个，包括 Llama-3.1、Qwen2.5、DeepSeek、GPT、Gemini、Claude、InternVL3 等 LLM/VLM，另加三名专家组成的人类基线。DeepSeek-VL2-27B 受 4K 上下文限制，只参加 Single-Violation（§4.1）。指标为 Partial 与 Full Accuracy（%）。

**实验 1（Single-Violation，Table 2，p.5）**：

| 模型 | Partial | Full |
|---|---|---|
| DeepSeek-R1（文本） | 54.64 | 25.45 |
| GPT-4.1（文本） | 52.74 | 31.59 |
| Claude-3.7（图像） | 58.79 | 23.42 |
| GPT-4o（图像） | 58.47 | 26.96 |
| DeepSeek-VL2（图像） | 29.12 | 12.24 |
| 人类（文本 / 图像） | 69.34 / 69.20 | 57.03 / 51.41 |

Partial 与 Full 的差距普遍超过 10 个百分点。Qwen3 的 thinking 模式几乎没有提升，Qwen3-32B 甚至下降（Table 3）。

**实验 2（All-in-One，Table 4，p.6）**：多数模型在此设置下提升，Partial 与 Full 的差距缩小到约 5 个百分点。示例（Partial / Full）：

| 模型 | Single-Violation（Table 2） | All-in-One Simplified | All-in-One Detailed |
|---|---|---|---|
| Qwen2.5-7B | 38.48 / 27.18 | 51.68 / 49.52 | 53.18 / 50.60 |
| Gemini2.5-pro | — | 70.57 / 54.45 | 70.43 / 51.94 |
| Qwen2.5VL-72B | — | 64.25 / 59.09 | 63.85 / 59.44 |

**实验 3（RAG/SFT，Fig.2，p.6）**：两者都显著提升；正文只给图形，没有数值表。

**实验 4（分解推理，Table 6，p.7）**：不分解时 GPT-4o 为 59.61/29.14；以 GPT-4o 描述图片、GPT-4.1 推理时为 61.65/32.76。

**边界**：

- 原文没有独立的 Limitations 节。
- 主结果没有方差或重复运行。
- 除 RAG/SFT 外没有训练/测试划分。
- Table 6 未说明使用的任务轨。其中 GPT-4o 不分解的结果（59.61/29.14）与 Table 2 的 58.47/26.96 不同，口径不明（阅读者分析）。
- 样本筛选和金标准修订都参照了参评模型的预测，见贡献栏（阅读者分析）。

依据：§4–6、Tables 2–6、Fig.2，PDF pp.4–7。
