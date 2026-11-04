# sembench-cars：逐查询逻辑计划

[返回总表](README.md)

图从下往上读：输入 → 算子 → 输出。S为语义算子；R为确定性关系/辅助步骤。检索与未决节点在标签中单独注明。

## sembench/cars/Q1

来源：[原件](</Volumes/Element/Github2/semantic-workload-bench/data/semantic-query-discovery-20260908/sembench/checkout/files/cars/query/natural_language/Q1.txt>) · `native_nl_reconstructed` · `logical_only` · `scan_projection_only`

```text

Find cars that were in a crash/accident/collision.

```

```mermaid
flowchart BT
  n0["R · Project | 车辆记录"]
  n1["S · SFilter | 投诉描述 crash / accident / collision"]
  n2["R · Scan | Cars：结构字段及关联 complaint / image / audio"]
  n2 --> n1
  n1 --> n0
  classDef semantic fill:#fff0d6,stroke:#9a5b00,color:#332000;
  class n1 semantic;
```

 图依据原自然语言重建；扫描中的关联媒体是概念输入，不假定已核对物理表名/外键。

## sembench/cars/Q2

来源：[原件](</Volumes/Element/Github2/semantic-workload-bench/data/semantic-query-discovery-20260908/sembench/checkout/files/cars/query/natural_language/Q2.txt>) · `native_nl_reconstructed` · `logical_only` · `substantive_relational`

```text

Find electric cars with available audio recordings that show a dead battery.

```

```mermaid
flowchart BT
  n0["R · Project | 车辆记录"]
  n1["S · SFilter | audio 表现为电池耗尽"]
  n2["R · Filter | electric AND audio available"]
  n3["R · Scan | Cars：结构字段及关联 complaint / image / audio"]
  n3 --> n2
  n2 --> n1
  n1 --> n0
  classDef semantic fill:#fff0d6,stroke:#9a5b00,color:#332000;
  class n1 semantic;
```

 图依据原自然语言重建；扫描中的关联媒体是概念输入，不假定已核对物理表名/外键。

## sembench/cars/Q3

来源：[原件](</Volumes/Element/Github2/semantic-workload-bench/data/semantic-query-discovery-20260908/sembench/checkout/files/cars/query/natural_language/Q3.txt>) · `native_nl_reconstructed` · `logical_only` · `substantive_relational`

```text

Find ten cars with manual transmission that are not damaged according to images. Return the VIN.

```

```mermaid
flowchart BT
  n0["R · Limit | 10; 未指定顺序"]
  n1["R · Project | VIN"]
  n2["S · SFilter | image 未显示损伤"]
  n3["R · Filter | manual transmission"]
  n4["R · Scan | Cars：结构字段及关联 complaint / image / audio"]
  n4 --> n3
  n3 --> n2
  n2 --> n1
  n1 --> n0
  classDef semantic fill:#fff0d6,stroke:#9a5b00,color:#332000;
  class n2 semantic;
```

 图依据原自然语言重建；扫描中的关联媒体是概念输入，不假定已核对物理表名/外键。

## sembench/cars/Q4

来源：[原件](</Volumes/Element/Github2/semantic-workload-bench/data/semantic-query-discovery-20260908/sembench/checkout/files/cars/query/natural_language/Q4.txt>) · `native_nl_reconstructed` · `logical_only` · `substantive_relational`

```text

What is the average age of cars with engine problems?

```

```mermaid
flowchart BT
  n0["R · Aggregate | 全局; AVG(age)"]
  n1["S · SFilter | 投诉涉及发动机问题"]
  n2["R · Scan | Cars：结构字段及关联 complaint / image / audio"]
  n2 --> n1
  n1 --> n0
  classDef semantic fill:#fff0d6,stroke:#9a5b00,color:#332000;
  class n1 semantic;
```

 图依据原自然语言重建；扫描中的关联媒体是概念输入，不假定已核对物理表名/外键。

## sembench/cars/Q5

来源：[原件](</Volumes/Element/Github2/semantic-workload-bench/data/semantic-query-discovery-20260908/sembench/checkout/files/cars/query/natural_language/Q5.txt>) · `native_nl_reconstructed` · `logical_only` · `substantive_relational`

```text

How many automatic cars are damaged according to both audio and images?

```

```mermaid
flowchart BT
  n0["R · Aggregate | 全局; COUNT(*)"]
  n1["S · SFilter | audio 与 image 均显示损伤"]
  n2["R · Filter | automatic transmission"]
  n3["R · Scan | Cars：结构字段及关联 complaint / image / audio"]
  n3 --> n2
  n2 --> n1
  n1 --> n0
  classDef semantic fill:#fff0d6,stroke:#9a5b00,color:#332000;
  class n1 semantic;
```

 图依据原自然语言重建；扫描中的关联媒体是概念输入，不假定已核对物理表名/外键。

## sembench/cars/Q6

来源：[原件](</Volumes/Element/Github2/semantic-workload-bench/data/semantic-query-discovery-20260908/sembench/checkout/files/cars/query/natural_language/Q6.txt>) · `native_nl_reconstructed` · `logical_only` · `substantive_relational`

```text

Find cars that are damaged according to one modality but not the other. For this query, for complaints, check if the car was on fire.

```

```mermaid
flowchart BT
  n0["R · Project | 车辆记录"]
  n1["R · Filter | 可用模态至少一个damage=true且至少一个damage=false"]
  n2["S · SMap | 各可用模态→damage；文本判定限定为着火"]
  n3["R · Scan | Cars：结构字段及关联 complaint / image / audio"]
  n3 --> n2
  n2 --> n1
  n1 --> n0
  classDef semantic fill:#fff0d6,stroke:#9a5b00,color:#332000;
  class n2 semantic;
```

图采用可用模态间有真有假的逻辑解释；缺媒体不视作健康/否定。原NL的one modality/the other需固定模态范围后执行。 图依据原自然语言重建；扫描中的关联媒体是概念输入，不假定已核对物理表名/外键。

## sembench/cars/Q7

来源：[原件](</Volumes/Element/Github2/semantic-workload-bench/data/semantic-query-discovery-20260908/sembench/checkout/files/cars/query/natural_language/Q7.txt>) · `native_nl_reconstructed` · `logical_only` · `substantive_relational`

```text

Find cars that are either dented (image), have worn out brakes (audio), or have electrical system problems (text), i.e., damaged at least according to a single modality.

```

```mermaid
flowchart BT
  n0["R · Project | 车辆记录"]
  n1["R · Filter | dented OR worn_brakes OR electrical_problem"]
  n2["S · SMap | image→凹陷；audio→刹车磨损；text→电路问题"]
  n3["R · Scan | Cars：结构字段及关联 complaint / image / audio"]
  n3 --> n2
  n2 --> n1
  n1 --> n0
  classDef semantic fill:#fff0d6,stroke:#9a5b00,color:#332000;
  class n2 semantic;
```

 图依据原自然语言重建；扫描中的关联媒体是概念输入，不假定已核对物理表名/外键。

## sembench/cars/Q8

来源：[原件](</Volumes/Element/Github2/semantic-workload-bench/data/semantic-query-discovery-20260908/sembench/checkout/files/cars/query/natural_language/Q8.txt>) · `native_nl_reconstructed` · `logical_only` · `substantive_relational`

```text

Find a hundred cars with punctures and paint scratches on images.

```

```mermaid
flowchart BT
  n0["R · Limit | 100; 未指定顺序"]
  n1["R · Project | 车辆记录"]
  n2["S · SFilter | image 同时有 puncture 和 paint scratch"]
  n3["R · Scan | Cars：结构字段及关联 complaint / image / audio"]
  n3 --> n2
  n2 --> n1
  n1 --> n0
  classDef semantic fill:#fff0d6,stroke:#9a5b00,color:#332000;
  class n2 semantic;
```

 图依据原自然语言重建；扫描中的关联媒体是概念输入，不假定已核对物理表名/外键。

## sembench/cars/Q9

来源：[原件](</Volumes/Element/Github2/semantic-workload-bench/data/semantic-query-discovery-20260908/sembench/checkout/files/cars/query/natural_language/Q9.txt>) · `native_nl_reconstructed` · `logical_only` · `scan_projection_only`

```text

Find cars that are torn according to images and have bad ignition according to audio.

```

```mermaid
flowchart BT
  n0["R · Project | 车辆记录"]
  n1["S · SFilter | image torn AND audio bad ignition"]
  n2["R · Scan | Cars：结构字段及关联 complaint / image / audio"]
  n2 --> n1
  n1 --> n0
  classDef semantic fill:#fff0d6,stroke:#9a5b00,color:#332000;
  class n1 semantic;
```

 图依据原自然语言重建；扫描中的关联媒体是概念输入，不假定已核对物理表名/外键。

## sembench/cars/Q10

来源：[原件](</Volumes/Element/Github2/semantic-workload-bench/data/semantic-query-discovery-20260908/sembench/checkout/files/cars/query/natural_language/Q10.txt>) · `native_nl_reconstructed` · `logical_only` · `scan_projection_only`

```text

For all complaints, classify which car component is problematic according to the complaint.

```

```mermaid
flowchart BT
  n0["R · Project | complaint_id, component"]
  n1["S · SMap | complaint→故障部件类别"]
  n2["R · Scan | Complaints"]
  n2 --> n1
  n1 --> n0
  classDef semantic fill:#fff0d6,stroke:#9a5b00,color:#332000;
  class n1 semantic;
```

 图依据原自然语言重建；扫描中的关联媒体是概念输入，不假定已核对物理表名/外键。
