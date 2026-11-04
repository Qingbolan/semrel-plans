# Wang, Wang, Shu, Liu, Shao, Liu, Chen — ChartInsighter: An Approach for Mitigating Hallucination in Time-series Chart Summary Generation with A Benchmark Dataset

本文面向时间序列折线图的自动摘要。作者先归纳 L1–L3 摘要要素和 10 类 LLM 幻觉，再提出 ChartInsighter：以 Vega-Lite 规格和数据表为输入，多个 GPT-4 代理调用外部数据分析模块，迭代生成摘要，最后用自一致性检验修正极值和幅度描述。

作者同时发布 75 张图表的基准，含金标准摘要和三种系统摘要的逐句幻觉标注。该基准上 ChartInsighter 幻觉率 0.14，GPT-4 为 0.48，VL2NL 为 1.63（Table 1）。全文已读，Table 1 页已渲染核对。

[原文](https://arxiv.org/abs/2501.09349)

版本：arXiv:2501.09349v1，11 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| problem | §1、§3，PDF pp.1–4 |
| method | §4、Fig.4，PDF pp.4–6 |
| evaluation | §5–6、Table 1、Fig.7，PDF pp.7–9；p.8 已渲染核对 |
| limitations | §7，PDF p.9 |
