# usecase

**用例：HybridQA 多跳问题**（Table 1、Figure 3，p.4–5）——“2008 年被西雅图水手队选中、出自佐治亚大学的球员在 MLB 中效力过哪些球队？”

数据组织：表 w(name, position, school) 来自 Wikipedia 选秀表，例如 “joshua fields / right-handed pitcher / university of georgia”；documents(title, content) 存 Wikipedia 正文，如 “josh fields (pitcher)：joshua david fields (born 1985-8-19) is an american professional baseball pitcher…”。

BlendSQL 的分解思路（步骤 1–2 依据 §2.2–2.3 原文；Figure 3 的查询为图片、文本层未能提取，步骤 3 及整体串联为阅读者推断）：
1. 先用普通 SQL 过滤 w.school = 'university of georgia'，只把这一子集交给 LLM（§2.3 的优化）；
2. 用 LLMJoin 把表中的 “joshua fields” 与文档标题 “josh fields (pitcher)” 对齐——两者无外键，但指同一人（相当于实体链接）；
3. 对对齐后的文档用 LLMQA 回答“效力过哪些 MLB 球队”。

另一个例子（Figure 1，OTT-QA）：先用 FTS5 检索与 “nba OR covid” 最相关的文档，再用 LLMQA 回答“哪个 NBA 赛季因 COVID-19 中断”，并用 options 把输出约束为 “Lebron James Career Statistics” 表 Year 列中的已有值（p.4）。

阅读者分析：这类用例对应本项目的“语义连接（实体对齐）+ 语义聚合/问答 + 关系过滤下推”组合；但论文没有报告 LLMJoin 的调用次数或批处理策略的成本细节（后续 SWAN 与 Sema-SQL 论文才讨论其批大小 5 的影响）。
