# Li et al. — ContextLens: Modeling Imperfect Privacy and Safety Context for Legal Compliance

本文提出 ContextLens：一种半规则方法，把 GDPR 与欧盟 AI 法案拆成适用范围、特殊条件、具体条款、一般原则四个优先级，让 LLM 逐条回答结构化问题（允许“不确定”或“以上皆非”），再按法律优先级规则汇总出 Permitted / Prohibited / Not Applicable，并列出缺失或含糊的语境因素。在 PrivaCI-Bench 测试集上，它显著提升指令微调模型（尤其 AI 法案子集），但对长思维链推理模型和 GDPR 子集不总是有效。例如 Llama-3.1-8B 的 AI 法案准确率从直接提示的 58.67% 升到 86.60%，而 DeepSeek-R1 的 GDPR 准确率从 90.44% 降到 80.89%（Table 2）。已阅读正文、局限及附录 A–D 的主要部分。

[原文](https://aclanthology.org/2026.acl-long.294)

版本：ACL 2026 长文，pp.6503–6518，16 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。PDF 页码 = 论文集页码 − 6502。

| 阅读内容 | 位置 |
|---|---|
| 问题 | §1、§3.1–3.2，PDF pp.1–4 |
| 方法 | §3.3–3.6、附录 A、D，PDF pp.4–5、12–13 |
| 评测 | §4–§6、Tables 1–6，PDF pp.5–9；附录 B–C Table 7，PDF p.12 |
| 局限 | Limitations，PDF pp.9–10 |
