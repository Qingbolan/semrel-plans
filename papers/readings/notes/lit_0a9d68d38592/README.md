# Lu, Song, Zhang, Wong — MultiVis-Agent: A Multi-Agent Framework with Logic Rules for Reliable and Comprehensive Cross-Modal Data Visualization

本文把 Text-to-Vis 扩展为四种场景（基础生成、参考图生成、参考代码生成、迭代修改），构建 1,202 例的 MultiVis-Bench（基于 141 个 Spider SQLite 库，输出可执行 Altair 代码），并提出由协调者调度数据库、可视化实现、验证评估三个智能体的框架，外加四层"逻辑规则"（任务分类、参数边界、错误恢复、迭代上限 T_max=10）。

Gemini-2.0-Flash 骨干下参考图场景得分 75.63%（基线 57.54–62.79%）；但迭代修改场景中 LLM Workflow 基线（74.69%）和"只生成"消融（76.44%）都高于完整系统（71.52%）。已阅读全文正文（无独立局限性章节）。

[原文](https://arxiv.org/abs/2601.18320)

版本：arXiv:2601.18320v1（2026-01-26），25 页；页眉标注为 Proc. ACM Manag. Data 4(1)（SIGMOD）Article 56，2026 年 2 月，DOI 10.1145/3786670。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| problem | §1、§2，PDF pp.1–4 |
| method | §3（基准构建）、§4（框架与逻辑规则、定理、算法 1–2），PDF pp.5–14 |
| evaluation | §5（评测指标）、§6、Tables 2–4、Figure 4，PDF pp.14–21 |
| limitations | 原文无局限性章节；§6.2、§6.3.1 承认迭代修改场景落后，PDF pp.18–19；其余由阅读者归纳 |
