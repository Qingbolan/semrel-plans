# Lima et al. — BidCorpus: A multifaceted learning dataset for public procurement

本文是 Data in Brief 数据论文，发布巴西公共采购招标公告语料 BidCorpus：采集 421,113 份招标公告，筛选后保留 373,650 份原始文本，并在"章节类型、采购标的、红旗（违规限制性要求）"三个数据集上标注 9 个侧面，人工标注合计一万余条，另有 221,417 条弱监督标签和模型标签。作者用 4 个葡萄牙语 BERT 类模型做 5 折验证，多数任务 F1 超过 80%（红旗分类 JurisBERT F1=92.93%），关键短语抽取使相似度判定 F1 从 32.6% 升到 96.3%。已通读全文（含局限章节）。

[原文](https://doi.org/10.1016/j.dib.2024.111202)

版本：Data in Brief 第 58 卷 111202（2024-12 在线，2025-02 期），PMC11715116 开放获取全文 JATS XML（Europe PMC REST），无页码；以下用章节与表号定位。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | Abstract、§1 Value of the Data、§2 Background |
| 方法 | §3 Data Description（Table 1–2）、§4.1–4.5（预处理、各数据集构建、Table 3–8） |
| 评测 | §4.6（Table 9–15） |
| 局限 | Limitations 章节 |
