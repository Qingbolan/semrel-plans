# Müller — pyMMAX2: Deep Access to MMAX2 Projects from Python

本文是一篇软件短文，介绍 pyMMAX2：一个用纯 Python 读写 MMAX2 离位（stand-off）标注数据的 API；其中标注方案（annotation scheme）的校验逻辑不重新实现，而是通过 JPype 在运行时调用原 MMAX2 Java 库，即标题中的"深度访问"。论文以三个代码示例说明功能：基础数据分词与渲染、对 ACL Anthology 共指语料的加载与校验、从 LitCovid BioC 文档创建新项目。论文没有定量实验。已通读全文 7 页。

[原文](https://aclanthology.org/2020.law-1.16)

版本：第 14 届 Linguistic Annotation Workshop（LAW 2020）论文集 pp.167–173，7 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | §1，PDF pp.1–2 |
| 方法 | §2、§2.1–2.2，PDF pp.2–4 |
| 评测 | 无定量评测；§2.2–2.3 示例输出，PDF pp.4–5 |
| 局限 | 无独立局限章节；§1 与 §2.2 中的范围说明，PDF pp.1–2、4 |
