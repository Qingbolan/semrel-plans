# Li et al. — GraphReader: Building Graph-based Agent to Enhance Long-Context Abilities of Large Language Models

GraphReader 把长文切块，用 LLM 抽取“原子事实”和关键元素并建成图，再让一个只用 4k 输入窗口的智能体按计划在图上由粗到细地读取原子事实、原文块和相邻节点，记笔记后作答。在 LV-Eval 的 HotpotWikiQA-mixup（16k–256k）上，它在所有长度都超过整篇读入的 GPT-4-128k（128k 档 LR-1 为 28 对 16，相对提升 75%），在 LongBench 的四个问答集上也优于 RAG 和 ReadAgent 等基线。已阅读正文 §1–6 和附录 B–H；附录 A、I 的提示与案例仅浏览。

[原文](https://arxiv.org/abs/2406.14550)

版本：arXiv:2406.14550v2（2024-11-05），29 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | §1–2，PDF pp.1–2 |
| 方法 | §3（Figure 2），PDF pp.2–4 |
| 评测 | §4（Tables 1–6、Figures 3–5），附录 B–H（Tables 7–9），PDF pp.4–8、12–15 |
| 局限 | §6 Limitations，PDF p.9 |
