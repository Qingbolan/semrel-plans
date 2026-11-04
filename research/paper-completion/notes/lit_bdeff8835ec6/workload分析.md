# 工作负载

数据集（附录 Table 6，p.12）：

| 数据集 | 划分 | 查询数 | 文档数 | 金标准文档/查询 |
|---|---|---|---|---|
| TopiOCQA（多轮对话，消歧） | train/test | 45,450 / 2,514 | 25,700,592 | 1 |
| HotpotQA（多跳，分解；BEIR 语料） | train/test | 85,000 / 7,405 | 5,233,329 | 2 |
| MultiHop-RAG（仅测试，域外） | test | 2,556 | 7,786 个块（609 篇原文按 256 token 切块，重叠 20） | 多个 |

检索器：TopiOCQA/HotpotQA 用 BM25（Pyserini）与 ANCE（Faiss，训练用 HNSW、评测用 flat 索引）；MultiHop-RAG 用 bge-large-en-v1.5 与 llm-embedder（LlamaIndex）。

训练：Qwen2.5-3B，verl + DAPO，8 卡，每查询 8 个 rollout，最大响应长 256 token。模型按数据集与检索器分别训练。HotpotQA 的 Stage I 先过滤掉表现较好的样本只保留约 50%；Stage II 动态过滤再保留约 50%，τ_thres=53（附录 A）。

§2 的复杂度分析使用每个数据集 200 条“代表性”查询，非全集。

阅读者分析：这是文本检索/RAG 的查询改写负载，单位是“问题→检索列表”，与 SQL 或语义算子查询优化不同；atlas 中若以“查询优化”归类需注意术语歧义。

依据：[arXiv:2601.21208v1，16 页](https://arxiv.org/abs/2601.21208)，§2.1、§4.1、附录 A、Table 6，PDF pp.3、7、11–12。
