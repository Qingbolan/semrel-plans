# 具体用例

**例 1：Movie Q7，评论之间的语义 join**（Table 4(a)，p.9）。查询把评论两两配对，判断情感是否相同或相反。这是 Movie 场景中唯一没有 LIMIT 的 join 查询，也是成本差异最大的一条。

| 系统 | 费用 | 质量 | 延迟 |
|---|---:|---:|---:|
| LOTUS | $1.81 | 0.21 | 431.8 s |
| Palimpzest | $7.72 | 0.68 | 1056.1 s |
| ThalamusDB | $0.15 | 0.57 | 636.9 s |
| BigQuery | $3.31 | 0.70 | 198.3 s |

LOTUS 先用嵌入距离筛选候选对，ThalamusDB 在一个提示里批量判断多行，两者都更便宜，但质量也受到影响（§5.3，p.8）。

**例 2：Wildlife，图像与音频上的过滤**（Example 4.2，p.4）。

```sql
SELECT DISTINCT city
FROM (SELECT city FROM ImageTable I WHERE AI.IF(I.image, 'the picture shows an elephant'))
UNION (SELECT city FROM AudioTable A WHERE AI.IF(A.audio, 'this sounds like an elephant'));
```

输入是带图片或音频列的记录表，“找大象”是查询意图，不是输入数据。§5.4 以 Q5（城市中有大象的图片或录音）为例：ThalamusDB 一旦为某个城市找到证据就停止求值该城市的其余行，所以费用远低于其他系统（p.11）。

Wildlife Q7 问的是斑马与黑斑羚共现的城市。规模越大，每个城市的支持行越多，系统至少判对一行的机会越大，所以质量随规模略有上升（§5.4）。

**例 3：MMQA，航空公司与 logo 的跨模态 join**（Example 4.5，p.6）。

```sql
SELECT t.Airlines, i.uri
FROM mmqa.tampa_international_airport t, mmqa.images i
WHERE AI.IF("... Determine if the image shows the logo of the airline. Airline: ", t.Airlines, ", Image: ", i.uri);
```

这类 join 在基础规模 200 下需要 40,000 次 LLM 调用。MMQA Q7 在 Palimpzest 上耗时超过 35 分钟，在 LOTUS 上接近 40 分钟，单条查询的费用是一条过滤查询的 1,000 倍以上（§5.3，p.10）。

依据：[arXiv 2511.01716v2](https://arxiv.org/abs/2511.01716v2)，Examples 4.2、4.5，§5.3–5.4，Table 4，PDF pp.4–11。
