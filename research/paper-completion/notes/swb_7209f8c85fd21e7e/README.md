# Queen, Zhang, Zou — CGBench: Benchmarking Language Model Scientific Reasoning for Clinical Genetics Research

CGBench 用 ClinGen 证据库中专家审核过的基因/变异整理记录，构造了三个“读论文并按指南判断证据”的任务：变异证据代码评分（E-Score）、证据代码是否满足的验证（E-Ver）、基因-疾病有效性的实验证据抽取（GCI）。8 个模型的零样本结果显示，细粒度三级代码的 Precision@5 最高只有 0.420（o4-mini），E-Ver 的 F1 最高为 0.634（GPT-4o），GCI 证据强度变化方向的匹配率最高为 0.445。已读正文与附录 B–D、F.3–F.4 的一部分；提示词全文（附录 K）与其他附录表只抽看。

[原文](https://arxiv.org/abs/2510.11985)

版本：arXiv:2510.11985v1（2025-10-13，NeurIPS 2025 Datasets & Benchmarks），37 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| problem | §1、§3.1–3.3，PDF pp.1–5 |
| method | §3.3、§4，附录 D.1–D.2，PDF pp.4–6、16–17 |
| evaluation | §5、Tables 1–4、Figure 3，PDF pp.7–9；附录 F.3–F.4 部分，PDF pp.20–22 |
| limitations | §6、附录 B、附录 C，PDF pp.9、15–16 |
