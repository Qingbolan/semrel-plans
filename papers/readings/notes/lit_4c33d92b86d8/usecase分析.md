# usecase

论文的贯穿例子来自 TAG（Figure 3，p.3；§3.2，p.6）：“县人口超过 200 万的学校中共有多少考生？”数据库只有学校与 SAT 成绩表，没有人口。

1. **问题分解**（p.6）：① 语义投影：从 schools 表的县名推断人口（理由：库里没有人口，需从县名推断）；② 选择 population > 2,000,000；③ 与 satscores 按 cds = CDSCode 连接；④ 对 NumTstTakr 求和。
2. **HRA 查询**（Fig. 3b）：γ SUM(NumTstTakr)( satscores ⋈ σ_population>2000000( Π ExtractPopulation(County)→population (schools)))。对比 LOTUS 版本需要用户手写提示、正则解析数字、先取去重县名（Fig. 3a）。
3. **执行**：语义投影只对去重后的 County 值调用 LLM，再连接回原表（Table 1、§5，pp.4、8）。

第二个例子（Fig. 6–7，p.7）：统计某场比赛中亚洲国籍车手数。原计划先对 drivers 做 LLM 选择“nationality is Asian”再连接；优化把 LLM 选择延后到连接与关系过滤之后，Z3 用符号表验证 σ_llm(T_d)⋈T_r ≡ σ_llm(T_d⋈T_r)，实测输入从 73 行降到 42 行（p.11）。

阅读者分析：这个用例体现了论文的边界——语义投影依赖模型参数知识（人口），因此答案正确性取决于 LLM 记忆；Table 4 中“Factual Error”占 4.1%–9.1%，正是这类错误。
