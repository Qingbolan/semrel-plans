# 工作负载

**数据集**（§4.1，p.8）：三个长文档集合，规模跨两个数量级。

| 数据集 | 规模 | 领域 |
|---|---|---|
| GovReport | 973 篇政府报告摘要 | 政府 |
| PubMed | 2,500 篇生物医学研究文档 | 生物医学 |
| BigPatent | 67,072 篇专利文档 | 专利 |

**查询工作负载**：每个数据集配一个包含 20 个人工撰写自然语言谓词的池（取自 ScaleDoc）。由此构造三种模式：Conjunction（100% AND）、Disjunction（100% OR）、Mixed（AND/OR 各 50%）。依据“62% 的 Snowflake 查询含 3–10 个过滤条件”，叶子数取 2–10，每个叶子数 5 个表达式；每种模式 45 个表达式，每个数据集 135 个表达式（§4.1）。Table 1 给出各模式整体表达式的平均选择率：

| 数据集 | Mixed | Conjunction | Disjunction |
|---|---|---|---|
| GovReport | 17% | 1% | 45% |
| PubMed | 28% | 3% | 83% |
| BigPatent | 36% | 4% | 89% |


**判定与嵌入**：每个（文档，谓词）对的真值预先用 Snowflake AI_FILTER 与 Llama 3.1-70B（温度 0）跑出并缓存；模拟器按短路逻辑只对实际求值的谓词计 token（§4.1，p.7）。文档与谓词嵌入用 voyage-multilingual-2（经 Snowflake AI_EMBED），均为 1024 维、预先计算（§4.1，p.8）。

**单位**：一个“查询”= 一个表达式树对整个集合执行；一个 episode = 一行（文档）通过一个过滤节点；Table 1 的 Calls 与 Tok 是 45 个表达式的合计（GovReport/PubMed 以 K 次与 M token 计，BigPatent 以 M 次与 M token 计）。

阅读者分析：工作负载是由谓词池组合成的合成表达式，而不是真实用户日志；数据规模（最大 6.7 万文档）对生产来说仍属中等。嵌入成本在实验中未计入 token 总量（假定已在摄入时计算），作者在 §5 讨论了这一前提。

依据：[arXiv 2606.07923v1](https://arxiv.org/abs/2606.07923)，§4.1、Table 1，PDF pp.7–9。
