# 工作负载

| 负载 | 用途 | 规模/设置（原文） |
|---|---|---|
| JOB（Join Order Benchmark） | 准备阶段：执行记录存入 C_p 作为参考样例；也用于 LLM 的 SFT；Table 2 也在 JOB 上报告结果 | 未给出使用的查询条数；脚注称 SFT 用的 JOB 训练集与评测用的 JOB 测试集不同 |
| CEB（Cardinality Estimation Benchmark） | 主评测负载 | 每个模板取 2 条查询，超时 10 s |
| Stack | 跨负载泛化评测 | 每个模板取 5 条查询，超时 30 s |

环境：单机 AMD Ryzen 9700X、128 GB 内存、NVIDIA A6000 48 GB；PostgreSQL 16.4 + pg_hint_plan；向量库 Milvus。模型：本地 DeepSeek-Coder-Instruct-7B、LLaMA3.1-8B、SFT 版 LLaMA3.2-3B，远程 GPT-o3-mini 与 DeepSeek-V3 Chat。实验前预热机器以减轻缓存影响。

迭代方式：每轮处理完整负载，同一负载重复多轮；§4.3 与 §4.5 均为 50 轮。

原文未说明：CEB 与 Stack 的模板数和最终查询总数、JOB 训练/测试的划分方式、数据库规模、每个设置是否多次运行。

阅读者分析：CEB 与 JOB 都建立在 IMDb 上，作者因此另用 Stack 测试“完全不同”的负载（§4.5）；但 Stack 只给出 Figure 5 的曲线，无表格数值。

依据：§4.1、§4.2 脚注 2、§4.5，PDF pp.3–4。
