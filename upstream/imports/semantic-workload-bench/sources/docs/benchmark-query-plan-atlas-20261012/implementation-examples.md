# implementation-examples：逐查询逻辑计划

[返回总表](README.md)

图从下往上读：输入 → 算子 → 输出。S为语义算子；R为确定性关系/辅助步骤。检索与未决节点在标签中单独注明。

## lotus/failure-mode-discovery

来源：[原件](</Volumes/Element/Github2/Awesome-Sem-Filter-Bench/baseline/LOTUS/repository/LOTUS/benchmarks/failure_mode_discovery/pipeline.py>) · `observed_source_pipeline` · `logical_only` · `substantive_relational`

```text

从失败的Agent轨迹归纳失败模式并展开为行。

```

```mermaid
flowchart BT
  n0["R · Transform | parse list → explode → rename"]
  n1["S · SAggregate | 失败轨迹→failure modes list"]
  n2["S · SFilter | agent failed to successfully complete task"]
  n3["R · Scan | agent traces"]
  n3 --> n2
  n2 --> n1
  n1 --> n0
  classDef semantic fill:#fff0d6,stroke:#9a5b00,color:#332000;
  class n1,n2 semantic;
```

SAggregate是语义归纳，不等于SQL COUNT/SUM；结构部分主要是解析、展开。未执行。

## lotus/rag-pubmedqa

来源：[原件](</Volumes/Element/Github2/Awesome-Sem-Filter-Bench/baseline/LOTUS/repository/LOTUS/benchmarks/rag_pubmedqa/pipeline.py>) · `observed_source_pipeline` · `logical_only` · `substantive_relational`

```text

分解问题、检索PubMed文献、按问题汇总证据并生成回答。

```

```mermaid
flowchart BT
  n0["R · LeftJoin | query；左=语义回答，右=文献payload"]
  n1["S · SAggregate | GROUP BY query；综合文献输出answer + yes/no"]
  n2["R · Unnest | apply/explode/reset_index/json_normalize"]
  n3["R · ExternalSearch | PubMed web_search；K=8/subquery；max24/query"]
  n4["R · Transform | parse_subqueries"]
  n5["S · SMap | 问题→2–4 subqueries"]
  n6["R · Scan | PubMedQA questions"]
  n7["R · Aggregate | query; first(subqueries), set(ids,titles,abstracts)"]
  n6 --> n5
  n5 --> n4
  n4 --> n3
  n3 --> n2
  n2 --> n1
  n1 --> n0
  n2 --> n7
  n7 --> n0
  classDef semantic fill:#fff0d6,stroke:#9a5b00,color:#332000;
  class n1,n5 semantic;
```

基于本地当前pipeline文件，不声称是某篇早期论文原始查询。ExternalSearch是外部检索依赖，非普通数据库Join；最终merge是结构左连接。

## palimpzest/real-estate

来源：[原件](</Volumes/Element/Github2/Awesome-Sem-Filter-Bench/baseline/Palimpzest/repository/Palimpzest/tests/pytest/fixtures/workloads.py>) · `observed_source_pipeline` · `logical_only` · `substantive_relational`

```text

根据室内照片、房源文字、地址与价格筛选房源。

```

```mermaid
flowchart BT
  n0["R · Filter | 600000 &lt; parsed_price ≤ 2000000"]
  n1["R · Filter | within_two_miles_of_mit(address) UDF"]
  n2["S · SFilter | modern and attractive AND natural sunlight"]
  n3["S · SMap | image_filepaths→image listing schema"]
  n4["S · SMap | text_content→listing schema"]
  n5["R · Scan | real_estate_eval_tiny"]
  n5 --> n4
  n4 --> n3
  n3 --> n2
  n2 --> n1
  n1 --> n0
  classDef semantic fill:#fff0d6,stroke:#9a5b00,color:#332000;
  class n2,n3,n4 semantic;
```

保留fixture源码顺序。距离函数实际使用街道黑名单近似，不是真实地理距离计算；不可把结果称为2英里精确查询。
