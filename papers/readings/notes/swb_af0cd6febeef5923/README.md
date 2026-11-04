# Wang et al. — LLM-based HSE Compliance Assessment: Benchmark, Performance, and Advancements

本文构建 HSE-Bench：从法规、法院案例、安全考试题和现场视频四类来源出发，用 GPT-4o 按 IRAC（问题识别、规则回忆、规则适用、结论）生成 1,020 道四选一题目，再经对抗式改写和两位专家复核。12 个 LLM 在给选项时准确率约 90%，不给选项时用嵌入相似度计算的 AUC-ROC 约 70%；作者据此认为模型依赖语义匹配，并提出“多专家推理”（RoE）提示词。已阅读正文、附录 A–C；附录 D 的案例表只做了浏览。

[原文](https://arxiv.org/abs/2505.22959)

版本：arXiv 2505.22959v1（2025-05-29），24 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | Abstract、§1–2，PDF pp.1–3 |
| 方法 | §3、Table 1，PDF pp.3–6；附录 C，PDF pp.15–18 |
| 评测 | §4、Figures 2–4，PDF pp.6–9；附录 A–B，PDF pp.14–15 |
| 局限 | §5，PDF p.9 |
