# 具体用例

**Oracle `LOG_FILE_SYNC`（日志同步延迟）**——贯穿全文的例子（Figure 1–4、§5–6、Table 8）：

1. **触发**：异常模型检测到平均等待时间 > 60ms，或 10 分钟急升且 > 6ms，并在 5 次评估中成立 3 次，触发 `LOG_FILE_SYNC` Trigger 顶点。
2. **隐式相关指标**：调用低代码工具 LogSync Performance Verifier（比较 log file sync 等待、redo 生成率、事务提交数与基线）和 RedoArchive Health Inspector（比较归档日志与 redo 大小、检查 `log_buffer`、`archive_lag_target` 等参数）。
3. **图演化**：Cypher 遍历发现 `REDO_ALLOCATION` 异常模型共享并发等待事件，建立交叉边并合并指标（如 `redo_buffer_busy`）；ADF 举例：`avg_log_sync_time` 序列 {12,14,55,58,61}，均值 40、σ≈21、基线 B_t≈15、偏离 D≈43，σ>θ（设 θ=10）则判异常并继续扩展。
4. **报告**：Table 8 中 DBAIOps 报告（HEval=1.00）给出根因"REDO 日志存储 I/O 性能不足""日志写入期间间歇性 I/O 压力尖峰"，推理依据 log_file_sync / log_file_parallel_write ≈ 2 → 存储 I/O 为主因，且所引用指标（log file sync max=15.2ms、avg=6.0ms）均在输入数据中；基线报告（HEval=0.40）只列 log file parallel write、checkpoint 延迟等症状，并引用了不存在的指标。

阅读者分析：这个例子显示系统的价值在于把"告警 → 相关指标 → 经验 → 根因"的路径显式提供给 LLM，并约束其只引用给定证据；图中具体阈值（60ms、6ms、3/5）属于专家规则而非学习所得。

依据：[arXiv:2508.01136v1](https://arxiv.org/abs/2508.01136)，Figure 1，p.1；§5.1–5.2，pp.6–7；§6.1，pp.7–8；§7.4、Table 8，p.12。
