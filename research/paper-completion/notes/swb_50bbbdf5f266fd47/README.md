# Imperial & Tayyar Madabushi — Scaling Policy Compliance Assessment in Language Models with Policy Reasoning Traces

本文提出 Policy Reasoning Traces（PRT）：用 DeepSeek-R1 或 SaulLM-54B 这类“伪专家”模型，根据训练集里的案例、金标准结论和政策全文，生成逐条引用条款的推理链；再把 PRT 当作少样本示例或 SFT 数据，提升模型判断“案例是否合规”的能力。在 HIPAA、GDPR、OpenAI ModelSpec 三套政策上评测，HIPAA 和 GDPR 提升明显，但已用 ModelSpec 做过安全对齐的 OpenAI 模型反而下降。已阅读正文 §1–§6、伦理/复现声明、附录 A 全表和附录 B 的 PRT 统计；附录 C 之后的 PRT 示例与提示词只抽查。

[原文](https://arxiv.org/abs/2509.23291)

版本：arXiv:2509.23291v1（2025-09-27 预印本），34 页（正文 10 页，附录至 p.34）。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | §1、§2.1–2.2，PDF pp.1–3 |
| 方法 | §2.3–2.4、§3，PDF pp.3–6 |
| 评测 | §4（Fig.3–4、Table 1–2），PDF pp.6–9；附录 A Table 3–4，pp.17–18 |
| 局限 | §6 结论、伦理声明，pp.9–10；附录 B PRT 统计，p.18 |
