# 具体用例

论文开头的例子是：给定 employees 和 manages 两张表，用户问"找出工资高于其经理的员工"，系统要生成相应 SQL（§1，p.1）。这类问题需要自连接或多表 JOIN，正是 §3 中 JOIN 类失败的典型。

§3 给出的模式链接失败例子更具体：问题"所有体育场的平均容量和最大容量是多少？"，模式中恰好有一列名为 average，模型直接选了这一列，而不是对 capacity 列取 AVG（p.3）。

按 DIN-SQL 流程处理这类问题时（§4，pp.4–6）：

1. 模式链接模块用"Let's think step by step"格式，列出问题中提到的列及其所属表、可能的取值；
2. 分类模块判断是否需要 JOIN 或子查询，并给出要连接的表；
3. 若为 non-nested complex，先生成 NatSQL 中间表示再生成 SQL；若为 nested complex，先写子问题对应的子查询；
4. 最后用 gentle（GPT-4）或 generic（CodeX）提示检查 DESC、DISTINCT、聚合等遗漏。

论文报告用 GPT-4 回答一个 Spider 问题约花费 0.5 美元、约 60 秒（§7，p.10）。

阅读者分析：每个问题至少 4 次串行 LLM 调用，部署时延迟和成本由调用链长度决定，而非单次生成。

依据：§1、§3、§4、§7，Figures 2–3，PDF pp.1–6、10。
