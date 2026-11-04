# Yu, Lin et al. — Benchmarking Multi-Step Legal Reasoning and Analyzing Chain-of-Thought Effects in Large Language Models

本文构建 MSLR：以中国内幕交易案件的 1,389 份官方法律决定书为语料、按 IRAC（Issue-Rule-Application-Conclusion）框架标注 59,771 个步骤级字段的中文多步法律推理基准，并用它评测 19 个通用、法律和推理类 LLM 的自动标注与法律推理能力。主要结论：模型在两项任务上均未超过 80%（推理任务中 o1-mini 的 IRAC Recall 最高为 72.49），人工设计的 CoT 提示对推理模型常有负作用，模型自拟推理路径（Self-Initiated CoT）优于人工设计 CoT。已通读正文全部章节和附录 A；Figure 3/4 的数值以 PDF 渲染核对了 Figure 4。

[原文](https://arxiv.org/abs/2511.07979)

版本：arXiv:2511.07979v3（2025-11-20），14 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | 摘要、§1–2，PDF pp.1–3 |
| 方法 | §3（数据来源、PPP 标注流程、Table 1）、§4（任务与指标、Listing 4.1），PDF pp.3–7 |
| 评测 | §5、Table 2–3、Figure 2–5，PDF pp.7–10；Figure 4 已渲染核对 |
| 局限 | 原文无独立局限章节；§5、§6 及附录 A 中的相关陈述，PDF pp.8–10、14 |
