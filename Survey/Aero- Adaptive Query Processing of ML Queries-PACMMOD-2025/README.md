# Aero: Adaptive Query Processing of ML Queries

ML 中心的 DBMS 把深度模型包成 UDF 谓词，静态优化器依赖采样得到的选择率与代价，但这些统计会随数据和缓存在执行中变化。Aero 在 EvaDB 上加入一个 AQP 算子：Eddy 在运行时按实测代价（并考虑缓存命中）为每批数据选择谓词顺序，Laminar 按 GPU 利用率伸缩 worker 并按输入大小做负载均衡。

在 4 个数据集、6 个查询上，Aero 相对 Viva 最高快 6.4×（Q3；相对 EvaDB 为 8.22×），查询结果与 EvaDB 完全一致（§7.2）。

[原文](https://upenn.ferric.systems/dbscholar/sigmod_papers/2025/3725408.pdf)

版本：PACMMOD 3(3)（SIGMOD 2025），Article 174，27 页，DOI 10.1145/3725408；全文取自[学术镜像](https://upenn.ferric.systems/dbscholar/sigmod_papers/2025/3725408.pdf)。已通读 §1–8，数字已对照全文复核（2026-11）；未复现实验。

另见：[出版方版本](https://doi.org/10.1145/3725408)。
