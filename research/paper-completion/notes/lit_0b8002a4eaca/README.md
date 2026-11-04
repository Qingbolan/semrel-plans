# Li, Yuan, Wang, Cong, Bing — LLM-R2: A Large Language Model Enhanced Rule-based Rewrite System for Boosting Query Efficiency

LLM-R2 让 LLM 从 Apache Calcite 的候选改写规则中选择规则序列，再由 Calcite 执行改写，从而保证改写后 SQL 可执行且与原查询等价；核心技术是用对比学习加课程学习训练的查询表示模型，为每条输入查询挑选一个 one-shot 示例。在 TPC-H、IMDB(JOB)、DSB 上，平均执行时间降到原查询的 52.5%、56.0%、39.8%，降到 Learned Rewrite 基线的 94.5%、63.1%、40.7%。

已阅读正文全部章节，并对照 `pdftotext -layout` 文本核对 Tables 2–7；未渲染核对 Tables 8–11 的排版。

[原文](https://doi.org/10.14778/3696435.3696440)

版本：PVLDB Vol.18 No.1，pp.53–65，2024，doi:10.14778/3696435.3696440（取自 vldb.org 的开放 PDF），13 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | §1、§2.1–2.2（Definition 2.1、式 1），PDF pp.1–2 |
| 方法 | §3–5（Definition 3.1、Figures 2–7、Algorithm 1、式 2–4），PDF pp.3–8 |
| 评测 | §6、Tables 2–11、Figure 8，PDF pp.8–12 |
| 局限 | §6.3、§6.5.3、§7，PDF pp.9–12 |
