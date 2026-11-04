# workload分析

§5评测：CUAD510份中的前50合同、41类专家标注；Steam10游戏，每份输入文档包含300评论；BlackVault733文章，平均700words；BioDEX250文章、24300labels。

批处理有不同含义。map是一条记录一次任务；长文档split按token拆分，Steam例选择104652 tokens/chunk；BlackVault reduce按41份文档fold batch推进。41是该计划归约批大小，不能复制到所有query。线程并行、输入记录数、prompt批、输出top-k须独立记录。

论文运行环境为2021 M1 Macbook Pro调用OpenAI；execution用gpt-4o-mini，optimizer通常gpt-4o-mini，BioDEX用gpt-4o。实验主要2024-09，Aryn与非LLM基线补于2025-02（p.3043）。这是复现实验配置，不是问题页“数据环境”定义。

来源：[DocETL: Agentic Query Rewriting and Evaluation for Complex Document Processing](https://www.vldb.org/pvldb/vol18/p3035-shankar.pdf)。
