# Zhu, Chen, Ke, Fang, Li, Gao, Jensen — Beyond Relational: Semantic-Aware Multi-Modal Analytics with LLM-Native Query Optimization

本文提出 Nirvana：一个带 map/filter/reduce/rank 语义算子的多模态分析框架。

核心是两层优化：用 LLM 按自然语言改写规则并以随机游走搜索候选逻辑计划（LLM-as-a-judge 在样本上判等价），以及以“improvement score”为每个算子贪心选择最具性价比的 LLM 后端。在 Movie/Estate/Game 三个数据集、各 12 条查询上，相对 Palimpzest 和 Lotus 中较优者，运行时间降低 10.16%–84.46%、成本降低 18.16%–97.96%（Table 4）。

已阅读正文与附录；Table 4–6 页已渲染核对。

[原文](https://arxiv.org/abs/2511.19830)

版本：arXiv:2511.19830v1，20 页（含附录）。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| problem | §1、§2，PDF pp.1–5 |
| method | §3–4、Alg.1–2、Eqs.1–8，PDF pp.5–9；附录 A |
| evaluation | §5、Tables 3–8、Figs.6–12，PDF pp.8–13；p.10 已渲染核对 |
| limitations | §5.3.3、§5.6.2、附录风险讨论，PDF pp.11、13、17 |
