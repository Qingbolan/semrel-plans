# 具体用例

**原文示例**（Figure 1、Example 1–2，§2，pp.3–4）：

```sql
SELECT name, team
FROM Players
WHERE age>35 AND all-stars>12
```

`all-stars` 保留论文写法（不是可执行的标准 SQL 标识符）。用户为 Players 给出描述，如 “name: Player's full name”、“team: Player's current team”。

**逐文档排序**（Example 1）：样本估计 all-stars 的选择率低于 age。但在文档 d1 上，all-stars 的相关片段 token 远多于 age，因此 QUEST 先抽 age；在 d2 上，all-stars 的代价只比 age 略低，于是凭更低的选择率先抽 all-stars。

**证据检索**（§2.3，p.3）：只用 “age: Player's age.” 去检索，可能漏掉 “Wardell Stephen Curry II (born March 14, 1988) is an American professional basketball player …” 这样的片段，因为其中没有 age 一词。抽样时 LLM 从这类片段中抽出年龄，QUEST 把它们作为证据向量，用来检索其他球员文档中类似的出生日期句子。

**join 转过滤**（Example 2）：Players 与 Teams 按 team = t_name 连接，Teams 另有 `T.championships>6`。若 Players 上的两个过滤只留下少数文档，其球队只有 Warriors、Lakers、Celtics，QUEST 就给 Teams 加上 IN 过滤 `T.t_name IN [Warriors, Celtics, Lakers]`，并与 championships 过滤一起排序；若它选择率低、代价小，就会先于 championships 执行。

阅读者分析：本地 QUEST 查询集合若有 83 条，只能对应其源文件版本；论文主评测是 50 条，不能宣称 83 条都出自论文正文。

依据：[arXiv 2507.06515v2](https://arxiv.org/abs/2507.06515v2)，§2.1–2.4、Figure 1、Examples 1–2，PDF pp.2–4。
