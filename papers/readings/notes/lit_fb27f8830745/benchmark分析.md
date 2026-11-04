# benchmark

**实验 1（Table 1，K=10）**：NVIDIA NeMo Recall 0.60、nDCG 0.42、MAP 0.34（最佳）；Amazon Nova Recall 0.58；Cohere v4 在 K=5 的 nDCG 0.33、MAP 0.35 最好；Jina v4 Recall 仅 0.33。

**实验 2（FRTR-Bench，Table 2）**：BRTR 下 GPT-5 与 Gemini 3 Pro 均为 0.99（157/159），Claude Opus 4.6、GPT-5.2 为 0.98；最佳单次 FRTR 为 0.74；SpreadsheetLLM 压缩为 0.06–0.34；Claude in Excel（Opus 4.6）为 0.84。GPT-5.2 平均 3.05 次调用、20,127 token、90.81 秒；Opus 4.6 平均 462,614 token。BRTR 仅 2 处错误，均为嵌入图像 OCR 误读。

**实验 2（SpreadsheetLLM 基准，Table 3）**：前沿模型 BRTR 最好，较弱模型反而不如单次方法。

| 模型 | BRTR | FRTR | SpreadsheetLLM 压缩 | 朴素全文 |
|---|---|---|---|---|
| GPT-5 | 0.98 | 0.87 | 0.90 | 0.68 |
| Claude Sonnet 4.5 | 0.97 | 0.84 | 0.91 | 0.55 |
| Gemini 2.5 Pro | 0.79 | 0.85 | 0.89 | 0.67 |
| GPT-4o | 0.56 | 0.77 | 0.78 | 0.35 |
| LLaMA 4 Maverick | 0.30 | 0.53 | 0.73 | 0.41 |

**实验 3（FINCH，Table 4）**：BRTR + Opus 4.6 为 95.3%（164/172），GPT-5.2 为 94.8%；相对单次调用 API agent 提升 +48.9（GPT-5.2）、+66.9（Sonnet 4.5）、+46.0（Gemini 3 Pro）个百分点；FINCH 原论文最好为 41.9%（自动评测）。成本为中位数：GPT-5.2 223K token/工作流，Opus 358K。失败集中在公式未求值、遗漏指令子步骤和多表生成不完整。

**实验 4（50 任务消融，Table 5）**：完整 0.88；无规划器 0.68（token 521K 对 312K）；朴素 0.46；全文注入 0.52（7/50 超出 200K 上下文，3 个网页任务无源文件）；无 agent 循环 0.00。

阅读者分析：摘要中的"在 SpreadsheetLLM 上超出 7 个点"只适用于前沿模型，较弱模型出现反转（作者在讨论中承认存在"能力阈值"）；FINCH 的"+32 点"对应 Opus 4.6 的 BRTR 0.95 对朴素 0.63，而与 FINCH 原论文 41.9% 的比较使用不同评测方式（人工对自动）。人工评审由作者团队完成，原文未报告评审间一致性，也未报告多次运行的方差。

依据：[arXiv:2603.06503v1，15 页](https://arxiv.org/abs/2603.06503)，§4.1–4.5、Tables 1–5，PDF pp.5–10；附录 B，PDF pp.13–14。
