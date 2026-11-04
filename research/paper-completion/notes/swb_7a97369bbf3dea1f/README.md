# Wang et al. — Demonstrating TOFFEE: A Learned System for Synthesizing Data Agent Trajectories at Scale

TOFFEE 是一篇 VLDB 演示论文：给定数据环境（数据库、CSV/JSON/Markdown 等文件），自动构造可验证的分析任务池，用带“学习型代价模型”（LCM）的 MCTS 搜索合成数据智能体轨迹，再导出用于 SFT 或 ICL 示例。初步结果显示同预算下轨迹质量高于 Single-Pass 与 Best-of-N，用轨迹微调的 TOFFEE-27B 在 KramaBench 上分数达到零样本基座的两倍以上。全文仅 4 页且实验只有一张图（Figure 3），已全部阅读并以 300 dpi 渲染核对该图。

[原文](https://www.vldb.org/pvldb/vol19/p4738-cong.pdf)

版本：PVLDB 19(12): 4738–4741, 2026（doi:10.14778/3827998.3828110，演示论文），4 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | §1（含 Challenges C1–C3）、Figure 1，PDF pp.1–2 |
| 方法 | §2（任务池构建、Trajectory Explorer、LCM、导出）、Figure 2，PDF pp.2–3 |
| 评测 | §3、Figure 3（已渲染），PDF p.3 |
| 局限 | 原文无局限性章节；§3 自称“初步结果”，§4 为演示场景，PDF pp.3–4 |
