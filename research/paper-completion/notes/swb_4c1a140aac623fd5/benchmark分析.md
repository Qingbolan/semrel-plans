# 评测与边界

**设置**：基线为 Tree Search、MedCodER、CLH（三者为 LLM 方法，与本文使用相同骨干和知识源），以及监督模型 PLM-ICD（约 1.6 万码空间）。骨干为 Qwen3、DeepSeek-V3、GPT-4o、GPT-4.1、GPT-5（low reasoning），温度 0.2。指标为就诊层面的 micro/macro P/R/F1，三次运行取均值（§6、§7，pp.5–6）。

**实验 1（MDACE，7 万码空间，Table 1，p.7）**，以 micro-F1 / macro-F1 表示：

| 骨干 | CLH | RAG-Coding |
|---|---|---|
| Qwen3 | 0.35 / 0.17 | 0.41 / 0.18 |
| DeepSeek-V3 | 0.41 / 0.21 | 0.44 / 0.22 |
| GPT-4.1 | 0.40 / 0.20 | 0.53 / 0.27 |
| GPT-5 | 0.46 / 0.24 | 0.54 / 0.32 |

**实验 2（与 PLM-ICD 比较，Table 2）**：RAG-Coding 预测经后处理限制在同样的 1.6 万码内。PLM-ICD 为 0.54/0.53/0.53（micro P/R/F1）；GPT-5 RAG-Coding 为 0.48/0.64/0.55。作者自己承认这并非完全对等的比较。

**实验 3（MDACE-2025，GPT-5，Table 3，p.8）**：RAG-Coding micro-F1 为 0.56，macro-F1 为 0.33；PLM-ICD 为 0.48 和 0.26；CLH 为 0.45 和 0.26。

**实验 4（消融，GPT-4.1，Table 4）**：只用步骤 1 时 micro-F1 为 0.41，加步骤 2 为 0.47，四步全用为 0.51。不使用外部知识、只让模型自我修正（closed-book）时没有提升（Table 11）。

**局限**：原文承认只评测了 ICD-10-CM 和英文文书（Limitations，p.9）。

**阅读者分析**：

- Table 4 中四步完整流程的 micro-F1 为 0.51，而 Table 1 同一骨干（GPT-4.1）为 0.53，P/R 也不同（0.48/0.54 对 0.47/0.59），论文未解释差异（阅读者分析）。
- 测试集只有 61 个就诊（阅读者分析）。

依据：§6–7、Tables 1–4、附录 F–G，PDF pp.5–9、13–15。
