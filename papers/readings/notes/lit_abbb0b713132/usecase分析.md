# usecase

**用例：Superhero 库中“列出漫威宇宙的英雄”**（Figure 1，pp.1–2；§3.2–3.4、§4.1，pp.3–4）。

1. **构造**：原 BIRD superhero 表有 publisher_id 外键指向 publisher 表。SWAN 删除 publisher_id 列和 publisher 表，使所有与出版商相关的问题无法从库内回答，但保留去重后的 publisher_name 列表，以便 LLM 输出规范值（避免 “Marvel” 与 “Marvel Comics” 无法自动比对）。键改为 (superhero_name, full_name)。
2. **HQDL**：对每个英雄发一次提示，要求按 10 个字段返回一行（眼睛/头发/皮肤颜色、出版商、种族、性别、阵营、能力等），提供候选值列表并采用 “No Explanation” 规则；one-shot 示例为 “3-D Man, Charles Chandler → … Marvel Comics …”。生成结果解析入表后，用普通 SQL 连接并过滤 publisher_name。
3. **混合 UDF**：在 SQL 中直接对英雄名调用 LLM 函数得到 publisher，再过滤 = 'Marvel'（p.4 给出 BigQuery 写法；实验用 BlendSQL）。

结果上 Superhero 是两种模型执行准确率最低的库（HQDL 5-shot：GPT-3.5 20.0%、GPT-4 Turbo 23.3%，Table 2）。作者解释该库很多题要求找出特定集合（如漫威英雄、蓝眼睛英雄），而只有约 1/10 题含 LIMIT，错误无法被掩盖（p.6）。

阅读者分析：这个用例说明 SWAN 的核心难点是“LLM 作为不可靠的数据源”，而非查询构造；对本项目，若把 SWAN 题当作语义投影/语义连接工作负载，应注意每个实体都需要一次知识检索，且真值是 BIRD 库内容，可能与 LLM 世界知识不一致。
