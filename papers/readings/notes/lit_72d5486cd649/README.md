# Jin, Choi, Zhu, Kang — Pervasive Annotation Errors Break Text-to-SQL Benchmarks and Leaderboards

这是一篇针对 Text-to-SQL 基准标注质量的实证研究：借助自建的审核智能体 SAR-Agent（o3 驱动、可多轮执行验证查询）生成诊断报告、再由作者人工裁定，发现 BIRD Mini-Dev 498 例中 52.8%、Spider 2.0-Snow 有公开金标准的 121 例中 62.8% 存在标注错误；人工修正 BIRD Dev 随机 100 例后重跑 16 个开源智能体，执行准确率相对变化 −7%～+31%，排名变化 −9～+9，原/修正子集排名的 Spearman 相关仅 0.32（p=0.23）。已阅读正文 §1–9 与附录 A.1–A.4（含 Tables 8–9）。

[原文](https://arxiv.org/abs/2601.08778)

版本：arXiv:2601.08778v3（2026-01-19），18 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| problem | Abstract、§1–2，PDF pp.1–3 |
| method | §3（SAR-Agent、SAPAR）、§4.1–4.2、§5.1，PDF pp.3–5、7–8；附录 A.1、A.3，PDF pp.15–16 |
| evaluation | §4.3–4.4（Tables 1–3）、§5.2–5.5（Table 4–6、Figures 6–9）、§6（Table 7、Figure 10）、§7（Figure 11），PDF pp.5–12；Tables 8–9，PDF pp.17–18 |
| limitations | 原文无局限性章节；附录 A.2 注明模型替换（Table 8 脚注，PDF p.17），其余局限由阅读者归纳 |
