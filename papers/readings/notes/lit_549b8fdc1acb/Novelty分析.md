# 贡献与评价

论文列出的贡献：(1) 多智能体 TQA 框架，同时支持单表和多表；(2) 三种 agent 调度算法：固定顺序轮转、LLM 根据 agent 功能描述选择、有限状态机（FSM）；(3) 基于 Trino 的数据连接器，自定义数据源只需实现五个接口；(4) 开源低代码工具 LinguFlow，用 DAG 构建和部署 LLM 应用，并带有按命名空间隔离的 few-shot 嵌入检索服务；(5) 已在 PingCAP 生产环境部署。

设计上的要点是 Engineer 只描述子任务，SQL/Python 由 Executor 调用外部工具完成，便于定位错误；作者称实践中很多错误来自外部工具而非 agent 本身。

阅读者分析：贡献偏系统工程与部署经验。多表能力只在私有工业数据集上验证，且没有可比的多表基线；FSM 调度本质是手写转移规则（Engineer 之后可转 Executor 或 Critic），新意有限。

依据：§1 Key Contributions，PDF p.2；§3.2，PDF p.4；§4.1–4.3、Algorithms 1–3，PDF pp.4–8。
