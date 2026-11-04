# 已审查询中的结构化算子与语义算子：逐题逻辑计划

整理日期：2026-10-12（Asia/Singapore）。范围是已有 2026-09-08 查询审查和 2026-09-15 五湖构造；没有找到 10 月 10–12 日的新查询账本。这里不把历史记录写成最近两天的新实验。

## 读图约定与结论

树根为输出，数据从叶子向上流动。`[R]` 是确定性关系/结构化操作；`[S]` 是需要理解文本、图像、音频或相关性的语义操作。Scan、π投影、σ筛选、γ分组聚合、⋈等值连接、δ去重、Limit、Unnest均属[R]；SEM_FILTER、SEM_MAP、SEM_JOIN、SEM_RANK属[S]。Validate与coverage是执行契约/账本，不是新的语义任务。

**所有图都是根据题义重建的逻辑计划，不是优化器 EXPLAIN、已观察执行树或最优物理计划。** 同一语义可有不同实现：先抽取规范字段再等值join，与直接SEM_JOIN不同。UDA-Bench尤其如此：原SQL面对的是关系视图；下图[S]是从原始文档建立该视图时的需求，在已标注gold表上执行SQL本身并没有语义推理。不能把gold表作为执行资源。

最有组合性的原题是：Movie Q4/Q5–Q8/Q10（本表核心审查含Q4/Q8）、Animals Q5–Q10、ecomm Q10、CSPaper Mixed1、Player/Med Join。单独SEM_MAP→π虽也有关系输出，但属于较弱混合，不应与多关系join/聚合复杂度混为一谈。五湖Q2/Q3是在共享语义结果上派生的查询；Q4是运行诊断。

## 来源与覆盖

- [原题索引](../artifact/evidence/semantic-query-discovery-20260908/query-inventory.json)：678定义/变体，仅索引不代表逐题审核。
- [已审簇及原题](../artifact/evidence/semantic-query-discovery-20260908/clusters.json)：15簇、57个不同原题；重复引用只列一次。下文保留原题全文与原路径。
- [五湖构造](shared-environment-five-lakes-build.md)：5个主任务、20个query定义。
- [Movie实际执行](semantic-query-composition-pilot.md)：派生36影评开发任务已跑；不能扩展为以下全部原题均已执行。

## A. 已审原题逐题计划

### C01 电影口碑复核

历史登记状态：`BUILT_AND_EXECUTED_DEVELOPMENT`。无独立确认；原二分类gold与clearly positive边界需审核；不能证明环境增益。

#### sembench/movie/Q2

来源路径：`files/movie/query/natural_language/Q2.txt`。

```text
Five positive reviews for movie "taken_3". Return reviewId.
```

```text
[R] Limit 5（原题无排序）
   └─ [R] π reviewId
      └─ [S] SEM_FILTER positive(reviewText)
         └─ [R] σ movieId = taken_3
            └─ [R] Scan Reviews
```

#### sembench/movie/Q3

来源路径：`files/movie/query/natural_language/Q3.txt`。

```text
Count of positive reviews for movie "taken_3". Return the count as positive_review_cnt.
```

```text
[R] γ COUNT(*) → positive_review_cnt
   └─ [S] SEM_FILTER positive(reviewText)
      └─ [R] σ movieId = taken_3
         └─ [R] Scan Reviews
```

#### sembench/movie/Q4

来源路径：`files/movie/query/natural_language/Q4.txt`。

```text
Positivity ratio of reviews for movie "taken_3". Return the ratio as positivity_ratio.
```

```text
[R] π positive_count / total_count → positivity_ratio
   └─ [R] γ SUM(sentiment=positive), COUNT(*)
      └─ [S] SEM_MAP reviewText → sentiment
         └─ [R] σ movieId = taken_3
            └─ [R] Scan Reviews
```

#### sembench/movie/Q8

来源路径：`files/movie/query/natural_language/Q8.txt`。

```text
Calculate the number of positive and negative reviews for movie "taken_3". Return scoreSentiment and count.
```

```text
[R] γ sentiment; COUNT(*)
   └─ [S] SEM_MAP reviewText → positive/negative
      └─ [R] σ movieId = taken_3
         └─ [R] Scan Reviews
```

### C02 商品属性目录

历史登记状态：`SOURCE_VERIFIED_NOT_BUILT`。原Q5/Q6只覆盖五种服装类型，不可直接包括鞋、配饰；商品原图/描述包尚未下载，需核类别范围。

#### sembench/ecomm/Q3

来源路径：`files/ecomm/queries/q3.toml`。

```text
For each product, extract the brand name from the product description and title.
Return the product id and the brand in a column titled 'category'.
```

```text
[R] π id,category
   └─ [S] SEM_MAP title,description → brand AS category
      └─ [R] Scan Products
```

#### sembench/ecomm/Q4

来源路径：`files/ecomm/queries/q4.toml`。

```text
For each product, extract the primary color of the depicted product.
Return the product id and the primary color in a column titled 'category'.
```

```text
[R] π id,category
   └─ [S] SEM_MAP image → primary_color AS category
      └─ [R] Scan Products
```

#### sembench/ecomm/Q5

来源路径：`files/ecomm/queries/q5.toml`。

```text
Based solely on the title and description of the product, classify each product into one of the following categories:

Dress: A dress is a one-piece outer garment that is worn on the torso, hangs down over the legs, and often consist of a bodice attached to a skirt.
Bottomwear: Bottomwear refers to clothing worn on the lower part of the body, such as trousers, jeans, skirts, shorts, and leggings.
Socks: Socks are a type of clothing worn on the feet, typically made of soft fabric, designed to provide comfort and warmth.
Topwear: Topwear refers to clothing worn on the upper part of the body, such as shirts, blouses, t-shirts, and jackets.
Innerwear: Innerwear refers to clothing worn beneath outer garments, typically close to the skin, such as underwear, bras, and undershirts.

Each product can only have one category.
Return the id of the product as well as its category.
```

```text
[R] π id,category
   └─ [S] SEM_MAP title,description → 五类服装 category
      └─ [R] Scan Products
```

#### sembench/ecomm/Q6

来源路径：`files/ecomm/queries/q6.toml`。

```text
Based solely on the image of the product, classify each product into one of the following categories:

Dress: A dress is a one-piece outer garment that is worn on the torso, hangs down over the legs, and often consist of a bodice attached to a skirt.
Bottomwear: Bottomwear refers to clothing worn on the lower part of the body, such as trousers, jeans, skirts, shorts, and leggings.
Socks: Socks are a type of clothing worn on the feet, typically made of soft fabric, designed to provide comfort and warmth.
Topwear: Topwear refers to clothing worn on the upper part of the body, such as shirts, blouses, t-shirts, and jackets.
Innerwear: Innerwear refers to clothing worn beneath outer garments, typically close to the skin, such as underwear, bras, and undershirts.

Each product can only have one category.
Return the id of the product as well as its category.
```

```text
[R] π id,category
   └─ [S] SEM_MAP image → 五类服装 category
      └─ [R] Scan Products
```

### C03 预算内同品牌同色三件穿搭

历史登记状态：`HOLD_SEMANTICS_AUDIT`。原NL写$10，gold和LOTUS脚本均price<=1000；LOTUS还公开预筛baseColour，不能将其复现成颜色缺失对照。

#### sembench/ecomm/Q10

来源路径：`files/ecomm/queries/q10.toml`。

```text
Based on product images, find matching outfits consisting of shoes,
bottomwear, and topwear in Black, Blue, Red, or White,
where all three items are from the same brand, same color,
and each is priced at $10 or less.
```

```text
[R] π shoe.id, bottom.id, top.id
└─ [R] ⋈ same brand AND same color（三路）
   ├─ [R] σ type=shoes ← A
   ├─ [R] σ type=bottomwear ← A
   └─ [R] σ type=topwear ← A

A（共享子计划）
└─ [R] σ color ∈ {Black,Blue,Red,White}
   └─ [S] SEM_MAP 图文 → brand,color,type
      └─ [R] σ price ≤ 原题阈值（单位待核）
         └─ [R] Scan Products
```

### C04 检索与Agent论文证据表

历史登记状态：`CANDIDATE_RAW_DOCUMENTS_PENDING`。200篇原文约678.3MB尚未下载；NQ字段含文本，禁止不对齐指标而直接排名；通用LOTUS脚本不是已跑通的逐题基线。

#### bench-u/CSPaper/Select/select_queries/1

来源路径：`Query/CSPaper/Select/select_queries.sql`。

```sql
SELECT uses_reranker, multi_turn_retrieval, agent_framework FROM cspaper;
```

```text
[R] π uses_reranker, multi_turn_retrieval, agent_framework
   └─ [S] SEM_MAP 从原始材料提取本题字段（含过滤/分组键）
      └─ [R] Scan CSPaper 原始材料
```

#### bench-u/CSPaper/Select/select_queries/2

来源路径：`Query/CSPaper/Select/select_queries.sql`。

```sql
SELECT use_agent, baseline, topic FROM cspaper;
```

```text
[R] π use_agent, baseline, topic
   └─ [S] SEM_MAP 从原始材料提取本题字段（含过滤/分组键）
      └─ [R] Scan CSPaper 原始材料
```

#### bench-u/CSPaper/Select/select_queries/3

来源路径：`Query/CSPaper/Select/select_queries.sql`。

```sql
SELECT agent_framework, performance_on_NQ, evaluation_metric FROM cspaper;
```

```text
[R] π agent_framework, performance_on_NQ, evaluation_metric
   └─ [S] SEM_MAP 从原始材料提取本题字段（含过滤/分组键）
      └─ [R] Scan CSPaper 原始材料
```

#### bench-u/CSPaper/Mixed/mixed_queries/1

来源路径：`Query/CSPaper/Mixed/mixed_queries.sql`。

```sql
SELECT uses_knowledge_graph, COUNT(evaluation_metric) AS count_evaluation_metric FROM cspaper WHERE reasoning_depth = 'multi-hop' GROUP BY uses_knowledge_graph;
```

```text
[R] γ uses_knowledge_graph; COUNT(evaluation_metric)（仅非NULL）
   └─ [R] σ reasoning_depth = 'multi-hop'
      └─ [S] SEM_MAP 从原始材料提取本题字段（含过滤/分组键）
         └─ [R] Scan CSPaper 原始材料
```

### C05 裁判及引用依据登记

历史登记状态：`CANDIDATE_RAW_DOCUMENTS_PENDING`。case_number是引用先例数；legal_basis_num是不同法规数；不是案号或法条数。566/570描述差异待清单；不构造责任/胜诉gold。

#### bench-u/Legal/Select/select_queries/1

来源路径：`Query/Legal/Select/select_queries.sql`。

```sql
SELECT nationality_for_applicant, plaintiff, fine_amount, plaintiff_current_status, legal_basis_num FROM legal;
```

```text
[R] π nationality_for_applicant, plaintiff, fine_amount, plaintiff_current_status, legal_basis_num
   └─ [S] SEM_MAP 从原始材料提取本题字段（含过滤/分组键）
      └─ [R] Scan Legal 原始材料
```

#### bench-u/Legal/Select/select_queries/2

来源路径：`Query/Legal/Select/select_queries.sql`。

```sql
SELECT judge_name, legal_basis_num, hearing_year FROM legal;
```

```text
[R] π judge_name, legal_basis_num, hearing_year
   └─ [S] SEM_MAP 从原始材料提取本题字段（含过滤/分组键）
      └─ [R] Scan Legal 原始材料
```

#### bench-u/Legal/Select/select_queries/3

来源路径：`Query/Legal/Select/select_queries.sql`。

```sql
SELECT case_number, plaintiff FROM legal;
```

```text
[R] π case_number, plaintiff
   └─ [S] SEM_MAP 从原始材料提取本题字段（含过滤/分组键）
      └─ [R] Scan Legal 原始材料
```

#### bench-u/Legal/Filter/filter_queries_Legal/5

来源路径：`Query/Legal/Filter/filter_queries_Legal.sql`。

```sql
SELECT evidence, hearing_year, verdict FROM Legal_Case WHERE hearing_year = 2007;
```

```text
[R] π evidence, hearing_year, verdict
   └─ [R] σ  hearing_year = 2007
      └─ [S] SEM_MAP 从原始材料提取本题字段（含过滤/分组键）
         └─ [R] Scan Legal 原始材料
```

### C06 球员球队归属与荣誉报告

历史登记状态：`CANDIDATE_RAW_DOCUMENTS_PENDING`。225份原文约2.43MB未下载；Data/Player/player.csv是gold非原文；同批实体的人工别名映射不能当独立历史经验。

#### bench-u/Player/Join/join_queries/1

来源路径：`Query/Player/Join/join_queries.sql`。

```sql
SELECT team.championships, team.location, player.age, player.olympic_gold_medals FROM player JOIN team ON player.team = team.team_name;
```

```text
[R] π team.championships, team.location, player.age, player.olympic_gold_medals
└─ [R] ⋈ player.team = team.team_name
   ├─ [S] SEM_MAP 提取 player 查询字段及连接键
   │  └─ [R] Scan player 原文
   └─ [S] SEM_MAP 提取 team 查询字段及连接键
      └─ [R] Scan team 原文
```

#### bench-u/Player/Join/join_queries/2

来源路径：`Query/Player/Join/join_queries.sql`。

```sql
SELECT team.founded_year, team.team_name, player.name, player.team FROM player JOIN team ON player.team = team.team_name;
```

```text
[R] π team.founded_year, team.team_name, player.name, player.team
└─ [R] ⋈ player.team = team.team_name
   ├─ [S] SEM_MAP 提取 player 查询字段及连接键
   │  └─ [R] Scan player 原文
   └─ [S] SEM_MAP 提取 team 查询字段及连接键
      └─ [R] Scan team 原文
```

#### bench-u/Player/Join/join_queries/3

来源路径：`Query/Player/Join/join_queries.sql`。

```sql
SELECT team.ownership, player.name, player.mvp_awards, team.championships FROM player JOIN team ON player.team = team.team_name;
```

```text
[R] π team.ownership, player.name, player.mvp_awards, team.championships
└─ [R] ⋈ player.team = team.team_name
   ├─ [S] SEM_MAP 提取 player 查询字段及连接键
   │  └─ [R] Scan player 原文
   └─ [S] SEM_MAP 提取 team 查询字段及连接键
      └─ [R] Scan team 原文
```

### C07 斑马影像观测汇总

历史登记状态：`CANDIDATE_MEDIA_PENDING`。媒体标签可追溯；城市/站点是构造字段，不能称真实生态共现证据；音频不是此簇必要输入。

#### sembench/animals/Q1

来源路径：`files/animals/query/natural_language/Q1.txt`。

```text
How many pictures of zebras do we have in our database?
```

```text
[R] γ COUNT(*)
   └─ [S] SEM_FILTER zebra(Images)
      └─ [R] Scan Images 与所需位置关系
```

#### sembench/animals/Q3

来源路径：`files/animals/query/natural_language/Q3.txt`。

```text
What is the city where we captured most pictures of zebras (ties are broken arbitrarily, consider only cities with at least one zebra picture)?
```

```text
[R] Limit 1（并列任取）
   └─ [R] Sort count DESC
      └─ [R] γ city; COUNT(*)
         └─ [R] ⋈ 公开位置键
            └─ [S] SEM_FILTER zebra(Images)
               └─ [R] Scan Images 与所需位置关系
```

#### sembench/animals/Q10

来源路径：`files/animals/query/natural_language/Q10.txt`。

```text
What is the city and station with most associated pictures showing zebras (ties are broken arbitrarily, only consider cities with at least one zebra picture)?
```

```text
[R] Limit 1（并列任取）
   └─ [R] Sort count DESC
      └─ [R] γ city,station; COUNT(*)
         └─ [R] ⋈ 公开位置键
            └─ [S] SEM_FILTER zebra(Images)
               └─ [R] Scan Images 与所需位置关系
```

### C08 图像与声音物种证据目录

历史登记状态：`CANDIDATE_MEDIA_PENDING`。只表达冻结库中的观测覆盖；拒绝由合成地点关系推出自然生态结论；音频LOTUS适配需实际核验。

#### sembench/animals/Q2

来源路径：`files/animals/query/natural_language/Q2.txt`。

```text
How many sound recordings of elephants do we have in our database?
```

```text
[R] γ COUNT(*)
   └─ [S] SEM_FILTER elephant(Audio)
      └─ [R] Scan Audio 与所需位置关系
```

#### sembench/animals/Q4

来源路径：`files/animals/query/natural_language/Q4.txt`。

```text
What is the city for which we have most recordings of elephants (ties are broken arbitrarily, consider only cities with at least one elephant recording)?
```

```text
[R] Limit 1（并列任取）
   └─ [R] Sort count DESC
      └─ [R] γ city; COUNT(*)
         └─ [R] ⋈ 公开位置键
            └─ [S] SEM_FILTER elephant(Audio)
               └─ [R] Scan Audio 与所需位置关系
```

#### sembench/animals/Q5

来源路径：`files/animals/query/natural_language/Q5.txt`。

```text
What is the list of cities for which we have either images or audio recordings of elephants?
```

```text
[R] UNION（city集合）
├─ [R] δ π city
│  └─ [R] ⋈ 公开站点/城市关联
│     └─ [S] SEM_FILTER elephant(Images)
│        └─ [R] Scan Images, location relations
└─ [R] δ π city
   └─ [R] ⋈ 公开站点/城市关联
      └─ [S] SEM_FILTER elephant(Audio)
         └─ [R] Scan Audio, location relations
```

#### sembench/animals/Q6

来源路径：`files/animals/query/natural_language/Q6.txt`。

```text
For which cities do we have images of monkeys but no audio recordings of monkeys?
```

```text
[R] EXCEPT / AntiJoin（city集合）
├─ [R] δ π city
│  └─ [R] ⋈ 公开站点/城市关联
│     └─ [S] SEM_FILTER monkey(Images)
│        └─ [R] Scan Images, location relations
└─ [R] δ π city
   └─ [R] ⋈ 公开站点/城市关联
      └─ [S] SEM_FILTER monkey(Audio)
         └─ [R] Scan Audio, location relations
```

#### sembench/animals/Q7

来源路径：`files/animals/query/natural_language/Q7.txt`。

```text
What are the cities for which zebras and impala co-occur, i.e., we have at least one image of a zebra and at least one image of an impala?
```

```text
[R] INTERSECT / SemiJoin（city集合）
├─ [R] δ π city
│  └─ [R] ⋈ 公开站点/城市关联
│     └─ [S] SEM_FILTER zebra(Images)
│        └─ [R] Scan Images, location relations
└─ [R] δ π city
   └─ [R] ⋈ 公开站点/城市关联
      └─ [S] SEM_FILTER impala(Images)
         └─ [R] Scan Images, location relations
```

#### sembench/animals/Q8

来源路径：`files/animals/query/natural_language/Q8.txt`。

```text
What is the list of cities for which we found at least one image or audio recording of elephants and at least one image or audio recording of monkeys?
```

```text
[R] INTERSECT（city）
├─ [R] UNION（大象图像城市，大象声音城市）
│  └─ [R] δ π city ← 位置连接 ← [S] 各模态大象筛选 ← Scan
└─ [R] UNION（猴子图像城市，猴子声音城市）
   └─ [R] δ π city ← 位置连接 ← [S] 各模态猴子筛选 ← Scan
```

#### sembench/animals/Q9

来源路径：`files/animals/query/natural_language/Q9.txt`。

```text
What is the list of cities for which we have both images and audio recordings of monkeys?
```

```text
[R] INTERSECT / SemiJoin（city集合）
├─ [R] δ π city
│  └─ [R] ⋈ 公开站点/城市关联
│     └─ [S] SEM_FILTER monkey(Images)
│        └─ [R] Scan Images, location relations
└─ [R] δ π city
   └─ [R] ⋈ 公开站点/城市关联
      └─ [S] SEM_FILTER monkey(Audio)
         └─ [R] Scan Audio, location relations
```

### C09 车辆材料损伤检查目录

历史登记状态：`HOLD_SYNTHETIC_ENTITY_AUDIT`。异源投诉/图片/音频经生成器配车，不是已核实同一真实车况。仅可作为合成基准；维修决策无gold。

#### sembench/cars/Q1

来源路径：`files/cars/query/natural_language/Q1.txt`。

```text
Find cars that were in a crash/accident/collision.
```

```text
[R] π car_id
   └─ [S] SEM_FILTER crash/accident/collision(complaint)
      └─ [R] Scan complaints 与所需car关联
```

#### sembench/cars/Q7

来源路径：`files/cars/query/natural_language/Q7.txt`。

```text
Find cars that are either dented (image), have worn out brakes (audio), or have electrical system problems (text), i.e., damaged at least according to a single modality.
```

```text
[R] δ UNION car IDs
├─ [R] π car_id ← [S] SEM_FILTER dent(image) ← [R] Scan images+关联
├─ [R] π car_id ← [S] SEM_FILTER worn_brakes(audio) ← [R] Scan audio+关联
└─ [R] π car_id ← [S] SEM_FILTER electrical_problem(text) ← [R] Scan complaints+关联
```

#### sembench/cars/Q10

来源路径：`files/cars/query/natural_language/Q10.txt`。

```text
For all complaints, classify which car component is problematic according to the complaint.
```

```text
[R] π complaint_id,component
   └─ [S] SEM_MAP complaint → component
      └─ [R] Scan complaints 与所需car关联
```

### C10 电影多标签类型索引

历史登记状态：`CANDIDATE_GOLD_COMPLETENESS_PENDING`。QA答案不自动覆盖所有负例；romcom等子类与父类规则需先冻结；源JSON的ground_truth禁止公开。

#### sembench/mmqa/Q3A

来源路径：`files/mmqa/query/natural_language/q3a.json`。

```text
Which movies are comedies?
```

```text
[R] δ π movie
   └─ [S] SEM_FILTER comedies
      └─ [R] 按公开ID组装电影证据
         └─ [R] Scan text/table/image
```

#### sembench/mmqa/Q3B

来源路径：`files/mmqa/query/natural_language/q3b.json`。

```text
Which movies are sci-fi?
```

```text
[R] δ π movie
   └─ [S] SEM_FILTER sci-fi
      └─ [R] 按公开ID组装电影证据
         └─ [R] Scan text/table/image
```

#### sembench/mmqa/Q3C

来源路径：`files/mmqa/query/natural_language/q3c.json`。

```text
Which movies are romances?
```

```text
[R] δ π movie
   └─ [S] SEM_FILTER romances
      └─ [R] 按公开ID组装电影证据
         └─ [R] Scan text/table/image
```

#### sembench/mmqa/Q3D

来源路径：`files/mmqa/query/natural_language/q3d.json`。

```text
Which movies are horror?
```

```text
[R] δ π movie
   └─ [S] SEM_FILTER horror
      └─ [R] 按公开ID组装电影证据
         └─ [R] Scan text/table/image
```

#### sembench/mmqa/Q3E

来源路径：`files/mmqa/query/natural_language/q3e.json`。

```text
Which movies are heist movies?
```

```text
[R] δ π movie
   └─ [S] SEM_FILTER heist movies
      └─ [R] 按公开ID组装电影证据
         └─ [R] Scan text/table/image
```

#### sembench/mmqa/Q3F

来源路径：`files/mmqa/query/natural_language/q3f.json`。

```text
Which movies are romantic comedies?
```

```text
[R] δ π movie
   └─ [S] SEM_FILTER romantic comedies
      └─ [R] 按公开ID组装电影证据
         └─ [R] Scan text/table/image
```

#### sembench/mmqa/Q3G

来源路径：`files/mmqa/query/natural_language/q3g.json`。

```text
Which movies are biographical comedies?
```

```text
[R] δ π movie
   └─ [S] SEM_FILTER biographical comedies
      └─ [R] 按公开ID组装电影证据
         └─ [R] Scan text/table/image
```

#### sembench/mmqa/Q4

来源路径：`files/mmqa/query/natural_language/q4.json`。

```text
Categorize the movies in the table by their genre. If a movie belongs to multiple genres, list it under each applicable genre.
```

```text
[R] γ genre; collect movies
   └─ [R] Unnest genres
      └─ [S] SEM_MAP 电影证据 → 多标签genres
         └─ [R] Scan 电影表及关联证据
```

### C11 航线目的地与航司logo目录

历史登记状态：`HOLD_EVIDENCE_COMPLETENESS`。不能把QA未返回项直接标False；目的地从城市到国家/洲的映射须给所有方法同样公开。

#### sembench/mmqa/Q6A

来源路径：`files/mmqa/query/natural_language/q6a.json`。

```text
Which airlines have destinations in Frankfurt?
```

```text
[R] δ π airline
   └─ [R] σ destination_scope = Frankfurt
      └─ [S] SEM_MAP 航线证据 → airline,destination,地域归属
         └─ [R] Scan 航线表/文字及所需图像
```

#### sembench/mmqa/Q6B

来源路径：`files/mmqa/query/natural_language/q6b.json`。

```text
Which airlines have destinations in Germany?
```

```text
[R] δ π airline
   └─ [R] σ destination_scope = Germany
      └─ [S] SEM_MAP 航线证据 → airline,destination,地域归属
         └─ [R] Scan 航线表/文字及所需图像
```

#### sembench/mmqa/Q6C

来源路径：`files/mmqa/query/natural_language/q6c.json`。

```text
Which airlines have destinations in Europe?
```

```text
[R] δ π airline
   └─ [R] σ destination_scope = Europe
      └─ [S] SEM_MAP 航线证据 → airline,destination,地域归属
         └─ [R] Scan 航线表/文字及所需图像
```

#### sembench/mmqa/Q7

来源路径：`files/mmqa/query/natural_language/q7.json`。

```text
[R] π airline,logo（缺失保留）
└─ [R] LeftJoin airline = logo.airline
   ├─ [R] δ π airline
   │  └─ [R] σ destination_scope = Europe
   │     └─ [S] SEM_MAP 航线证据 → airline,destination,地域归属
   │        └─ [R] Scan 航线表与文字
   └─ [S] SEM_MAP 图像/上下文 → 航司logo关联
      └─ [R] Scan 图像与关联上下文
```

```text
[R] π airline,logo（缺失保留）
   └─ [R] LeftJoin airline=logo.airline
      └─ [S] SEM_MAP 图像/上下文 → 航司logo关联（独立输入分支）
         └─ [R] σ destination_scope = Europe
            └─ [S] SEM_MAP 航线证据 → airline,destination,地域归属
               └─ [R] Scan 航线表/文字及所需图像
```

### C12 多模态症状材料登记

历史登记状态：`HOLD_CLINICAL_VALIDITY`。生成患者和异源材料不是真实关联病历；不合并skin和lung为相互矛盾的健康结论，不作诊断有效性声明。

#### sembench/medical/Q1

来源路径：`files/medical/query/natural_language/Q1.txt`。

```text
Which patients have symptoms of allergy in our database?
```

```text
[R] π patient_id
   └─ [S] SEM_FILTER allergy(symptoms)
      └─ [R] Scan symptoms 与所需patient关系
```

#### sembench/medical/Q4

来源路径：`files/medical/query/natural_language/Q4.txt`。

```text
What is an average age of patients with acne?
```

```text
[R] γ AVG(age)
   └─ [R] ⋈ patient_id（关联公开年龄）
      └─ [S] SEM_FILTER acne(symptoms)
         └─ [R] Scan symptoms 与所需patient关系
```

#### sembench/medical/Q10

来源路径：`files/medical/query/natural_language/Q10.txt`。

```text
For all symptoms, generate disease name from a given list of diseases.
```

```text
[R] π symptom_id,disease
   └─ [S] SEM_MAP symptoms → 给定疾病目录
      └─ [R] Scan symptoms 与所需patient关系
```

### C13 年度报告字段核对表

历史登记状态：`CANDIDATE_RAW_DOCUMENTS_PENDING`。100份原文约413.6MB未下载；原列名bussiness_cost保留；禁止跨币种/年度直接平均金额。

#### bench-u/Finan/Select/select_queries/1

来源路径：`Query/Finan/Select/select_queries.sql`。

```sql
SELECT earnings_per_share FROM finance;
```

```text
[R] π earnings_per_share
   └─ [S] SEM_MAP 从原始材料提取本题字段（含过滤/分组键）
      └─ [R] Scan Finan 原始材料
```

#### bench-u/Finan/Select/select_queries/2

来源路径：`Query/Finan/Select/select_queries.sql`。

```sql
SELECT principal_activities, remuneration_policy, bussiness_cost, company_name FROM finance;
```

```text
[R] π principal_activities, remuneration_policy, bussiness_cost, company_name
   └─ [S] SEM_MAP 从原始材料提取本题字段（含过滤/分组键）
      └─ [R] Scan Finan 原始材料
```

#### bench-u/Finan/Select/select_queries/3

来源路径：`Query/Finan/Select/select_queries.sql`。

```sql
SELECT total_assets, remuneration_policy FROM finance;
```

```text
[R] π total_assets, remuneration_policy
   └─ [S] SEM_MAP 从原始材料提取本题字段（含过滤/分组键）
      └─ [R] Scan Finan 原始材料
```

### C14 作品构图与色彩目录

历史登记状态：`HOLD_SCHEMA_AUDIT`。当前暂不接受未核name含义的组合；1000份WikiArt材料没有自动形成符合批次语义的任务。

#### bench-u/Art/Select/select_queries/1

来源路径：`Query/Art/Select/select_queries.sql`。

```sql
SELECT color FROM art;
```

```text
[R] π color
   └─ [S] SEM_MAP 从原始材料提取本题字段（含过滤/分组键）
      └─ [R] Scan Art 原始材料
```

#### bench-u/Art/Select/select_queries/2

来源路径：`Query/Art/Select/select_queries.sql`。

```sql
SELECT composition, name FROM art;
```

```text
[R] π composition, name
   └─ [S] SEM_MAP 从原始材料提取本题字段（含过滤/分组键）
      └─ [R] Scan Art 原始材料
```

#### bench-u/Art/Select/select_queries/3

来源路径：`Query/Art/Select/select_queries.sql`。

```sql
SELECT name FROM art;
```

```text
[R] π name
   └─ [S] SEM_MAP 从原始材料提取本题字段（含过滤/分组键）
      └─ [R] Scan Art 原始材料
```

### C15 疾病相关药物资料目录

历史登记状态：`HOLD_SCALE_AND_GOLD_AUDIT`。10万原文和分表实体关系未下载校验；非用药建议、非患者级治疗gold。

#### bench-u/Med/Join/join_queries/1

来源路径：`Query/Med/Join/join_queries.sql`。

```sql
SELECT disease.diagnostic_methods, drug.manufacturer, drug.brand_name, disease.disease_name FROM drug JOIN disease ON drug.disease_name = disease.disease_name;
```

```text
[R] π disease.diagnostic_methods, drug.manufacturer, drug.brand_name, disease.disease_name
└─ [R] ⋈ drug.disease_name = disease.disease_name
   ├─ [S] SEM_MAP 提取 drug 查询字段及连接键
   │  └─ [R] Scan drug 原文
   └─ [S] SEM_MAP 提取 disease 查询字段及连接键
      └─ [R] Scan disease 原文
```

#### bench-u/Med/Join/join_queries/2

来源路径：`Query/Med/Join/join_queries.sql`。

```sql
SELECT drug.mechanism_of_action, drug.storage_conditions, disease.diagnosis_challenges, disease.disease_name FROM drug JOIN disease ON drug.disease_name = disease.disease_name;
```

```text
[R] π drug.mechanism_of_action, drug.storage_conditions, disease.diagnosis_challenges, disease.disease_name
└─ [R] ⋈ drug.disease_name = disease.disease_name
   ├─ [S] SEM_MAP 提取 drug 查询字段及连接键
   │  └─ [R] Scan drug 原文
   └─ [S] SEM_MAP 提取 disease 查询字段及连接键
      └─ [R] Scan disease 原文
```

#### bench-u/Med/Join/join_queries/3

来源路径：`Query/Med/Join/join_queries.sql`。

```sql
SELECT drug.single_dose, disease.pathogenesis, drug.recommended_usage, disease.diagnosis_challenges FROM drug JOIN disease ON drug.disease_name = disease.disease_name;
```

```text
[R] π drug.single_dose, disease.pathogenesis, drug.recommended_usage, disease.diagnosis_challenges
└─ [R] ⋈ drug.disease_name = disease.disease_name
   ├─ [S] SEM_MAP 提取 drug 查询字段及连接键
   │  └─ [R] Scan drug 原文
   └─ [S] SEM_MAP 提取 disease 查询字段及连接键
      └─ [R] Scan disease 原文
```

## B. 五湖派生查询：逐题计划

这些是本项目构造的查询，不是五个来源benchmark原生发布的20条SQL。Q1语义流程仅有契约；Q2–Q4确定性执行已实现。下图按冻结dag逐节点翻转画出；Q1是共享子计划引用，实际复用时形成DAG。retrieve节点的内部检索实现未冻结，不能当成已执行的语义推理。

### stard

原相关性标签不保证完整依据或回答充分性；全量关联校验不等于语义正确。

[冻结契约](../workloads/stard-batch/queries.json)

#### stard-Q1-v1

For every question in records.json, return a ranked, duplicate-free list of relevant article IDs from lake/catalog.jsonl. Use the frozen article corpus. This is relevant-article retrieval, not a legal ruling or a complete legal answer. Do not infer that unannotated or unreturned articles are legally inapplicable.

```text
[R] validate_article_ids
   └─ [S] sem_map_relevance_rank
      └─ [未冻结实现] retrieve_full_catalog
         └─ [S] sem_map_decompose_issues
            └─ [R] scan_questions
```

#### stard-Q2-v1

返回涉及指定法条的咨询记录清单与数量

```text
[R] count
   └─ [R] project_record_id
      └─ [R] filter_predicted_label_or_prefix
         └─ [引用] Q1
```

#### stard-Q3-v1

按法条统计命中的咨询数，生成咨询—法条索引

```text
[R] emit_completeness
   └─ [R] count_distinct_records
      └─ [R] group_by_label_and_source_entity
         └─ [R] unnest_unique_labels
            └─ [引用] Q1
```

#### stard-Q4-v1

返回未完成记录及原因，并报告全量coverage；缺事实和运行失败均需保留原因，不当负例。

```text
[R] coverage
   └─ [R] project_id_reason
      └─ [R] filter_status_ABSTAIN
         └─ [引用] Q1
```

### annoctr

3348条源TECHNIQUE正链接中11条指向软件，另18条技术链接缺KG；原gold全部保留，29条不在578技术输出catalog中，不能将不可达标签当模型语义错误。湖含120报告，当前给定提及覆盖112报告。原文保留明示ID捷径。

[冻结契约](../workloads/annoctr-batch/queries.json)

#### annoctr-Q1-v1

For every supplied mention and its context, use its complete report and frozen definitions to return the ATT&CK technique ID(s) it denotes. Boundaries and technical-mention selection are given. This is conditional linking of published positive annotations, not end-to-end detection, negative detection, or a complete report inventory. Preserve subtechnique specificity: use Txxxx.xxx, without collapsing to the parent. Return a duplicate-free list.

```text
[R] normalize_original_id_granularity
   └─ [S] sem_map_link_technique
      └─ [未冻结实现] retrieve_definitions
         └─ [R] read_report_context
            └─ [R] scan_given_mentions
```

#### annoctr-Q2-v1

返回链接到指定技术的提及清单，并关联所属报告

```text
[R] count
   └─ [R] project_record_id
      └─ [R] filter_predicted_label_or_prefix
         └─ [引用] Q1
```

#### annoctr-Q3-v1

对本批给定提及按报告归并技术集合，同时区分提及数与报告数

```text
[R] emit_completeness
   └─ [R] count_distinct_records
      └─ [R] group_by_label_and_source_entity
         └─ [R] unnest_unique_labels
            └─ [引用] Q1
```

#### annoctr-Q4-v1

返回未完成记录及原因，并报告全量coverage；缺事实和运行失败均需保留原因，不当负例。

```text
[R] coverage
   └─ [R] project_id_reason
      └─ [R] filter_status_ABSTAIN
         └─ [引用] Q1
```

### codiesp

原标签已有侧别及词义冲突；119份无P标注只作原集合空集；SEDOM历史资源未闭合；X不与P混评。

[冻结契约](../workloads/codiesp-batch/queries.json)

#### codiesp-Q1-v1

For every complete Spanish case report, return a ranked, duplicate-free list of procedure codes under the supplied CodiEsp guidelines and frozen 2018 coding resources. Use lowercase codes and preserve allowed four- or seven-character specificity; do not invent missing axes. Code mention scope under the task guidelines, not whether a procedure actually occurred. Include all reports; an empty completed list means no selected codable mentions, not absence of real procedures. This task is P, not D or X.

```text
[R] rank_unique_codes
   └─ [S] sem_map_resolve_axes_and_specificity
      └─ [未冻结实现] retrieve_code_candidates_and_guidelines
         └─ [S] sem_map_procedure_mentions
            └─ [R] scan_full_reports
```

#### codiesp-Q2-v1

返回含指定操作代码提及的报告清单；不解释为患者接受该操作

```text
[R] count
   └─ [R] project_record_id
      └─ [R] filter_predicted_label_or_prefix
         └─ [引用] Q1
```

#### codiesp-Q3-v1

按操作代码统计报告数；不把重复提及或同论文病例算成独立患者

```text
[R] emit_completeness
   └─ [R] count_distinct_records
      └─ [R] group_by_label_and_source_entity
         └─ [R] unnest_unique_labels
            └─ [引用] Q1
```

#### codiesp-Q4-v1

返回未完成记录及原因，并报告全量coverage；缺事实和运行失败均需保留原因，不当负例。

```text
[R] coverage
   └─ [R] project_id_reason
      └─ [R] filter_status_ABSTAIN
         └─ [引用] Q1
```

### hscodecomp

图片、单位价格、外部裁定及汇率事实未闭合；不可用缺事实造成的失败证明Agent优势。

[冻结契约](../workloads/hscodecomp-batch/queries.json)

#### hscodecomp-Q1-v1

For every product in records.json, use its published title, attributes, price, currency and marketplace categories with frozen HTS 2025 Revision 15 to return one 10-digit HTS code as a singleton string list. Consult hierarchy, unnumbered parent rows and full notes. Do not assume price is per item, invent photos, convert currency without evidence, or reconstruct missing product facts. If a supported classification cannot be completed, ABSTAIN with null value and a concrete reason. The source-label task supplies no independent UNKNOWN gold.

```text
[R] validate_10_digit_code_or_abstain
   └─ [S] sem_map_resolve_exclusions_and_classification
      └─ [未冻结实现] retrieve_hts_tree_and_notes
         └─ [S] sem_map_extract_material_use_unit_facts
            └─ [R] scan_products
```

#### hscodecomp-Q2-v1

按参数化2/4/6/8/10位编码前缀返回商品清单及数量

```text
[R] count
   └─ [R] project_record_id
      └─ [R] filter_predicted_label_or_prefix
         └─ [引用] Q1
```

#### hscodecomp-Q3-v1

按预测完整编码统计商品数；前缀筛选为派生诊断，不是独立专家gold

```text
[R] emit_completeness
   └─ [R] count_distinct_records
      └─ [R] group_by_label_and_source_entity
         └─ [R] unnest_unique_labels
            └─ [引用] Q1
```

#### hscodecomp-Q4-v1

返回未完成记录及原因，并报告全量coverage；缺事实和运行失败均需保留原因，不当负例。

```text
[R] coverage
   └─ [R] project_id_reason
      └─ [R] filter_status_ABSTAIN
         └─ [引用] Q1
```

### udrp

仍有4处既有残余instruction-transfer词面标记，语义泄漏未清；外部调查未封存；1513/59严重偏斜；禁止将本构造视为可用预测实验证据。

[冻结契约](../workloads/udrp-batch/queries.json)

#### udrp-Q1-v1

For each supplied case, apply the frozen WIPO Overview 3.0 to attributed party contentions and recorded facts, and return a singleton list containing RELIEF_GRANTED or DENIED. Missing support is not a denial: ABSTAIN with null value and a reason when unable to complete. These are retrospective pre-analysis case extracts, not original filings. This query is registered for inspection: residual answer leakage and external-fact gaps remain, so it is not an evaluation-ready prediction benchmark.

```text
[R] combine_decision_or_abstain
   └─ [S] sem_map_evaluate_three_elements
      └─ [未冻结实现] retrieve_overview_elements_and_exceptions
         └─ [R] scan_attributed_case_facts
```

#### udrp-Q2-v1

筛出预测驳回案件，生成需复核的少数类清单

```text
[R] count
   └─ [R] project_record_id
      └─ [R] filter_predicted_label_or_prefix
         └─ [引用] Q1
```

#### udrp-Q3-v1

统计两种预测决定及未完成数量；不得只报多数类准确率

```text
[R] emit_completeness
   └─ [R] count_distinct_records
      └─ [R] group_by_label_and_source_entity
         └─ [R] unnest_unique_labels
            └─ [引用] Q1
```

#### udrp-Q4-v1

返回未完成记录及原因，并报告全量coverage；缺事实和运行失败均需保留原因，不当负例。

```text
[R] coverage
   └─ [R] project_id_reason
      └─ [R] filter_status_ABSTAIN
         └─ [引用] Q1
```

## C. 不混入原题表的已有控制

- PCB：`[R] COUNT ← [R] π record_id ← [S] 铜缺陷SEM_FILTER ← [R] Scan tested/template pairs`。语义任务可由固定视觉算法实现；语义算子不等于必须调用LLM。
- CUAD：`[R] π contract_id,category,span ← [R] Unnest spans ← [S] SEM_MAP 合同→条款集合 ← [R] Scan contracts`。这是抽取任务；本轮没有凭空添加合同风险聚合。
- BioDEX：`[R] π report_id,ranked_terms ← [S] 术语归一/排序 ← [S] 事件抽取 ← [R] Scan reports + 公开术语目录`。目录关联的内部策略依具体比较臂而异。
- DataSpace task184派生基金任务：虽然通过自然语言/Agent探索SQLite，但已有手写SQL完整完成，不能仅因使用Agent就判定数据路径存在必需语义算子。

## 组合与复用的具体含义

Movie的情感列可同时服务清单、计数、比例、分组；Animals的“城市×物种×模态存在关系”可服务UNION/INTERSECT/EXCEPT；ecomm规范品牌/颜色/类别可服务多路等值join；论文抽取表可服务过滤与COUNT。值得提取的边界是这些有稳定输入输出的中间关系，而不是把整段query和实例答案固化。

NULL、ABSTAIN、空集合、无观测和语义否定必须分开。正向比例的分母不能偷偷删除失败行；COUNT(field)不能改COUNT(*)；LIMIT无ORDER BY不能补造排名；集合查询需要去重，SQL多重集查询不应任意去重。五湖Q2/Q3只消费已经产生的标签，不会自动修复Q1错误。
