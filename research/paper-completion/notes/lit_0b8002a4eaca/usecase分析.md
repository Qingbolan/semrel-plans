# 具体用例

Figure 4（§3.2）给出 IMDB 上的例子。输入查询：

`SELECT * FROM title t, movie_companies mc WHERE t.id=mc.movie_id AND mc.company_id>11145 AND mc.company_type_id=1;`，原代价 0.994。

- 选到“好示例”（`title` 与 `cast_info` 的连接查询，结构相近）时，LLM 输出 `[FILTER_INTO_JOIN]`，改写后代价 0.692。
- 选到“坏示例”（`movie_keyword` 单表查询）时，LLM 输出空规则列表，不改写。

这说明同一个 LLM 的规则推荐随示例而变，构成了训练示例选择模型的动机。Figure 8（§6.6）还给出 TPC-H 案例：一条查询中 Learned Rewrite 未找到规则，LLM-R2 采用 `FILTER_INTO_JOIN` 等规则降低代价；另一条查询中 Learned Rewrite 反而把高效查询改成了较慢版本。

阅读者分析：示例中的“代价”是估计代价而非实测时间，与 §6 主结果使用的执行时间不是同一度量。

依据：[PVLDB 18(1) 53–65](https://www.vldb.org/pvldb/vol18/p53-yuan.pdf)，§3.2 Figure 4、§6.6 Figure 8，PDF pp.4、12。
