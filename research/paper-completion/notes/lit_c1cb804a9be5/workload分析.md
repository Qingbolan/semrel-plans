# 工作负载

**知识库**：Aurora PostgreSQL（APG）与 Aurora MySQL（AMS）的 wait event 文档，共约 2.5K 份、6.25M token；文档通常 2–4 页，含“可能原因/边界情况/处理动作”等小节；工单为短问答对。

**遥测**：250 个数据库指标，7 天、1 分钟粒度，共约 2.5M 个数据点。

**问题集**：作者围绕 Performance Insights 客户最常问的 wait event 手工设计 50 条排障问题，APG 和 AMS 各 25 条。Table 2 只列出 6 类常见场景，例如 APG 的 `Lock:Tuple`（应用设计不当）、`Lock:TransactionId`（长事务）、`Client:ClientRead`（网络），AMS 的 `io/redo_log_flush`（过量提交）、`synch/mutex/innodb/buf_pool_mutex` 等；另外 44 条未公开列出。

没有训练/测试划分，没有公开数据或问题清单；历史客户工单因敏感不向用户展示，论文也未给出工单数量。（阅读者分析）

依据：[原文](https://www.vldb.org/cidrdb/papers/2024/p6-singh.pdf)，§2.2、§3、Table 2，PDF pp.3–4。
