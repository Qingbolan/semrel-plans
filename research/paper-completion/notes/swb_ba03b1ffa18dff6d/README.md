# Wang et al. — Chain-of-Table: Evolving Tables in the Reasoning Chain for Table Understanding

Chain-of-Table 是 UCSD 与 Google 提出的表格推理提示框架：LLM 每步从 5 个原子表操作中选一个并生成参数，程序执行后把中间表回传给 LLM，直到输出结束标记，再基于最终表作答。论文在 WikiTQ、TabFact（PaLM 2 与 GPT 3.5）和 FeTaQA（PaLM 2）上报告优于通用推理和程序辅助基线，如 PaLM 2 下 TabFact 86.61%、WikiTQ 67.31%。已阅读正文 §1–6 与附录 A–D；提示词附录 E–F 仅浏览。

[原文](https://proceedings.iclr.cc/paper_files/paper/2024/hash/f53fd88a4340063ecd258c0ae9948b40-Abstract-Conference.html)

版本：ICLR 2024 会议论文（proceedings 版 PDF），24 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | §1、§3 Problem Formulation，PDF pp.1–4 |
| 方法 | §3.1–3.4、Algorithm 1、Fig.2，PDF pp.4–5；附录 A.1，p.13 |
| 评测 | §4、Tables 1–4，PDF pp.5–9；附录 A.2、B、C、D，pp.13–16 |
| 局限 | 无独立局限章节；附录 A.1 末句、B（ROUGE 不敏感），pp.13–14 |
