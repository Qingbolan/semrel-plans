# 具体用例

**原文的动机查询**（§1 p.1）：

```sql
SELECT user_id, request, support_response,
  LLM('Did {support_response} address {request}?', support_response, request) AS success
FROM customer_tickets
WHERE support_response <> NULL
```

对客服工单表的每一行调用一次 LLM，判断客服回复是否解决了请求。

**评测中的具体查询：Movies 上的 LLM filter**（附录 A，p.12）：

```sql
SELECT t.movietitle FROM MOVIES
WHERE LLM('Given the following fields, determine whether the movie is suitable for kids.
           Answer ONLY with "Yes" or "No".',
          movieinfo, reviewcontent, reviewtype, movietitle) = 'Yes'
```

**为什么能省**：表中每行是一条影评，同一部电影有多条影评，而 movieinfo、movietitle 等字段对同一部电影完全相同，且互相函数依赖（附录 B）。默认顺序下，各行的差异出现在靠前的字段，或同一电影的行不相邻，前缀几乎不能复用。

**GGR 怎么做**（§4.2、§6.2）：按命中贡献选出某部电影的 movieinfo 值，把该电影的所有行排在一起，并把 movieinfo 及其函数依赖字段放在每行最前面；每行各不相同的 reviewcontent 放在后面。于是同一电影的第二行起，整段电影描述的 KV 状态都能复用，每行仍单独得到一个 Yes/No 答案。

**效果**（Table 2、Figure 3a，p.8）：Movies 的 filter 查询前缀命中率从 35% 升到 86%。Figure 3a 中 Movies 的柱标为 3.8× 和 2.5×，按图例顺序应分别是相对 No Cache 和相对 Cache (Original) 的加速（阅读者按图推断）。

正文对 Movies、Products、BIRD 的概括是比原顺序快 2.5–3 倍，命中率“提高 57–74%”；按 Table 2 计算，三者分别提高 51、56、75 个百分点（阅读者分析）。

依据：[MLSys 2025](https://proceedings.mlsys.org/paper_files/paper/2025/file/b5dc49f44db2fadc5c4d717c57f4a424-Paper-Conference.pdf)，§1、§4.2、§6.2、Table 2、Figure 3a、附录 A–B，PDF pp.1、5、8、12–13。
