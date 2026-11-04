# usecase

论文的贯穿示例是 bookreview：问题为“哪些属于 ‘Literature & Fiction’ 类别的英文书平均评分恰为 5.0？”。books_info 表在 PostgreSQL 中，原有的 publishedDate、publisher、language 列已被删除，其值由 GPT-4o 改写进 details 文本列；review 表在 SQLite 中。两表的书籍标识分别为 book_id 和 purchase_id，值也加上了不同前缀（bid_ 与 bref_）。hints 提示二者可以模糊连接，并提示部分查询需要用到 details 或 categories。Figure 1 的轨迹中，代理先分别列出两库的表，在 PostgreSQL 中用 ILIKE 从 details 中过滤 English，在 SQLite 中按 bref 分组求平均评分，再用 pandas 把 bref_x 转为 bid_x 并完成连接，最后写出答案。

阅读者分析：从语义算子的角度看，这一例子相当于“文本属性抽取/语义过滤 + 跨库模糊连接 + 关系聚合”。论文 §4.4 显示代理几乎只用正则表达式做抽取，patents 中多样的日期写法无法被正则覆盖。把它改写成语义算子计划属于本项目的派生任务，原论文并未评测这种做法。

依据：[arXiv:2603.20576v3（2026-10-07），27 页](https://arxiv.org/abs/2603.20576)，§3.2–3.3、§4.4，Figure 1，PDF pp.2、4–6、8–9。
