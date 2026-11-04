# Shen, Wadlom, Lu（NUS）— Batch Query Processing and Optimization for Agentic Workflows

当同一个 agentic workflow 要对成百上千条查询重复执行时，现有 LLM 服务引擎只优化单次调用，多 agent 框架只管编排，结果是重复的 SQL/HTTP 调用、重复的提示前缀和 CPU–GPU 交替时的空等。本文提出 Halo：把每个 workflow 表示为由 GPU 上的 LLM 节点和 CPU 上的工具节点组成的固定 DAG，用按 epoch 离散化的动态规划决定 LLM 节点的批次与 GPU 放置，运行时再合并完全相同的工具调用、复用 KV cache、让 CPU 工具与 GPU 推理流水重叠。

在 6 个作者构造的 workflow（IMDb、FineWiki、TPC-H SF10 三个 PostgreSQL 库）上，batch 模式相对 LangGraph/AgentScope/Parrot 最高 3.6 倍加速，在线模式吞吐最高约 2.6 倍；DP 调度的端到端延迟与 MILP 最优解相差不到 0.5%（据 Table 4 计算），求解时间从 1.44 小时降到 2.24 秒（W1，N=256）。

[原文](https://arxiv.org/abs/2509.02121v2)

版本：arXiv 2509.02121v2（2026-01-19，cs.DB；首页 ACM 会议信息为模板占位），14 页。2026-10-14 通读正文 §1–8、算法 1、表 1–5、图 6–11；2026-11 按全文重新核对数字。未复现实验。v1 摘要报告的是 18.6 倍 batch 加速与 4.7 倍在线吞吐，与 v2 不可混用。
