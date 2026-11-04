# 具体用例

论文的运行例围绕 PostgreSQL 的 `shared_buffers` 与 `random_page_cost`（Table 1，PDF p.2）：

1. 手册称 `shared_buffers` 可设为内存的 25%、不超过 40%；在 16 GB 内存机器上，DBA 会把范围从默认 [0.125 MB, 8192 GB] 缩到 [4 GB, 6.4 GB]。
2. 论坛建议 SSD 上 `random_page_cost` 设为 1.x，范围可从 [0, 1.79×10^308] 缩到 [1.0, 2.0]。
3. GPTuner 自动完成这一过程：收集 GPT-4、手册和网页知识，过滤与 `pg_settings` 冲突的内容，抽取成 JSON 属性（Figure 3 中 `shared_buffers` 的建议值 27.5 GB、上界 44 GB 等），再据此选 knob、丢弃不合理区间。
4. 对 `lock_timeout` 这类“0 表示禁用”的 knob，用 `control_knob` 在正常区间与特殊值之间切换，避免优化器几乎不会采样到 0（§6.2，PDF p.8）。

最终在 TPC-H 上跑约 100 次压力测试，输出 95 分位延迟最低的配置。

这是“读文档→生成结构化约束→驱动数值优化”的范式，结构化抽取的错误会直接改变搜索空间；论文用 §8.4 的错误注入实验评估这一风险（阅读者分析）。

依据：Table 1、Figure 3、§6.2，PDF pp.2、5、8。
