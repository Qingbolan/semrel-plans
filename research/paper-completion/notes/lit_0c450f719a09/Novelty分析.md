# 贡献与评价

| 贡献 | 原文要点 |
|---|---|
| Semantic Variable 抽象 | 保留提示结构与请求间数据流，提交与获取分离（异步 future） |
| 依赖请求服务端执行 | 图执行器在生产者完成后立即派发，变量值经消息队列传递，支持 LangChain 式输出解析变换 |
| 性能目标推导 | 从延迟敏感的最终变量逆拓扑传播，把并行同层请求归为 task group，整组追求低完成时间（可用大批次） |
| 前缀共享 | 按变量边界哈希建索引；新 attention 核结合 FlashAttention 与 PagedAttention，共享前缀 KV 只加载一次 |
| 应用感知调度 | Algorithm 1：拓扑序、task group 整体放置、共享前缀同引擎、按延迟需求控制引擎 token 容量 |

实现约 14,000 行 Python，其中前端 1,600、管理器 3,200、引擎 5,400 行 Python 加 1,600 行 CUDA。

阅读者分析：依赖感知调度、前缀缓存各自已有先例，Parrot 的贡献是用一个变量级抽象把这些信息暴露给公共服务端并统一利用。代价是应用需改写为 SemanticFunction；FindEngine 细节因篇幅省略，难以独立复现调度策略。

依据：[原文](https://www.usenix.org/system/files/osdi24-lin-chaofan.pdf)，§4–5、§7、§9，PDF pp.5–10、14–15。
