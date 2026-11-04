# Li, Chen, Xue, Mei, Luo — DeepEye-SQL: A Software-Engineering-Inspired Text-to-SQL Framework

DeepEye-SQL 把 Text-to-SQL 视为“写一个小程序”，按软件开发生命周期组织为四阶段：语义取值检索与鲁棒模式链接、三种生成器的 N-version 生成、确定性检查器工具链修正、基于执行一致性的置信门控选择。论文报告用约 30B 开源模型、无微调即在 BIRD-Dev 达到 73.5% EX、BIRD-Test 75.07%、Spider-Test 89.8%，Spider 2.0-Snow/Lite 为 50.5%/38.2%（DeepSeek-R1）。已阅读正文 §1–§6 与主要表格；参考文献外无附录。

[原文](https://arxiv.org/abs/2510.17586)

版本：arXiv:2510.17586v3（2026-04-03），PACMMOD/SIGMOD 2026 Vol.4 No.3 Article 158，28 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| problem | §1，pp.1–4，Table 1 |
| method | §2–§3（Alg.1–5、Table 2），pp.4–14 |
| evaluation | §4，Tables 3–11、Figs.5–9，pp.14–23 |
| limitations | §4 RQ10 错误分析，pp.22–23（无单列 limitations 章节） |
