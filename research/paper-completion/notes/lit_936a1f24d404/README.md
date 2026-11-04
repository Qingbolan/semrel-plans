# Korini & Bizer — Evaluating Knowledge Generation and Self-refinement Strategies for LLM-Based Column Type Annotation

本文实验比较 LLM 列类型标注（CTA）的几种策略：零样本/五样本/自一致性基线、让 LLM 生成标签定义（知识生成提示）、基于验证集错误自我精炼定义、两步自我纠错，以及微调与定义结合。

在 SOTAB V2、WikiTURL（均降采样）和 Limaye 三个数据集、四个模型上，结论是没有统一最优策略；精炼定义在 12 个设置中的 10 个平均比未精炼定义高 3.9% F1；微调 gpt-4o 再配精炼定义得到 SOTAB V2 最高 91.8 F1。已阅读全文（§1–9）；未查看 GitHub 中的完整提示与逐标签误差。

[原文](https://link.springer.com/chapter/10.1007/978-3-032-05281-0_8)

版本：arXiv:2503.02718v1（2025-03-04，ACM 排版预印本），14 页；Springer ADBIS 2025 正式版未获取（OpenAlex 将该 arXiv 版本列为同一作品的开放获取副本），正式版文字与页码可能不同。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| problem | §1，pp.1–2；Fig. 1 |
| method | §3 实验设置、§5.1 定义生成与精炼、§6 自我纠错、§7 微调，pp.3–4、6、8–11 |
| evaluation | §4–7，Tables 2–13，pp.4–12 |
| limitations | §4–7 中的成本与失败分析、§8 结论，pp.5、8–12；论文无单独局限章节 |
