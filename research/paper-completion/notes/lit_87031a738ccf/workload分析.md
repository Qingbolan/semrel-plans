# 工作负载

**规模**（Table 2、§2.3–2.4）：

| 项目 | 数值 |
|---|---|
| 题目数 | DE-Arch 30 / DE-Impl 30 / DE-Evol 50 / DA 100，共 210 |
| DE 来源 | 73 个企业级 SaaS 领域的 schema 与配套开源 dbt 转换项目（许可为 Apache-2.0、MIT 等），规范化为纯 SQL 仓库，并灌入合成但满足参照完整性的数据（App. E.1–E.2） |
| DE-Impl 原始数据 | 平均 23.3 张表 / 381.6 列（Table 2）；正文另称平均 32 表、412 列 |
| DE 代码规模 | Table 2：Impl/Evol 平均 2,296 / 949.6 LOC，改动文件 37.0 / 11.7；正文 §2.4 另写 4,612 LOC/43 文件与 1,718 LOC/13 文件 |
| DE-Impl 分层节点 | staging 16.0 / core 11.8 / mart 8.8 |
| DE-Evol 表改动 | create 3.76 / edit 7.90 |
| DA 数据 | 从 Web 收集 100 个复杂数据库，补充基于 DE 转换数据的分析建模层；每题平均 3.9 表、84.7 列，参考解平均 433 LOC（正文写 347） |
| DA rubric | 平均 3.1 需求 / 5.7 子需求 / 12.7 路径 / 22.4 条目；条目权重 Completeness 14%、Accuracy 66%、Insightfulness 20% |

**任务产生方式**：DA 每张分析表先由标注者写 8 个开放问题，5 人投票保留 2 个；DE-Evol 由数据工程师写变更需求；DE-Impl 由选定 SaaS 项目逆向成单个 `data_contract.yaml`；DE-Arch 每项目提 5 个候选需求，由数据工程师选 1 个（§2.3）。共 8 名专家参与构建。

**划分**：论文只描述测试题集，未提供训练/开发划分。DA 题被手工分为 Descriptive、Diagnostic、Strategic、Pattern Recognition、Profiling 五类（§3.5）。

阅读者分析：Table 2 与 §2.4 正文对 schema 列数、LOC、文件数给出不同数字（可能是统计口径不同，如"全部代码"与"需改动代码"，但原文未解释），引用时应注明出处表格（阅读者分析）。

依据：[arXiv:2512.04324v1](https://arxiv.org/abs/2512.04324)，§2.3–2.4、Table 2、Figure 3，PDF pp.4–6；§3.5，p.10；App. E，pp.34–39。
