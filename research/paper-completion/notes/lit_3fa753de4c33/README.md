# Zeng, Hong et al.（Alibaba）— QwenPaw-Data: Bridging Facts, Methodology, and Execution for Autonomous Enterprise Data Analytics

这是阿里巴巴的系统技术报告：把企业数据分析智能体拆成三个子系统——DataBridge（元数据图/知识图/轨迹图三图语义证据层）、Skill-Hub（按 Agent Skills 标准打包的分层分析方法技能）和 Host（DAG 化、沙箱化、带产物登记与恢复的运行时），并让语义、方法和轨迹回流形成“自演化资产飞轮”。

内部 BI 部署中 29 条客观查询正确率约 96.5%，37 条开放分析的用户满意度 78.3 vs 通用智能体 34.1；公开基准 KramaBench 68.32、DAComp 62.38。报告以架构描述为主，评测细节（底层 LLM、对比智能体、评判设置）披露有限。已通读全文（24 页，含 §6 评测与 §7 未来工作）。

[原文](https://arxiv.org/abs/2607.11019)

版本：arXiv:2607.11019v2（Technical Report，2026-07-14），24 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| problem | §1.1–1.3、Table 1，PDF pp.2–5 |
| method | §2–5、Figs.1–7，PDF pp.7–19 |
| evaluation | §6、Tables 3–4，PDF pp.19–21 |
| limitations | 无独立局限章节；§7 未来工作，PDF pp.21–22；阅读者据 §6 评测披露整理 |
