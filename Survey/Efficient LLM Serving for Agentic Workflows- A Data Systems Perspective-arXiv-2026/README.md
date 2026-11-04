# Efficient LLM Serving for Agentic Workflows: A Data Systems Perspective

现有 LLM 推理引擎（如 vLLM）按单次调用优化，看不到批量 agent 工作流里跨调用的依赖与重复提示；编排框架又把 LLM 当黑盒 UDF，不了解 KV 缓存。本文提出 Helium（NUS，Wadlom、Shen、Lu），把一批 agentic 工作流当作以 LLM 为一等算子的查询计划：逻辑层做算子剪枝、公共子图消除和结果缓存替换，物理层用“模板化基数树”（TRT）建模提示前缀与依赖，做代价驱动、缓存感知的调度，并预先固定静态前缀的 KV 缓存。

在 5 个原语工作流上，Helium 相对 KVFlow 最高快 1.56×（平均 1.32×）；在 19 个 agent、88 个 LLM 算子的 Trading 工作流上相对 KVFlow 最高快 1.34×，相对逐查询顺序执行的 vLLM 最高快 39.50×。所有优化保持输出不变（只缓存确定性算子、全部 greedy 采样）。

[原文](https://arxiv.org/abs/2603.16104v1)

版本：arXiv 2603.16104v1（2026-03-17，cs.MA），PDF 标题带 “(Extended)”，正文 13 页 + 参考文献与附录 A–D，共 18 页；代码 github.com/mlsys-io/helium_demo。阅读范围：正文 §1–10、算法 1、表 1–5、附录 A–D；2026-11 对照全文复核数字。未复现实验。
