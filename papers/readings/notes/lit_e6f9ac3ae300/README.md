# Lee et al. — A Human-Inspired Reading Agent with Gist Memory of Very Long Contexts

ReadAgent 是一个纯提示（无训练）的长文档阅读智能体：LLM 先把长文本分成“页”（情节片段），把每页压缩成带页号的要点（gist），再在回答问题时根据全部要点决定回看哪些原文页。以 8K 上下文的 PaLM 2-L 为主模型，在 QuALITY、NarrativeQA、QMSum 上均优于 BM25 与神经检索基线，有效上下文长度扩大 3.5–20 倍。已阅读正文 §1–§5 与附录 B–E、G 的相关部分。

[原文](https://arxiv.org/abs/2402.09727)

版本：arXiv:2402.09727v3（2024-07-22，ICML 2024 / PMLR 235），20 页（正文 9 页）。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| problem | §1–§2，PDF pp.1–3 |
| method | §3（3.1–3.4），PDF pp.3–5 |
| evaluation | §4、Tables 1–6，PDF pp.5–9；附录 B–E（Tables 7–10），PDF pp.13–17 |
| limitations | §2 检索比较段、§5 结论、Impact Statement，PDF pp.2、9 |
