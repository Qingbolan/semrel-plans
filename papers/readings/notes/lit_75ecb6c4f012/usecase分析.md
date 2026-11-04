# 具体用例

论文 Fig.2（p.4）展示执行提示，对应一条 IMDB 查询 `SELECT * FROM title t, movie_info_idx mi_idx WHERE … AND t.kind_id > 2 AND t.production_year > 2010 AND mi_idx.info_type_id = 99`。线性化计划包括：

- Hash Join，条件 mi_idx.movie_id = t.id；
- 对 movie_info_idx 的并行顺序扫描返回约 193.7K 行，同时“Rows Removed by Filter: 306.7K”；
- 对 title 的扫描带过滤 kind_id > 2 AND production_year > 2010，约 113.9K 行；
- 另列出代价、时间与 Hash 的 buckets/batches/内存。

模型把这段计划与原 SQL 一起读入，能看到大量后置过滤和无索引顺序扫描等瓶颈，从而生成更高效的改写（例如提前过滤或改变求值结构）。若改写通过等价验证且提速超过 1.5×，该（原查询，改写）对加入示范池，供后续相似查询检索（p.5）。

阅读者分析：Fig.2 只展示输入提示，论文没有给出该查询对应的具体改写结果与提速数字，因此这里只能说明输入形态。部署时需要在线执行 EXPLAIN；训练阶段使用的 EXPLAIN ANALYZE 会真正执行查询，代价随数据规模增长。

依据：[arXiv v2，9 页](https://arxiv.org/abs/2508.09023)，Fig.2，p.4；p.5。
