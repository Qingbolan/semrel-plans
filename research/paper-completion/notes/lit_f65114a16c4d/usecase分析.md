# 具体用例

**场景**（Figure 1–2 的示意）：分析师要为“Company X 2023”季度表撰写评论，表含 Q1–Q4 行与 Revenue、Expenses 两列（Q1 收入 $1B、支出 $.25B，……，Q4 收入 $.3B、支出 $.75B）。

**流程**：

1. 程序生成模块（LLM 或 PCFG）输出一批程序，如 `get({revenue}, {Q1})`、`sum({revenue})`、`less_than(sum({revenue}), sum({expenses}))`。
2. Python 解释器执行，得到 $1B、$4.3B、False。
3. GPT-4 表层实现写出“Firm X revenue in Q1 2023 was $1B”“Firm X total revenue in 2023 was $4.3B”“Total revenue was not less than total expenses, indicating a profit in 2023”。
4. 用户在界面中看到每句话、对应程序和被高亮的表头单元格，例如 `argmax({Q4}) = Expenses` 高亮 Q4 行，从而无需自己重算就能判断是否接受。
5. 被接受的样本成为下一轮的少样本示例；PCFG 版本则提高对应产生式的概率。

**注意**：第 3 句中“indicating a profit”是表层实现添加的推断，程序只证明了比较关系；按原文标准，若用户认为这超出程序内容，应判为幻觉而拒绝（阅读者分析）。

依据：§3、§3.6、Figures 1–2，PDF pp.2–4。
