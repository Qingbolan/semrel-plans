# Kim, Kim & Aizawa — Refining and Reusing Annotation Guidelines for LLM Annotation

本文研究把面向人工标注者的标注指南放入 LLM 提示中，并用"审核（moderation）"循环自动修订指南：在 10 篇开发文档上比对金标、找出主导错误模式，再由 LLM 生成规则写回指南。在 NCBI Disease、BC5CDR、BioRED 三个生物医学 NER 任务上，加入原指南使严格 F1 提高 0.02–0.27，自动修订再提高 0.01–0.06，后者仅部分达到统计显著。已阅读正文、局限及附录 Figures 5–7、Tables 4–7。

[原文](https://aclanthology.org/2026.acl-long.1760)

版本：ACL 2026 长文，ACL Anthology 2026.acl-long.1760，pp.37951–37964，14 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | §1、§3.1，PDF pp.1–3 |
| 方法 | §3.2–3.4、Figures 1–2，PDF pp.3–5 |
| 评测 | §4–5、Tables 1–3、附录 Tables 4–7，PDF pp.5–9、11、14 |
| 局限 | §6.2、Limitations，PDF pp.8–10 |
