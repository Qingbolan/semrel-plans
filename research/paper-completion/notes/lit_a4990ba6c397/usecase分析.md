# 具体用例

**范围歧义：健身房课程**（Figure 1a、Figure 2，pp.2、4）。数据库中有 Gyms、Classes 和关联表 Gyms_Classes，Yoga 被多个健身房提供。

问题“What activities does each gym offer?”有两种解读：
1. 集合读法：所有健身房都提供的课程。SQL 用 `GROUP BY ... HAVING COUNT(DISTINCT GymID) = (SELECT COUNT(*) FROM Gyms)`；
2. 分配读法：列出每个健身房各自的课程。SQL 是 Gyms 与 Classes 的连接投影。

**模型表现**（附录 G，p.23 的错误示例）：在一个同构的 Agriculture 例子“What kind of crop does each farm offer?”中，Llama3-70B 给出两条 SQL。两条都正确，但都对应分配读法，因此没有覆盖集合读法。

Table 4（p.9）显示，在至少答对一条的歧义样例中，分配读法占 83.5%（Prompt）。

阅读者分析：如果系统要对自然语言问题做语义查询，这个例子说明，模型“返回多条 SQL”不等于“覆盖了多种解读”。评测时应按执行结果去重后再计算覆盖率。

依据：[arXiv:2406.19073v2，29 页](https://arxiv.org/pdf/2406.19073v2)，§3.2、Figure 1–2，PDF pp.2–4；Table 4，p.9；附录 G，p.23。
