# Saad-Falcon et al. — PDFTriage: Question Answering over Long, Structured Documents

本文提出 PDFTriage：先把 PDF 解析成包含章节、页码、表格、图注的结构化元数据，再让 LLM 通过函数调用按页、按章节、按表格/图或按语义检索取回上下文后回答问题。作者用众包构造了 82 篇文档、908 个问题、10 类问题的评测集，以人工排序和打分比较 PDFTriage 与按页检索、按块检索两种基线；PDFTriage 在 50.8% 的题目中被排第一。已阅读正文 §1–7 及附录 A–B（问题类别示例、标注者信息、GPT 自动评测、上下文长度相关性、函数表）；附录中按类别的分数图只读了说明文字。

[原文](https://aclanthology.org/2024.emnlp-industry.13.pdf)

版本：EMNLP 2024 Industry Track，pp.153–169，17 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | Abstract、§1，PDF pp.1–2 |
| 方法 | §3.1–3.3，Figure 1，PDF pp.3–4；附录 B.5、Tables 6–7，p.17 |
| 评测 | §4–6，Tables 1–2，PDF pp.4–6；附录 A–B，Figure 3，pp.9–17 |
| 局限 | 无单独局限章节；§1 预告的 §7 实为“Future Work & Conclusions”，p.6；附录 B.2–B.3，p.14 |
