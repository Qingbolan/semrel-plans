# Anderson et al. — The Design of an LLM-powered Unstructured Analytics System

这是 Aryn 公司的系统设计论文（CIDR 2025）：用户以自然语言提问，Luna 用 LLM 生成由结构化与语义算子组成的查询计划，交由 Sycamore 在分层文档集合 DocSet 上执行，DocParse 负责把 PDF 等解析成 DocSet。在 100 份 NTSB 事故报告、30 个问题的初步评测中，Luna 答对 20 题，RAG 只答对 2 题。已读全文；评测规模小，属于设计与愿景性质。

[原文](https://arxiv.org/abs/2409.00847)

版本：arXiv:2409.00847v3（2024-12-28），CIDR 2025，10 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| problem | Abstract、§1–2，pp.1–3 |
| method | §3–6（DocParse、Sycamore、Luna），pp.3–7 |
| evaluation | §4.1 Table 1，p.4；§7、Tables 3–4，pp.7–9 |
| limitations | §7.2 错误分析，p.8；§8–9，pp.9–10 |
