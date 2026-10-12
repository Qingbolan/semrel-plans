# 逐查询逻辑计划

由 `python3 scripts/build.py` 生成；请编辑 data/ 下的规范化数据表。

[论文与数据来源](sources.md) · [范围与限制](scope.md) · [交互图册](../index.html)

## SemBench / movie / Q1 — 任意电影：取5条明显正面影评

源码重建逻辑计划；实质混合。[查询定义 / 实现](https://github.com/sembench/SemBench/blob/8c2cac89b21c6782239e8e5b03d326d0c029b655/files/movie/query/bigquery/Q1.sql)

- **论文**：[Lao et al. — SemBench: A Benchmark for Semantic Query Processing Engines](https://arxiv.org/abs/2511.01716v2)。arXiv v2, 2026-03-16；arXiv 注记 accepted VLDB 2026；定位：§4.1。论文提供 benchmark 背景；本图册依据链接的查询代码重建逻辑计划，不是论文原图或实际 EXPLAIN。
- **数据**：[Clapper / Rotten Tomatoes movies and reviews](https://www.kaggle.com/datasets/andrezaza/clapper-massive-rotten-tomatoes-movies-and-reviews)。原始数据版本未逐文件核验；定位：§4.1。影评与电影数据；当前使用子集、处理和 gold 以固定代码为准。

```text
LIMIT 5
└─ π reviewId
   └─ SEM_FILTER 明显正面
      └─ Scan reviews
```



## SemBench / movie / Q2 — Taken 3：取5条正面影评

源码重建逻辑计划；实质混合。[查询定义 / 实现](https://github.com/sembench/SemBench/blob/8c2cac89b21c6782239e8e5b03d326d0c029b655/files/movie/query/bigquery/Q2.sql)

- **论文**：[Lao et al. — SemBench: A Benchmark for Semantic Query Processing Engines](https://arxiv.org/abs/2511.01716v2)。arXiv v2, 2026-03-16；arXiv 注记 accepted VLDB 2026；定位：§4.1。论文提供 benchmark 背景；本图册依据链接的查询代码重建逻辑计划，不是论文原图或实际 EXPLAIN。
- **数据**：[Clapper / Rotten Tomatoes movies and reviews](https://www.kaggle.com/datasets/andrezaza/clapper-massive-rotten-tomatoes-movies-and-reviews)。原始数据版本未逐文件核验；定位：§4.1。影评与电影数据；当前使用子集、处理和 gold 以固定代码为准。

```text
LIMIT 5
└─ π reviewId
   └─ SEM_FILTER 明显正面
      └─ σ id = taken_3
         └─ Scan reviews
```



## SemBench / movie / Q3 — Taken 3：正面影评数

源码重建逻辑计划；实质混合。[查询定义 / 实现](https://github.com/sembench/SemBench/blob/8c2cac89b21c6782239e8e5b03d326d0c029b655/files/movie/query/bigquery/Q3.sql)

- **论文**：[Lao et al. — SemBench: A Benchmark for Semantic Query Processing Engines](https://arxiv.org/abs/2511.01716v2)。arXiv v2, 2026-03-16；arXiv 注记 accepted VLDB 2026；定位：§4.1。论文提供 benchmark 背景；本图册依据链接的查询代码重建逻辑计划，不是论文原图或实际 EXPLAIN。
- **数据**：[Clapper / Rotten Tomatoes movies and reviews](https://www.kaggle.com/datasets/andrezaza/clapper-massive-rotten-tomatoes-movies-and-reviews)。原始数据版本未逐文件核验；定位：§4.1。影评与电影数据；当前使用子集、处理和 gold 以固定代码为准。

```text
γ COUNT(*) → positive_review_cnt
└─ SEM_FILTER 明显正面
   └─ σ id = taken_3
      └─ Scan reviews
```



## SemBench / movie / Q4 — Taken 3：正面影评占比

源码重建逻辑计划；实质混合。[查询定义 / 实现](https://github.com/sembench/SemBench/blob/8c2cac89b21c6782239e8e5b03d326d0c029b655/files/movie/query/bigquery/Q4.sql)

- **论文**：[Lao et al. — SemBench: A Benchmark for Semantic Query Processing Engines](https://arxiv.org/abs/2511.01716v2)。arXiv v2, 2026-03-16；arXiv 注记 accepted VLDB 2026；定位：§4.1。论文提供 benchmark 背景；本图册依据链接的查询代码重建逻辑计划，不是论文原图或实际 EXPLAIN。
- **数据**：[Clapper / Rotten Tomatoes movies and reviews](https://www.kaggle.com/datasets/andrezaza/clapper-massive-rotten-tomatoes-movies-and-reviews)。原始数据版本未逐文件核验；定位：§4.1。影评与电影数据；当前使用子集、处理和 gold 以固定代码为准。

```text
γ SUM(positive ? 1 : 0) / COUNT(*)
└─ SEM_MAP positive := 明显正面
   └─ σ id = taken_3
      └─ Scan reviews
```

分母必须保留全部影评，不能先过滤只保留正面。

## SemBench / movie / Q5 — 10对蚁人影评：同为正面或同为负面

源码重建逻辑计划；实质混合。[查询定义 / 实现](https://github.com/sembench/SemBench/blob/8c2cac89b21c6782239e8e5b03d326d0c029b655/files/movie/query/bigquery/Q5.sql)

- **论文**：[Lao et al. — SemBench: A Benchmark for Semantic Query Processing Engines](https://arxiv.org/abs/2511.01716v2)。arXiv v2, 2026-03-16；arXiv 注记 accepted VLDB 2026；定位：§4.1。论文提供 benchmark 背景；本图册依据链接的查询代码重建逻辑计划，不是论文原图或实际 EXPLAIN。
- **数据**：[Clapper / Rotten Tomatoes movies and reviews](https://www.kaggle.com/datasets/andrezaza/clapper-massive-rotten-tomatoes-movies-and-reviews)。原始数据版本未逐文件核验；定位：§4.1。影评与电影数据；当前使用子集、处理和 gold 以固定代码为准。

```text
LIMIT 10
└─ π r1.id, r1.reviewId, r2.reviewId
   └─ SEM_FILTER 同为正面或同为负面
      └─ ⋈ r1.id=r2.id AND r1.reviewId≠r2.reviewId
         ├─ σ r1.id = ant_man_and_the_wasp_quantumania
         │  └─ Scan reviews r1
         └─ Scan reviews r2
```

二元语义谓词也可表示为受结构化键约束的 SEM_JOIN；保留有向配对和原 SQL 的重复语义。

## SemBench / movie / Q6 — 10对蚁人影评：一正一负

源码重建逻辑计划；实质混合。[查询定义 / 实现](https://github.com/sembench/SemBench/blob/8c2cac89b21c6782239e8e5b03d326d0c029b655/files/movie/query/bigquery/Q6.sql)

- **论文**：[Lao et al. — SemBench: A Benchmark for Semantic Query Processing Engines](https://arxiv.org/abs/2511.01716v2)。arXiv v2, 2026-03-16；arXiv 注记 accepted VLDB 2026；定位：§4.1。论文提供 benchmark 背景；本图册依据链接的查询代码重建逻辑计划，不是论文原图或实际 EXPLAIN。
- **数据**：[Clapper / Rotten Tomatoes movies and reviews](https://www.kaggle.com/datasets/andrezaza/clapper-massive-rotten-tomatoes-movies-and-reviews)。原始数据版本未逐文件核验；定位：§4.1。影评与电影数据；当前使用子集、处理和 gold 以固定代码为准。

```text
LIMIT 10
└─ π r1.id, r1.reviewId, r2.reviewId
   └─ SEM_FILTER 一正一负
      └─ ⋈ r1.id=r2.id AND r1.reviewId≠r2.reviewId
         ├─ σ r1.id = ant_man_and_the_wasp_quantumania
         │  └─ Scan reviews r1
         └─ Scan reviews r2
```

二元语义谓词也可表示为受结构化键约束的 SEM_JOIN；保留有向配对和原 SQL 的重复语义。

## SemBench / movie / Q7 — 全部蚁人影评：一正一负

源码重建逻辑计划；实质混合。[查询定义 / 实现](https://github.com/sembench/SemBench/blob/8c2cac89b21c6782239e8e5b03d326d0c029b655/files/movie/query/bigquery/Q7.sql)

- **论文**：[Lao et al. — SemBench: A Benchmark for Semantic Query Processing Engines](https://arxiv.org/abs/2511.01716v2)。arXiv v2, 2026-03-16；arXiv 注记 accepted VLDB 2026；定位：§4.1。论文提供 benchmark 背景；本图册依据链接的查询代码重建逻辑计划，不是论文原图或实际 EXPLAIN。
- **数据**：[Clapper / Rotten Tomatoes movies and reviews](https://www.kaggle.com/datasets/andrezaza/clapper-massive-rotten-tomatoes-movies-and-reviews)。原始数据版本未逐文件核验；定位：§4.1。影评与电影数据；当前使用子集、处理和 gold 以固定代码为准。

```text
π r1.id, r1.reviewId, r2.reviewId
└─ SEM_FILTER 一正一负
   └─ ⋈ r1.id=r2.id AND r1.reviewId≠r2.reviewId
      ├─ σ r1.id = ant_man_and_the_wasp_quantumania
      │  └─ Scan reviews r1
      └─ Scan reviews r2
```

二元语义谓词也可表示为受结构化键约束的 SEM_JOIN；保留有向配对和原 SQL 的重复语义。

## SemBench / movie / Q8 — Taken 3：按正面/负面统计影评

源码重建逻辑计划；实质混合。[查询定义 / 实现](https://github.com/sembench/SemBench/blob/8c2cac89b21c6782239e8e5b03d326d0c029b655/files/movie/query/bigquery/Q8.sql)

- **论文**：[Lao et al. — SemBench: A Benchmark for Semantic Query Processing Engines](https://arxiv.org/abs/2511.01716v2)。arXiv v2, 2026-03-16；arXiv 注记 accepted VLDB 2026；定位：§4.1。论文提供 benchmark 背景；本图册依据链接的查询代码重建逻辑计划，不是论文原图或实际 EXPLAIN。
- **数据**：[Clapper / Rotten Tomatoes movies and reviews](https://www.kaggle.com/datasets/andrezaza/clapper-massive-rotten-tomatoes-movies-and-reviews)。原始数据版本未逐文件核验；定位：§4.1。影评与电影数据；当前使用子集、处理和 gold 以固定代码为准。

```text
γ GROUP BY sentiment; COUNT(*)
└─ SEM_MAP AI.IF 为真→POSITIVE，否则→NEGATIVE
   └─ σ id = taken_3
      └─ Scan reviews
```

这是源码二值映射；并不等于独立识别全部负面/中性。

## SemBench / movie / Q9 — 蚁人影评：逐条给1–5分

源码重建逻辑计划；实质混合。[查询定义 / 实现](https://github.com/sembench/SemBench/blob/8c2cac89b21c6782239e8e5b03d326d0c029b655/files/movie/query/bigquery/Q9.sql)

- **论文**：[Lao et al. — SemBench: A Benchmark for Semantic Query Processing Engines](https://arxiv.org/abs/2511.01716v2)。arXiv v2, 2026-03-16；arXiv 注记 accepted VLDB 2026；定位：§4.1。论文提供 benchmark 背景；本图册依据链接的查询代码重建逻辑计划，不是论文原图或实际 EXPLAIN。
- **数据**：[Clapper / Rotten Tomatoes movies and reviews](https://www.kaggle.com/datasets/andrezaza/clapper-massive-rotten-tomatoes-movies-and-reviews)。原始数据版本未逐文件核验；定位：§4.1。影评与电影数据；当前使用子集、处理和 gold 以固定代码为准。

```text
π reviewId, reviewScore
└─ SEM_MAP reviewScore := 情绪评分1–5
   └─ σ id = ant_man_and_the_wasp_quantumania
      └─ Scan reviews
```



## SemBench / movie / Q10 — 逐电影计算影评平均分

源码重建逻辑计划；实质混合。[查询定义 / 实现](https://github.com/sembench/SemBench/blob/8c2cac89b21c6782239e8e5b03d326d0c029b655/files/movie/query/bigquery/Q10.sql)

- **论文**：[Lao et al. — SemBench: A Benchmark for Semantic Query Processing Engines](https://arxiv.org/abs/2511.01716v2)。arXiv v2, 2026-03-16；arXiv 注记 accepted VLDB 2026；定位：§4.1。论文提供 benchmark 背景；本图册依据链接的查询代码重建逻辑计划，不是论文原图或实际 EXPLAIN。
- **数据**：[Clapper / Rotten Tomatoes movies and reviews](https://www.kaggle.com/datasets/andrezaza/clapper-massive-rotten-tomatoes-movies-and-reviews)。原始数据版本未逐文件核验；定位：§4.1。影评与电影数据；当前使用子集、处理和 gold 以固定代码为准。

```text
γ GROUP BY id; AVG(score)
└─ SEM_MAP score := 情绪评分1–5
   └─ Scan reviews
```

自然语言用 rank；此 SQL 仅分组求均值，没有 ORDER BY，图不补排序。

## SemBench / animals / Q1 — 统计斑马图片数量

源码重建逻辑计划；实质混合。[查询定义 / 实现](https://github.com/sembench/SemBench/blob/8c2cac89b21c6782239e8e5b03d326d0c029b655/files/animals/query/bigquery/Q1.sql)

- **论文**：[Lao et al. — SemBench: A Benchmark for Semantic Query Processing Engines](https://arxiv.org/abs/2511.01716v2)。arXiv v2, 2026-03-16；arXiv 注记 accepted VLDB 2026；定位：§4.2。论文提供 benchmark 背景；本图册依据链接的查询代码重建逻辑计划，不是论文原图或实际 EXPLAIN。
- **数据**：[DSAIL-Porini images](https://www.kaggle.com/datasets/hypnotu/dsail-porini)。原始数据版本未逐文件核验；定位：§4.2。真实图像/音频加随机生成的 city、stationID；不是真实站点联合观测。
- **数据**：[Animal voice recordings](https://www.kaggle.com/datasets/rushibalajiputthewad/sound-classification-of-animal-voice)。原始数据版本未逐文件核验；定位：§4.2。真实图像/音频加随机生成的 city、stationID；不是真实站点联合观测。

```text
γ COUNT(*)
└─ SEM_FILTER 图像含斑马
   └─ Scan ImageData
```



## SemBench / animals / Q2 — 统计大象录音数量

源码重建逻辑计划；实质混合。[查询定义 / 实现](https://github.com/sembench/SemBench/blob/8c2cac89b21c6782239e8e5b03d326d0c029b655/files/animals/query/bigquery/Q2.sql)

- **论文**：[Lao et al. — SemBench: A Benchmark for Semantic Query Processing Engines](https://arxiv.org/abs/2511.01716v2)。arXiv v2, 2026-03-16；arXiv 注记 accepted VLDB 2026；定位：§4.2。论文提供 benchmark 背景；本图册依据链接的查询代码重建逻辑计划，不是论文原图或实际 EXPLAIN。
- **数据**：[DSAIL-Porini images](https://www.kaggle.com/datasets/hypnotu/dsail-porini)。原始数据版本未逐文件核验；定位：§4.2。真实图像/音频加随机生成的 city、stationID；不是真实站点联合观测。
- **数据**：[Animal voice recordings](https://www.kaggle.com/datasets/rushibalajiputthewad/sound-classification-of-animal-voice)。原始数据版本未逐文件核验；定位：§4.2。真实图像/音频加随机生成的 city、stationID；不是真实站点联合观测。

```text
γ COUNT(*)
└─ SEM_FILTER 音频含大象
   └─ Scan AudioData
```



## SemBench / animals / Q3 — 斑马图片最多的城市

源码重建逻辑计划；实质混合。[查询定义 / 实现](https://github.com/sembench/SemBench/blob/8c2cac89b21c6782239e8e5b03d326d0c029b655/files/animals/query/bigquery/Q3.sql)

- **论文**：[Lao et al. — SemBench: A Benchmark for Semantic Query Processing Engines](https://arxiv.org/abs/2511.01716v2)。arXiv v2, 2026-03-16；arXiv 注记 accepted VLDB 2026；定位：§4.2。论文提供 benchmark 背景；本图册依据链接的查询代码重建逻辑计划，不是论文原图或实际 EXPLAIN。
- **数据**：[DSAIL-Porini images](https://www.kaggle.com/datasets/hypnotu/dsail-porini)。原始数据版本未逐文件核验；定位：§4.2。真实图像/音频加随机生成的 city、stationID；不是真实站点联合观测。
- **数据**：[Animal voice recordings](https://www.kaggle.com/datasets/rushibalajiputthewad/sound-classification-of-animal-voice)。原始数据版本未逐文件核验；定位：§4.2。真实图像/音频加随机生成的 city、stationID；不是真实站点联合观测。

```text
π city
└─ LIMIT 1
   └─ τ count DESC
      └─ γ GROUP BY city; COUNT(*) → count
         └─ SEM_FILTER 图像含斑马
            └─ Scan ImageData
```



## SemBench / animals / Q4 — 大象录音最多的城市

源码重建逻辑计划；实质混合。[查询定义 / 实现](https://github.com/sembench/SemBench/blob/8c2cac89b21c6782239e8e5b03d326d0c029b655/files/animals/query/bigquery/Q4.sql)

- **论文**：[Lao et al. — SemBench: A Benchmark for Semantic Query Processing Engines](https://arxiv.org/abs/2511.01716v2)。arXiv v2, 2026-03-16；arXiv 注记 accepted VLDB 2026；定位：§4.2。论文提供 benchmark 背景；本图册依据链接的查询代码重建逻辑计划，不是论文原图或实际 EXPLAIN。
- **数据**：[DSAIL-Porini images](https://www.kaggle.com/datasets/hypnotu/dsail-porini)。原始数据版本未逐文件核验；定位：§4.2。真实图像/音频加随机生成的 city、stationID；不是真实站点联合观测。
- **数据**：[Animal voice recordings](https://www.kaggle.com/datasets/rushibalajiputthewad/sound-classification-of-animal-voice)。原始数据版本未逐文件核验；定位：§4.2。真实图像/音频加随机生成的 city、stationID；不是真实站点联合观测。

```text
π city
└─ LIMIT 1
   └─ τ count DESC
      └─ γ GROUP BY city; COUNT(*) → count
         └─ SEM_FILTER 音频含大象
            └─ Scan AudioData
```



## SemBench / animals / Q5 — 有大象图片或录音的城市

源码重建逻辑计划；实质混合。[查询定义 / 实现](https://github.com/sembench/SemBench/blob/8c2cac89b21c6782239e8e5b03d326d0c029b655/files/animals/query/bigquery/Q5.sql)

- **论文**：[Lao et al. — SemBench: A Benchmark for Semantic Query Processing Engines](https://arxiv.org/abs/2511.01716v2)。arXiv v2, 2026-03-16；arXiv 注记 accepted VLDB 2026；定位：§4.2。论文提供 benchmark 背景；本图册依据链接的查询代码重建逻辑计划，不是论文原图或实际 EXPLAIN。
- **数据**：[DSAIL-Porini images](https://www.kaggle.com/datasets/hypnotu/dsail-porini)。原始数据版本未逐文件核验；定位：§4.2。真实图像/音频加随机生成的 city、stationID；不是真实站点联合观测。
- **数据**：[Animal voice recordings](https://www.kaggle.com/datasets/rushibalajiputthewad/sound-classification-of-animal-voice)。原始数据版本未逐文件核验；定位：§4.2。真实图像/音频加随机生成的 city、stationID；不是真实站点联合观测。

```text
δ DISTINCT
└─ UNION ALL
   ├─ π city
   │  └─ SEM_FILTER 大象存在
   │     └─ Scan ImageData
   └─ π city
      └─ SEM_FILTER 大象存在
         └─ Scan AudioData
```



## SemBench / animals / Q6 — 有猴子图片但没有猴子录音的城市

源码重建逻辑计划；实质混合。[查询定义 / 实现](https://github.com/sembench/SemBench/blob/8c2cac89b21c6782239e8e5b03d326d0c029b655/files/animals/query/bigquery/Q6.sql)

- **论文**：[Lao et al. — SemBench: A Benchmark for Semantic Query Processing Engines](https://arxiv.org/abs/2511.01716v2)。arXiv v2, 2026-03-16；arXiv 注记 accepted VLDB 2026；定位：§4.2。论文提供 benchmark 背景；本图册依据链接的查询代码重建逻辑计划，不是论文原图或实际 EXPLAIN。
- **数据**：[DSAIL-Porini images](https://www.kaggle.com/datasets/hypnotu/dsail-porini)。原始数据版本未逐文件核验；定位：§4.2。真实图像/音频加随机生成的 city、stationID；不是真实站点联合观测。
- **数据**：[Animal voice recordings](https://www.kaggle.com/datasets/rushibalajiputthewad/sound-classification-of-animal-voice)。原始数据版本未逐文件核验；定位：§4.2。真实图像/音频加随机生成的 city、stationID；不是真实站点联合观测。

```text
δ DISTINCT
└─ ANTI JOIN on city
   ├─ π city
   │  └─ SEM_FILTER 猴子存在
   │     └─ Scan ImageData
   └─ π city
      └─ SEM_FILTER 猴子存在
         └─ Scan AudioData
```



## SemBench / animals / Q7 — 同时有斑马和黑斑羚图片的城市

源码重建逻辑计划；实质混合。[查询定义 / 实现](https://github.com/sembench/SemBench/blob/8c2cac89b21c6782239e8e5b03d326d0c029b655/files/animals/query/bigquery/Q7.sql)

- **论文**：[Lao et al. — SemBench: A Benchmark for Semantic Query Processing Engines](https://arxiv.org/abs/2511.01716v2)。arXiv v2, 2026-03-16；arXiv 注记 accepted VLDB 2026；定位：§4.2。论文提供 benchmark 背景；本图册依据链接的查询代码重建逻辑计划，不是论文原图或实际 EXPLAIN。
- **数据**：[DSAIL-Porini images](https://www.kaggle.com/datasets/hypnotu/dsail-porini)。原始数据版本未逐文件核验；定位：§4.2。真实图像/音频加随机生成的 city、stationID；不是真实站点联合观测。
- **数据**：[Animal voice recordings](https://www.kaggle.com/datasets/rushibalajiputthewad/sound-classification-of-animal-voice)。原始数据版本未逐文件核验；定位：§4.2。真实图像/音频加随机生成的 city、stationID；不是真实站点联合观测。

```text
INTERSECT DISTINCT
├─ π city
│  └─ SEM_FILTER 斑马存在
│     └─ Scan ImageData
└─ π city
   └─ SEM_FILTER 黑斑羚存在
      └─ Scan ImageData
```



## SemBench / animals / Q8 — 大象和猴子均有至少一种模态证据的城市

源码重建逻辑计划；实质混合。[查询定义 / 实现](https://github.com/sembench/SemBench/blob/8c2cac89b21c6782239e8e5b03d326d0c029b655/files/animals/query/bigquery/Q8.sql)

- **论文**：[Lao et al. — SemBench: A Benchmark for Semantic Query Processing Engines](https://arxiv.org/abs/2511.01716v2)。arXiv v2, 2026-03-16；arXiv 注记 accepted VLDB 2026；定位：§4.2。论文提供 benchmark 背景；本图册依据链接的查询代码重建逻辑计划，不是论文原图或实际 EXPLAIN。
- **数据**：[DSAIL-Porini images](https://www.kaggle.com/datasets/hypnotu/dsail-porini)。原始数据版本未逐文件核验；定位：§4.2。真实图像/音频加随机生成的 city、stationID；不是真实站点联合观测。
- **数据**：[Animal voice recordings](https://www.kaggle.com/datasets/rushibalajiputthewad/sound-classification-of-animal-voice)。原始数据版本未逐文件核验；定位：§4.2。真实图像/音频加随机生成的 city、stationID；不是真实站点联合观测。

```text
INTERSECT DISTINCT
├─ δ DISTINCT
│  └─ UNION ALL
│     ├─ π city
│     │  └─ SEM_FILTER 大象存在
│     │     └─ Scan ImageData
│     └─ π city
│        └─ SEM_FILTER 大象存在
│           └─ Scan AudioData
└─ δ DISTINCT
   └─ UNION ALL
      ├─ π city
      │  └─ SEM_FILTER 猴子存在
      │     └─ Scan ImageData
      └─ π city
         └─ SEM_FILTER 猴子存在
            └─ Scan AudioData
```



## SemBench / animals / Q9 — 同时有猴子图片和录音的城市

源码重建逻辑计划；实质混合。[查询定义 / 实现](https://github.com/sembench/SemBench/blob/8c2cac89b21c6782239e8e5b03d326d0c029b655/files/animals/query/bigquery/Q9.sql)

- **论文**：[Lao et al. — SemBench: A Benchmark for Semantic Query Processing Engines](https://arxiv.org/abs/2511.01716v2)。arXiv v2, 2026-03-16；arXiv 注记 accepted VLDB 2026；定位：§4.2。论文提供 benchmark 背景；本图册依据链接的查询代码重建逻辑计划，不是论文原图或实际 EXPLAIN。
- **数据**：[DSAIL-Porini images](https://www.kaggle.com/datasets/hypnotu/dsail-porini)。原始数据版本未逐文件核验；定位：§4.2。真实图像/音频加随机生成的 city、stationID；不是真实站点联合观测。
- **数据**：[Animal voice recordings](https://www.kaggle.com/datasets/rushibalajiputthewad/sound-classification-of-animal-voice)。原始数据版本未逐文件核验；定位：§4.2。真实图像/音频加随机生成的 city、stationID；不是真实站点联合观测。

```text
INTERSECT DISTINCT
├─ π city
│  └─ SEM_FILTER 猴子存在
│     └─ Scan ImageData
└─ π city
   └─ SEM_FILTER 猴子存在
      └─ Scan AudioData
```



## SemBench / animals / Q10 — 斑马图片最多的城市—站点

源码重建逻辑计划；实质混合。[查询定义 / 实现](https://github.com/sembench/SemBench/blob/8c2cac89b21c6782239e8e5b03d326d0c029b655/files/animals/query/bigquery/Q10.sql)

- **论文**：[Lao et al. — SemBench: A Benchmark for Semantic Query Processing Engines](https://arxiv.org/abs/2511.01716v2)。arXiv v2, 2026-03-16；arXiv 注记 accepted VLDB 2026；定位：§4.2。论文提供 benchmark 背景；本图册依据链接的查询代码重建逻辑计划，不是论文原图或实际 EXPLAIN。
- **数据**：[DSAIL-Porini images](https://www.kaggle.com/datasets/hypnotu/dsail-porini)。原始数据版本未逐文件核验；定位：§4.2。真实图像/音频加随机生成的 city、stationID；不是真实站点联合观测。
- **数据**：[Animal voice recordings](https://www.kaggle.com/datasets/rushibalajiputthewad/sound-classification-of-animal-voice)。原始数据版本未逐文件核验；定位：§4.2。真实图像/音频加随机生成的 city、stationID；不是真实站点联合观测。

```text
π city, stationID
└─ LIMIT 1
   └─ τ count DESC
      └─ γ GROUP BY city, stationID; COUNT(*) → count
         └─ SEM_FILTER 图像含斑马
            └─ Scan ImageData
```



## SemBench / cars / Q1 — 找出投诉中提到发生碰撞的车

源码重建逻辑计划；实质混合。[查询定义 / 实现](https://github.com/sembench/SemBench/blob/8c2cac89b21c6782239e8e5b03d326d0c029b655/files/cars/query/bigquery/Q1.sql)

- **论文**：[Lao et al. — SemBench: A Benchmark for Semantic Query Processing Engines](https://arxiv.org/abs/2511.01716v2)。arXiv v2, 2026-03-16；arXiv 注记 accepted VLDB 2026；定位：§4.4。论文提供 benchmark 背景；本图册依据链接的查询代码重建逻辑计划，不是论文原图或实际 EXPLAIN。
- **数据**：[VehiDE vehicle damage images](https://www.kaggle.com/ds/3685629)。原始数据版本未逐文件核验；定位：§4.4。真实多模态素材与合成车辆属性/关联组合；不是真实车辆的联合理赔记录。
- **数据**：[Stanford Cars](https://www.kaggle.com/datasets/jutrera/stanford-car-dataset-by-classes-folder)。原始数据版本未逐文件核验；定位：§4.4。真实多模态素材与合成车辆属性/关联组合；不是真实车辆的联合理赔记录。
- **数据**：[Car diagnostics audio](https://www.kaggle.com/datasets/malakragaie/car-diagnostics-dataset)。原始数据版本未逐文件核验；定位：§4.4。真实多模态素材与合成车辆属性/关联组合；不是真实车辆的联合理赔记录。
- **数据**：[NHTSA complaints](https://www.kaggle.com/datasets/alshival/nhtsa-complaints)。原始数据版本未逐文件核验；定位：§4.4。真实多模态素材与合成车辆属性/关联组合；不是真实车辆的联合理赔记录。

```text
δ DISTINCT
└─ π car_id
   └─ SEM_FILTER 投诉表明碰撞/事故
      └─ Scan complaints
```



## SemBench / cars / Q2 — 找出录音表明电池耗尽的电动车

源码重建逻辑计划；实质混合。[查询定义 / 实现](https://github.com/sembench/SemBench/blob/8c2cac89b21c6782239e8e5b03d326d0c029b655/files/cars/query/bigquery/Q2.sql)

- **论文**：[Lao et al. — SemBench: A Benchmark for Semantic Query Processing Engines](https://arxiv.org/abs/2511.01716v2)。arXiv v2, 2026-03-16；arXiv 注记 accepted VLDB 2026；定位：§4.4。论文提供 benchmark 背景；本图册依据链接的查询代码重建逻辑计划，不是论文原图或实际 EXPLAIN。
- **数据**：[VehiDE vehicle damage images](https://www.kaggle.com/ds/3685629)。原始数据版本未逐文件核验；定位：§4.4。真实多模态素材与合成车辆属性/关联组合；不是真实车辆的联合理赔记录。
- **数据**：[Stanford Cars](https://www.kaggle.com/datasets/jutrera/stanford-car-dataset-by-classes-folder)。原始数据版本未逐文件核验；定位：§4.4。真实多模态素材与合成车辆属性/关联组合；不是真实车辆的联合理赔记录。
- **数据**：[Car diagnostics audio](https://www.kaggle.com/datasets/malakragaie/car-diagnostics-dataset)。原始数据版本未逐文件核验；定位：§4.4。真实多模态素材与合成车辆属性/关联组合；不是真实车辆的联合理赔记录。
- **数据**：[NHTSA complaints](https://www.kaggle.com/datasets/alshival/nhtsa-complaints)。原始数据版本未逐文件核验；定位：§4.4。真实多模态素材与合成车辆属性/关联组合；不是真实车辆的联合理赔记录。

```text
δ DISTINCT
└─ π car_id
   └─ SEM_FILTER 录音表明 dead battery
      └─ ⋈ car_id
         ├─ σ fuel_type = Electric
         │  └─ Scan cars
         └─ Scan audio_mm 录音
```



## SemBench / cars / Q3 — 找10辆图片显示无损伤的手动挡车

源码重建逻辑计划；实质混合。[查询定义 / 实现](https://github.com/sembench/SemBench/blob/8c2cac89b21c6782239e8e5b03d326d0c029b655/files/cars/query/bigquery/Q3.sql)

- **论文**：[Lao et al. — SemBench: A Benchmark for Semantic Query Processing Engines](https://arxiv.org/abs/2511.01716v2)。arXiv v2, 2026-03-16；arXiv 注记 accepted VLDB 2026；定位：§4.4。论文提供 benchmark 背景；本图册依据链接的查询代码重建逻辑计划，不是论文原图或实际 EXPLAIN。
- **数据**：[VehiDE vehicle damage images](https://www.kaggle.com/ds/3685629)。原始数据版本未逐文件核验；定位：§4.4。真实多模态素材与合成车辆属性/关联组合；不是真实车辆的联合理赔记录。
- **数据**：[Stanford Cars](https://www.kaggle.com/datasets/jutrera/stanford-car-dataset-by-classes-folder)。原始数据版本未逐文件核验；定位：§4.4。真实多模态素材与合成车辆属性/关联组合；不是真实车辆的联合理赔记录。
- **数据**：[Car diagnostics audio](https://www.kaggle.com/datasets/malakragaie/car-diagnostics-dataset)。原始数据版本未逐文件核验；定位：§4.4。真实多模态素材与合成车辆属性/关联组合；不是真实车辆的联合理赔记录。
- **数据**：[NHTSA complaints](https://www.kaggle.com/datasets/alshival/nhtsa-complaints)。原始数据版本未逐文件核验；定位：§4.4。真实多模态素材与合成车辆属性/关联组合；不是真实车辆的联合理赔记录。

```text
LIMIT 10
└─ π vin
   └─ SEM_FILTER 图片显示无损伤
      └─ ⋈ car_id
         ├─ σ transmission = Manual
         │  └─ Scan cars
         └─ Scan car_mm 图片
```



## SemBench / cars / Q4 — 发动机有问题车辆的平均年龄

源码重建逻辑计划；实质混合。[查询定义 / 实现](https://github.com/sembench/SemBench/blob/8c2cac89b21c6782239e8e5b03d326d0c029b655/files/cars/query/bigquery/Q4.sql)

- **论文**：[Lao et al. — SemBench: A Benchmark for Semantic Query Processing Engines](https://arxiv.org/abs/2511.01716v2)。arXiv v2, 2026-03-16；arXiv 注记 accepted VLDB 2026；定位：§4.4。论文提供 benchmark 背景；本图册依据链接的查询代码重建逻辑计划，不是论文原图或实际 EXPLAIN。
- **数据**：[VehiDE vehicle damage images](https://www.kaggle.com/ds/3685629)。原始数据版本未逐文件核验；定位：§4.4。真实多模态素材与合成车辆属性/关联组合；不是真实车辆的联合理赔记录。
- **数据**：[Stanford Cars](https://www.kaggle.com/datasets/jutrera/stanford-car-dataset-by-classes-folder)。原始数据版本未逐文件核验；定位：§4.4。真实多模态素材与合成车辆属性/关联组合；不是真实车辆的联合理赔记录。
- **数据**：[Car diagnostics audio](https://www.kaggle.com/datasets/malakragaie/car-diagnostics-dataset)。原始数据版本未逐文件核验；定位：§4.4。真实多模态素材与合成车辆属性/关联组合；不是真实车辆的联合理赔记录。
- **数据**：[NHTSA complaints](https://www.kaggle.com/datasets/alshival/nhtsa-complaints)。原始数据版本未逐文件核验；定位：§4.4。真实多模态素材与合成车辆属性/关联组合；不是真实车辆的联合理赔记录。

```text
π 2026 - avg_year
└─ γ AVG(year) → avg_year
   └─ SEM_FILTER 投诉涉及发动机问题
      └─ ⋈ car_id
         ├─ Scan cars
         └─ Scan complaints
```

依源码按连接后的投诉行求平均；多投诉车辆可能重复计权，不擅自改成去重车辆均值。

## SemBench / cars / Q5 — 图像与录音均表明损伤的自动挡车数量

源码重建逻辑计划；实质混合。[查询定义 / 实现](https://github.com/sembench/SemBench/blob/8c2cac89b21c6782239e8e5b03d326d0c029b655/files/cars/query/bigquery/Q5.sql)

- **论文**：[Lao et al. — SemBench: A Benchmark for Semantic Query Processing Engines](https://arxiv.org/abs/2511.01716v2)。arXiv v2, 2026-03-16；arXiv 注记 accepted VLDB 2026；定位：§4.4。论文提供 benchmark 背景；本图册依据链接的查询代码重建逻辑计划，不是论文原图或实际 EXPLAIN。
- **数据**：[VehiDE vehicle damage images](https://www.kaggle.com/ds/3685629)。原始数据版本未逐文件核验；定位：§4.4。真实多模态素材与合成车辆属性/关联组合；不是真实车辆的联合理赔记录。
- **数据**：[Stanford Cars](https://www.kaggle.com/datasets/jutrera/stanford-car-dataset-by-classes-folder)。原始数据版本未逐文件核验；定位：§4.4。真实多模态素材与合成车辆属性/关联组合；不是真实车辆的联合理赔记录。
- **数据**：[Car diagnostics audio](https://www.kaggle.com/datasets/malakragaie/car-diagnostics-dataset)。原始数据版本未逐文件核验；定位：§4.4。真实多模态素材与合成车辆属性/关联组合；不是真实车辆的联合理赔记录。
- **数据**：[NHTSA complaints](https://www.kaggle.com/datasets/alshival/nhtsa-complaints)。原始数据版本未逐文件核验；定位：§4.4。真实多模态素材与合成车辆属性/关联组合；不是真实车辆的联合理赔记录。

```text
γ GROUP BY transmission; COUNT(*)
└─ δ DISTINCT
   └─ π car_id, transmission
      └─ SEM_FILTER 图片损伤 AND 录音损伤
         └─ ⋈ car_id
            ├─ ⋈ car_id
            │  ├─ σ transmission = Automatic
            │  │  └─ Scan cars
            │  └─ Scan audio_mm 录音
            └─ Scan car_mm 图片
```



## SemBench / cars / Q6 — 找跨模态损伤判断不一致的车

源码重建逻辑计划；实质混合。[查询定义 / 实现](https://github.com/sembench/SemBench/blob/8c2cac89b21c6782239e8e5b03d326d0c029b655/files/cars/query/bigquery/Q6.sql)

- **论文**：[Lao et al. — SemBench: A Benchmark for Semantic Query Processing Engines](https://arxiv.org/abs/2511.01716v2)。arXiv v2, 2026-03-16；arXiv 注记 accepted VLDB 2026；定位：§4.4。论文提供 benchmark 背景；本图册依据链接的查询代码重建逻辑计划，不是论文原图或实际 EXPLAIN。
- **数据**：[VehiDE vehicle damage images](https://www.kaggle.com/ds/3685629)。原始数据版本未逐文件核验；定位：§4.4。真实多模态素材与合成车辆属性/关联组合；不是真实车辆的联合理赔记录。
- **数据**：[Stanford Cars](https://www.kaggle.com/datasets/jutrera/stanford-car-dataset-by-classes-folder)。原始数据版本未逐文件核验；定位：§4.4。真实多模态素材与合成车辆属性/关联组合；不是真实车辆的联合理赔记录。
- **数据**：[Car diagnostics audio](https://www.kaggle.com/datasets/malakragaie/car-diagnostics-dataset)。原始数据版本未逐文件核验；定位：§4.4。真实多模态素材与合成车辆属性/关联组合；不是真实车辆的联合理赔记录。
- **数据**：[NHTSA complaints](https://www.kaggle.com/datasets/alshival/nhtsa-complaints)。原始数据版本未逐文件核验；定位：§4.4。真实多模态素材与合成车辆属性/关联组合；不是真实车辆的联合理赔记录。

```text
σ 至少一个标志=1 AND 至少一个标志=0
└─ 构造各模态 1/0/NULL 标志
   └─ LEFT JOIN sick_* on car_id
      ├─ CTE two_more_modalities
      │  └─ σ 至少两种模态输入存在
      │     └─ LEFT JOIN ×3 on car_id
      │        ├─ Scan cars
      │        ├─ Scan car_mm 图片
      │        ├─ Scan audio_mm 录音
      │        └─ Scan complaints
      ├─ π car_id
      │  └─ SEM_FILTER 录音表明损伤
      │     └─ σ 对应模态 ID 非空
      │        └─ CTE REF two_more_modalities
      ├─ π car_id
      │  └─ SEM_FILTER 图片表明损伤
      │     └─ σ 对应模态 ID 非空
      │        └─ CTE REF two_more_modalities
      └─ π car_id
         └─ SEM_FILTER 投诉表明起火
            └─ σ 对应模态 ID 非空
               └─ CTE REF two_more_modalities
```

图中 CTE REF 引用同一中间关系，是 DAG 的树形展开。SQL 按 car_id 回连阳性集合；多条模态记录可能放大行数。源码还有括号可执行性风险，本次不修复、不运行。

## SemBench / cars / Q7 — 凹陷、刹车磨损或电气故障任一成立的车

源码重建逻辑计划；实质混合。[查询定义 / 实现](https://github.com/sembench/SemBench/blob/8c2cac89b21c6782239e8e5b03d326d0c029b655/files/cars/query/bigquery/Q7.sql)

- **论文**：[Lao et al. — SemBench: A Benchmark for Semantic Query Processing Engines](https://arxiv.org/abs/2511.01716v2)。arXiv v2, 2026-03-16；arXiv 注记 accepted VLDB 2026；定位：§4.4。论文提供 benchmark 背景；本图册依据链接的查询代码重建逻辑计划，不是论文原图或实际 EXPLAIN。
- **数据**：[VehiDE vehicle damage images](https://www.kaggle.com/ds/3685629)。原始数据版本未逐文件核验；定位：§4.4。真实多模态素材与合成车辆属性/关联组合；不是真实车辆的联合理赔记录。
- **数据**：[Stanford Cars](https://www.kaggle.com/datasets/jutrera/stanford-car-dataset-by-classes-folder)。原始数据版本未逐文件核验；定位：§4.4。真实多模态素材与合成车辆属性/关联组合；不是真实车辆的联合理赔记录。
- **数据**：[Car diagnostics audio](https://www.kaggle.com/datasets/malakragaie/car-diagnostics-dataset)。原始数据版本未逐文件核验；定位：§4.4。真实多模态素材与合成车辆属性/关联组合；不是真实车辆的联合理赔记录。
- **数据**：[NHTSA complaints](https://www.kaggle.com/datasets/alshival/nhtsa-complaints)。原始数据版本未逐文件核验；定位：§4.4。真实多模态素材与合成车辆属性/关联组合；不是真实车辆的联合理赔记录。

```text
UNION DISTINCT car_id
├─ π car_id
│  └─ SEM_FILTER 录音：刹车磨损
│     └─ ⋈ car_id
│        ├─ Scan cars
│        └─ Scan audio_mm 录音
├─ π car_id
│  └─ SEM_FILTER 投诉：电气故障
│     └─ ⋈ car_id
│        ├─ Scan cars
│        └─ Scan complaints
└─ π car_id
   └─ SEM_FILTER 图片：凹陷
      └─ ⋈ car_id
         ├─ Scan cars
         └─ Scan car_mm 图片
```



## SemBench / cars / Q8 — 找100条图片同时有穿孔和漆面划痕的车记录

源码重建逻辑计划；实质混合。[查询定义 / 实现](https://github.com/sembench/SemBench/blob/8c2cac89b21c6782239e8e5b03d326d0c029b655/files/cars/query/bigquery/Q8.sql)

- **论文**：[Lao et al. — SemBench: A Benchmark for Semantic Query Processing Engines](https://arxiv.org/abs/2511.01716v2)。arXiv v2, 2026-03-16；arXiv 注记 accepted VLDB 2026；定位：§4.4。论文提供 benchmark 背景；本图册依据链接的查询代码重建逻辑计划，不是论文原图或实际 EXPLAIN。
- **数据**：[VehiDE vehicle damage images](https://www.kaggle.com/ds/3685629)。原始数据版本未逐文件核验；定位：§4.4。真实多模态素材与合成车辆属性/关联组合；不是真实车辆的联合理赔记录。
- **数据**：[Stanford Cars](https://www.kaggle.com/datasets/jutrera/stanford-car-dataset-by-classes-folder)。原始数据版本未逐文件核验；定位：§4.4。真实多模态素材与合成车辆属性/关联组合；不是真实车辆的联合理赔记录。
- **数据**：[Car diagnostics audio](https://www.kaggle.com/datasets/malakragaie/car-diagnostics-dataset)。原始数据版本未逐文件核验；定位：§4.4。真实多模态素材与合成车辆属性/关联组合；不是真实车辆的联合理赔记录。
- **数据**：[NHTSA complaints](https://www.kaggle.com/datasets/alshival/nhtsa-complaints)。原始数据版本未逐文件核验；定位：§4.4。真实多模态素材与合成车辆属性/关联组合；不是真实车辆的联合理赔记录。

```text
LIMIT 100
└─ π car_id
   └─ SEM_FILTER 图片：穿孔 AND 漆面划痕
      └─ ⋈ car_id
         ├─ Scan cars
         └─ Scan car_mm 图片
```

源码没有 DISTINCT，不能保证100个不同车辆。

## SemBench / cars / Q9 — 图片撕裂且录音点火异常的车

源码重建逻辑计划；实质混合。[查询定义 / 实现](https://github.com/sembench/SemBench/blob/8c2cac89b21c6782239e8e5b03d326d0c029b655/files/cars/query/bigquery/Q9.sql)

- **论文**：[Lao et al. — SemBench: A Benchmark for Semantic Query Processing Engines](https://arxiv.org/abs/2511.01716v2)。arXiv v2, 2026-03-16；arXiv 注记 accepted VLDB 2026；定位：§4.4。论文提供 benchmark 背景；本图册依据链接的查询代码重建逻辑计划，不是论文原图或实际 EXPLAIN。
- **数据**：[VehiDE vehicle damage images](https://www.kaggle.com/ds/3685629)。原始数据版本未逐文件核验；定位：§4.4。真实多模态素材与合成车辆属性/关联组合；不是真实车辆的联合理赔记录。
- **数据**：[Stanford Cars](https://www.kaggle.com/datasets/jutrera/stanford-car-dataset-by-classes-folder)。原始数据版本未逐文件核验；定位：§4.4。真实多模态素材与合成车辆属性/关联组合；不是真实车辆的联合理赔记录。
- **数据**：[Car diagnostics audio](https://www.kaggle.com/datasets/malakragaie/car-diagnostics-dataset)。原始数据版本未逐文件核验；定位：§4.4。真实多模态素材与合成车辆属性/关联组合；不是真实车辆的联合理赔记录。
- **数据**：[NHTSA complaints](https://www.kaggle.com/datasets/alshival/nhtsa-complaints)。原始数据版本未逐文件核验；定位：§4.4。真实多模态素材与合成车辆属性/关联组合；不是真实车辆的联合理赔记录。

```text
δ DISTINCT
└─ π car_id
   └─ SEM_FILTER 图片撕裂 AND 录音点火异常（联合判断）
      └─ ⋈ car_id
         ├─ ⋈ car_id
         │  ├─ Scan cars
         │  └─ Scan car_mm 图片
         └─ Scan audio_mm 录音
```



## SemBench / cars / Q10 — 将投诉分类到故障部件

源码重建逻辑计划；实质混合。[查询定义 / 实现](https://github.com/sembench/SemBench/blob/8c2cac89b21c6782239e8e5b03d326d0c029b655/files/cars/query/bigquery/Q10.sql)

- **论文**：[Lao et al. — SemBench: A Benchmark for Semantic Query Processing Engines](https://arxiv.org/abs/2511.01716v2)。arXiv v2, 2026-03-16；arXiv 注记 accepted VLDB 2026；定位：§4.4。论文提供 benchmark 背景；本图册依据链接的查询代码重建逻辑计划，不是论文原图或实际 EXPLAIN。
- **数据**：[VehiDE vehicle damage images](https://www.kaggle.com/ds/3685629)。原始数据版本未逐文件核验；定位：§4.4。真实多模态素材与合成车辆属性/关联组合；不是真实车辆的联合理赔记录。
- **数据**：[Stanford Cars](https://www.kaggle.com/datasets/jutrera/stanford-car-dataset-by-classes-folder)。原始数据版本未逐文件核验；定位：§4.4。真实多模态素材与合成车辆属性/关联组合；不是真实车辆的联合理赔记录。
- **数据**：[Car diagnostics audio](https://www.kaggle.com/datasets/malakragaie/car-diagnostics-dataset)。原始数据版本未逐文件核验；定位：§4.4。真实多模态素材与合成车辆属性/关联组合；不是真实车辆的联合理赔记录。
- **数据**：[NHTSA complaints](https://www.kaggle.com/datasets/alshival/nhtsa-complaints)。原始数据版本未逐文件核验；定位：§4.4。真实多模态素材与合成车辆属性/关联组合；不是真实车辆的联合理赔记录。

```text
π car_id, problem_category
└─ SEM_CLASSIFY 投诉→24个部件类别
   └─ ⋈ car_id
      ├─ Scan cars
      └─ Scan complaints
```



## SemBench / ecomm / q1 — 筛出 Reebok 背包

源码重建逻辑计划；轻混合（仅投影）。[查询定义 / 实现](https://github.com/sembench/SemBench/blob/8c2cac89b21c6782239e8e5b03d326d0c029b655/files/ecomm/queries/dialects/bigquery/q1.sql)

- **论文**：[Lao et al. — SemBench: A Benchmark for Semantic Query Processing Engines](https://arxiv.org/abs/2511.01716v2)。arXiv v2, 2026-03-16；arXiv 注记 accepted VLDB 2026；定位：§4.3。论文提供 benchmark 背景；本图册依据链接的查询代码重建逻辑计划，不是论文原图或实际 EXPLAIN。
- **数据**：[Fashion product dataset](https://www.kaggle.com/ds/139630)。原始数据版本未逐文件核验；定位：§4.3。商品图像、描述与结构化字段；gold 使用源结构化标签。

```text
π id
└─ SEM_FILTER 描述：Reebok 背包
   └─ Scan STYLES_DETAILS
```



## SemBench / ecomm / q2 — 筛出黄银双色运动鞋图片

源码重建逻辑计划；轻混合（仅投影）。[查询定义 / 实现](https://github.com/sembench/SemBench/blob/8c2cac89b21c6782239e8e5b03d326d0c029b655/files/ecomm/queries/dialects/bigquery/q2.sql)

- **论文**：[Lao et al. — SemBench: A Benchmark for Semantic Query Processing Engines](https://arxiv.org/abs/2511.01716v2)。arXiv v2, 2026-03-16；arXiv 注记 accepted VLDB 2026；定位：§4.3。论文提供 benchmark 背景；本图册依据链接的查询代码重建逻辑计划，不是论文原图或实际 EXPLAIN。
- **数据**：[Fashion product dataset](https://www.kaggle.com/ds/139630)。原始数据版本未逐文件核验；定位：§4.3。商品图像、描述与结构化字段；gold 使用源结构化标签。

```text
π 从图片 URI 解析 id
└─ SEM_FILTER 图像：黄银双色运动鞋
   └─ Scan IMAGES
```



## SemBench / ecomm / q3 — 从描述抽取商品品牌

源码重建逻辑计划；轻混合（仅投影）。[查询定义 / 实现](https://github.com/sembench/SemBench/blob/8c2cac89b21c6782239e8e5b03d326d0c029b655/files/ecomm/queries/dialects/bigquery/q3.sql)

- **论文**：[Lao et al. — SemBench: A Benchmark for Semantic Query Processing Engines](https://arxiv.org/abs/2511.01716v2)。arXiv v2, 2026-03-16；arXiv 注记 accepted VLDB 2026；定位：§4.3。论文提供 benchmark 背景；本图册依据链接的查询代码重建逻辑计划，不是论文原图或实际 EXPLAIN。
- **数据**：[Fashion product dataset](https://www.kaggle.com/ds/139630)。原始数据版本未逐文件核验；定位：§4.3。商品图像、描述与结构化字段；gold 使用源结构化标签。

```text
π id, category=品牌
└─ SEM_MAP 描述→品牌
   └─ Scan STYLES_DETAILS
```



## SemBench / ecomm / q4 — 在简单颜色子集抽取图片主色

源码重建逻辑计划；实质混合。[查询定义 / 实现](https://github.com/sembench/SemBench/blob/8c2cac89b21c6782239e8e5b03d326d0c029b655/files/ecomm/queries/dialects/bigquery/q4.sql)

- **论文**：[Lao et al. — SemBench: A Benchmark for Semantic Query Processing Engines](https://arxiv.org/abs/2511.01716v2)。arXiv v2, 2026-03-16；arXiv 注记 accepted VLDB 2026；定位：§4.3。论文提供 benchmark 背景；本图册依据链接的查询代码重建逻辑计划，不是论文原图或实际 EXPLAIN。
- **数据**：[Fashion product dataset](https://www.kaggle.com/ds/139630)。原始数据版本未逐文件核验；定位：§4.3。商品图像、描述与结构化字段；gold 使用源结构化标签。

```text
π id, category=主色
└─ SEM_MAP 图像→主色
   └─ ⋈ filename = basename(uri)
      ├─ ⋈ imageURL = link
      │  ├─ σ baseColour ∈ Black/Blue/Red/White/Orange/Green
      │  │  └─ Scan STYLES_DETAILS
      │  └─ Scan IMAGE_MAPPING
      └─ Scan IMAGES
```



## SemBench / ecomm / q5 — 将商品描述分类为五种服装类别

源码重建逻辑计划；实质混合。[查询定义 / 实现](https://github.com/sembench/SemBench/blob/8c2cac89b21c6782239e8e5b03d326d0c029b655/files/ecomm/queries/dialects/bigquery/q5.sql)

- **论文**：[Lao et al. — SemBench: A Benchmark for Semantic Query Processing Engines](https://arxiv.org/abs/2511.01716v2)。arXiv v2, 2026-03-16；arXiv 注记 accepted VLDB 2026；定位：§4.3。论文提供 benchmark 背景；本图册依据链接的查询代码重建逻辑计划，不是论文原图或实际 EXPLAIN。
- **数据**：[Fashion product dataset](https://www.kaggle.com/ds/139630)。原始数据版本未逐文件核验；定位：§4.3。商品图像、描述与结构化字段；gold 使用源结构化标签。

```text
π id, category
└─ SEM_CLASSIFY 描述→Dress/Bottomwear/Socks/Topwear/Innerwear
   └─ σ masterCategory=Apparel; 排除 Saree/Apparel Set/Loungewear and Nightwear
      └─ Scan STYLES_DETAILS
```



## SemBench / ecomm / q6 — 将商品图片分类为五种服装类别

源码重建逻辑计划；实质混合。[查询定义 / 实现](https://github.com/sembench/SemBench/blob/8c2cac89b21c6782239e8e5b03d326d0c029b655/files/ecomm/queries/dialects/bigquery/q6.sql)

- **论文**：[Lao et al. — SemBench: A Benchmark for Semantic Query Processing Engines](https://arxiv.org/abs/2511.01716v2)。arXiv v2, 2026-03-16；arXiv 注记 accepted VLDB 2026；定位：§4.3。论文提供 benchmark 背景；本图册依据链接的查询代码重建逻辑计划，不是论文原图或实际 EXPLAIN。
- **数据**：[Fashion product dataset](https://www.kaggle.com/ds/139630)。原始数据版本未逐文件核验；定位：§4.3。商品图像、描述与结构化字段；gold 使用源结构化标签。

```text
π id, category
└─ SEM_CLASSIFY 图片→五种服装类别
   └─ ⋈ filename = basename(uri)
      ├─ ⋈ imageURL = link
      │  ├─ σ masterCategory=Apparel; 排除 Saree/Apparel Set/Loungewear and Nightwear
      │  │  └─ Scan STYLES_DETAILS
      │  └─ Scan IMAGE_MAPPING
      └─ Scan IMAGES
```



## SemBench / ecomm / q7 — 配对500以内同品牌同类别商品

源码重建逻辑计划；实质混合。[查询定义 / 实现](https://github.com/sembench/SemBench/blob/8c2cac89b21c6782239e8e5b03d326d0c029b655/files/ecomm/queries/dialects/bigquery/q7.sql)

- **论文**：[Lao et al. — SemBench: A Benchmark for Semantic Query Processing Engines](https://arxiv.org/abs/2511.01716v2)。arXiv v2, 2026-03-16；arXiv 注记 accepted VLDB 2026；定位：§4.3。论文提供 benchmark 背景；本图册依据链接的查询代码重建逻辑计划，不是论文原图或实际 EXPLAIN。
- **数据**：[Fashion product dataset](https://www.kaggle.com/ds/139630)。原始数据版本未逐文件核验；定位：§4.3。商品图像、描述与结构化字段；gold 使用源结构化标签。

```text
π p1.id-p2.id
└─ SEM_JOIN 描述：同品牌 AND 同类别
   ├─ σ price ≤ 500
   │  └─ Scan STYLES_DETAILS
   └─ σ price ≤ 500
      └─ Scan STYLES_DETAILS
```

SQL 未排除自身配对；图保留该语义。

## SemBench / ecomm / q8 — 长商品描述与匹配图片连接

源码重建逻辑计划；实质混合。[查询定义 / 实现](https://github.com/sembench/SemBench/blob/8c2cac89b21c6782239e8e5b03d326d0c029b655/files/ecomm/queries/dialects/bigquery/q8.sql)

- **论文**：[Lao et al. — SemBench: A Benchmark for Semantic Query Processing Engines](https://arxiv.org/abs/2511.01716v2)。arXiv v2, 2026-03-16；arXiv 注记 accepted VLDB 2026；定位：§4.3。论文提供 benchmark 背景；本图册依据链接的查询代码重建逻辑计划，不是论文原图或实际 EXPLAIN。
- **数据**：[Fashion product dataset](https://www.kaggle.com/ds/139630)。原始数据版本未逐文件核验；定位：§4.3。商品图像、描述与结构化字段；gold 使用源结构化标签。

```text
π 源码拼接 imageID-imageID
└─ SEM_JOIN 图像符合描述
   ├─ σ description 长度 ≥ 3000
   │  └─ Scan STYLES_DETAILS
   └─ Scan IMAGES
```

源码输出两次使用同一图片 ID，未输出商品 ID；图忠实记录，不能冒称正确 pair key。

## SemBench / ecomm / q9 — 低价单色商品：左外语义连接相同类别/颜色图片

源码重建逻辑计划；实质混合。[查询定义 / 实现](https://github.com/sembench/SemBench/blob/8c2cac89b21c6782239e8e5b03d326d0c029b655/files/ecomm/queries/dialects/bigquery/q9.sql)

- **论文**：[Lao et al. — SemBench: A Benchmark for Semantic Query Processing Engines](https://arxiv.org/abs/2511.01716v2)。arXiv v2, 2026-03-16；arXiv 注记 accepted VLDB 2026；定位：§4.3。论文提供 benchmark 背景；本图册依据链接的查询代码重建逻辑计划，不是论文原图或实际 EXPLAIN。
- **数据**：[Fashion product dataset](https://www.kaggle.com/ds/139630)。原始数据版本未逐文件核验；定位：§4.3。商品图像、描述与结构化字段；gold 使用源结构化标签。

```text
π p1.id-p2.id
└─ SEM_LEFT_JOIN 不同URI AND 图像同类别同主色
   ├─ ⋈ filename = basename(uri)
   │  ├─ ⋈ imageURL = link
   │  │  ├─ σ 简单六色 AND colour1=空 AND colour2=空 AND price<800
   │  │  │  └─ Scan STYLES_DETAILS
   │  │  └─ Scan IMAGE_MAPPING
   │  └─ Scan IMAGES
   └─ ⋈ filename = basename(uri)
      ├─ ⋈ imageURL = link
      │  ├─ σ 简单六色 AND colour1=空 AND colour2=空 AND price<800
      │  │  └─ Scan STYLES_DETAILS
      │  └─ Scan IMAGE_MAPPING
      └─ Scan IMAGES
```

保留 LEFT OUTER JOIN 的无匹配行语义。

## SemBench / ecomm / q10 — 组合相同品牌及主色的鞋、下装、上装

源码重建逻辑计划；实质混合。[查询定义 / 实现](https://github.com/sembench/SemBench/blob/8c2cac89b21c6782239e8e5b03d326d0c029b655/files/ecomm/queries/dialects/bigquery/q10.sql)

- **论文**：[Lao et al. — SemBench: A Benchmark for Semantic Query Processing Engines](https://arxiv.org/abs/2511.01716v2)。arXiv v2, 2026-03-16；arXiv 注记 accepted VLDB 2026；定位：§4.3。论文提供 benchmark 背景；本图册依据链接的查询代码重建逻辑计划，不是论文原图或实际 EXPLAIN。
- **数据**：[Fashion product dataset](https://www.kaggle.com/ds/139630)。原始数据版本未逐文件核验；定位：§4.3。商品图像、描述与结构化字段；gold 使用源结构化标签。

```text
π 三商品 id 拼接
└─ SEM_JOIN 下装与上装同主色同品牌
   ├─ SEM_JOIN 鞋与下装同主色同品牌
   │  ├─ SEM_FILTER 图像：鞋类
   │  │  └─ ⋈ filename = basename(uri)
   │  │     ├─ ⋈ imageURL = link
   │  │     │  ├─ σ baseColour ∈ Black/Blue/Red/White AND price≤1000
   │  │     │  │  └─ Scan STYLES_DETAILS
   │  │     │  └─ Scan IMAGE_MAPPING
   │  │     └─ Scan IMAGES
   │  └─ SEM_FILTER 图像：下装
   │     └─ ⋈ filename = basename(uri)
   │        ├─ ⋈ imageURL = link
   │        │  ├─ σ baseColour ∈ Black/Blue/Red/White AND price≤1000
   │        │  │  └─ Scan STYLES_DETAILS
   │        │  └─ Scan IMAGE_MAPPING
   │        └─ Scan IMAGES
   └─ SEM_FILTER 图像：上装，非连衣裙
      └─ ⋈ filename = basename(uri)
         ├─ ⋈ imageURL = link
         │  ├─ σ baseColour ∈ Black/Blue/Red/White AND price≤1000
         │  │  └─ Scan STYLES_DETAILS
         │  └─ Scan IMAGE_MAPPING
         └─ Scan IMAGES
```



## SemBench / ecomm / q11 — 黑色鞋/下装/上装，加500以内同品牌配饰

源码重建逻辑计划；实质混合。[查询定义 / 实现](https://github.com/sembench/SemBench/blob/8c2cac89b21c6782239e8e5b03d326d0c029b655/files/ecomm/queries/dialects/bigquery/q11.sql)

- **论文**：[Lao et al. — SemBench: A Benchmark for Semantic Query Processing Engines](https://arxiv.org/abs/2511.01716v2)。arXiv v2, 2026-03-16；arXiv 注记 accepted VLDB 2026；定位：§4.3。论文提供 benchmark 背景；本图册依据链接的查询代码重建逻辑计划，不是论文原图或实际 EXPLAIN。
- **数据**：[Fashion product dataset](https://www.kaggle.com/ds/139630)。原始数据版本未逐文件核验；定位：§4.3。商品图像、描述与结构化字段；gold 使用源结构化标签。

```text
π 四商品 id 拼接
└─ SEM_JOIN 上装与配饰同品牌
   ├─ SEM_JOIN 下装与上装同品牌
   │  ├─ SEM_JOIN 鞋与下装同品牌
   │  │  ├─ SEM_FILTER 图文：黑色鞋
   │  │  │  └─ ⋈ filename = basename(uri)
   │  │  │     ├─ ⋈ imageURL = link
   │  │  │     │  ├─ Scan STYLES_DETAILS
   │  │  │     │  └─ Scan IMAGE_MAPPING
   │  │  │     └─ Scan IMAGES
   │  │  └─ SEM_FILTER 图文：黑色下装，非泳装
   │  │     └─ ⋈ filename = basename(uri)
   │  │        ├─ ⋈ imageURL = link
   │  │        │  ├─ Scan STYLES_DETAILS
   │  │        │  └─ Scan IMAGE_MAPPING
   │  │        └─ Scan IMAGES
   │  └─ SEM_FILTER 图文：黑色上装，非泳装/连衣裙
   │     └─ ⋈ filename = basename(uri)
   │        ├─ ⋈ imageURL = link
   │        │  ├─ Scan STYLES_DETAILS
   │        │  └─ Scan IMAGE_MAPPING
   │        └─ Scan IMAGES
   └─ SEM_FILTER 图文：手表/珠宝/包
      └─ σ price≤500
         └─ ⋈ filename = basename(uri)
            ├─ ⋈ imageURL = link
            │  ├─ Scan STYLES_DETAILS
            │  └─ Scan IMAGE_MAPPING
            └─ Scan IMAGES
```



## SemBench / ecomm / q12 — Adidas/Puma 商品抽取品牌与大类JSON

源码重建逻辑计划；实质混合。[查询定义 / 实现](https://github.com/sembench/SemBench/blob/8c2cac89b21c6782239e8e5b03d326d0c029b655/files/ecomm/queries/dialects/bigquery/q12.sql)

- **论文**：[Lao et al. — SemBench: A Benchmark for Semantic Query Processing Engines](https://arxiv.org/abs/2511.01716v2)。arXiv v2, 2026-03-16；arXiv 注记 accepted VLDB 2026；定位：§4.3。论文提供 benchmark 背景；本图册依据链接的查询代码重建逻辑计划，不是论文原图或实际 EXPLAIN。
- **数据**：[Fashion product dataset](https://www.kaggle.com/ds/139630)。原始数据版本未逐文件核验；定位：§4.3。商品图像、描述与结构化字段；gold 使用源结构化标签。

```text
π 生成JSON（SQL 别名 id）
└─ SEM_MAP 图文→id/brand/category JSON
   └─ SEM_FILTER 描述：Adidas 或 Puma
      └─ ⋈ filename = basename(uri)
         ├─ ⋈ imageURL = link
         │  ├─ σ masterCategory ∈ Accessories/Apparel/Footwear
         │  │  └─ Scan STYLES_DETAILS
         │  └─ Scan IMAGE_MAPPING
         └─ Scan IMAGES
```



## SemBench / ecomm / q13 — 按复杂跑步衫需求筛选图文商品

源码重建逻辑计划；实质混合。[查询定义 / 实现](https://github.com/sembench/SemBench/blob/8c2cac89b21c6782239e8e5b03d326d0c029b655/files/ecomm/queries/dialects/bigquery/q13.sql)

- **论文**：[Lao et al. — SemBench: A Benchmark for Semantic Query Processing Engines](https://arxiv.org/abs/2511.01716v2)。arXiv v2, 2026-03-16；arXiv 注记 accepted VLDB 2026；定位：§4.3。论文提供 benchmark 背景；本图册依据链接的查询代码重建逻辑计划，不是论文原图或实际 EXPLAIN。
- **数据**：[Fashion product dataset](https://www.kaggle.com/ds/139630)。原始数据版本未逐文件核验；定位：§4.3。商品图像、描述与结构化字段；gold 使用源结构化标签。

```text
π id
└─ SEM_FILTER 男士圆领短袖跑步衫；颜色/条纹/天气需求
   └─ ⋈ filename = basename(uri)
      ├─ ⋈ imageURL = link
      │  ├─ Scan STYLES_DETAILS
      │  └─ Scan IMAGE_MAPPING
      └─ Scan IMAGES
```

需求中的偏好、排除和条件句按原查询保留，不擅自化简成新 gold。

## SemBench / ecomm / q14 — 130以下商品：匹配白袜图片并按分数取一个

源码重建逻辑计划；实质混合。[查询定义 / 实现](https://github.com/sembench/SemBench/blob/8c2cac89b21c6782239e8e5b03d326d0c029b655/files/ecomm/queries/dialects/bigquery/q14.sql)

- **论文**：[Lao et al. — SemBench: A Benchmark for Semantic Query Processing Engines](https://arxiv.org/abs/2511.01716v2)。arXiv v2, 2026-03-16；arXiv 注记 accepted VLDB 2026；定位：§4.3。论文提供 benchmark 背景；本图册依据链接的查询代码重建逻辑计划，不是论文原图或实际 EXPLAIN。
- **数据**：[Fashion product dataset](https://www.kaggle.com/ds/139630)。原始数据版本未逐文件核验；定位：§4.3。商品图像、描述与结构化字段；gold 使用源结构化标签。

```text
γ GROUP BY 商品id/标题/描述; ARRAY_AGG(imageID ORDER BY score ASC LIMIT 1)
└─ SEM_MAP score := 图像与描述匹配度
   └─ SEM_FILTER 图像：白袜
      └─ SEM_JOIN 图像符合描述
         ├─ σ price<130
         │  └─ Scan STYLES_DETAILS
         └─ Scan IMAGES
```

源码按 score ASC 取首项；不能画成“最高分”。

## SemBench / mmqa / q1 — Ben Piazza 饰演 Bob Whitewood 的电影导演

源码重建逻辑计划；实质混合。[查询定义 / 实现](https://github.com/sembench/SemBench/blob/8c2cac89b21c6782239e8e5b03d326d0c029b655/files/mmqa/query/bigquery/q1.sql)

- **论文**：[Lao et al. — SemBench: A Benchmark for Semantic Query Processing Engines](https://arxiv.org/abs/2511.01716v2)。arXiv v2, 2026-03-16；arXiv 注记 accepted VLDB 2026；定位：§4.5。论文提供 benchmark 背景；本图册依据链接的查询代码重建逻辑计划，不是论文原图或实际 EXPLAIN。
- **数据**：[MultiModalQA dataset repository](https://github.com/allenai/multimodalqa)。原始数据版本未逐文件核验；定位：§4.5。基于 MultiModalQA 重新组织关系表；论文 11 个问题，当前代码含 16 个查询变体。

```text
π director
└─ ⋈ Title = title
   ├─ σ Role = Bob Whitewood
   │  └─ Scan ben_piazza
   └─ SEM_MAP 文本→导演名
      └─ Scan ben_piazza_text_data
```



## SemBench / mmqa / q2a — 将赛马场连接到对应logo图片

源码重建逻辑计划；轻混合（仅投影）。[查询定义 / 实现](https://github.com/sembench/SemBench/blob/8c2cac89b21c6782239e8e5b03d326d0c029b655/files/mmqa/query/bigquery/q2a.sql)

- **论文**：[Lao et al. — SemBench: A Benchmark for Semantic Query Processing Engines](https://arxiv.org/abs/2511.01716v2)。arXiv v2, 2026-03-16；arXiv 注记 accepted VLDB 2026；定位：§4.5。论文提供 benchmark 背景；本图册依据链接的查询代码重建逻辑计划，不是论文原图或实际 EXPLAIN。
- **数据**：[MultiModalQA dataset repository](https://github.com/allenai/multimodalqa)。原始数据版本未逐文件核验；定位：§4.5。基于 MultiModalQA 重新组织关系表；论文 11 个问题，当前代码含 16 个查询变体。

```text
π ID, uri
└─ SEM_JOIN 图片是赛马场 logo
   ├─ Scan ap_warrior
   └─ Scan images
```



## SemBench / mmqa / q2b — 连接赛马场logo并抽取颜色

源码重建逻辑计划；轻混合（仅投影）。[查询定义 / 实现](https://github.com/sembench/SemBench/blob/8c2cac89b21c6782239e8e5b03d326d0c029b655/files/mmqa/query/bigquery/q2b.sql)

- **论文**：[Lao et al. — SemBench: A Benchmark for Semantic Query Processing Engines](https://arxiv.org/abs/2511.01716v2)。arXiv v2, 2026-03-16；arXiv 注记 accepted VLDB 2026；定位：§4.5。论文提供 benchmark 背景；本图册依据链接的查询代码重建逻辑计划，不是论文原图或实际 EXPLAIN。
- **数据**：[MultiModalQA dataset repository](https://github.com/allenai/multimodalqa)。原始数据版本未逐文件核验；定位：§4.5。基于 MultiModalQA 重新组织关系表；论文 11 个问题，当前代码含 16 个查询变体。

```text
π ID, uri, color
└─ SEM_MAP logo图像→颜色
   └─ SEM_JOIN 图片是赛马场 logo
      ├─ Scan ap_warrior
      └─ Scan images
```



## SemBench / mmqa / q3a — 筛选喜剧电影

源码重建逻辑计划；轻混合（仅投影）。[查询定义 / 实现](https://github.com/sembench/SemBench/blob/8c2cac89b21c6782239e8e5b03d326d0c029b655/files/mmqa/query/bigquery/q3a.sql)

- **论文**：[Lao et al. — SemBench: A Benchmark for Semantic Query Processing Engines](https://arxiv.org/abs/2511.01716v2)。arXiv v2, 2026-03-16；arXiv 注记 accepted VLDB 2026；定位：§4.5。论文提供 benchmark 背景；本图册依据链接的查询代码重建逻辑计划，不是论文原图或实际 EXPLAIN。
- **数据**：[MultiModalQA dataset repository](https://github.com/allenai/multimodalqa)。原始数据版本未逐文件核验；定位：§4.5。基于 MultiModalQA 重新组织关系表；论文 11 个问题，当前代码含 16 个查询变体。

```text
π title
└─ SEM_FILTER 描述表明：喜剧
   └─ Scan lizzy_caplan_text_data
```



## SemBench / mmqa / q3b — 筛选科幻电影

源码重建逻辑计划；轻混合（仅投影）。[查询定义 / 实现](https://github.com/sembench/SemBench/blob/8c2cac89b21c6782239e8e5b03d326d0c029b655/files/mmqa/query/bigquery/q3b.sql)

- **论文**：[Lao et al. — SemBench: A Benchmark for Semantic Query Processing Engines](https://arxiv.org/abs/2511.01716v2)。arXiv v2, 2026-03-16；arXiv 注记 accepted VLDB 2026；定位：§4.5。论文提供 benchmark 背景；本图册依据链接的查询代码重建逻辑计划，不是论文原图或实际 EXPLAIN。
- **数据**：[MultiModalQA dataset repository](https://github.com/allenai/multimodalqa)。原始数据版本未逐文件核验；定位：§4.5。基于 MultiModalQA 重新组织关系表；论文 11 个问题，当前代码含 16 个查询变体。

```text
π title
└─ SEM_FILTER 描述表明：科幻
   └─ Scan lizzy_caplan_text_data
```



## SemBench / mmqa / q3c — 筛选爱情电影

源码重建逻辑计划；轻混合（仅投影）。[查询定义 / 实现](https://github.com/sembench/SemBench/blob/8c2cac89b21c6782239e8e5b03d326d0c029b655/files/mmqa/query/bigquery/q3c.sql)

- **论文**：[Lao et al. — SemBench: A Benchmark for Semantic Query Processing Engines](https://arxiv.org/abs/2511.01716v2)。arXiv v2, 2026-03-16；arXiv 注记 accepted VLDB 2026；定位：§4.5。论文提供 benchmark 背景；本图册依据链接的查询代码重建逻辑计划，不是论文原图或实际 EXPLAIN。
- **数据**：[MultiModalQA dataset repository](https://github.com/allenai/multimodalqa)。原始数据版本未逐文件核验；定位：§4.5。基于 MultiModalQA 重新组织关系表；论文 11 个问题，当前代码含 16 个查询变体。

```text
π title
└─ SEM_FILTER 描述表明：爱情
   └─ Scan lizzy_caplan_text_data
```



## SemBench / mmqa / q3d — 筛选恐怖电影

源码重建逻辑计划；轻混合（仅投影）。[查询定义 / 实现](https://github.com/sembench/SemBench/blob/8c2cac89b21c6782239e8e5b03d326d0c029b655/files/mmqa/query/bigquery/q3d.sql)

- **论文**：[Lao et al. — SemBench: A Benchmark for Semantic Query Processing Engines](https://arxiv.org/abs/2511.01716v2)。arXiv v2, 2026-03-16；arXiv 注记 accepted VLDB 2026；定位：§4.5。论文提供 benchmark 背景；本图册依据链接的查询代码重建逻辑计划，不是论文原图或实际 EXPLAIN。
- **数据**：[MultiModalQA dataset repository](https://github.com/allenai/multimodalqa)。原始数据版本未逐文件核验；定位：§4.5。基于 MultiModalQA 重新组织关系表；论文 11 个问题，当前代码含 16 个查询变体。

```text
π title
└─ SEM_FILTER 描述表明：恐怖
   └─ Scan lizzy_caplan_text_data
```



## SemBench / mmqa / q3e — 筛选盗窃题材电影

源码重建逻辑计划；轻混合（仅投影）。[查询定义 / 实现](https://github.com/sembench/SemBench/blob/8c2cac89b21c6782239e8e5b03d326d0c029b655/files/mmqa/query/bigquery/q3e.sql)

- **论文**：[Lao et al. — SemBench: A Benchmark for Semantic Query Processing Engines](https://arxiv.org/abs/2511.01716v2)。arXiv v2, 2026-03-16；arXiv 注记 accepted VLDB 2026；定位：§4.5。论文提供 benchmark 背景；本图册依据链接的查询代码重建逻辑计划，不是论文原图或实际 EXPLAIN。
- **数据**：[MultiModalQA dataset repository](https://github.com/allenai/multimodalqa)。原始数据版本未逐文件核验；定位：§4.5。基于 MultiModalQA 重新组织关系表；论文 11 个问题，当前代码含 16 个查询变体。

```text
π title
└─ SEM_FILTER 描述表明：盗窃题材
   └─ Scan lizzy_caplan_text_data
```



## SemBench / mmqa / q3f — 筛选浪漫喜剧电影

源码重建逻辑计划；轻混合（仅投影）。[查询定义 / 实现](https://github.com/sembench/SemBench/blob/8c2cac89b21c6782239e8e5b03d326d0c029b655/files/mmqa/query/bigquery/q3f.sql)

- **论文**：[Lao et al. — SemBench: A Benchmark for Semantic Query Processing Engines](https://arxiv.org/abs/2511.01716v2)。arXiv v2, 2026-03-16；arXiv 注记 accepted VLDB 2026；定位：§4.5。论文提供 benchmark 背景；本图册依据链接的查询代码重建逻辑计划，不是论文原图或实际 EXPLAIN。
- **数据**：[MultiModalQA dataset repository](https://github.com/allenai/multimodalqa)。原始数据版本未逐文件核验；定位：§4.5。基于 MultiModalQA 重新组织关系表；论文 11 个问题，当前代码含 16 个查询变体。

```text
π title
└─ SEM_FILTER 描述表明：浪漫喜剧
   └─ Scan lizzy_caplan_text_data
```



## SemBench / mmqa / q3g — 筛选传记喜剧电影

源码重建逻辑计划；轻混合（仅投影）。[查询定义 / 实现](https://github.com/sembench/SemBench/blob/8c2cac89b21c6782239e8e5b03d326d0c029b655/files/mmqa/query/bigquery/q3g.sql)

- **论文**：[Lao et al. — SemBench: A Benchmark for Semantic Query Processing Engines](https://arxiv.org/abs/2511.01716v2)。arXiv v2, 2026-03-16；arXiv 注记 accepted VLDB 2026；定位：§4.5。论文提供 benchmark 背景；本图册依据链接的查询代码重建逻辑计划，不是论文原图或实际 EXPLAIN。
- **数据**：[MultiModalQA dataset repository](https://github.com/allenai/multimodalqa)。原始数据版本未逐文件核验；定位：§4.5。基于 MultiModalQA 重新组织关系表；论文 11 个问题，当前代码含 16 个查询变体。

```text
π title
└─ SEM_FILTER 描述表明：传记喜剧
   └─ Scan lizzy_caplan_text_data
```



## SemBench / mmqa / q4 — 按多标签电影类型组织电影列表

源码重建逻辑计划；实质混合。[查询定义 / 实现](https://github.com/sembench/SemBench/blob/8c2cac89b21c6782239e8e5b03d326d0c029b655/files/mmqa/query/bigquery/q4.sql)

- **论文**：[Lao et al. — SemBench: A Benchmark for Semantic Query Processing Engines](https://arxiv.org/abs/2511.01716v2)。arXiv v2, 2026-03-16；arXiv 注记 accepted VLDB 2026；定位：§4.5。论文提供 benchmark 背景；本图册依据链接的查询代码重建逻辑计划，不是论文原图或实际 EXPLAIN。
- **数据**：[MultiModalQA dataset repository](https://github.com/allenai/multimodalqa)。原始数据版本未逐文件核验；定位：§4.5。基于 MultiModalQA 重新组织关系表；论文 11 个问题，当前代码含 16 个查询变体。

```text
τ genre ASC
└─ γ GROUP BY genre; STRING_AGG(title)
   └─ UNNEST genres[]
      └─ SEM_MAP 文本→全部genres[]
         └─ σ title ∈ 原SQL的24部电影
            └─ Scan lizzy_caplan_text_data
```



## SemBench / mmqa / q5 — 找出参演给定16部电影的共同演员

拟议逻辑计划；SQL缺失；实质混合。[查询定义 / 实现](https://github.com/sembench/SemBench/blob/8c2cac89b21c6782239e8e5b03d326d0c029b655/files/mmqa/query/bigquery/q5.sql)

- **论文**：[Lao et al. — SemBench: A Benchmark for Semantic Query Processing Engines](https://arxiv.org/abs/2511.01716v2)。arXiv v2, 2026-03-16；arXiv 注记 accepted VLDB 2026；定位：§4.5。论文提供 benchmark 背景；本图册依据链接的查询代码重建逻辑计划，不是论文原图或实际 EXPLAIN。
- **数据**：[MultiModalQA dataset repository](https://github.com/allenai/multimodalqa)。原始数据版本未逐文件核验；定位：§4.5。基于 MultiModalQA 重新组织关系表；论文 11 个问题，当前代码含 16 个查询变体。

```text
π actor
└─ σ COUNT(DISTINCT title)=16
   └─ γ GROUP BY actor; COUNT(DISTINCT title)
      └─ UNNEST actors[]
         └─ SEM_MAP 文本→演员列表
            └─ σ title ∈ 指定16部电影
               └─ Scan lizzy_caplan_text_data
```

此 BigQuery 文件为空。这里是按自然语言重建的关系除法候选计划，不是现有实现。自然语言来源见同目录 natural_language/q5.json。

## SemBench / mmqa / q6a — 找有航线到 Frankfurt 的航空公司

源码重建逻辑计划；轻混合（仅投影）。[查询定义 / 实现](https://github.com/sembench/SemBench/blob/8c2cac89b21c6782239e8e5b03d326d0c029b655/files/mmqa/query/bigquery/q6a.sql)

- **论文**：[Lao et al. — SemBench: A Benchmark for Semantic Query Processing Engines](https://arxiv.org/abs/2511.01716v2)。arXiv v2, 2026-03-16；arXiv 注记 accepted VLDB 2026；定位：§4.5。论文提供 benchmark 背景；本图册依据链接的查询代码重建逻辑计划，不是论文原图或实际 EXPLAIN。
- **数据**：[MultiModalQA dataset repository](https://github.com/allenai/multimodalqa)。原始数据版本未逐文件核验；定位：§4.5。基于 MultiModalQA 重新组织关系表；论文 11 个问题，当前代码含 16 个查询变体。

```text
π Airlines
└─ SEM_FILTER Destinations 包含 Frankfurt 的目的地
   └─ Scan tampa_international_airport
```



## SemBench / mmqa / q6b — 找有航线到 Germany 的航空公司

源码重建逻辑计划；轻混合（仅投影）。[查询定义 / 实现](https://github.com/sembench/SemBench/blob/8c2cac89b21c6782239e8e5b03d326d0c029b655/files/mmqa/query/bigquery/q6b.sql)

- **论文**：[Lao et al. — SemBench: A Benchmark for Semantic Query Processing Engines](https://arxiv.org/abs/2511.01716v2)。arXiv v2, 2026-03-16；arXiv 注记 accepted VLDB 2026；定位：§4.5。论文提供 benchmark 背景；本图册依据链接的查询代码重建逻辑计划，不是论文原图或实际 EXPLAIN。
- **数据**：[MultiModalQA dataset repository](https://github.com/allenai/multimodalqa)。原始数据版本未逐文件核验；定位：§4.5。基于 MultiModalQA 重新组织关系表；论文 11 个问题，当前代码含 16 个查询变体。

```text
π Airlines
└─ SEM_FILTER Destinations 包含 Germany 的目的地
   └─ Scan tampa_international_airport
```



## SemBench / mmqa / q6c — 找有航线到 Europe 的航空公司

源码重建逻辑计划；轻混合（仅投影）。[查询定义 / 实现](https://github.com/sembench/SemBench/blob/8c2cac89b21c6782239e8e5b03d326d0c029b655/files/mmqa/query/bigquery/q6c.sql)

- **论文**：[Lao et al. — SemBench: A Benchmark for Semantic Query Processing Engines](https://arxiv.org/abs/2511.01716v2)。arXiv v2, 2026-03-16；arXiv 注记 accepted VLDB 2026；定位：§4.5。论文提供 benchmark 背景；本图册依据链接的查询代码重建逻辑计划，不是论文原图或实际 EXPLAIN。
- **数据**：[MultiModalQA dataset repository](https://github.com/allenai/multimodalqa)。原始数据版本未逐文件核验；定位：§4.5。基于 MultiModalQA 重新组织关系表；论文 11 个问题，当前代码含 16 个查询变体。

```text
π Airlines
└─ SEM_FILTER Destinations 包含 Europe 的目的地
   └─ Scan tampa_international_airport
```



## SemBench / mmqa / q7 — 有欧洲航线的航空公司及logo

查询意图计划；SQL存在差异；实质混合。[查询定义 / 实现](https://github.com/sembench/SemBench/blob/8c2cac89b21c6782239e8e5b03d326d0c029b655/files/mmqa/query/bigquery/q7.sql)

- **论文**：[Lao et al. — SemBench: A Benchmark for Semantic Query Processing Engines](https://arxiv.org/abs/2511.01716v2)。arXiv v2, 2026-03-16；arXiv 注记 accepted VLDB 2026；定位：§4.5。论文提供 benchmark 背景；本图册依据链接的查询代码重建逻辑计划，不是论文原图或实际 EXPLAIN。
- **数据**：[MultiModalQA dataset repository](https://github.com/allenai/multimodalqa)。原始数据版本未逐文件核验；定位：§4.5。基于 MultiModalQA 重新组织关系表；论文 11 个问题，当前代码含 16 个查询变体。

```text
π Airlines, uri
└─ SEM_JOIN 图像是航空公司logo
   ├─ SEM_FILTER 有欧洲目的地
   │  └─ Scan tampa_international_airport
   └─ Scan images
```

图按自然语言补足欧洲条件；当前 BigQuery SQL 缺少该过滤，不能称与源码等价。

## TAG-Bench / 0 — 数学均分>560的学校中，有多少位于湾区

手写基线源码重建；实质混合。[查询定义 / 实现](https://github.com/TAG-Research/TAG-Bench/blob/f97b0b5ca211573837cf3236224ac658b4a959bc/tag/hand_written.py#L18)

- **论文**：[Biswal et al. — Text2SQL is Not Enough: Unifying AI and Databases with TAG](https://arxiv.org/abs/2408.14717v1)。arXiv v1, 2024；定位：§4.1–4.2；Appendix A。论文提供 benchmark 背景；本图册依据链接的查询代码重建逻辑计划，不是论文原图或实际 EXPLAIN。
- **数据**：[BIRD databases used by TAG-Bench](https://bird-bench.github.io/)。原始数据版本未逐文件核验；定位：TAG §4.1。TAG 在 BIRD 数据库上修改问题并制作答案；具体数据库由本条查询定义确定。此处仅收录 12 个选例。

```text
γ COUNT(*)
└─ SEMI JOIN cname
   ├─ σ AvgScrMath > 560
   │  └─ σ rtype=S
   │     └─ Scan satscores
   └─ SEM_FILTER 县位于湾区
      └─ δ DISTINCT
         └─ π cname
            └─ σ AvgScrMath > 560
               └─ σ rtype=S
                  └─ Scan satscores
```

去重后按县判断，再回连学校；两个 f 是同一中间关系引用，不代表必须扫描两次。

## TAG-Bench / 1 — 南加州阅读均分最低学校的电话

手写基线源码重建；实质混合。[查询定义 / 实现](https://github.com/TAG-Research/TAG-Bench/blob/f97b0b5ca211573837cf3236224ac658b4a959bc/tag/hand_written.py#L33)

- **论文**：[Biswal et al. — Text2SQL is Not Enough: Unifying AI and Databases with TAG](https://arxiv.org/abs/2408.14717v1)。arXiv v1, 2024；定位：§4.1–4.2；Appendix A。论文提供 benchmark 背景；本图册依据链接的查询代码重建逻辑计划，不是论文原图或实际 EXPLAIN。
- **数据**：[BIRD databases used by TAG-Bench](https://bird-bench.github.io/)。原始数据版本未逐文件核验；定位：TAG §4.1。TAG 在 BIRD 数据库上修改问题并制作答案；具体数据库由本条查询定义确定。此处仅收录 12 个选例。

```text
π Phone
└─ ⋈ cds=CDSCode
   ├─ ARGMIN AvgScrRead
   │  └─ SEMI JOIN cname
   │     ├─ σ rtype=S
   │     │  └─ Scan satscores
   │     └─ SEM_FILTER 县位于南加州
   │        └─ δ DISTINCT
   │           └─ π cname
   │              └─ σ rtype=S
   │                 └─ Scan satscores
   └─ Scan schools
```



## TAG-Bench / 3 — 人口超过200万的县中学校考生总数

手写基线源码重建；实质混合。[查询定义 / 实现](https://github.com/TAG-Research/TAG-Bench/blob/f97b0b5ca211573837cf3236224ac658b4a959bc/tag/hand_written.py#L53)

- **论文**：[Biswal et al. — Text2SQL is Not Enough: Unifying AI and Databases with TAG](https://arxiv.org/abs/2408.14717v1)。arXiv v1, 2024；定位：§4.1–4.2；Appendix A。论文提供 benchmark 背景；本图册依据链接的查询代码重建逻辑计划，不是论文原图或实际 EXPLAIN。
- **数据**：[BIRD databases used by TAG-Bench](https://bird-bench.github.io/)。原始数据版本未逐文件核验；定位：TAG §4.1。TAG 在 BIRD 数据库上修改问题并制作答案；具体数据库由本条查询定义确定。此处仅收录 12 个选例。

```text
γ SUM(NumTstTakr)
└─ ⋈ cds=CDSCode
   ├─ σ rtype=S
   │  └─ Scan satscores
   └─ SEMI JOIN County
      ├─ Scan schools
      └─ σ parsed_population > 2000000
         └─ SEM_MAP 县→人口估计
            └─ δ DISTINCT
               └─ π County
                  └─ Scan schools
```

源码要求模型猜人口并解析数字；没有冻结年份，不当成可靠人口事实查询。

## TAG-Bench / 4 — 硅谷地区经度最高学校的年级范围

手写基线源码重建；实质混合。[查询定义 / 实现](https://github.com/TAG-Research/TAG-Bench/blob/f97b0b5ca211573837cf3236224ac658b4a959bc/tag/hand_written.py#L77)

- **论文**：[Biswal et al. — Text2SQL is Not Enough: Unifying AI and Databases with TAG](https://arxiv.org/abs/2408.14717v1)。arXiv v1, 2024；定位：§4.1–4.2；Appendix A。论文提供 benchmark 背景；本图册依据链接的查询代码重建逻辑计划，不是论文原图或实际 EXPLAIN。
- **数据**：[BIRD databases used by TAG-Bench](https://bird-bench.github.io/)。原始数据版本未逐文件核验；定位：TAG §4.1。TAG 在 BIRD 数据库上修改问题并制作答案；具体数据库由本条查询定义确定。此处仅收录 12 个选例。

```text
π GSoffered
└─ LIMIT 1
   └─ τ Longitude DESC
      └─ SEMI JOIN County
         ├─ Scan schools
         └─ SEM_FILTER County 位于硅谷
            └─ DROP NULL
               └─ δ DISTINCT
                  └─ π County
                     └─ Scan schools
```

CSV自然语言说 cities，手写源码按 County 判断；图对应实现，存在语义差异。

## TAG-Bench / 5 — 最常见的两个女性管理员名字

手写基线源码重建；实质混合。[查询定义 / 实现](https://github.com/TAG-Research/TAG-Bench/blob/f97b0b5ca211573837cf3236224ac658b4a959bc/tag/hand_written.py#L91)

- **论文**：[Biswal et al. — Text2SQL is Not Enough: Unifying AI and Databases with TAG](https://arxiv.org/abs/2408.14717v1)。arXiv v1, 2024；定位：§4.1–4.2；Appendix A。论文提供 benchmark 背景；本图册依据链接的查询代码重建逻辑计划，不是论文原图或实际 EXPLAIN。
- **数据**：[BIRD databases used by TAG-Bench](https://bird-bench.github.io/)。原始数据版本未逐文件核验；定位：TAG §4.1。TAG 在 BIRD 数据库上修改问题并制作答案；具体数据库由本条查询定义确定。此处仅收录 12 个选例。

```text
LIMIT 2
└─ π AdmFName1
   └─ SEM_FILTER 名字被判断为女性名字
      └─ LIMIT 20
         └─ τ count DESC
            └─ γ GROUP BY AdmFName1; COUNT(*) → count
               └─ Scan schools
```

源码先截频率前20再判断名字，可能漏掉真正答案；姓名推断不等于真实自报性别，非人员决策建议。

## TAG-Bench / 6 — csgillespie 的根帖中提及学术论文的数量

手写基线源码重建；实质混合。[查询定义 / 实现](https://github.com/TAG-Research/TAG-Bench/blob/f97b0b5ca211573837cf3236224ac658b4a959bc/tag/hand_written.py#L104)

- **论文**：[Biswal et al. — Text2SQL is Not Enough: Unifying AI and Databases with TAG](https://arxiv.org/abs/2408.14717v1)。arXiv v1, 2024；定位：§4.1–4.2；Appendix A。论文提供 benchmark 背景；本图册依据链接的查询代码重建逻辑计划，不是论文原图或实际 EXPLAIN。
- **数据**：[BIRD databases used by TAG-Bench](https://bird-bench.github.io/)。原始数据版本未逐文件核验；定位：TAG §4.1。TAG 在 BIRD 数据库上修改问题并制作答案；具体数据库由本条查询定义确定。此处仅收录 12 个选例。

```text
γ COUNT(*)
└─ SEM_FILTER Body 提及学术论文
   └─ ⋈ Id=OwnerUserId
      ├─ σ DisplayName = csgillespie
      │  └─ Scan users
      └─ σ ParentId IS NULL
         └─ Scan posts
```



## TAG-Bench / 8 — 分数17的评论中，关于统计学的数量

手写基线源码重建；实质混合。[查询定义 / 实现](https://github.com/TAG-Research/TAG-Bench/blob/f97b0b5ca211573837cf3236224ac658b4a959bc/tag/hand_written.py#L118)

- **论文**：[Biswal et al. — Text2SQL is Not Enough: Unifying AI and Databases with TAG](https://arxiv.org/abs/2408.14717v1)。arXiv v1, 2024；定位：§4.1–4.2；Appendix A。论文提供 benchmark 背景；本图册依据链接的查询代码重建逻辑计划，不是论文原图或实际 EXPLAIN。
- **数据**：[BIRD databases used by TAG-Bench](https://bird-bench.github.io/)。原始数据版本未逐文件核验；定位：TAG §4.1。TAG 在 BIRD 数据库上修改问题并制作答案；具体数据库由本条查询定义确定。此处仅收录 12 个选例。

```text
γ COUNT(*)
└─ SEM_FILTER Text 关于统计学
   └─ σ Score=17
      └─ Scan comments
```



## TAG-Bench / 10 — 浏览量超过80000的帖子中，讨论R语言的数量

手写基线源码重建；实质混合。[查询定义 / 实现](https://github.com/TAG-Research/TAG-Bench/blob/f97b0b5ca211573837cf3236224ac658b4a959bc/tag/hand_written.py#L129)

- **论文**：[Biswal et al. — Text2SQL is Not Enough: Unifying AI and Databases with TAG](https://arxiv.org/abs/2408.14717v1)。arXiv v1, 2024；定位：§4.1–4.2；Appendix A。论文提供 benchmark 背景；本图册依据链接的查询代码重建逻辑计划，不是论文原图或实际 EXPLAIN。
- **数据**：[BIRD databases used by TAG-Bench](https://bird-bench.github.io/)。原始数据版本未逐文件核验；定位：TAG §4.1。TAG 在 BIRD 数据库上修改问题并制作答案；具体数据库由本条查询定义确定。此处仅收录 12 个选例。

```text
γ COUNT(*)
└─ SEM_FILTER Body 讨论R语言
   └─ σ ViewCount>80000
      └─ Scan posts
```



## TAG-Bench / 11 — 中东面积最小国家的赛道举办的比赛名称

手写基线源码重建；实质混合。[查询定义 / 实现](https://github.com/TAG-Research/TAG-Bench/blob/f97b0b5ca211573837cf3236224ac658b4a959bc/tag/hand_written.py#L140)

- **论文**：[Biswal et al. — Text2SQL is Not Enough: Unifying AI and Databases with TAG](https://arxiv.org/abs/2408.14717v1)。arXiv v1, 2024；定位：§4.1–4.2；Appendix A。论文提供 benchmark 背景；本图册依据链接的查询代码重建逻辑计划，不是论文原图或实际 EXPLAIN。
- **数据**：[BIRD databases used by TAG-Bench](https://bird-bench.github.io/)。原始数据版本未逐文件核验；定位：TAG §4.1。TAG 在 BIRD 数据库上修改问题并制作答案；具体数据库由本条查询定义确定。此处仅收录 12 个选例。

```text
TAKE FIRST
└─ δ DISTINCT
   └─ π name_race
      └─ ⋈ circuitId
         ├─ SEM_FILTER country 是中东面积最小国家
         │  └─ Scan circuits
         └─ Scan races
```



## TAG-Bench / 48 — 三个指定赛道中哪个离首都最近

手写基线源码重建；实质混合。[查询定义 / 实现](https://github.com/TAG-Research/TAG-Bench/blob/f97b0b5ca211573837cf3236224ac658b4a959bc/tag/hand_written.py#L624)

- **论文**：[Biswal et al. — Text2SQL is Not Enough: Unifying AI and Databases with TAG](https://arxiv.org/abs/2408.14717v1)。arXiv v1, 2024；定位：§4.1–4.2；Appendix A。论文提供 benchmark 背景；本图册依据链接的查询代码重建逻辑计划，不是论文原图或实际 EXPLAIN。
- **数据**：[BIRD databases used by TAG-Bench](https://bird-bench.github.io/)。原始数据版本未逐文件核验；定位：TAG §4.1。TAG 在 BIRD 数据库上修改问题并制作答案；具体数据库由本条查询定义确定。此处仅收录 12 个选例。

```text
π name
└─ SEM_TOPK 距首都近; k=1
   └─ σ name ∈ Silverstone/Hockenheimring/Hungaroring
      └─ Scan circuits
```



## TAG-Bench / 50 — 500以上考生的磁校中名称最有未来感者

手写基线源码重建；实质混合。[查询定义 / 实现](https://github.com/TAG-Research/TAG-Bench/blob/f97b0b5ca211573837cf3236224ac658b4a959bc/tag/hand_written.py#L656)

- **论文**：[Biswal et al. — Text2SQL is Not Enough: Unifying AI and Databases with TAG](https://arxiv.org/abs/2408.14717v1)。arXiv v1, 2024；定位：§4.1–4.2；Appendix A。论文提供 benchmark 背景；本图册依据链接的查询代码重建逻辑计划，不是论文原图或实际 EXPLAIN。
- **数据**：[BIRD databases used by TAG-Bench](https://bird-bench.github.io/)。原始数据版本未逐文件核验；定位：TAG §4.1。TAG 在 BIRD 数据库上修改问题并制作答案；具体数据库由本条查询定义确定。此处仅收录 12 个选例。

```text
π School
└─ SEM_TOPK 名称未来感; k=1
   └─ ⋈ CDSCode=cds
      ├─ σ Magnet=1
      │  └─ Scan schools
      └─ σ NumTstTakr>500
         └─ σ rtype=S
            └─ Scan satscores
```



## TAG-Bench / 85 — 总结 csgillespie 帖子标题的共同特点

手写基线源码重建；实质混合。[查询定义 / 实现](https://github.com/TAG-Research/TAG-Bench/blob/f97b0b5ca211573837cf3236224ac658b4a959bc/tag/hand_written.py#L952)

- **论文**：[Biswal et al. — Text2SQL is Not Enough: Unifying AI and Databases with TAG](https://arxiv.org/abs/2408.14717v1)。arXiv v1, 2024；定位：§4.1–4.2；Appendix A。论文提供 benchmark 背景；本图册依据链接的查询代码重建逻辑计划，不是论文原图或实际 EXPLAIN。
- **数据**：[BIRD databases used by TAG-Bench](https://bird-bench.github.io/)。原始数据版本未逐文件核验；定位：TAG §4.1。TAG 在 BIRD 数据库上修改问题并制作答案；具体数据库由本条查询定义确定。此处仅收录 12 个选例。

```text
SEM_AGG 总结Title共同特点
└─ ⋈ Id=OwnerUserId
   ├─ σ DisplayName = csgillespie
   │  └─ Scan users
   └─ Scan posts
```

SEM_AGG 是跨行语义归纳；区别于普通 COUNT/SUM/GROUP BY。

## UDA-Bench / Art/Mixed/1 — 19–20世纪艺术家按领域求平均年龄

端到端解释计划；实质混合。[查询定义 / 实现](https://github.com/unimib-datAI/UDA-Bench/blob/50039a527f156eeb9cad80118637da47db94b976/Query/Art/Mixed/mixed_queries.sql)

- **论文**：[Deng et al. — Unstructured Data Analysis using LLMs: A Comprehensive Benchmark](https://arxiv.org/abs/2510.27119v1)。arXiv v1, 2025；定位：§3.1–3.3；Table 2。论文提供 benchmark 背景；本图册依据链接的查询代码重建逻辑计划，不是论文原图或实际 EXPLAIN。 论文 v1 为 5 数据集/240 查询；固定仓库含 CSPaper 等扩展共 608 SQL，不能混同。
- **数据**：[WikiArt](https://www.wikiart.org/)。原始数据版本未逐文件核验；定位：UDA §3.2 / Table 2。艺术家文档与作品图像。

```text
γ GROUP BY field; AVG(age)
└─ σ century = '19th-20th'
   └─ SEM_MAP 文档→century, field, age
      └─ Scan Art 原始文档
```

端到端重建：SEM_MAP 是抽取阶段的解释，不在原SQL中；已有物化表时该查询为纯SQL。原SQL：SELECT field, AVG(age) AS avg_age FROM art WHERE century = '19th-20th' GROUP BY field;

## UDA-Bench / CSPaper/Mixed/1 — 多跳推理论文按是否用知识图谱计数

端到端解释计划；实质混合。[查询定义 / 实现](https://github.com/unimib-datAI/UDA-Bench/blob/50039a527f156eeb9cad80118637da47db94b976/Query/CSPaper/Mixed/mixed_queries.sql)

- **论文**：[Deng et al. — Unstructured Data Analysis using LLMs: A Comprehensive Benchmark](https://arxiv.org/abs/2510.27119v1)。arXiv v1, 2025；定位：§3.1–3.3；Table 2。论文提供 benchmark 背景；本图册依据链接的查询代码重建逻辑计划，不是论文原图或实际 EXPLAIN。 论文 v1 为 5 数据集/240 查询；固定仓库含 CSPaper 等扩展共 608 SQL，不能混同。 CSPaper 不在该版论文 Table 2 中，论文仅作为系统背景，不能证明此查询/数据来源。
- **数据**：[查询定义 / 实现（固定版本或本地快照）](https://github.com/unimib-datAI/UDA-Bench/blob/50039a527f156eeb9cad80118637da47db94b976/Query/CSPaper/Mixed/mixed_queries.sql)。见 URL 或本地快照；沿用 2026-10-05 来源收据；定位：仓库扩展。仓库扩展；原始论文集合、许可、下载版本未在当前快照中核实。

```text
γ GROUP BY uses_knowledge_graph; COUNT(evaluation_metric)
└─ σ reasoning_depth = 'multi-hop'
   └─ SEM_MAP 文档→reasoning_depth, uses_knowledge_graph, evaluation_metric
      └─ Scan CSPaper 原始文档
```

端到端重建：SEM_MAP 是抽取阶段的解释，不在原SQL中；已有物化表时该查询为纯SQL。原SQL：SELECT uses_knowledge_graph, COUNT(evaluation_metric) AS count_evaluation_metric FROM cspaper WHERE reasoning_depth = 'multi-hop' GROUP BY uses_knowledge_graph;

## UDA-Bench / Finan/Mixed/1 — 绩效薪酬公司按审计师求平均营业利润

端到端解释计划；实质混合。[查询定义 / 实现](https://github.com/unimib-datAI/UDA-Bench/blob/50039a527f156eeb9cad80118637da47db94b976/Query/Finan/Mixed/mixed_queries.sql)

- **论文**：[Deng et al. — Unstructured Data Analysis using LLMs: A Comprehensive Benchmark](https://arxiv.org/abs/2510.27119v1)。arXiv v1, 2025；定位：§3.1–3.3；Table 2。论文提供 benchmark 背景；本图册依据链接的查询代码重建逻辑计划，不是论文原图或实际 EXPLAIN。 论文 v1 为 5 数据集/240 查询；固定仓库含 CSPaper 等扩展共 608 SQL，不能混同。
- **数据**：[Enterprise RAG Challenge](https://rag.abdullin.com/)。原始数据版本未逐文件核验；定位：UDA §3.2 / Table 2。2022 年企业报告；所用处理版本以仓库为准。

```text
γ GROUP BY auditor; AVG(bussiness_profit)
└─ σ remuneration_policy = 'Performance-based'
   └─ SEM_MAP 文档→remuneration_policy, auditor, bussiness_profit
      └─ Scan Finan 原始文档
```

端到端重建：SEM_MAP 是抽取阶段的解释，不在原SQL中；已有物化表时该查询为纯SQL。原SQL：SELECT auditor, AVG(bussiness_profit) AS avg_bussiness_profit FROM finance WHERE remuneration_policy = 'Performance-based' GROUP BY auditor;

## UDA-Bench / Legal/Mixed/1 — 原告状态非Activist的案件按判决求最小案件号

端到端解释计划；实质混合。[查询定义 / 实现](https://github.com/unimib-datAI/UDA-Bench/blob/50039a527f156eeb9cad80118637da47db94b976/Query/Legal/Mixed/mixed_queries.sql)

- **论文**：[Deng et al. — Unstructured Data Analysis using LLMs: A Comprehensive Benchmark](https://arxiv.org/abs/2510.27119v1)。arXiv v1, 2025；定位：§3.1–3.3；Table 2。论文提供 benchmark 背景；本图册依据链接的查询代码重建逻辑计划，不是论文原图或实际 EXPLAIN。 论文 v1 为 5 数据集/240 查询；固定仓库含 CSPaper 等扩展共 608 SQL，不能混同。
- **数据**：[AustLII](https://www.austlii.edu.au/)。原始数据版本未逐文件核验；定位：UDA §3.2 / Table 2。论文 Table 2 为 566 文件，正文为 570；数量不一致保留。

```text
γ GROUP BY verdict; MIN(case_number)
└─ σ plaintiff_current_status != 'Activist'
   └─ SEM_MAP 文档→plaintiff_current_status, verdict, case_number
      └─ Scan Legal 原始文档
```

端到端重建：SEM_MAP 是抽取阶段的解释，不在原SQL中；已有物化表时该查询为纯SQL。原SQL：SELECT verdict, MIN(case_number) AS min_case_number FROM legal WHERE plaintiff_current_status != 'Activist' GROUP BY verdict;

## UDA-Bench / Player/FilterJoin/2 — 指定出生日期球员，连接球队、老板和城市

端到端解释计划；实质混合。[查询定义 / 实现](https://github.com/unimib-datAI/UDA-Bench/blob/50039a527f156eeb9cad80118637da47db94b976/Query/Player/Mixed/mixed_queries_filter_join.sql)

- **论文**：[Deng et al. — Unstructured Data Analysis using LLMs: A Comprehensive Benchmark](https://arxiv.org/abs/2510.27119v1)。arXiv v1, 2025；定位：§3.1–3.3；Table 2。论文提供 benchmark 背景；本图册依据链接的查询代码重建逻辑计划，不是论文原图或实际 EXPLAIN。 论文 v1 为 5 数据集/240 查询；固定仓库含 CSPaper 等扩展共 608 SQL，不能混同。
- **数据**：[NBA / Wikipedia](https://en.wikipedia.org/wiki/National_Basketball_Association)。原始数据版本未逐文件核验；定位：UDA §3.2 / Table 2。Wikipedia 抓取文档，非实时球员数据库。

```text
π manager.age, team.founded_year, player.name, city.city_name
└─ σ player.birth_date='1994/2/2'
   └─ ⋈ team.location=city.city_name
      ├─ ⋈ team.ownership=manager.name
      │  ├─ ⋈ player.team=team.team_name
      │  │  ├─ SEM_MAP 球员文档→球员属性
      │  │  │  └─ Scan player 文档
      │  │  └─ SEM_MAP 球队文档→球队属性
      │  │     └─ Scan team 文档
      │  └─ SEM_MAP 老板文档→老板属性
      │     └─ Scan manager 文档
      └─ SEM_MAP 城市文档→城市属性
         └─ Scan city 文档
```

原文件Query 2；SEM_MAP为端到端解释节点；不能把四个等值连接叫语义连接。

## UDA-Bench / Med/FilterJoin/2 — 先天性疾病，连接研究机构和药物属性

端到端解释计划；实质混合。[查询定义 / 实现](https://github.com/unimib-datAI/UDA-Bench/blob/50039a527f156eeb9cad80118637da47db94b976/Query/Med/Mixed/mixed_queries_filter_join.sql)

- **论文**：[Deng et al. — Unstructured Data Analysis using LLMs: A Comprehensive Benchmark](https://arxiv.org/abs/2510.27119v1)。arXiv v1, 2025；定位：§3.1–3.3；Table 2。论文提供 benchmark 背景；本图册依据链接的查询代码重建逻辑计划，不是论文原图或实际 EXPLAIN。 论文 v1 为 5 数据集/240 查询；固定仓库含 CSPaper 等扩展共 608 SQL，不能混同。
- **数据**：[UDA Healthcare / MMedC 来源说明](https://arxiv.org/html/2510.27119v1#S3.SS2)。原始数据版本未逐文件核验；定位：UDA §3.2 / Table 2。论文说明来自 MMedC；原始文件子集、抽样版本尚未逐文件核验。

```text
π key_achievements, manufacturer, funding_sources, disease_type
└─ σ pathogenesis='congenital'
   └─ ⋈ disease_name
      ├─ ⋈ disease.disease_name=institution.research_diseases
      │  ├─ SEM_MAP 疾病文档→属性
      │  │  └─ Scan disease 文档
      │  └─ SEM_MAP 机构文档→属性
      │     └─ Scan institution 文档
      └─ SEM_MAP 药物文档→属性
         └─ Scan drug 文档
```

原文件Query 2混用Med_*限定名与未带前缀表名；图归一化标识，不宣称原SQL可直接运行。

## 近期派生工作负载 / TAR/CD005139 — 按综述协议生成进入全文筛查的论文清单

本仓逻辑任务；非上游原生混合SQL；实质混合。[查询定义 / 实现](../docs/references/research/sem-filter-workloads-2026-10-02.md.txt)

- **论文**：[Kanoulas et al. — CLEF 2019 Technology Assisted Reviews in Empirical Medicine Overview](https://ceur-ws.org/Vol-2380/paper_250.pdf)。CLEF 2019 / CEUR Vol.2380；定位：2019 Task 1 / CD005139。论文/协议提供筛查任务；批量过滤与逻辑树由本项目构造，进入全文筛查不等于最终纳入。
- **数据**：[CLEF TAR 2019](https://github.com/CLEF-TAR/tar)。原始数据版本未逐文件核验；定位：2019 Task 1 / CD005139。论文/协议提供筛查任务；批量过滤与逻辑树由本项目构造，进入全文筛查不等于最终纳入。

```text
π PMID
└─ SEM_FILTER title/abstract 满足初筛协议 CD005139
   └─ ⋈ PMID
      ├─ σ review_id=CD005139
      │  └─ Scan 候选PMID关系
      └─ Scan 论文 title/abstract
```

沿用摘要初筛标签；全文最终纳入是另一任务。协议是SEM_FILTER参数，不是可枚举的关系表。

## 近期派生工作负载 / TREC-Legal/301 — 按Topic301披露请求筛邮件家族

本仓逻辑任务；非上游原生混合SQL；实质混合。[查询定义 / 实现](../docs/references/research/sem-filter-workloads-2026-10-02.md.txt)

- **论文**：[Overview of the TREC 2010 Legal Track](https://trec-legal.umiacs.umd.edu/other/legal10m.pdf)。TREC 2010；定位：Topic 301。原任务为法律检索；邮件家族过滤 plan 为本项目派生。历史记录中 qrels 获取受限，未声称完整复现。
- **数据**：[TREC Legal 2010 data](https://trec.nist.gov/data/legal10.html)。原始数据版本未逐文件核验；定位：Topic 301。原任务为法律检索；邮件家族过滤 plan 为本项目派生。历史记录中 qrels 获取受限，未声称完整复现。

```text
π message_id
└─ SEM_FILTER 邮件家族 responsive to Topic301
   └─ γ GROUP BY message_id; COLLECT(attachments)
      └─ LEFT JOIN message_id
         ├─ Scan canonical messages
         └─ Scan attachments
```

邮件正文随分组保留；家族构造是关系化表达。qrels及全文可获取性尚未闭合。

## 近期派生工作负载 / ContractNLI/conjunction — 筛出全部指定NDA假设均被支持的合同

本仓逻辑任务；非上游原生混合SQL；实质混合。[查询定义 / 实现](../docs/references/research/sem-filter-workloads-2026-10-02.md.txt)

- **论文**：[ContractNLI: A Dataset for Document-level Natural Language Inference for Contracts](https://aclanthology.org/2021.findings-emnlp.164/)。Findings of EMNLP 2021；定位：合同级 NLI / 指定假设 conjunction。原文提供合同—假设标签；多个假设全部成立的选择查询由本项目派生。
- **数据**：[ContractNLI dataset](https://stanfordnlp.github.io/contract-nli/)。原始数据版本未逐文件核验；定位：合同级 NLI / 指定假设 conjunction。原文提供合同—假设标签；多个假设全部成立的选择查询由本项目派生。

```text
π contract_id
└─ σ 所有所需假设都有标签且全为Entailment
   └─ γ GROUP BY contract_id; 聚合状态并核对假设覆盖
      └─ SEM_MAP 全文×假设→E/C/NotMentioned
         └─ CROSS JOIN
            ├─ Scan 合同全文
            └─ Scan 预先冻结的原17项假设子集
```

本仓拟议派生；NotMentioned与模型ABSTAIN单列；多假设合取不产生新的人工gold。

## 近期派生工作负载 / MAUD/MAE — 筛出MAE前瞻标准作用于完成交易能力的条款

本仓逻辑任务；非上游原生混合SQL；轻混合（仅投影）。[查询定义 / 实现](../docs/references/research/sem-filter-workloads-2026-10-02.md.txt)

- **论文**：[MAUD: An Expert-Annotated Legal NLP Dataset for Merger Agreement Understanding](https://aclanthology.org/2023.emnlp-main.1019/)。EMNLP 2023；定位：MAE / 完成交易能力。原文为专家标注条款问答；批量过滤由本项目派生，输入条款不能写成系统自行定位的完整合同。
- **数据**：[MAUD dataset](https://github.com/The-Atticus-Project/maud)。原始数据版本未逐文件核验；定位：MAE / 完成交易能力。原文为专家标注条款问答；批量过滤由本项目派生，输入条款不能写成系统自行定位的完整合同。

```text
π deal_id
└─ SEM_FILTER 原问题选项包含 Ability to consummate transaction
   └─ Scan 给定deal-point文本
```

人工已提取条款；轻混合仅投影，不假装系统从合同全文定位条款。

## 近期派生工作负载 / ShARC/YES — 同一固定规则下筛出明确YES个案

本仓逻辑任务；非上游原生混合SQL；实质混合。[查询定义 / 实现](../docs/references/research/sem-filter-workloads-2026-10-02.md.txt)

- **论文**：[Interpretation of Natural Language Rules in Conversational Machine Reading](https://aclanthology.org/D18-1233/)。EMNLP 2018；定位：YES label。原文为规则对话任务；固定规则下批量筛选 YES 为本项目派生；众包场景不等于真实申请记录。
- **数据**：[ShARC dataset](https://sharc-data.github.io/data.html)。原始数据版本未逐文件核验；定位：YES label。原文为规则对话任务；固定规则下批量筛选 YES 为本项目派生；众包场景不等于真实申请记录。

```text
π case_id
└─ σ state=YES
   └─ SEM_MAP scenario/history + 固定rule/question → 四态
      └─ Scan 同规则个案
```

MORE、IRRELEVANT不能归为NO；同对话变体不是独立记录。

## 近期派生工作负载 / ClinGen/Q1 — 筛出SOP8下至少1分的动物模型证据

本仓逻辑任务；非上游原生混合SQL；轻混合（仅投影）。[查询定义 / 实现](../docs/references/query/clingen-model-evidence/queries.sql.txt)

- **规则协议**：[ClinGen Gene–Disease Clinical Validity SOP v8](https://www.clinicalgenome.org/tools/educational-resources/materials/gene-disease-clinical-validity-sop-v8/)。SOP v8；2020-10-28；定位：Experimental evidence / model systems。规则来源；不是 benchmark 论文。当前 local SQL 仅给出字段与规则，逐条动物模型证据论文、DOI、补充材料与数据快照仍缺失。设计阶段，不能声称论文提供此查询。

```text
π record_id,gene,disease,inheritance
└─ SEM_FILTER paper/supplements/background/context 按 SOP8 至少1分
   └─ Scan animal_model_evidence
```

保持当前最终用户SEM_FILTER契约；typed抽取/机制对齐是候选内部物理分解，并非已发现计划。

## 近期派生工作负载 / TalentCLEF/29243 — 为Healthcare Data Analyst职位筛简历

本仓逻辑任务；非上游原生混合SQL；轻混合（仅投影）。[查询定义 / 实现](../docs/references/query/talentclef-job-fit/query.sql.txt)

- **论文**：[Overview of the TalentCLEF 2026: Skill and Job Title Intelligence for Human Capital Management](https://arxiv.org/abs/2606.31692v1)。arXiv v1, 2026 / CLEF 2026 overview；定位：Task A；本地 job 29243。岗位与简历文本由真实结构化资料合成并人工核查；论文提供匹配任务，当前过滤 plan 是本项目派生。29243 与发布包的逐文件校验尚未补齐。
- **数据**：[TalentCLEF 2026 Task A corpus](https://talentclef.github.io/talentclef/docs/talentclef-2026/data/description_corpus/)。原始数据版本未逐文件核验；定位：Task A；本地 job 29243。岗位与简历文本由真实结构化资料合成并人工核查；论文提供匹配任务，当前过滤 plan 是本项目派生。29243 与发布包的逐文件校验尚未补齐。

```text
π candidate_id
└─ SEM_FILTER 简历/公开投影满足 jobs/29243.html
   └─ Scan candidates
```

共10职位是参数实例，此处逐条展示当前SQL明确指定的29243；仅正向qrels，未判项不是负例。

## 近期派生工作负载 / Trial/Q1 — 判断每个已评判患者—试验对

本仓逻辑任务；非上游原生混合SQL；实质混合。[查询定义 / 实现](../docs/references/query/trial-prescreen/Q-TP-1.md.txt)

- **论文**：[Overview of TREC 2021](https://trec.nist.gov/pubs/trec30/papers/Overview-2021.pdf)。TREC 2021 proceedings, published 2022；总览，非专项 track paper；定位：Clinical Trials track；Q1/Q2/Q3。源任务为给定患者检索试验；逐对判断、反向患者清单与标签计数由本项目派生。qrels：0 不相关、1 排除、2 eligible；不是实际临床入组结果。
- **数据**：[TREC 2021 Clinical Trials topics and qrels](https://trec.nist.gov/data/trials2021.html)。原始数据版本未逐文件核验；定位：Clinical Trials track；Q1/Q2/Q3。源任务为给定患者检索试验；逐对判断、反向患者清单与标签计数由本项目派生。qrels：0 不相关、1 排除、2 eligible；不是实际临床入组结果。

```text
π record_id,value
└─ SEM_MAP 患者×试验→eligible/excluded/not_relevant
   └─ ⋈ trial_id
      ├─ Scan Pairs（含患者文本路径）
      └─ Scan Trials（入排标准）
```

本仓Q1逻辑SQL；不把所有笛卡尔积对当作有gold。

## 近期派生工作负载 / Trial/Q2 — 指定试验的eligible患者清单

本仓逻辑任务；非上游原生混合SQL；实质混合。[查询定义 / 实现](../docs/references/query/trial-prescreen/Q-TP-2.md.txt)

- **论文**：[Overview of TREC 2021](https://trec.nist.gov/pubs/trec30/papers/Overview-2021.pdf)。TREC 2021 proceedings, published 2022；总览，非专项 track paper；定位：Clinical Trials track；Q1/Q2/Q3。源任务为给定患者检索试验；逐对判断、反向患者清单与标签计数由本项目派生。qrels：0 不相关、1 排除、2 eligible；不是实际临床入组结果。
- **数据**：[TREC 2021 Clinical Trials topics and qrels](https://trec.nist.gov/data/trials2021.html)。原始数据版本未逐文件核验；定位：Clinical Trials track；Q1/Q2/Q3。源任务为给定患者检索试验；逐对判断、反向患者清单与标签计数由本项目派生。qrels：0 不相关、1 排除、2 eligible；不是实际临床入组结果。

```text
π patient_id
└─ σ trial_id=:trial AND value=eligible
   └─ SEM_MAP 患者×试验→eligible/excluded/not_relevant
      └─ ⋈ trial_id
         ├─ Scan Pairs（含患者文本路径）
         └─ Scan Trials（入排标准）
```

这里展示从原输入端到端展开；只读Q1预测物化表时Q2本身是纯SQL。

## 近期派生工作负载 / Trial/Q3 — 每个试验按资格标签计数

本仓逻辑任务；非上游原生混合SQL；实质混合。[查询定义 / 实现](../docs/references/query/trial-prescreen/Q-TP-3.md.txt)

- **论文**：[Overview of TREC 2021](https://trec.nist.gov/pubs/trec30/papers/Overview-2021.pdf)。TREC 2021 proceedings, published 2022；总览，非专项 track paper；定位：Clinical Trials track；Q1/Q2/Q3。源任务为给定患者检索试验；逐对判断、反向患者清单与标签计数由本项目派生。qrels：0 不相关、1 排除、2 eligible；不是实际临床入组结果。
- **数据**：[TREC 2021 Clinical Trials topics and qrels](https://trec.nist.gov/data/trials2021.html)。原始数据版本未逐文件核验；定位：Clinical Trials track；Q1/Q2/Q3。源任务为给定患者检索试验；逐对判断、反向患者清单与标签计数由本项目派生。qrels：0 不相关、1 排除、2 eligible；不是实际临床入组结果。

```text
γ GROUP BY trial_id,value; COUNT(*)
└─ SEM_MAP 患者×试验→eligible/excluded/not_relevant
   └─ ⋈ trial_id
      ├─ Scan Pairs（含患者文本路径）
      └─ Scan Trials（入排标准）
```

展示Q3按试验统计分支；按患者统计是另一参数化分组。未完成组需标记不完整。
