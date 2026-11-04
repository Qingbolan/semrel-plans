# Gao, Wang et al.（Alibaba）— Text-to-SQL Empowered by Large Language Models: A Benchmark Evaluation

本文系统比较 LLM Text-to-SQL 的提示工程选项（5 种问题表示、外键与规则两个提示成分、4 种示例选择、3 种示例组织）以及开源模型的零/少样本与监督微调，并据此提出 DAIL-SQL：用 `CREATE TABLE` 代码表示 schema，按问题与 SQL 骨架双重相似度选例，只放问题–SQL 对。DAIL-SQL + GPT-4 在 Spider-dev 上执行准确率 83.5%，在 Spider 排行榜测试集上 86.2%，加自一致性后 86.6%（2023-09-19 排名第一）。已阅读正文 §1–§6 与附录 A.2、C.3、F。

[原文](https://arxiv.org/abs/2308.15363)

版本：arXiv 2308.15363v4（2023-11-20），22 页（正文 13 页 + 附录）。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | §1–§3 开头，PDF pp.1–3 |
| 方法 | §3.1–3.4、Listings 1–8、附录 A.2，PDF pp.3–6、15–16 |
| 评测 | §4.1–4.5、Tables 2–4、Figures 1–7、附录 C.3 Table 12、附录 F，PDF pp.6–12、18、21–22；Tables 2、3、12 已用版面文本核对 |
| 局限 | §5 末段，PDF p.13 |
