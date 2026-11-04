# 具体用例

原文 Fig. 2 的例子（§II-B，PDF p.3）：用户问 “Find the names of all customers who checked out books on exactly 3 different genres on Labor Day in 2023”，数据库包含 Customer、Book、BookOrder 等表。

- 第 1 步（理解 NL）：识别实体/属性（names、customers、books、genres）、时间（Labor Day in 2023）和条件（exactly 3 different genres）。
- 第 2 步（找相关表、列、值）：“genres” 既可指 LiteraryGenre，也可指 SubjectGenre；“Labor Day” 在美国是 2023-09-04，在中国是 2023-05-01，需要依赖领域知识或附加信息（图中提示 Labor Day 指 5 月 1 日）。这一步对应 schema linking、数据库内容检索和附加信息获取三个模块。
- 第 3 步（写 SQL）：可用 NATURAL JOIN 加 GROUP BY … HAVING COUNT(DISTINCT SubjectGenre)=3，也可写成子查询，两者等价。Fig. 2(b) 展示 schema 变更（新增 Account 表）后 SQL 必须随之改变。

阅读者分析：这个例子说明 Text-to-SQL 的正确性依赖 schema 与值层面的对齐，“正确答案不唯一”也会影响 EX/EM 的评测口径。
