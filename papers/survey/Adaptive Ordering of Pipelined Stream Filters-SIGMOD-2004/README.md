# Babu, Motwani, Munagala, Nishizawa, Widom（Stanford / Hitachi）— Adaptive Ordering of Pipelined Stream Filters

连续查询要对数据流依次执行一组可交换的过滤器，流与过滤器的特性会随时间不可预测地变化，而且各过滤器的选择率可能相关。本文提出 A-Greedy：对一小部分已被丢弃的元组继续执行剩余过滤器，建立“条件丢弃率”画像，在线维持贪心不变式；若特性稳定，所得顺序的代价至多为最优的 4 倍（Theorem 4.1）。作者还给出 Sweep、Independent、LocalSwaps 三个变体，在收敛保证、运行开销与适应速度三者间取舍，并说明同一方法适用于一大类多路流连接（MJoin）。

在 STREAM 原型中用合成过滤器测试：稳定时 A-Greedy 通常找到最优顺序，Independent 几乎总更差；A-Greedy 的画像开销从 n=3、p=0.01 时不到 1% 增至 n=8、p=0.05 时 13.34%（Table 2），变化频繁时它胜过 Sweep，变化稀少时 Sweep 反超（Figure 19）。

[原文](https://www.cs.emory.edu/~cheung/Courses/584/Syllabus/papers/2004-Babu-Ordering-Stream-filters.pdf)

版本：SIGMOD 2004（Paris），12 页 PDF（SHA-256 `84d48afab5223a7130aa1e21c00a61cbda252e86bbee8345529ba0bcbe2401cc`）。2026-11-04 用全文复核 §1–10 与实验数值；Theorem 4.1 的完整证明在技术报告中，未复核；未复现实验。
