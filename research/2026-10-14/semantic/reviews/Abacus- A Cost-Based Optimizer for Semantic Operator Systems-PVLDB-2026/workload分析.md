# workload分析

§4.3每个系统在10个不同test抽样上执行；每份BioDEX split250条，CUAD与MMQA各100条。MMQA为控制费用，只保留与至少一个ground-truth question相关的数据项，不能解释成对完整开放数据湖检索。

对照实验统一允许GPT-4o-mini、text-embedding-3-small、clip-ViT-B-32；系统实现可用的模型集合更大，但不要把这个集合写成所有表2实验都混用（§4.1 vs §4.3）。

采样默认k=6个物理算子、j=4个输入；sample budget=50×semantic operator数。这是优化采样批，不是整个数据输入批大小，也不是LLM一次prompt含4条。MAB frontier内部可并行，frontier之间顺序依赖（§5）。本论文不提供多独立用户查询共享执行benchmark。

来源：[Abacus: A Cost-Based Optimizer for Semantic Operator Systems](https://arxiv.org/abs/2505.14661v3)。
