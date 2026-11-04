# 贡献与评价

原文声称的贡献：
1. 一组 LLM 标量/聚合函数，以及 rerank（first/last）和 fusion（rrf、combanz、combmed、combmnz、combsum）等内置函数，作者称 Query 3 是其所知首个在 SQL 内实现的完整混合检索（§1、§2.2，PDF pp.1–3）。
2. 资源独立性：新增 DDL 资源 MODEL 与 PROMPT，可 Local/Global 作用域，修改时自动生成新版本，旧版本可查看使用（§2.1，PDF p.2）。
3. 自动优化：元提示（meta-prompt，KV-cache 友好的模板，Fig.1）、元组批处理、预测缓存、去重后预测；篇幅原因只详述前两项（§2.3，PDF pp.3–4）。

MODEL/PROMPT 作为版本化模式对象是较明确的工程设计点。摘要称“cost-based optimizations”，但正文只描述了按上下文窗口贪心填充批次、失败时每次缩小 10% 的启发式，没有成本模型或计划选择算法；缓存与去重仅被列出未展开。与 Palimpzest、TAG 的比较只在 §3 一句提及，没有实验对比。作为演示论文，其新意主要在系统集成与接口，而非优化算法。（阅读者分析）
