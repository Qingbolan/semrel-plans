# 工作负载

**要验证什么**（§IV，p.6）：四个研究问题。RQ1 效果：在结构异构的系统和不同 LLM 上是否超过基线；RQ2 效率：token 与墙钟时间；RQ3 消融：各模块贡献及是否依赖系统特定 prompt；RQ4 失败分析：残余错误的类型与结构瓶颈。

**数据**：沿用 OpenRCA 的既有遥测，本文没有新增事故集（§IV-A，p.6）。三个系统在各结构维度上都不同（Table I，p.3）：

| 维度 | Bank | Telecom | Market |
|---|---|---|---|
| 案例数 | 136 | 51 | 148 |
| 候选层级 | pod | node、pod、service | node、pod、service |
| 候选组件 | 14 pod（6 service） | 22 node、8 pod、13 service | 6 node、40 pod、10 service |
| 纵向拓扑 | 无 | node–pod 共部署 | 编码在 pod 名中；有故障转移 |
| 模态 | 指标、调用链、日志 | 指标、调用链（无日志） | 指标、调用链、日志 |
| 黄金信号 | 合成服务测试 | 单一网关（OSB） | 每服务 |
| 原因类型数 | 8 | 5 | 15 |
| 时间单位 | 指标 s、调用链 ms、日志 s | 全部 ms | 指标 s、调用链 ms、日志 s |

Market 合并了 cloudbed-1 与 cloudbed-2 两个部署。

**评分**（§IV-A，p.6）：使用 OpenRCA 评分器。Correct 要求所有被查询字段正确且预测根因数等于注入故障数，时间误差 ±60 s；Partial 按答对的字段比例计分。难度按查询模板分：easy 问 1 个元素（task 1–3）、middle 问 2 个（task 4–6）、hard 问全部 3 个（task 7）。

**模型**：deepseek-v4-pro 与 qwen3.7-plus，系统与基线都用这两个模型运行；Overall 按案例数加权（§IV-A、Table III）。

依据：[arXiv 2609.19825v1](https://arxiv.org/abs/2609.19825v1)，§II-B、§IV-A、Tables I、III，pp.2–3、6–7。
