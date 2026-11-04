# 具体用例

论文 Figure 1 的例子（pp.2、4）：一张衬衫表含 Shirt（带文本描述，如“100% cotton”）、Made_in、Sales、Price 列，问题是“产自北美且不含化学成分的最畅销衬衫是哪件？”。

纯 SQL 无法完成，因为国家名本身不包含所属大洲，“不含化学成分”也要从文本描述中推断。Binder 生成的 SQL 为：

`SELECT Shirt FROM T WHERE f("No chemicals?"; Shirt) = 'yes' AND f("North America?"; Made_in) = 'yes' ORDER BY Sales DESC LIMIT 1`

执行时，Codex 分别对 Made_in 列和 Shirt 列逐值回答 yes/no，生成两列新列（North_America、No_chemicals），之后交给标准 SQL 引擎完成过滤与排序，得到 Polo。同一问题也可以写成 Python/Pandas 版本：`df = df[f("North America?"; Made_in) == 'yes']`，再按 Sales 降序排序。

**调试例子**（Table 5，p.7）：问题“kansas state 第一次以两位数分差获胜是哪年？”（标准答案 1926）。端到端 QA 给出 1967，看不出原因；纯 SQL 直接用文本列相减，语法上无法修正；Binder 用 `f("Points?"; win_team) - f("Points?"; los_team) > 10` 取分数，但 `win_team='kansas state'` 应改为 `LIKE '%kansas state%'`，错误位置清楚可修。

这个用例与“在关系查询中嵌入语义过滤/映射”的语义算子场景直接对应，`f_col` 相当于对一列逐行调用 LLM 的语义映射（阅读者分析）。

依据：§1、§2.3、§4.2、Figure 1、Table 5，PDF pp.2、4、7。
