# 具体用例

Table 4 的例子：用户问“Aurora MySQL 有大量会话在等 CPU 和 `io/redo_log_flush`，原因和修法？”。Panda 结合文档判断原因是过多提交与写 I/O，建议把写操作合并、使用更大批次或批量插入以减少提交次数，并附 Aurora 用户指南第 901–903 页的行级引用。GPT-4 的回答建议调 `innodb_log_file_size`、拆分大事务；评审 DBE 指出 Aurora 不使用该参数，且“拆小事务”方向与正确做法相反。

Table 3 的 APG `lock:tuple` 例子中，Panda 建议找出长时间 idle in transaction 的阻塞会话，短期用 `pg_terminate_backend`，长期调整应用并发，并用 `aurora_stat_backend_waits` 分析历史等待。

这是“文本证据 + 遥测特征 + 系统元数据”一起作为 LLM 上下文的诊断问答，不是对表做语义查询；若用于本项目，只能作为多源上下文拼装和引用校验的参考（阅读者分析）。

依据：[原文](https://www.vldb.org/cidrdb/papers/2024/p6-singh.pdf)，§3、Tables 3–4，PDF p.5。
