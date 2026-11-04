# 评测与边界

**基线**：Direct（多选题模板直接提示）、Long CoT（DeepSeek-R1、o3-mini、Gemini-2.5-Flash）、RAG（BM25 检索法条，按 PrivaCI-Bench 实现）、Fine-tuned（在 PrivaCI-Bench 训练集上 SFT/PPO 的 ContextReasoner-7B）。指标为准确率与 Macro-F1，无法解析的输出算错。

**实验 1（整体合规，Table 2，准确率 %）**：

| 模型 | 设置 | AI Act | GDPR | 平均 |
|---|---|---|---|---|
| GPT-4o-mini | Direct | 71.16 | 92.19 | 81.68 |
| GPT-4o-mini | ContextLens | 88.11 | 91.87 | 89.99 |
| Llama-3.1-8B | Direct | 58.67 | 86.88 | 72.78 |
| Llama-3.1-8B | ContextLens | 86.60 | 88.85 | 87.73 |
| ContextReasoner-7B-PPO | Fine-tuned | 84.33 | 92.19 | 88.25 |
| DeepSeek-R1 | Long CoT | 84.00 | 90.44 | 87.22 |
| DeepSeek-R1 | ContextLens | 86.31 | 80.89 | 83.60 |

收益主要来自 AI 法案子集；GDPR 上不稳定，长思维链模型使用 ContextLens 或 RAG 后 GDPR 准确率下降（如 Gemini-2.5-Flash 92.03→83.12）。

**实验 2（语境不完整，Tables 3–4、7）**：三种模型标出不完整语境的比例为 98.33–100%，每例平均 4.93–7.48 个未知因素。GPT-4o-mini 在 Art. 6 上，错误判断中含未知因素的比例比正确判断高 28.76 点。人工与 LLM 的 Cohen’s κ 在 GDPR 为 1.00，在 AI 法案为 0.91–0.97；三模型间 Fleiss’ κ 在 GDPR 只有 0.21。

**实验 3（成本，Table 6）**：GPT-4o-mini + ContextLens 平均准确率高于 GPT-4o 直接提示，但 GDPR 输入 token 增至约 20 倍。

**边界与不一致（阅读者分析）**：

- 局限节称 ContextLens 对指令微调模型“总是有效”，但 Table 2 中 Qwen2.5-7B（88.37→85.19）和 GPT-4o（92.19→89.31）在 GDPR 上都下降（阅读者分析）。
- 正文称“近 100% 案例含 5 个以上未知因素”，但 Llama 在 GDPR 上平均仅 4.93（阅读者分析）。
- Qwen2.5-7B 的 ContextLens 平均准确率表中为 70.61，而按两子集简单平均计算为 69.91（阅读者分析）。
- §4.2 的模型列表未列出表中出现的 Llama-3.1-8B、OpenThinker-7B 和 GPT-5（阅读者分析）。

依据：[ACL 2026 长文，pp.6503–6518，16 页](https://aclanthology.org/2026.acl-long.294)，§4.2–4.3，PDF pp.5–6；§5.1–5.2、Tables 2–4，PDF pp.6–8；§6、Table 6，PDF pp.8–9；Limitations，PDF pp.9–10；附录 C.1、Table 7，PDF p.12。
