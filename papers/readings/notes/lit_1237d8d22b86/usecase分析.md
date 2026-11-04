# 具体用例

原文 Fig.4（PDF p.5）给出的一个 IMDB 三表查询：

```
SELECT * FROM movie_companies, title, movie_info_idx
WHERE title.movie_id = movie_companies.movie_id AND title.movie_id = movie_info_idx.movie_id
  AND movie_companies.company_type_id = 1 AND title.product_year < 1904 AND title.product_year > 58;
```

提示中附上每列统计，如 `title (movie_id: [0,2527968,2527969], ...)`，并要求“think step by step”。模型输出 planning path：Step1 `[movie_companies, title, HashJoin]`，Step2 `[movie_info_idx, HashJoin (movie_companies title), HashJoin]`，最终答案为括号表示，再经 pg_hint_plan 转成 PostgreSQL 计划执行。

§7.8 的 DSB tpl040 案例（Fig.8，PDF p.12）：PostgreSQL 计划 4.49s，Oracle 2.26s，Qit 计划与 PostgreSQL 相似却耗时 106.08s（一个 NestLoopJoin 消耗 101.8s），Qdpo 计划 2.18s。作者用它说明 Qit 保证有效性、Qdpo 学到更高效的偏好。

该案例同时显示 Qit 单独使用可能产生严重退化的计划，表格平均值会掩盖这种尾部风险。（阅读者分析）
