# CADENZA: Compiling Natural-Language Intent into Task-Specific Operator DAGs for Semantic Query Processing

语义查询引擎（LOTUS、Palimpzest 等）把一个语义算子实例当作黑盒 LLM 调用，中间结果无法被过滤、重排、按行路由或联合调参。CADENZA（Ha、Park、Han，POSTECH/UIUC）把每个语义算子实例编译成带类型的任务 DAG（如 OCR → TxtQA → 关系过滤），逻辑层由 LLM 生成并修复种子计划、再做依赖检查的结构重写与语义替代，物理层为每个任务算子合成按行分流的 router，并用贝叶斯优化联合调整切点、后端参数和关系阈值。

在 SemBench 55 条查询上，相对 LOTUS 平均质量 +0.10、延迟 3.80×、费用 4.88×，相对 Palimpzest +0.11/4.42×/21.83×（Table 3）；摘要中的 +0.49/165.7×/310.3× 是单个场景的最大值。已通读正文 §1–9 与附录 A–J，数字已对照本地 PDF。

[原文](https://arxiv.org/abs/2606.29151v3)

版本：arXiv 2606.29151v3（2026-07-13，cs.DB），27 页；[本地 PDF](2606.29151v3.pdf)。首页为 SIGMOD ’27 模板，年份与 DOI 仍是 2018/占位，不能据此认定已录用。只优化单个语义算子实例，跨算子联合优化不在本文范围（§1）。

| 阅读内容 | 位置 |
|---|---|
| problem | §1–2、Figures 1–2，PDF pp.1–4 |
| method | §3 TxRA，pp.4–5；§4 逻辑规划，pp.5–7；§5 物理规划，pp.7–8；§6 实现，pp.8–9 |
| evaluation | §7、Tables 2–6、Figures 4–5，pp.9–13；附录 A–I、Tables 7–20，pp.16–23 |
| queries | 附录 J，pp.24–27 |
| limitations | 无独立章节；见 §1（单算子范围）、§6.2（漂移需重优化）、§7.3.2（BO 预算留待未来工作）、附录 G（只测一个查询的标签噪声） |
