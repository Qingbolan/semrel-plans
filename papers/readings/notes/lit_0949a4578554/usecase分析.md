# 具体用例

§6.3 对 TPC-H 1GB on PostgreSQL 的深入分析（Table 5、Figure 5，pp.10–12）：

**提示内容**：按 Listing 1 模板，说明目标系统（Postgres）、压缩后的连接结构（每行“连接键 A：与 A 连接的所有列”）、内存与 CPU 核数（§3.1，p.3）。

**λ-Tune 选出的配置**（Table 5，p.11）：

| 类别 | 参数 | 值 |
|---|---|---|
| 内存 | shared_buffers | 15GB |
| 内存 | work_mem | 1GB |
| 优化器 | effective_cache_size | 45GB |
| 内存 | maintenance_work_mem | 2GB |
| 日志 | checkpoint_completion_target / wal_buffers | 0.9 / 16MB |
| 优化器 | default_statistics_target / random_page_cost | 100 / 1.1 |
| IO | effective_io_concurrency | 200 |

索引为单列树索引，覆盖 lineitem（l_suppkey、l_orderkey、l_partkey）、orders、part、partsupp、supplier、customer、nation 等表上的连接列。

作者解读：shared_buffers 约为 61GB 内存的 25%，与 Postgres 手册建议一致；增大 effective_cache_size、降低 random_page_cost 会促使优化器更多使用索引，与同时推荐建索引相呼应（§6.3，pp.11–12）。对 TPC-H 提示采样 15 次时，出现运行时间最高达最优 5 倍的离群配置，说明需要有界的配置选择（p.12）。Figure 5 显示所选配置下 22 条查询每条都不慢于默认配置。

阅读者分析：这个用例可看作“LLM 生成候选 + 系统按实测代价选择”的模式，适用于其他由 LLM 提出方案、由执行反馈裁决的数据系统任务。

依据：§3.1、§6.3、Table 5、Figure 5，PDF pp.3、10–12。
