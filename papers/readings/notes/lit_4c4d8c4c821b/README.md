# Zhou et al. — D-Bot: Database Diagnosis System using Large Language Models

D-Bot 是一个基于 LLM 的数据库异常诊断系统。它离线从诊断文档中抽取知识块并注册工具 API；在线时按异常指标匹配知识与工具，用树搜索加反思引导 LLM 多步分析，复杂异常则由多个"专家" LLM 异步协作并交叉评审，最终生成根因和解决方案报告。在 PostgreSQL 上构造的 539 个异常（6 类应用）中，D-Bot(GPT-4) 的准确率明显高于 DNN、决策树和直接使用 GPT-4，并接近一名有 2 年经验的 DBA：单根因异常 Acc 0.754（GPT-4 直接诊断 0.351，DBA 0.955），多根因异常 0.655（DBA 0.487）（Table 2）。

已阅读正文 §1–§10。

[原文](https://arxiv.org/abs/2312.01454)

版本：arXiv:2312.01454v2（2023-12-06），15 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | §1–§2（Figures 1–2），pp.1–4 |
| 方法 | §3–§7（Figures 3–7，Algorithm 1），pp.4–9 |
| 评测 | §8（Table 1–2，Figures 8–11），pp.9–12；Figures 8–9 与 Table 2 已渲染核对 |
| 局限 | 无专门章节；限制见 §2.2 脚注 3、§8.3–8.5，pp.3、10–12 |
