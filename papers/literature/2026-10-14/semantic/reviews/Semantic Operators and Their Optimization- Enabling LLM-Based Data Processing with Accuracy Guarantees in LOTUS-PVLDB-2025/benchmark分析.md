# 基准评测

表2：FEVER优化LOTUS accuracy91.0%，batched190.0s；未优化91.2%、329.1s；FacTool80.9%、无batched实现，unbatched5396.11s。对照必须保持batched/unbatched口径。

表3：BioDEX Llama-70B设置，LOTUS join+rank RP@5=0.265、RP@10=0.280，2503s；DocETL join+rank0.262/0.282、2342s。表4 GPT-4o-mini设置，LOTUS0.289/0.296、647s；DocETL0.268/0.287、583s。不能泛化为LOTUS在该任务总是更快。DocETL只统计3次成功运行，失败重试不包括在该表均值内。

表6：SciFact LOTUS nDCG@10=0.765、36.3s，reranker0.741、2.64s；HellaSwag-bench0.919对0.461。收益主要在复杂语义排序，而普通相关性排序的更小模型有明显延迟优势。§5.5用20/50次trial检查目标与失败概率。以上是作者实验，未重新执行。

来源：[Semantic Operators and Their Optimization: Enabling LLM-Based Data Processing with Accuracy Guarantees in LOTUS](https://www.vldb.org/pvldb/vol18/p4171-patel.pdf)。
