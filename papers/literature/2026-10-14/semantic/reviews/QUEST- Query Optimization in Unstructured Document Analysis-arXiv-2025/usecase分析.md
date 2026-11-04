# 具体用例

Figure1的原始SQL示例是：

```sql
SELECT name, team
FROM Players
WHERE age>35 AND all-stars>12
```

该图另给出Players与Teams的join示例。这是论文插图原文，`all-stars`保留作者写法，不能在原始query栏中悄悄改成可执行标准SQL。

输入是用户选定的文档集合与属性说明：Players文档提供name、team、age、all-stars，Teams提供球队及championships等。数据环境包括这些文档构建的两级索引；join则再需要另一集合。每条属性描述不是数据记录本身。

现有本地QUEST集合若有83条查询，只能对应其源文件版本；论文表1主评测50查询，不能直接宣称83条逐一来自论文正文或覆盖论文所有实验。

来源：[QUEST: Query Optimization in Unstructured Document Analysis](https://arxiv.org/abs/2507.06515v2)。
