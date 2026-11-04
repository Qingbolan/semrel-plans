# An Adaptive Query Execution System for Data Integration

数据集成要跨网络查询自治来源，但统计缺失、数据到达慢且突发，来源还常有镜像或重叠。本文提出 Tukwila：优化器可只交出部分计划，执行完一个片段后按实际基数重新优化；执行器用双流水哈希连接（double pipelined join）和可编程的 dynamic collector 适应来源行为，统一由事件-条件-动作规则驱动。

在 TPC-D 数据上，"物化并重规划"比全流水静态计划总快 1.42 倍、比只物化快 1.69 倍；保存优化器状态（带 usage pointers）比从头重规划最多快 1.64 倍；双流水连接首批结果明显更早（§6）。

[原文](https://www.cis.upenn.edu/~zives/research/adaptive_exec.pdf)

版本：SIGMOD 1999（Ives, Florescu, Friedman, Levy, Weld），12 页，原文 SHA-256 `6fc421aaa3f78e4ba9ac11e465aa8dc0f5d95d4ec5fb826ac3cb1f1208e49dd8`。已对照全文核读 §1、§3–4、§6–8，数字已核对，未复现实验。
