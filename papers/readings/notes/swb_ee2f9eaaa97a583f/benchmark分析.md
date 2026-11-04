# 评测与边界

**被测模型**（§4.1）：7 个闭源模型、8 个开源模型（Qwen2.5 1.5B–14B、Qwen3 4B/14B、Llama3.2-3B、Llama3.1-8B）和 2 个护栏模型；论文未说明解码温度或是否只跑一次。

**实验 1（主结果，Figure 2 平均 macro-F1，PDF p.5）**：

| 模型 | 平均 macro-F1 |
|---|---|
| GLM-4.5 | 92.28 |
| DeepSeek-V3.2 | 92.24 |
| GPT-4o-Mini | 91.73 |
| Qwen2.5-3B-Instruct | 88.62 |
| Claude-3.5-Haiku | 87.95 |
| Grok-4.1 | 85.60 |
| Llama3.1-8B-Instruct | 76.02 |
| Qwen2.5-1.5B-Instruct | 57.06 |
| WildGuard-7B / Llama-Guard-3-8B | 38.41 / 28.16 |

作者结论：平台政策类低于正式法律（GLM-4.5 为 89.61 vs 93.65）；"教育：偏见与歧视"最难；EU 金融法规普遍 95–97；3B 左右是保持较好表现的经验下限；Qwen 系列优于同规模 Llama；护栏模型很差，GDPR、HIPAA 上 Llama-Guard 只有 24.58、19.09（§4.2.1）。

**实验 2（分类别 F1，Figure 3）**：小模型 permitted 类 F1 明显低于 prohibited，如 Llama3.2-3B 在 HIPAA 上相差 29.02。

**实验 3（EU AI Act 分章，Figure 4）**：第二章"禁止的 AI 实践"上四个模型均低于 80。

**实验 4（规则–案例对齐，Table 3，PDF p.8）**：1–3 分量表，归一化后平均 DeepSeek-V3.2 91.32、GPT-4o-Mini 92.51、Gemini-2.5-Flash 95.90；人工（每部法规抽 30 例，共 2,220 例，3 名博士生）91.77。Reddit 政策最低（人工 82.59）。

**边界**：人工只抽检相关性，未核验案例真实性与标签正确性（Limitations，PDF p.9）；案例可能含个人信息，作者称发布前会过滤。阅读者分析：护栏模型的设计目标是有害内容审核，而非法规合规判断，用于比较时任务不匹配。Table 3 中出现"Data Act (CN)"一行，与 Table 2 的"Data Security"不一致，可能是笔误。
