# sembench-animals：逐查询逻辑计划

[返回总表](README.md)

图从下往上读：输入 → 算子 → 输出。S为语义算子；R为确定性关系/辅助步骤。检索与未决节点在标签中单独注明。

## sembench/animals/Q1

来源：[原件](</Volumes/Element/Github2/semantic-workload-bench/data/semantic-query-discovery-20260908/sembench/checkout/files/animals/query/natural_language/Q1.txt>) · `native_nl_reconstructed` · `logical_only` · `substantive_relational`

```text

How many pictures of zebras do we have in our database?

```

```mermaid
flowchart BT
  n0["R · Aggregate | 全局; COUNT(*)"]
  n1["S · SFilter | 包含 zebra"]
  n2["R · Scan | ImageData"]
  n2 --> n1
  n1 --> n0
  classDef semantic fill:#fff0d6,stroke:#9a5b00,color:#332000;
  class n1 semantic;
```

 图依据原自然语言重建；扫描中的关联媒体是概念输入，不假定已核对物理表名/外键。

## sembench/animals/Q2

来源：[原件](</Volumes/Element/Github2/semantic-workload-bench/data/semantic-query-discovery-20260908/sembench/checkout/files/animals/query/natural_language/Q2.txt>) · `native_nl_reconstructed` · `logical_only` · `substantive_relational`

```text

How many sound recordings of elephants do we have in our database?

```

```mermaid
flowchart BT
  n0["R · Aggregate | 全局; COUNT(*)"]
  n1["S · SFilter | 包含 elephant"]
  n2["R · Scan | AudioData"]
  n2 --> n1
  n1 --> n0
  classDef semantic fill:#fff0d6,stroke:#9a5b00,color:#332000;
  class n1 semantic;
```

 图依据原自然语言重建；扫描中的关联媒体是概念输入，不假定已核对物理表名/外键。

## sembench/animals/Q3

来源：[原件](</Volumes/Element/Github2/semantic-workload-bench/data/semantic-query-discovery-20260908/sembench/checkout/files/animals/query/natural_language/Q3.txt>) · `native_nl_reconstructed` · `logical_only` · `substantive_relational`

```text

What is the city where we captured most pictures of zebras (ties are broken arbitrarily, consider only cities with at least one zebra picture)?

```

```mermaid
flowchart BT
  n0["R · Project | city"]
  n1["R · Limit | 1; 未指定顺序"]
  n2["R · Sort | cnt DESC"]
  n3["R · Aggregate | city; COUNT(*) AS cnt"]
  n4["S · SFilter | 包含 zebra"]
  n5["R · Scan | ImageData"]
  n5 --> n4
  n4 --> n3
  n3 --> n2
  n2 --> n1
  n1 --> n0
  classDef semantic fill:#fff0d6,stroke:#9a5b00,color:#332000;
  class n4 semantic;
```

NL允许任意打破并列；随库gold SQL用cnt=MAX(cnt)返回所有并列。图按NL保留一项；不能称二者完全等价。 图依据原自然语言重建；扫描中的关联媒体是概念输入，不假定已核对物理表名/外键。

## sembench/animals/Q4

来源：[原件](</Volumes/Element/Github2/semantic-workload-bench/data/semantic-query-discovery-20260908/sembench/checkout/files/animals/query/natural_language/Q4.txt>) · `native_nl_reconstructed` · `logical_only` · `substantive_relational`

```text

What is the city for which we have most recordings of elephants (ties are broken arbitrarily, consider only cities with at least one elephant recording)?

```

```mermaid
flowchart BT
  n0["R · Project | city"]
  n1["R · Limit | 1; 未指定顺序"]
  n2["R · Sort | cnt DESC"]
  n3["R · Aggregate | city; COUNT(*) AS cnt"]
  n4["S · SFilter | 包含 elephant"]
  n5["R · Scan | AudioData"]
  n5 --> n4
  n4 --> n3
  n3 --> n2
  n2 --> n1
  n1 --> n0
  classDef semantic fill:#fff0d6,stroke:#9a5b00,color:#332000;
  class n4 semantic;
```

NL允许任意打破并列；随库gold SQL用cnt=MAX(cnt)返回所有并列。图按NL保留一项；不能称二者完全等价。 图依据原自然语言重建；扫描中的关联媒体是概念输入，不假定已核对物理表名/外键。

## sembench/animals/Q5

来源：[原件](</Volumes/Element/Github2/semantic-workload-bench/data/semantic-query-discovery-20260908/sembench/checkout/files/animals/query/natural_language/Q5.txt>) · `native_nl_reconstructed` · `logical_only` · `substantive_relational`

```text

What is the list of cities for which we have either images or audio recordings of elephants?

```

```mermaid
flowchart BT
  n0["R · Union | UNION DISTINCT"]
  n1["R · Distinct | 集合语义"]
  n2["R · Project | city"]
  n3["S · SFilter | 识别 elephant"]
  n4["R · Scan | ImageData"]
  n5["R · Distinct | 集合语义"]
  n6["R · Project | city"]
  n7["S · SFilter | 识别 elephant"]
  n8["R · Scan | AudioData"]
  n4 --> n3
  n3 --> n2
  n2 --> n1
  n1 --> n0
  n8 --> n7
  n7 --> n6
  n6 --> n5
  n5 --> n0
  classDef semantic fill:#fff0d6,stroke:#9a5b00,color:#332000;
  class n3,n7 semantic;
```

 图依据原自然语言重建；扫描中的关联媒体是概念输入，不假定已核对物理表名/外键。

## sembench/animals/Q6

来源：[原件](</Volumes/Element/Github2/semantic-workload-bench/data/semantic-query-discovery-20260908/sembench/checkout/files/animals/query/natural_language/Q6.txt>) · `native_nl_reconstructed` · `logical_only` · `substantive_relational`

```text

For which cities do we have images of monkeys but no audio recordings of monkeys?

```

```mermaid
flowchart BT
  n0["R · AntiJoin | I.city = A.city；不存在猴子音频记录"]
  n1["R · Distinct | 集合语义"]
  n2["R · Project | city"]
  n3["S · SFilter | 识别 monkey"]
  n4["R · Scan | ImageData"]
  n5["R · Distinct | 集合语义"]
  n6["R · Project | city"]
  n7["S · SFilter | 识别 monkey"]
  n8["R · Scan | AudioData"]
  n4 --> n3
  n3 --> n2
  n2 --> n1
  n1 --> n0
  n8 --> n7
  n7 --> n6
  n6 --> n5
  n5 --> n0
  classDef semantic fill:#fff0d6,stroke:#9a5b00,color:#332000;
  class n3,n7 semantic;
```

 图依据原自然语言重建；扫描中的关联媒体是概念输入，不假定已核对物理表名/外键。

## sembench/animals/Q7

来源：[原件](</Volumes/Element/Github2/semantic-workload-bench/data/semantic-query-discovery-20260908/sembench/checkout/files/animals/query/natural_language/Q7.txt>) · `native_nl_reconstructed` · `logical_only` · `substantive_relational`

```text

What are the cities for which zebras and impala co-occur, i.e., we have at least one image of a zebra and at least one image of an impala?

```

```mermaid
flowchart BT
  n0["R · Intersect | 城市集合交集"]
  n1["R · Distinct | 集合语义"]
  n2["R · Project | city"]
  n3["S · SFilter | 识别 zebra"]
  n4["R · Scan | ImageData"]
  n5["R · Distinct | 集合语义"]
  n6["R · Project | city"]
  n7["S · SFilter | 识别 impala"]
  n8["R · Scan | ImageData"]
  n4 --> n3
  n3 --> n2
  n2 --> n1
  n1 --> n0
  n8 --> n7
  n7 --> n6
  n6 --> n5
  n5 --> n0
  classDef semantic fill:#fff0d6,stroke:#9a5b00,color:#332000;
  class n3,n7 semantic;
```

 图依据原自然语言重建；扫描中的关联媒体是概念输入，不假定已核对物理表名/外键。

## sembench/animals/Q8

来源：[原件](</Volumes/Element/Github2/semantic-workload-bench/data/semantic-query-discovery-20260908/sembench/checkout/files/animals/query/natural_language/Q8.txt>) · `native_nl_reconstructed` · `logical_only` · `substantive_relational`

```text

What is the list of cities for which we found at least one image or audio recording of elephants and at least one image or audio recording of monkeys?

```

```mermaid
flowchart BT
  n0["R · Intersect | 两物种均有至少一种媒体"]
  n1["R · Union | DISTINCT"]
  n2["R · Distinct | 集合语义"]
  n3["R · Project | city"]
  n4["S · SFilter | 识别 elephant"]
  n5["R · Scan | ImageData"]
  n6["R · Distinct | 集合语义"]
  n7["R · Project | city"]
  n8["S · SFilter | 识别 elephant"]
  n9["R · Scan | AudioData"]
  n10["R · Union | DISTINCT"]
  n11["R · Distinct | 集合语义"]
  n12["R · Project | city"]
  n13["S · SFilter | 识别 monkey"]
  n14["R · Scan | ImageData"]
  n15["R · Distinct | 集合语义"]
  n16["R · Project | city"]
  n17["S · SFilter | 识别 monkey"]
  n18["R · Scan | AudioData"]
  n5 --> n4
  n4 --> n3
  n3 --> n2
  n2 --> n1
  n9 --> n8
  n8 --> n7
  n7 --> n6
  n6 --> n1
  n1 --> n0
  n14 --> n13
  n13 --> n12
  n12 --> n11
  n11 --> n10
  n18 --> n17
  n17 --> n16
  n16 --> n15
  n15 --> n10
  n10 --> n0
  classDef semantic fill:#fff0d6,stroke:#9a5b00,color:#332000;
  class n4,n8,n13,n17 semantic;
```

 图依据原自然语言重建；扫描中的关联媒体是概念输入，不假定已核对物理表名/外键。

## sembench/animals/Q9

来源：[原件](</Volumes/Element/Github2/semantic-workload-bench/data/semantic-query-discovery-20260908/sembench/checkout/files/animals/query/natural_language/Q9.txt>) · `native_nl_reconstructed` · `logical_only` · `substantive_relational`

```text

What is the list of cities for which we have both images and audio recordings of monkeys?

```

```mermaid
flowchart BT
  n0["R · Intersect | 城市集合交集"]
  n1["R · Distinct | 集合语义"]
  n2["R · Project | city"]
  n3["S · SFilter | 识别 monkey"]
  n4["R · Scan | ImageData"]
  n5["R · Distinct | 集合语义"]
  n6["R · Project | city"]
  n7["S · SFilter | 识别 monkey"]
  n8["R · Scan | AudioData"]
  n4 --> n3
  n3 --> n2
  n2 --> n1
  n1 --> n0
  n8 --> n7
  n7 --> n6
  n6 --> n5
  n5 --> n0
  classDef semantic fill:#fff0d6,stroke:#9a5b00,color:#332000;
  class n3,n7 semantic;
```

 图依据原自然语言重建；扫描中的关联媒体是概念输入，不假定已核对物理表名/外键。

## sembench/animals/Q10

来源：[原件](</Volumes/Element/Github2/semantic-workload-bench/data/semantic-query-discovery-20260908/sembench/checkout/files/animals/query/natural_language/Q10.txt>) · `native_nl_reconstructed` · `logical_only` · `substantive_relational`

```text

What is the city and station with most associated pictures showing zebras (ties are broken arbitrarily, only consider cities with at least one zebra picture)?

```

```mermaid
flowchart BT
  n0["R · Project | city, stationID"]
  n1["R · Limit | 1; 未指定顺序"]
  n2["R · Sort | cnt DESC"]
  n3["R · Aggregate | city, stationID; COUNT(*) AS cnt"]
  n4["S · SFilter | 包含 zebra"]
  n5["R · Scan | ImageData"]
  n5 --> n4
  n4 --> n3
  n3 --> n2
  n2 --> n1
  n1 --> n0
  classDef semantic fill:#fff0d6,stroke:#9a5b00,color:#332000;
  class n4 semantic;
```

NL允许任意打破并列；随库gold SQL用cnt=MAX(cnt)返回所有并列。图按NL保留一项；不能称二者完全等价。 图依据原自然语言重建；扫描中的关联媒体是概念输入，不假定已核对物理表名/外键。
