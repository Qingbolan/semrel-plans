# Yu, Chen & Wang — Table-Critic: A Multi-Agent Framework for Collaborative Criticism and Refinement in Table Reasoning

本文提出 Table-Critic：在 Chain-of-Table 生成的表格推理链之上，用 Judge、Critic、Refiner、Curator 四个提示式 LLM 角色多轮查错与重写，并用一棵“自演化模板树”积累批评模板。在 WikiTQ 与 TabFact 上，三种 LLM 平均准确率为 73.7% 与 91.7%，高于所有基线，成本约为 Chain-of-Table 的 1.9–2.2 倍。已读正文、实验节、附录 B–D，附录 E 的提示词只作浏览。

[原文](https://aclanthology.org/2025.acl-long.853/)

版本：ACL 2025 Long，pp.17432–17451，PDF 20 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| problem | Abstract、§1，PDF pp.1–2 |
| method | §3.1–3.4，PDF pp.3–5；附录 B（Algorithm 1）、附录 D，PDF pp.12–14 |
| evaluation | §4.1–4.6、Tables 1–3、Figures 2–3，PDF pp.5–8；附录 C Table 4，PDF pp.12–13 |
| limitations | Limitations 节，PDF p.9；成本见 §4.5、附录 C |
