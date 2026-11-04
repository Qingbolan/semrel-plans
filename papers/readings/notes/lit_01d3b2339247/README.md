# Wang, Ren et al. — REAR: A Relevance-Aware Retrieval-Augmented Framework for Open-Domain Question Answering

REAR 是一个面向开放域问答的检索增强生成（RAG）框架：在 LLaMA2-7B 内加入显式的相关性评估模块（线性打分头），把每篇检索文档的相关性分数嵌入后引导生成，并用“知识一致性”打分在多个单文档答案中选出最终答案。仅用 NQ 训练，在 NQ、TriviaQA、WebQ、SQuAD 上的平均 EM/F1 为 47.10/57.68，高于同检索文档下的 Self-RAG 与 RobustLM（Table 3）。已阅读正文、局限及附录 A–E；未复现实验，未逐图核对 Fig. 3 数值。

[原文](https://aclanthology.org/2024.emnlp-main.321.pdf)

版本：EMNLP 2024 主会论文，pages 5613–5626，ACL Anthology PDF，14 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | §1、§3，PDF pp.1–3 |
| 方法 | §4.1–4.3、Tables 1–2，PDF pp.3–5 |
| 评测 | §5、Tables 3–6、Fig. 3，PDF pp.5–8；附录 B–C、Tables 7–9，PDF pp.13–14 |
| 局限 | Limitations，PDF p.9 |
