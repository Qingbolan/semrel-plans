# 具体用例

原文 Figure 1 的运行例子（PDF p.2）：用户说 “Can you recommend me an Italian restaurant with a romantic atmosphere?”。

**SUQL 路径**：少样本解析器结合数据库模式生成

`SELECT *, summary(reviews) FROM restaurants WHERE 'italian' = ANY (cuisines) AND answer(reviews, 'is this restaurant romantic?') = 'Yes' LIMIT 1;`

执行过程：
1. 编译器先用结构化谓词筛出意大利菜；
2. 用评论嵌入检索与“浪漫”相关的候选；
3. 用 LLM 复核 `answer(...) = 'Yes'`；
4. 满足 `LIMIT 1` 后停止，并对评论做摘要；
5. 最终回复 Penny Roma，并描述其约会氛围。

**线性化路径**：整行转为文本向量，取余弦最近邻，结果为 Hummus Mediterranean Kitchen，菜系错误，评论也没有提到浪漫。

这个例子正好对应“结构化过滤 + 语义过滤 + LIMIT”的混合查询。但示例中的执行顺序和检索截断参数（取多少候选再复核）在正文中没有给出具体数值（阅读者分析）
