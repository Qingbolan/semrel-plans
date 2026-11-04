# 工作负载

**数据集**（Table 1，§6.1.1 pp.6–7）：

| 数据集 | 行数 | 字段数 | 平均输入 token | 平均输出 token | 查询类型 |
|---|---|---|---|---|---|
| Movies（Rotten Tomatoes） | 15,000 | 8 | 276 | {2, 29, 16, 2} | T1–T4 |
| Products（Amazon 评论） | 14,890 | 8 | 377 | {3, 107, 62, 2} | T1–T4 |
| BIRD（Posts ⋈ Comments） | 14,920 | 4 | 765 | {2, 43} | T1、T2 |
| PDMX（MusicXML 元数据） | 10,000 | 57 | 738 | {2, 72} | T1、T2 |
| Beer（RateBeer） | 28,479 | 8 | 156 | {2, 38} | T1、T2 |
| SQuAD | 22,665 | 5 | 1,047 | 11 | T5 |
| FEVER | 19,929 | 5 | 1,302 | 3 | T5 |

**查询**（§6.1.2 p.7）：共 16 个，分 5 类。T1 filter 5 个、T2 projection 5 个（都不含 SQuAD、FEVER）；T3 多次 LLM 调用 2 个、T4 聚合 2 个（Movies、Products）；T5 RAG 2 个（FEVER 取 4 段上下文，SQuAD 取 5 段）。查询和提示由作者编写，见附录 A、C。

**函数依赖**（附录 B，p.13）：例如 Movies 中 movieinfo、movietitle、rottentomatoeslink 互相决定；Products 中 parent_asin 与 product_title；SQuAD 与 FEVER 没有函数依赖。

**模型与硬件**（§6.1.3 p.7）：Llama-3-8B-Instruct 单张 L4（24GB）；Llama-3-70B-Instruct 在 8 张 L4 上张量并行，只跑 filter；RAG 用 gte-base-en-v1.5 嵌入加 FAISS 检索；费用实验用 GPT-4o-mini 与 Claude 3.5 Sonnet 的 API；附录 D.2 另测 Llama-3.2-1B。

**单位**：一个查询是一个 LLM 算子对整张表执行一遍，每行一次请求；指标是整批任务的端到端时间（job completion time）、API 费用和前缀命中率（PHR）。

阅读者分析：数据源是真实的推荐和 QA 数据，但查询是作者构造的，没有来自生产日志的查询分布；工作负载都是离线批处理，不涉及在线请求或多个查询之间的缓存共享。

依据：[MLSys 2025](https://proceedings.mlsys.org/paper_files/paper/2025/file/b5dc49f44db2fadc5c4d717c57f4a424-Paper-Conference.pdf)，§6.1、Table 1、附录 A–C，PDF pp.6–7、12–14。
