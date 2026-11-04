# Khoja et al. — Weaver: Interweaving SQL and LLM for Table Reasoning

Weaver 用于表格问答（Table QA）。LLM 先生成一份逐步计划，每一步标为 SQL 步或 LLM 步：SQL 步负责过滤、聚合和格式化，LLM 步通过语义推断向中间表追加新列；计划经过验证后依次执行，最后由 LLM 从中间表提取答案。作者从 WikiTQ、TabFact、FinQA 筛出“混合”子集（510/303/1,006 题），用 4 个 LLM 评测；GPT-4o 版本得分为 70.7/83.4/60.8，但并非所有设置下都优于基线。已读正文和附录 A.7、B–G。

[原文](https://arxiv.org/abs/2505.18961)

版本：arXiv:2505.18961v2（2025-09-23），27 页（正文 9 页 + 附录）。批次元数据标注为 EMNLP 2025，PDF 本身未印会议版式。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| problem | §1–§2.1，PDF pp.1–3 |
| method | §2.1–2.2、Appendix C、E.2–E.3，PDF pp.2–4、22–26 |
| evaluation | §3、Tables 1–6、Appendix A.7、B、D、E.1，PDF pp.4–8、21–25 |
| limitations | Limitations、Appendix G，PDF pp.9、26 |
