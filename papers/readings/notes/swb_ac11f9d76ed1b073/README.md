# Wang et al. — Match, Compare, or Select? An Investigation of Large Language Models for Entity Matching

本文比较三种基于 LLM 的实体匹配策略：逐对判断是否匹配（matching）、两两比较哪个候选更像锚记录（comparing）、从候选列表中直接选出匹配项（selecting），并提出组合框架 ComEM：先用中等规模模型按 matching 排序筛出 top-4，再用更强的模型做 selecting。在 8 个 clean-clean 实体解析数据集上，selecting 平均比 matching 高 16.02 个 F1 点；ComEM 用 GPT-4o Mini 平均 F1 为 86.42，成本 0.09 美元。已阅读正文 §1–5、Limitations 及附录 A–C 全部内容。

[原文](https://aclanthology.org/2025.coling-main.8)

版本：COLING 2025（Proceedings of the 31st International Conference on Computational Linguistics，pp.96–109），14 页；目录记录为 arXiv 2024，实际下载的是 ACL Anthology 正式版。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | §1、§3.1，Table 1，PDF pp.1–3；附录 A，p.13 |
| 方法 | §3.2–3.5，Table 2、Figure 2，PDF pp.3–6；附录 B，p.13 |
| 评测 | §4，Tables 3–4、Figures 3–6，PDF pp.6–9；附录 C、Table 6，pp.13–14 |
| 局限 | Limitations，PDF p.9 |
