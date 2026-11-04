# Dou et al. — DeonticBench: A Benchmark for Reasoning over Rules

DeonticBench 是一个关于义务、许可与禁止的规则推理（deontic reasoning）基准，共 6,232 个任务，覆盖美国联邦税（SARA Numeric / Binary）、航空行李政策（Airline）、美国州住房法（Housing）和新建的移民上诉数据集（USCIS-AAO），每个实例附参考 Prolog 程序。模型可直接回答，也可把法条与案情翻译成 Prolog 交给 SWI-Prolog 执行。在困难子集上，前沿模型在 SARA Numeric 上最高仅约 44%，SFT/DPO/GRPO 训练 Qwen2.5-32B 后 SARA Numeric 仍低于 10。已阅读正文 §1–6 及附录 B.1–B.3、B.5、C.1–C.2、D；Table 2 以 200 dpi 渲染核对。

[原文](https://arxiv.org/abs/2604.04443)

版本：arXiv:2604.04443v1（2026-04-06，预印本 under review），31 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | §1、Figure 1，PDF pp.1–2 |
| 方法 | §2.1–2.6、Table 1，PDF pp.2–5；附录 B.1–B.2、D，PDF pp.15–16、22 |
| 评测 | §3–4、Tables 2–4，PDF pp.5–9；附录 B.3、C.1–C.2、Table 7，PDF pp.16、21–22 |
| 局限 | 原文无局限性章节；§4.1–4.3 的失败分析与 §6、伦理声明，PDF pp.6–10 |
