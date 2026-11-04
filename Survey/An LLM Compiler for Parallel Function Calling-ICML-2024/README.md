# An LLM Compiler for Parallel Function Calling

ReAct 式智能体每次只决定一个工具调用，互不依赖的查找也要串行等待，延迟和 token 成本随调用次数增长。LLMCompiler 借鉴编译器思路：Planner 一次生成带 `$1` 占位依赖的任务 DAG，Task Fetching Unit 在依赖就绪时分发，Executor 并行执行，必要时把中间结果回送 Planner 重规划。相对 ReAct，作者报告最高 3.7× 延迟加速、6.7× 成本下降、约 9% 准确率提升（Abstract、§5.1–5.2）。

[原文](https://www.stat.berkeley.edu/~mmahoney/pubs/icml2024_kim24y.pdf)

版本：ICML 2024（PMLR 235）正式版，作者镜像 PDF，22 页；2026-11 重新取得全文并按 §3–5、表 1–3、附录 A/B/D/E/I/K 核对本目录数字。未复现实验。
