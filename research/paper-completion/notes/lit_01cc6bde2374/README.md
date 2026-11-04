# Sarthi et al. — RAPTOR: Recursive Abstractive Processing for Tree-Organized Retrieval

RAPTOR 是一种检索索引方法：把文档切成约 100 token 的块，递归地做“嵌入—软聚类—LLM 摘要”，自底向上构成多层摘要树，查询时在所有层的节点中按相似度检索（collapsed tree）。在 NarrativeQA、QASPER、QuALITY 上，同一检索器加上 RAPTOR 树后都有提升；RAPTOR+GPT-4 在 QuALITY 测试集达到 82.6%，比此前最佳的 62.3% 高约 20 个百分点。已读正文及附录 A–I；未复现实验。

[原文](https://arxiv.org/abs/2401.18059)

版本：arXiv:2401.18059v1（2024-01-31），ICLR 2024 会议论文，23 页（含附录）。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | 摘要、§1–2，PDF pp.1–3 |
| 方法 | §3、Figures 1–3，PDF pp.3–6；附录 D、F |
| 评测 | §4、Tables 1–8，PDF pp.6–9；附录 A–C、E、H、I，PDF pp.15–22 |
| 局限 | §3（摘要幻觉、collapsed tree 需全量相似度计算）、附录 E、H，PDF pp.4、6、17–21；无独立局限章节 |
