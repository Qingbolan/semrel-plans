# Hu, Jing et al. — OmniCompliance-100K: A Multi-Domain, Rule-Grounded, Real-World Safety Compliance Dataset

本文把 74 部法规与政策（9 个领域）人工整理成树结构，遍历得到 12,985 条规则，再用 Grok-4.1 搜索代理为每条规则检索并总结案例，得到 106,009 个"违反/遵守"案例。作者用"permitted/prohibited"二分类评测 17 个模型：GLM-4.5 平均 macro-F1 最高（92.28），Llama-Guard-3-8B 仅 28.16。规则–案例相关性由三个 LLM 全量打分、人工抽查 2,220 条，平均约 91–96%。已阅读正文 §1–5、Limitations、Ethics 及附录 A–C 的提示模板；未复现实验。

[原文](https://arxiv.org/abs/2603.13933)

版本：arXiv:2603.13933v2（2026-04-16），19 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | Abstract、§1–2、Table 1，PDF pp.1–3 |
| 方法 | §3、Figure 1、Table 2、附录 Tables 4–6（提示模板），PDF pp.3–4、17–18 |
| 评测 | §4、Figures 2–6、Table 3，PDF pp.4–8、17 |
| 局限 | Limitations、Ethics，PDF p.9 |
