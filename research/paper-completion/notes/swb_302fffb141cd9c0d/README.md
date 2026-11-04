# Chen et al. — TabFact: A Large-scale Dataset for Table-based Fact Verification

TabFact 是以维基百科半结构化表格为证据的事实核验数据集：约 16K 张表、118K 条众包陈述，标签为 ENTAILED 或 REFUTED。作者提出 Table-BERT（表格线性化后做 NLI）和 LPA（潜在程序搜索加判别器排序）两类基线，两者测试准确率约 65%，远低于人类在小测试集上的 92.1%。已阅读正文与附录（函数集、触发词、错误分析、实体链接、标注界面说明）。给定的 OpenReview PDF 链接返回 HTML 页面，实际保存的是同一论文的 arXiv v5（ICLR 2020 camera-ready）。

[原文](https://openreview.net/pdf?id=rkeJRhNYDH)

版本：ICLR 2020 会议版，arXiv:1909.02164v5（2020-06-14），25 页（含附录）。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | §1、§3 开头，PDF pp.1–4 |
| 方法 | §2 数据构建，§3.1 LPA，§3.2 Table-BERT，PDF pp.3–6 |
| 评测 | §4、Table 2，PDF pp.7–8 |
| 局限 | §4 Results、附录错误分析，PDF pp.8、15–17 |
