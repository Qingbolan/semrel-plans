# 基准评测

§4.1：Llama-3.1-70B-Instruct，vLLM，8×A100 80GB，SQL用SQLite3，RAG用E5-base与FAISS。对照包括Text2SQL、RAG、Retrieval+LM Rank、Text2SQL+LM、手工TAG。

表1：手工TAG总体exact match0.55、平均2.94秒；Text2SQL 0.17/5.63秒；RAG 0/3.23秒；Retrieval+LM Rank0.02/4.82秒；Text2SQL+LM0.13/9.08秒。总体exact match只覆盖60条非聚合问题。手工TAG在match/comparison/ranking为0.60/0.65/0.40。聚合仅图2定性举例。

不能把55%写成全部80条问题的统一准确率，也不能把手工流水线成绩当作自动query生成成绩。
