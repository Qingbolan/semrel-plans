# Fan et al. — AutoPrep: Natural Language Question-Aware Data Preparation with a Multi-Agent Framework

AutoPrep 针对表格问答（TQA）提出“按问题做数据准备”：Planner 用 Chain-of-Clauses 先写出类 SQL 的 Analysis Sketch，再生成 Derive / Normalize / Filter 逻辑操作，由各 Programmer 从函数池选函数并填参数，Executor 执行并回传错误。论文报告 NL2SQL + AutoPrep 在四种骨干 LLM 上平均比 NL2SQL 提升 12.22（WikiTQ）和 13.23（TabFact）个点。已读正文全部章节；技术报告中的完整提示与表格规模分析未读。

[原文](https://arxiv.org/abs/2412.10422)

版本：arXiv:2412.10422v4（2025-07-09），PVLDB 18(10) 版式，14 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | §1、§2.1–2.3、Figure 1–3，PDF pp.1–4 |
| 方法 | §3–§5、Figure 4–6，PDF pp.4–8 |
| 评测 | §6、Tables 1–5、Figures 7–8，PDF pp.8–12；p.11 已渲染核对 |
| 局限 | §1 Remarks、§2.2 Remarks、§8 Future Work，PDF pp.3–4、12 |
