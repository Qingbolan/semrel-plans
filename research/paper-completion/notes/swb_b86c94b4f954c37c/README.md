# Ju & Lee — Citation-Closure Retrieval and Per-Rule Attribution for Real-World Regulatory Compliance Question Answering

本文提出“法规合规问答”任务与 RegOps-Bench：基于 12 部韩国国家研发法规构建运营知识图谱（OKG），并由 56 条真实 IITP 问答扩展出 231 个带确定性引用闭包的问题。配套方法 RefWalk 用主题锚点生成三视角查询，沿引用边扩展一跳，用 Reciprocal Rank MAX 融合，并用“按条款归属”的 JSON 模式生成答案。在 RegOps 上检索 R@10 为 63.8（最强基线 57.9），35B 模型引用 F1 为 54.9（NativeRAG 46.7）；HIPAA 对照集上各方法检索基本饱和。已阅读正文、局限与附录 A.1–A.9。

[原文](https://arxiv.org/abs/2605.29742)

版本：arXiv:2605.29742v2（2026-08-31），26 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | §1、§3 开头，PDF pp.1–3 |
| 方法 | §3.1–3.2、§4，Tables 1–2、Figure 1，PDF pp.3–6；附录 A.1–A.2，PDF p.12 |
| 评测 | §5、Tables 3–9，PDF pp.6–8；附录 A.3–A.8、Tables 12–20，PDF pp.13–16 |
| 局限 | §7 Limitations，PDF p.9；附录 A.3 人工验证，PDF pp.13–14 |
