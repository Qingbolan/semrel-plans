# Novelty分析

贡献集中在三个层次：以 reference algorithm 界定自然语言算子行为；以统计采样定义近似优化允许的误差；为 join、filter、group-by、top-k 设计可由系统选择的具体实现（§2–3）。相对仅把 LLM 包进 UDF，接口携带了可用于优化的操作语义。

方法边界：代理与任务相关性决定节省幅度；reference 本身可犯错；natural-language aggregation 的结合性与交换性不是任意提示都满足，论文允许自定义 partitioner（p.4174脚注）。本文不研究 map/aggregation 的全面优化。

证据审查：§3.1写默认采样 max(1%数据量,100)，§5方法设置写0.01%且至少100；复现时必须按具体实验和实现确认，不能填一个统一数值。BioDEX 的“1000倍”比较对象是不可实际完整运行的参考算法估计成本，不能写成相对所有系统都实测加速1000倍。

来源：[Semantic Operators and Their Optimization: Enabling LLM-Based Data Processing with Accuracy Guarantees in LOTUS](https://www.vldb.org/pvldb/vol18/p4171-patel.pdf)。
