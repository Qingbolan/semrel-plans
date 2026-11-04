# Optimizing LLM Queries in Relational Data Analytics Workloads

在 SQL 或 DataFrame 中对表逐行调用 LLM 时，许多行共享相同的字段值（如同一商品的描述），但默认的行序和字段序让这些重复内容很少落在可复用的提示前缀里，前缀 KV 缓存命中率低。本文在发出请求前重排行顺序和每行内部的字段顺序，以最大化前缀命中：OPHR 是精确的递归算法（指数复杂度），GGR 是利用函数依赖和表统计量的贪心近似；实现在 PySpark 上，后端为 vLLM。

在作者构建的 16 个查询、7 个数据集上（Llama-3-8B，单张 L4），端到端时间相对“开缓存但不重排”快 1.5–3.4 倍，相对不开缓存快 1.8–3.8 倍；在 FEVER 上调用商用 API，GPT-4o-mini 省 32% 费用，Claude 3.5 Sonnet 省 21%。

[原文](https://proceedings.mlsys.org/paper_files/paper/2025/file/b5dc49f44db2fadc5c4d717c57f4a424-Paper-Conference.pdf)

版本：Liu, Biswal, Kamsetty, Cheng, Schroeder, Patel, Cao, Mo, Stoica, Gonzalez, Zaharia（UC Berkeley 等），MLSys 2025 正式版，15 页（含附录 A–D）。另比对了 arXiv 2403.05821v2：除摘要中的成本示例外文字一致（正式版写“约一个月、约 $18K”，arXiv 版写“约一天、约 $10K”）。已通读正文 §1–8 与附录，数字已对照全文核查；未复现实验。

| 阅读内容 | 位置 |
|---|---|
| problem | §1–3，PDF pp.1–4 |
| method | §4.1–4.2.3、Algorithm 1，pp.4–6；§5 实现，p.6 |
| evaluation | §6.1–6.5、Tables 1–5、Figures 3–6，pp.6–10；附录 D、Tables 6–7，p.15 |
| limitations | 无独立局限章节；假设见 §3.1（p.3），质量影响见 §6.4（pp.9–10） |
