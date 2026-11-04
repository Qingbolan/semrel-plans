# 评测与边界

**对比设置**：学习模型为 Qwen2.5-7B/32B、DeepSeek-R1-Llama-8B、GPT-OSS-20B、DeepSeek-R1、GPT-5-mini、Gemini-2.5-Flash。提示方式为 Base（只给案例和政策）、Few-shot（3 个无 PRT 示例）、Self-Refine（1 轮），各自再加随机或相似 PRT。指标为准确率；条款分析用 Recall 和 Exact-Match。

**实验 1（推理时 ICL，Table 3）**：

| 政策 / 模型 | 无 PRT 最好 | 加 PRT 最好 | 说明 |
|---|---|---|---|
| HIPAA / 开源小模型 | — | +16–30 点 | Qwen2.5-7B、R1-Llama-8B（原文概述） |
| GDPR / DeepSeek-R1 | 78.5 | 81.0 | Specialist PRT 随机示例 |
| GDPR / GPT-5-mini | 76.9 | 81.0 | Generalist PRT 相似示例 |
| ModelSpec / GPT-5-mini | 92.7（Base） | 92.1 | OpenAI 模型加 PRT 后平均下降 4.7 |

**实验 2（SFT，Table 4）**：HIPAA 上 Qwen2.5-7B 微调后加 PRT 示例达 80.4/81.3，超过 GoldCoin 79.9；但 ModelSpec 上 Qwen2.5-7B 微调后 Base 86.2 反而高于加 PRT 的 64.4–79.6，R1-Llama-8B Few-shot 为 0.0。

**实验 3（条款引用，Table 1）**：加 PRT 后 Recall 普遍上升，Exact-Match 接近 0。阅读者分析：正文写 Recall 增益 “+2.0–9.0”，但 Table 1 实际为 +1.9 到 +30.0（GPT-5-mini ModelSpec），正文与表不一致。

**边界**：无独立 Limitations 节；结论承认更高质量 PRT 需专家标注，附录 B 承认 PRT 长度波动大。伦理声明强调不应取代人工合规审查。阅读者分析：PRT 由已知答案引导生成，未评估其推理正确性；Table 2 的“利用率”由 GPT-5-mini 识别 CoT 中的引用短语得出，只说明提到 PRT，不说明推理因此正确；SFT 结果未报告多次运行方差。

依据：[arXiv:2509.23291v1](https://arxiv.org/pdf/2509.23291v1)，§3–4，PDF pp.5–9；附录 A Table 3–4，pp.17–18；§6、伦理声明，pp.9–10。
