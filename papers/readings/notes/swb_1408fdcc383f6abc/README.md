# Li, Hu, Jing et al. — PrivaCI-Bench: Evaluating Privacy with Contextual Integrity and Legal Compliance

本文按情境完整性（Contextual Integrity, CI）理论构建隐私合规评测：收集 HIPAA 判例、GDPR 执法案例、隐私政策、基于 EU AI Act 官方合规检查器生成的合成案例和 ACLU 案例，让 LLM 判断“允许 / 禁止 / 不适用”，并由 CI 参数生成 147,840 道多选题，用于检测模型对情境的理解。

结果显示模型能较好识别 CI 参数（Easy 约 90%、Hard 约 60%），但合规判断仍不稳定；朴素 CoT 与 RAG 并不总是有效，给入金标准 CI 参数和适用法条后效果最好。已阅读正文、Limitations 与附录 A–C。

[原文](https://aclanthology.org/2025.acl-long.518)

版本：ACL 2025 Long Papers（ACL Anthology 2025.acl-long.518，pp.10544–10559），16 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | §1–2、Table 1，PDF pp.1–3 |
| 方法 | §3（数据收集、CI 解析、多选题、知识库）、§4，PDF pp.3–6；附录 A–B，p.13 |
| 评测 | §5、Tables 2–5、Fig.2，PDF pp.6–8；附录 C、Tables 10–14，pp.13–15 |
| 局限 | Limitations、Ethical Considerations，PDF p.9；附录 C.2，p.14 |
