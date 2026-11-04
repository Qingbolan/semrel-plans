# Asai et al. — Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection

Self-RAG 训练一个 LM（Llama2 7B/13B），让它在生成时输出“反思 token”，用于决定是否检索、判断段落相关性、生成内容是否被证据支持以及整体有用性；推理时据此做段落级束搜索和可调约束。论文在 6 个任务上优于同规模开源模型和检索增强基线，部分任务优于 ChatGPT：例如 Self-RAG 13B 在 PubHealth 上准确率 74.5（检索版 ChatGPT 54.7），ASQA 引用精确率 70.3（检索版 ChatGPT 65.1）。已读正文全部章节、附录 A（反思 token、critic 数据与准确率）及训练数据表。

[原文](https://arxiv.org/abs/2310.11511)

版本：arXiv:2310.11511v1（2023-10-17 预印本），30 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | §1、§3.1，PDF pp.1–4 |
| 方法 | §3.1–3.3、Table 1、Algorithm 1–2，PDF pp.3–6、18 |
| 评测 | §4–5、Table 2、Figure 3–4，PDF pp.6–10；附录 A.2、Table 3、Figure 5，PDF pp.17–18 |
| 局限 | 无独立局限章节；Ethical Concerns，PDF p.11；§5.2 分析，PDF pp.9–10 |
