# Carnot: Interpretable, Interactive, and Optimized Execution of Deep Research Queries

Deep Research 类系统是黑盒，用户看不到中间检索和推理步骤，也无法控制费用；语义算子系统虽有查询计划，但提交后用户难以中途发现错误、局部修正并复用已有结果。Carnot（Russo 等，MIT）把自然语言查询编译成由语义算子和 agentic 算子组成的物理 DAG，并以 notebook 呈现：每个单元格对应一个算子，可查看意图、代码/提示和原始输入输出，可逐步执行、就地修改，修改后只重新优化和执行受影响部分；优化器按用户给的成本或延迟约束选择实现。

这是一篇 4 页系统演示论文，没有量化评测或基线对比，只描述三个演示场景（§3）。

[原文](https://www.vldb.org/pvldb/vol19/p4642-russo.pdf)

版本：PVLDB 19(12):4642–4645（2026），DOI 10.14778/3827998.3828086；对应 arXiv 2608.09532v1。作者：Matthew Russo、Yash Agarwal、Tianyu Li、Zhuohan Gu、Michael Cafarella、Omar Khattab、Tim Kraska、Samuel Madden。已通读全文 §1–4 与 Figures 1–2，内容已对照全文复核（2026-11）；未运行代码。
