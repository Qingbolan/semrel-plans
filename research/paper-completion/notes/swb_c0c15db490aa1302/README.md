# Loukas et al. — FiNER: Financial Numeric Entity Recognition for XBRL Tagging

本文把为美国 SEC 年报/季报文字附注标注 XBRL 标签定义为新的实体抽取任务，发布 FiNER-139：约 110 万句、139 个 US-GAAP 标签，约 91% 的标注片段是数字。作者发现 BERT 的子词切分会把数字切碎，提出用 `[NUM]` 或 `[SHAPE]` 伪 token 替换数字，并发布在 20 万份 SEC 文件上预训练的 SEC-BERT；SEC-BERT-SHAPE 测试集实体级 µ-F1=82.1。已通读正文与附录 A–B；图 2–5 只依据正文与图注。

[原文](https://aclanthology.org/2022.acl-long.303)

版本：ACL 2022 长文，论文集 pp.4419–4431（ACL Anthology 2022.acl-long.303），13 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | §1–3，PDF pp.1–4 |
| 方法 | §4、§6–7，PDF pp.4–6；附录 A，p.12 |
| 评测 | §5、§8–9.3、Tables 3–6，PDF pp.4–8；附录 B（Tables 8–9），p.13 |
| 局限 | §9.4、§10，PDF pp.8–9 |
