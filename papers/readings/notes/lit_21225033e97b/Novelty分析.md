# 贡献与评价

原文主张三项贡献。其一，半自动的真值生成与指标验证流程。

其二，TFC 评价框架：由 GPT-4o-mini 为每个提示选择任务类型、生成评价函数和代码；再把函数聚合为每类 top-K（K=5），共 25 个（§3.3、Figure 3）。

其三，对 23 个模型做粗、细粒度评测，并与 HumanEval、LiveCodeBench（LCB）、BigCodeBench（BCB）比较。与 LCB 的 Pearson/Spearman 为 0.853/0.673，与 BCB 为 0.823/0.808（Figure 6、附录 A.2 Table 3）。

评价：新意主要在评测工程，即把多子任务提示拆成可执行检查，不是新的建模方法（阅读者分析）。

真值由强 LLM 生成再经人工审核，原文未报告复核一致率；评价函数也由 LLM 生成，存在“LLM 出题又评分”的循环风险（阅读者分析）。

依据：§1 Contributions、§3.3、Figure 3、附录 A.2 Table 3，PDF pp.2–5、11。
