# Weng et al. — DataLab: A Unified Platform for LLM-Powered Business Intelligence

DataLab 是浙江大学与腾讯合作的商业智能（BI）平台，把多智能体 LLM 框架嵌入扩展版 JupyterLab 笔记本，在同一环境中支持 SQL、Python/PySpark、Markdown 与图表单元。三项核心模块为：从企业脚本与血缘中自动生成领域知识、基于有限状态机（FSM）的结构化智能体通信、基于单元依赖 DAG 的上下文裁剪。在 8 个公开基准上，DataLab 与单任务 SOTA 方法互有胜负；在腾讯内部数据上，知识注入使 NL2DSL 准确率提高 58.58 个百分点，DAG 上下文管理使每次查询 token 降低 61.65%。

已阅读正文 §I–X 全部内容，并渲染核对 p.10 的 Table I 与 Figure 6。

[原文](https://arxiv.org/abs/2412.02205)

版本：arXiv:2412.02205v3（2025-04-07，cs.DB），14 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | §I 挑战 C1–C3、§II，PDF pp.1–3 |
| 方法 | §III–VI、Algorithms 1–3、Figures 1–5，PDF pp.3–9 |
| 评测 | §VII、Tables I–IV、Figures 6–7，PDF pp.9–12；Table I 已渲染核对 |
| 局限 | §VII-C/E 中的失败分析、§VIII 部署，PDF pp.11–12；无独立局限章节 |
