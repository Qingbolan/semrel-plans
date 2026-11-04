# 具体用例

论文主例（Figure 1–2）：一张 2007–08 赛季 Minnesota Wild 的比赛表，列为 Date、Visitor、Score、Home、Decision、Attendance、Record；待核查陈述是“minnesota played at home more times than they played away”。

1. **证据分解**：LLM 选出相关列（如 Date、Visitor、Home）和相关行，得到子表。
2. **解析**：生成完形子问题“q1: {...} times minnesota played at home.”与“q2: {...} times minnesota played away.”。
3. **执行**：生成 `SELECT COUNT(*) FROM w WHERE home = 'minnesota'` 和对 visitor 的同类查询，执行结果为 6 和 8。
4. **回填与推理**：子问题变成“{6} times … at home”“{8} times … away”，推理器据此判断陈述为假。

Table 6 的 WTQ 案例显示同一机制的价值：问 barrington、farmington、rochester 三地清单合计数，Codex 的思维链自造“1+1+1=3”，Dater 通过三条 COUNT 查询得到 1、1、3，答案 5 正确。

这一模式相当于“LLM 负责语义对齐与规划、SQL 负责精确计数”，与语义算子系统中将 LLM 判断与关系执行混合的思路相近；但论文只处理单张小型 Wikipedia 表，不涉及多表或大规模数据（阅读者分析）。

依据：Figure 1–2，pp.2、4；§4.3.1，p.6；Table 6，p.11。
