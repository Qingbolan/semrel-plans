# Zhao et al. — LongRAG: A Dual-Perspective Retrieval-Augmented Generation Paradigm for Long-Context Question Answering

本文提出面向长上下文问答（LCQA）的 RAG 流程 LongRAG：混合检索器取回 chunk 后，一路把 chunk 映射回源段落并由 LLM 抽取“全局信息”，另一路用 CoT 引导的过滤器逐个判断 chunk 是否支持回答，最后由生成器综合两路信息。在 LongBench 的 HotpotQA、2WikiMQA、MuSiQue 三个多跳子集（各 200 题）上，以 F1 计，相对 Vanilla RAG 最高提升 17.25 个点。已阅读正文 §1–7 及附录 A–C（检索设置、基线复现、语料构造、微调数据统计）；未逐条审读附录 D–E 的全部提示词与示例。

[原文](https://aclanthology.org/2024.emnlp-main.1259.pdf)

版本：EMNLP 2024 main，pp.22600–22632，33 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | Abstract、§1、§3.1，PDF pp.1–3 |
| 方法 | §3.2、§4.1–4.5，Figure 2，PDF pp.3–6；附录 C，pp.15–16、22 |
| 评测 | §5.1–5.4，Tables 1–3、Figures 3–4，PDF pp.6–9；附录 A–B，pp.14–15 |
| 局限 | §7，PDF p.9 |
