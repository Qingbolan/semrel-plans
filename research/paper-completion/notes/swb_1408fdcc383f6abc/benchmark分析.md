# 评测与边界

**模型**：Mistral-7B-Instruct-v0.2、Qwen2.5-7B-Instruct、Llama-3.1-8B-Instruct、GPT-4o-mini、QwQ-32B、DeepSeek-R1（671B）。推理模型不跑 RAG（§4.2，p.6）。

**实验 1（合规判断准确率，Table 2，p.7，%）**：节选 DP / CoT。

| 模型 | AI Act DP/CoT | GDPR DP/CoT | HIPAA DP/CoT | ACLU DP/CoT |
|---|---|---|---|---|
| Llama-3.1-8B | 61.30 / 59.40 | 85.30 / 90.27 | 77.57 / 85.51 | 66.17 / 66.67 |
| GPT-4o-mini | 73.76 / 66.60 | 92.03 / 65.69 | 80.84 / 67.75 | 69.56 / 31.88 |
| QwQ-32B | 78.22 / 75.30 | 80.45 / 90.08 | 70.09 / 88.31 | 55.07 / 55.07 |
| DeepSeek-R1 | 72.90 / 60.67 | 90.66 / 47.88 | 89.25 / 81.77 | 65.21 / 59.42 |

原文结论：AI Act 与 ACLU 最难；CoT 效果因模型而异（GPT-4o-mini、R1 用 CoT 反而下降）；RAG 仅在 HIPAA 上最好（Llama 88.31），在 GDPR 与 AI Act 上明显下降。

**实验 2（AI Act 分类细节，Table 3）**：Mistral-7B DP 的“允许”召回仅 0.49%，“不适用”召回 99.90%，模型分不清允许与不适用。

**实验 3（情境理解多选题，Table 4，p.8）**：平均准确率 Easy 约 88–92%、Medium 约 78–86%、Hard 约 55–67%；GPT-4o-mini 在 GDPR 与 HIPAA 上平均约 89%，AI Act 普遍最低（平均 73.65）。

**实验 4（消融，Fig.2）**：DP+CI 明显提升，HIPAA 与 ACLU 提升尤为明显；DP+CI+LAW 在所有方法中最好。原文据此认为检索到相关且适用的法条时 RAG 有效，朴素检索失败会拖累表现。

**实验 5（人工核查，Table 5）**：3 名作者每域抽 30 例，Role/TP/Label 一致率 90–100%；AI Act 案例的 Role 最低（90.00）。

**边界（原文）**：只以法律条文作为隐私规范，不涵盖文化与伦理规范；不做 few-shot；主实验单次运行；提示敏感性仅在附录对两个模型做 3 次运行（Tables 13–14，CoT 标准差最高 14.38）；AI Act 合成情境叙事不连贯（Limitations p.9、附录 C.2–C.3）。

依据：§4–5、Tables 2–5、Fig.2，PDF pp.5–8；Limitations p.9；附录 C、Tables 12–14，pp.13–15。
