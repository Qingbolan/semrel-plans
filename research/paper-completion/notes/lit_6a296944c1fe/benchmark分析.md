# benchmark

设置：Snowflake 的编码 agent Cortex Code（CoCo）v1.0.80 + Claude Opus 4.7。两种范式：
- Agent as Compiler：agent 用 Python/SQL 等工具理解数据后，为每个问题生成一个静态流水线，内含单个语义查询；分别用 AISQL（直接在 Snowflake 上执行）和 LOTUS 1.1.4（经 Snowflake REST API 使用同一模型）。因 REST API 不提供 log-prob，LOTUS 的语义排序算子被禁用。
- Agent as Orchestrator：agent 交互式地使用 AISQL 与其他工具解决全部查询，可根据新观测修正推理。

评审：Claude Opus 4.7 作为 LLM-as-a-Judge，18 条每条 0–5 分；每种方法跑 3 次，报告均值 ± 标准差。

| 方法 | 得分（%） |
|---|---|
| CoCo Compiled LOTUS | 12.2 ± 3.0 |
| CoCo Compiled AISQL | 17.0 ± 3.3 |
| CoCo as Orchestrator | 25.9 ± 5.5 |

发现：最强配置也只恢复约 26%；三种方法都只部分恢复客群（编译 AISQL 漏 sports_fan，编译 LOTUS 漏 patriotic），编译式 agent 会根据少量评论样本和领域知识硬编码"看似合理"的通用客群；客群错误引发雪崩效应，使后续按群体计算的消费与满意度指标针对的是数据中不存在的群体；时间事件被合并。

局限（§5）：LLM 评审有长度、位置、与细则词面重叠等偏差，作者计划用人类专家校准子集和多评审一致性，并明确尚未声称评审稳健；合成数据与真实数据有差距（真实企业有遗留怪癖、外生事件、自然演化的分类体系），定位为与 KramaBench、DAB 互补的受控实验室；部分条目存在解释歧义（如聚类粒度），目前靠人工误差分析调整，未来计划用进化方法（GEPA）。

阅读者分析：评审模型与被测 agent 使用同一模型族（Claude Opus 4.7），存在自我偏好风险，原文未讨论；LOTUS 禁用了 sem_topk，因此 LOTUS 与 AISQL 的差距不能完全归于引擎本身；三次试验、18 个条目的样本很小，标准差 3–5.5 个百分点，编译式两种之间的差异需谨慎看待。

依据：[arXiv:2605.24183v1，4 页](https://arxiv.org/abs/2605.24183)，§4.1–4.2、Table 2、§5，PDF pp.3–4。
