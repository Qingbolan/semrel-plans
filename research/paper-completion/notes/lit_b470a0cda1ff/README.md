# Sun, Xu et al. — DBAIOps: A Reasoning LLM-Enhanced Database Operation and Maintenance System using Knowledge Graphs

DBAIOps 是一个数据库运维（O&M）诊断系统：把 DBA 经验编码成异构知识图（Neo4j），用 800+ 个多指标异常模型触发诊断，经"邻近图推断扩展 + 自适应异常指标裁剪"两阶段图演化收集证据路径，再由推理 LLM（DeepSeek-R1 等）生成根因与修复报告。在 Oracle、MySQL、PostgreSQL、DM8 共 558 个异常场景上，作者报告其综合诊断性能 0.92–0.94，高于仅用 LLM 与 D-Bot、ChatDBA 等方法。已阅读正文全部 8 节；论文无附录，HEval 打分细则在外部 GitHub 文件中，未查看；未复现实验。

[原文](https://arxiv.org/abs/2508.01136)

版本：arXiv:2508.01136v1（2025-08-02），13 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| problem | §1、§2、Figure 1、Table 1，PDF pp.1–3 |
| method | §3–6、Figures 2–4、Tables 2–3，PDF pp.3–9 |
| evaluation | §7、Tables 4–8、Figure 5，PDF pp.9–12 |
| limitations | 正文无局限章节；§7.1 基线排除说明，p.9；§8 结论，p.12 |
