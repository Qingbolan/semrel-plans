# Zhang et al. — DataClawBench: An Agent Benchmark for Exploratory Real-World Financial Data Analysis

DataClawBench 评测智能体在“不给数据源提示、不给完整 schema、不预清洗噪声”的条件下做探索式数据分析。数据环境来自金融智库咨询实践，约 206 万条记录、3 个领域、18 个源文件；上面定义 492 个多步跨域任务，每题有唯一答案和中间里程碑。用 OpenClaw 框架评测 8 个模型，最好的 Claude Opus 4.6 总准确率 63.4%，其余均低于 50%；里程碑指标用于区分失败方式。已阅读正文、局限与附录 A、D、E；未逐个阅读附录中的个案。

[原文](https://arxiv.org/abs/2605.02503)

版本：arXiv:2605.02503v3（2026-05-27），25 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| problem | Abstract、§1、§2.1、Table 1，PDF pp.1–2 |
| method | §2.2、§3、Tables 2–3、Figure 1，PDF pp.2–5；附录 D，pp.17–20 |
| evaluation | §4 Q1–Q7、Tables 4–6、Figures 2–3，PDF pp.5–8；附录 A、E，pp.12、20 |
| limitations | Limitations and Future work，PDF p.9 |
