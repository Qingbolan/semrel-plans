# Xie et al. — The CLC-UKET Dataset: Benchmarking Case Outcome Prediction for the UK Employment Tribunal

本文基于剑桥法律语料库（CLC）中的英国就业法庭（UKET）判决，用 GPT-4-turbo 自动抽取事实、诉求、法条与判例引用、结果等注释，构建 CLC-UKET：注释集 19,090 案，结果预测集 14,582 案。预测任务只给事实和诉求，输出四类结果（申请人胜/败/部分胜/其他）；测试集 1,371 案的结果标签由法律专家人工标注，并收集两名法律专家的预测作为参照。微调 T5 的加权 F 值 0.564 为模型最佳，专家为 0.672。已阅读正文、局限与附录 A–D。

[原文](https://aclanthology.org/2024.nllp-1.7)

版本：NLLP Workshop 2024 论文集 pp.81–96（ACL Anthology 2024.nllp-1.7），16 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | §1–2、§5.1，PDF pp.1–2、4 |
| 方法 | §4、§5.2–5.3、§6.1–6.2，PDF pp.3–6 |
| 评测 | §6.3、Tables 2–5，PDF pp.6–8 |
| 局限 | §7、Limitations，附录 B–C，PDF pp.8–9、14–16 |
