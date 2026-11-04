# workload分析

[论文原文](https://arxiv.org/html/2609.24137v1)

§2原文示例：“Which product experienced the largest decline in sales, and why?” 输入为销售表与评论，环境含语义目录、索引和历史知识；SQL先定位下降产品，语义过滤负评，再抽取/分组原因。该例没有给出具体列schema或公开文件路径，因此不编造可执行query JSON。§5-A明确记录合批、级联和共享前缀KV复用，但未给统一batch size。
