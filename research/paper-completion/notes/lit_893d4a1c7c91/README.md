# Zhang, Liu et al. — AutoDDG: Automated Dataset Description Generation using Large Language Models

AutoDDG 为表格数据集自动生成描述：先用 Datamart Profiler 对全表做统计画像，再用 LLM 做逐列语义画像和主题生成，最后产出面向阅读的 UFD 与面向检索的 SFD。

作者把 ECIR 与 NTCIR 表格检索集合改造成 ECIR-DDG（120 查询、1,015 表）和 NTCIR-DDG（32 查询、615 表），在 BM25 下 SFD-GPT 的 ECIR NDCG@10 为 0.856，而原始描述为 0.658。已阅读正文 §1–4、§6 和附录中的提示词与统计；未逐项核对附录全部 SPLADE 数值。

[原文](https://arxiv.org/abs/2502.01050)

版本：arXiv:2502.01050v3（2025-12-18，J. ACM 排版预印本），32 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| problem | §1–2，PDF pp.1–6 |
| method | §2.1–2.2、Algorithm 1、Figs.2–7，PDF pp.6–9 |
| evaluation | §3–4、Tables 1–5、Figs.8–11，PDF pp.10–20 |
| limitations | §3.2、§4.3 用户评估、§6，PDF pp.11–12、16、22–23 |
