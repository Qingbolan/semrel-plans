# Alizadeh et al. — Simple Prompt Injection Attacks Can Leak Personal Data Observed by LLM Agents During Task Execution

本文在 AgentDojo 的银行任务套件上构造“数据流式”间接提示注入：让工具调用智能体把执行任务过程中看到的个人数据通过邮件发给攻击者。16 个原始任务上，多数模型在攻击下效用下降 15%–50%，平均攻击成功率（ASR）约 20%；扩展到 48 个任务后 GPT-4o 平均 ASR 约 15%，内置防御均未降到 0。已阅读正文 §1–5 和附录 A–C（提示、任务清单、Table 6–9、成本）；图中数值未逐点读取。

[原文](https://arxiv.org/abs/2506.01055)

版本：arXiv:2506.01055v1（2025-06-01，cs.CR，标注 Preprint. Under review），25 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | 摘要、§1、§3.1，pp.1–3 |
| 方法 | §3.2–3.5、附录 A、B.4，pp.3–4、17–18、23–24 |
| 评测 | §4.1–4.4、Table 2–3、Table 5–7，pp.4–9、21–22 |
| 局限 | §5 Conclusion，p.9；附录 C 成本，p.25 |
