# Bodensohn, Brackmann, Vogel, Sanghi, Binnig — Unveiling Challenges for LLMs in Enterprise Data Engineering

本文用 SAP 真实客户数据和贴近真实的案例，系统评测 LLM 在企业数据工程中的表现，把难点归为数据、任务、知识三类（C1–C10），另讨论成本。核心发现：列类型标注在公开基准上 F1 可达 0.9 以上，在 SAP 数据上带列名也只有 0.07–0.34；付款—发票匹配随任务复杂度增加从约 0.97–0.99 降到 0.45–0.72；Text-to-SIGNAL 执行准确率最高约 0.35。

这是评测研究，不是新系统。已阅读正文 §1–§8，并渲染核对 Table 6、Table 7、Figure 10。

[原文](https://www.vldb.org/pvldb/vol19/p196-bodensohn.pdf)

版本：PVLDB 19(2): 196–209, 2025，doi:10.14778/3773749.3773758，14 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。部分设置细节（附录 A.1–A.5）在扩展技术报告中，未阅读。

| 阅读内容 | 位置 |
|---|---|
| 问题 | §1、§3，PDF pp.1–4 |
| 方法 | §2（Table 1 模型）、§3（Figure 2）、各实验 Setup 段，PDF pp.2–4、5、7–9、11 |
| 评测 | §4.2、§5.2–5.3、§6.2、§7，Tables 2–7、Figures 1、3–11，PDF pp.4–12；Table 6/7、Figure 10 已渲染核对 |
| 局限 | §2“Working with real enterprise data”、§4.3、§5.4、§6.3、§8，PDF pp.3、6、10–12 |
