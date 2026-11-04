# 具体用例

原文 Figure 3 与 Figure 5 给出的 MySQL 旋钮推荐用例（PDF pp.5、9）：

- **环境**：RDS MySQL 5.7，8 vCPU、16 GB 内存；负载为 SYSBENCH 读写混合（读写比 50%，32 线程），数据 13 GB、50 张表、每表 100 万行。
- **提示输入**：任务描述“根据内部指标和负载特征推荐最优旋钮配置以优化吞吐”；一条改进示范（如 thread_cache_size 50→75、innodb_log_file_size 512M→1024M）；内部指标与旋钮的文字说明；当前配置（如 tmp_table_size=16777216）；数据库反馈（Throughput=100，lock_timeouts=0，dml_updates=22692 等）。
- **LLM 输出**：JSON 格式的新配置，并附带理由，例如“缓冲池从 13GB 增到 14GB 以减少磁盘读”“buffer_pool_read_ahead 为 0，调整 innodb_read_ahead_threshold 到 24”“写 I/O 线程从 16 增到 32”。
- **迭代**：新配置应用于数据库，重启并压测得到新反馈，再进入下一轮（§2 Eq.3，PDF pp.3–4）。

剪枝用例：GPT-4o 选出的 10 个旋钮与专家高度重合，区别在于选了 join_buffer_size 而专家选了 max_connections；作者解释后者在超过实际连接数后对性能无影响（§5.3、Table 1，PDF pp.6–7）。

阅读者分析：这是“LLM 读取系统遥测并生成结构化动作”的闭环用例，与语义查询处理不同，输出的正确性由实际执行性能而非标注答案判定。

依据：§2、§3.3、§5.3、§7.3、Figures 3、5、Table 1，PDF pp.3–9。
