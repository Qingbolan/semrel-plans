# derived-five-lakes：逐查询逻辑计划

[返回总表](README.md)

图从下往上读：输入 → 算子 → 输出。S为语义算子；R为确定性关系/辅助步骤。检索与未决节点在标签中单独注明。

## annoctr-Q1-v1

来源：[原件](</Volumes/Element/Github2/semantic-workload-bench/workloads/annoctr-batch/queries.json>) · `local_derived` · `registered_not_executed` · `substantive_relational`

```text

For every supplied mention and its context, use its complete report and frozen definitions to return the ATT&CK technique ID(s) it denotes. Boundaries and technical-mention selection are given. This is conditional linking of published positive annotations, not end-to-end detection, negative detection, or a complete report inventory. Preserve subtechnique specificity: use Txxxx.xxx, without collapsing to the parent. Return a duplicate-free list.

```

```mermaid
flowchart BT
  n0["R · Transform | normalize_original_id_granularity"]
  n1["S · SMap | sem_map_link_technique"]
  n2["R · Lookup | retrieve_definitions；检索实现尚未指定"]
  n3["R · Lookup | read_report_context；检索实现尚未指定"]
  n4["R · Scan | annoctr public records"]
  n5["R · Scan | annoctr frozen public lake / catalog / full references"]
  n4 --> n3
  n5 --> n3
  n3 --> n2
  n5 --> n2
  n2 --> n1
  n1 --> n0
  classDef semantic fill:#fff0d6,stroke:#9a5b00,color:#332000;
  class n1 semantic;
```

DEVELOPMENT_CONDITIONAL_LINKING_ONLY；本地派生任务，非原benchmark官方查询；没有模型执行或K测量。专家技术URL映射为ATT&CK ID；不按父技术折叠，粒度与论文部分实验不同

## annoctr-Q2-v1

来源：[原件](</Volumes/Element/Github2/semantic-workload-bench/workloads/annoctr-batch/queries.json>) · `local_derived` · `registered_not_executed` · `substantive_relational`

```text

返回链接到指定技术的提及清单，并关联所属报告

```

```mermaid
flowchart BT
  n0["R · ResultBundle | 清单和总数"]
  n1["R · Distinct | record_id；一个实体不因多个标签重复计数"]
  n2["R · Project | record_id及原请求字段"]
  n3["R · Filter | status=OK AND label匹配参数（HTS为显式前缀；其他按原契约）"]
  n4["R · Unnest | value中的去重标签"]
  n5["R · Transform | normalize_original_id_granularity"]
  n6["S · SMap | sem_map_link_technique"]
  n7["R · Lookup | retrieve_definitions；检索实现尚未指定"]
  n8["R · Lookup | read_report_context；检索实现尚未指定"]
  n9["R · Scan | annoctr public records"]
  n10["R · Scan | annoctr frozen public lake / catalog / full references"]
  n11["R · Aggregate | 全局; COUNT(*)"]
  n9 --> n8
  n10 --> n8
  n8 --> n7
  n10 --> n7
  n7 --> n6
  n6 --> n5
  n5 --> n4
  n4 --> n3
  n3 --> n2
  n2 --> n1
  n1 --> n0
  n1 --> n11
  n11 --> n0
  classDef semantic fill:#fff0d6,stroke:#9a5b00,color:#332000;
  class n6 semantic;
```

DEVELOPMENT_CONDITIONAL_LINKING_ONLY；本地派生任务，非原benchmark官方查询；没有模型执行或K测量。Derived from the same Q1 labels; not independent gold

## annoctr-Q3-v1

来源：[原件](</Volumes/Element/Github2/semantic-workload-bench/workloads/annoctr-batch/queries.json>) · `local_derived` · `registered_not_executed` · `substantive_relational`

```text

对本批给定提及按报告归并技术集合，同时区分提及数与报告数

```

```mermaid
flowchart BT
  n0["R · ResultBundle | 统计和completeness（缺失不是0或负例）"]
  n1["R · Aggregate | label及原请求source_entity; COUNT(DISTINCT record_id)；需要时COLLECT DISTINCT label"]
  n2["R · Unnest | status=OK的去重value；空集合不产生标签行"]
  n3["R · Transform | normalize_original_id_granularity"]
  n4["S · SMap | sem_map_link_technique"]
  n5["R · Lookup | retrieve_definitions；检索实现尚未指定"]
  n6["R · Lookup | read_report_context；检索实现尚未指定"]
  n7["R · Scan | annoctr public records"]
  n8["R · Scan | annoctr frozen public lake / catalog / full references"]
  n9["R · Aggregate | 全批; COUNT status=ABSTAIN；完成数/总数"]
  n7 --> n6
  n8 --> n6
  n6 --> n5
  n8 --> n5
  n5 --> n4
  n4 --> n3
  n3 --> n2
  n2 --> n1
  n1 --> n0
  n3 --> n9
  n9 --> n0
  classDef semantic fill:#fff0d6,stroke:#9a5b00,color:#332000;
  class n4 semantic;
```

DEVELOPMENT_CONDITIONAL_LINKING_ONLY；本地派生任务，非原benchmark官方查询；没有模型执行或K测量。Derived from Q1; partial groups explicitly marked incomplete

## annoctr-Q4-v1

来源：[原件](</Volumes/Element/Github2/semantic-workload-bench/workloads/annoctr-batch/queries.json>) · `local_derived` · `registered_not_executed` · `substantive_relational`

```text

返回未完成记录及原因，并报告全量coverage；缺事实和运行失败均需保留原因，不当负例。

```

```mermaid
flowchart BT
  n0["R · ResultBundle | 拒答队列及全量coverage"]
  n1["R · Project | record_id, reason"]
  n2["R · Filter | status=ABSTAIN"]
  n3["R · Transform | normalize_original_id_granularity"]
  n4["S · SMap | sem_map_link_technique"]
  n5["R · Lookup | retrieve_definitions；检索实现尚未指定"]
  n6["R · Lookup | read_report_context；检索实现尚未指定"]
  n7["R · Scan | annoctr public records"]
  n8["R · Scan | annoctr frozen public lake / catalog / full references"]
  n9["R · Aggregate | 全批; COUNT(status=OK)/COUNT(*)"]
  n7 --> n6
  n8 --> n6
  n6 --> n5
  n8 --> n5
  n5 --> n4
  n4 --> n3
  n3 --> n2
  n2 --> n1
  n1 --> n0
  n3 --> n9
  n9 --> n0
  classDef semantic fill:#fff0d6,stroke:#9a5b00,color:#332000;
  class n4 semantic;
```

DEVELOPMENT_CONDITIONAL_LINKING_ONLY；本地派生任务，非原benchmark官方查询；没有模型执行或K测量。No independent gold; this is execution accounting, not missing-fact correctness 运行管理派生，不新增独立语义问题。

## codiesp-Q1-v1

来源：[原件](</Volumes/Element/Github2/semantic-workload-bench/workloads/codiesp-batch/queries.json>) · `local_derived` · `registered_not_executed` · `substantive_relational`

```text

For every complete Spanish case report, return a ranked, duplicate-free list of procedure codes under the supplied CodiEsp guidelines and frozen 2018 coding resources. Use lowercase codes and preserve allowed four- or seven-character specificity; do not invent missing axes. Code mention scope under the task guidelines, not whether a procedure actually occurred. Include all reports; an empty completed list means no selected codable mentions, not absence of real procedures. This task is P, not D or X.

```

```mermaid
flowchart BT
  n0["R · Transform | rank_unique_codes"]
  n1["S · SMap | sem_map_resolve_axes_and_specificity"]
  n2["R · Lookup | retrieve_code_candidates_and_guidelines；检索实现尚未指定"]
  n3["S · SMap | sem_map_procedure_mentions"]
  n4["R · Scan | codiesp public records"]
  n5["R · Scan | codiesp frozen public lake / catalog / full references"]
  n4 --> n3
  n3 --> n2
  n5 --> n2
  n2 --> n1
  n1 --> n0
  classDef semantic fill:#fff0d6,stroke:#9a5b00,color:#332000;
  class n1,n3 semantic;
```

DEVELOPMENT_SOURCE_LABEL_REPRODUCTION_ONLY；本地派生任务，非原benchmark官方查询；没有模型执行或K测量。源P病例-code集合，保留全部标签；原排序预测任务主指标MAP，集合为补充

## codiesp-Q2-v1

来源：[原件](</Volumes/Element/Github2/semantic-workload-bench/workloads/codiesp-batch/queries.json>) · `local_derived` · `registered_not_executed` · `substantive_relational`

```text

返回含指定操作代码提及的报告清单；不解释为患者接受该操作

```

```mermaid
flowchart BT
  n0["R · ResultBundle | 清单和总数"]
  n1["R · Distinct | record_id；一个实体不因多个标签重复计数"]
  n2["R · Project | record_id及原请求字段"]
  n3["R · Filter | status=OK AND label匹配参数（HTS为显式前缀；其他按原契约）"]
  n4["R · Unnest | value中的去重标签"]
  n5["R · Transform | rank_unique_codes"]
  n6["S · SMap | sem_map_resolve_axes_and_specificity"]
  n7["R · Lookup | retrieve_code_candidates_and_guidelines；检索实现尚未指定"]
  n8["S · SMap | sem_map_procedure_mentions"]
  n9["R · Scan | codiesp public records"]
  n10["R · Scan | codiesp frozen public lake / catalog / full references"]
  n11["R · Aggregate | 全局; COUNT(*)"]
  n9 --> n8
  n8 --> n7
  n10 --> n7
  n7 --> n6
  n6 --> n5
  n5 --> n4
  n4 --> n3
  n3 --> n2
  n2 --> n1
  n1 --> n0
  n1 --> n11
  n11 --> n0
  classDef semantic fill:#fff0d6,stroke:#9a5b00,color:#332000;
  class n6,n8 semantic;
```

DEVELOPMENT_SOURCE_LABEL_REPRODUCTION_ONLY；本地派生任务，非原benchmark官方查询；没有模型执行或K测量。Derived from the same Q1 labels; not independent gold

## codiesp-Q3-v1

来源：[原件](</Volumes/Element/Github2/semantic-workload-bench/workloads/codiesp-batch/queries.json>) · `local_derived` · `registered_not_executed` · `substantive_relational`

```text

按操作代码统计报告数；不把重复提及或同论文病例算成独立患者

```

```mermaid
flowchart BT
  n0["R · ResultBundle | 统计和completeness（缺失不是0或负例）"]
  n1["R · Aggregate | label及原请求source_entity; COUNT(DISTINCT record_id)；需要时COLLECT DISTINCT label"]
  n2["R · Unnest | status=OK的去重value；空集合不产生标签行"]
  n3["R · Transform | rank_unique_codes"]
  n4["S · SMap | sem_map_resolve_axes_and_specificity"]
  n5["R · Lookup | retrieve_code_candidates_and_guidelines；检索实现尚未指定"]
  n6["S · SMap | sem_map_procedure_mentions"]
  n7["R · Scan | codiesp public records"]
  n8["R · Scan | codiesp frozen public lake / catalog / full references"]
  n9["R · Aggregate | 全批; COUNT status=ABSTAIN；完成数/总数"]
  n7 --> n6
  n6 --> n5
  n8 --> n5
  n5 --> n4
  n4 --> n3
  n3 --> n2
  n2 --> n1
  n1 --> n0
  n3 --> n9
  n9 --> n0
  classDef semantic fill:#fff0d6,stroke:#9a5b00,color:#332000;
  class n4,n6 semantic;
```

DEVELOPMENT_SOURCE_LABEL_REPRODUCTION_ONLY；本地派生任务，非原benchmark官方查询；没有模型执行或K测量。Derived from Q1; partial groups explicitly marked incomplete

## codiesp-Q4-v1

来源：[原件](</Volumes/Element/Github2/semantic-workload-bench/workloads/codiesp-batch/queries.json>) · `local_derived` · `registered_not_executed` · `substantive_relational`

```text

返回未完成记录及原因，并报告全量coverage；缺事实和运行失败均需保留原因，不当负例。

```

```mermaid
flowchart BT
  n0["R · ResultBundle | 拒答队列及全量coverage"]
  n1["R · Project | record_id, reason"]
  n2["R · Filter | status=ABSTAIN"]
  n3["R · Transform | rank_unique_codes"]
  n4["S · SMap | sem_map_resolve_axes_and_specificity"]
  n5["R · Lookup | retrieve_code_candidates_and_guidelines；检索实现尚未指定"]
  n6["S · SMap | sem_map_procedure_mentions"]
  n7["R · Scan | codiesp public records"]
  n8["R · Scan | codiesp frozen public lake / catalog / full references"]
  n9["R · Aggregate | 全批; COUNT(status=OK)/COUNT(*)"]
  n7 --> n6
  n6 --> n5
  n8 --> n5
  n5 --> n4
  n4 --> n3
  n3 --> n2
  n2 --> n1
  n1 --> n0
  n3 --> n9
  n9 --> n0
  classDef semantic fill:#fff0d6,stroke:#9a5b00,color:#332000;
  class n4,n6 semantic;
```

DEVELOPMENT_SOURCE_LABEL_REPRODUCTION_ONLY；本地派生任务，非原benchmark官方查询；没有模型执行或K测量。No independent gold; this is execution accounting, not missing-fact correctness 运行管理派生，不新增独立语义问题。

## hscodecomp-Q1-v1

来源：[原件](</Volumes/Element/Github2/semantic-workload-bench/workloads/hscodecomp-batch/queries.json>) · `local_derived` · `registered_not_executed` · `substantive_relational`

```text

For every product in records.json, use its published title, attributes, price, currency and marketplace categories with frozen HTS 2025 Revision 15 to return one 10-digit HTS code as a singleton string list. Consult hierarchy, unnumbered parent rows and full notes. Do not assume price is per item, invent photos, convert currency without evidence, or reconstruct missing product facts. If a supported classification cannot be completed, ABSTAIN with null value and a concrete reason. The source-label task supplies no independent UNKNOWN gold.

```

```mermaid
flowchart BT
  n0["R · Transform | validate_10_digit_code_or_abstain"]
  n1["S · SMap | sem_map_resolve_exclusions_and_classification"]
  n2["R · Lookup | retrieve_hts_tree_and_notes；检索实现尚未指定"]
  n3["S · SMap | sem_map_extract_material_use_unit_facts"]
  n4["R · Scan | hscodecomp public records"]
  n5["R · Scan | hscodecomp frozen public lake / catalog / full references"]
  n4 --> n3
  n3 --> n2
  n5 --> n2
  n2 --> n1
  n1 --> n0
  classDef semantic fill:#fff0d6,stroke:#9a5b00,color:#332000;
  class n1,n3 semantic;
```

DEVELOPMENT_INCOMPLETE_INPUT_DIAGNOSTIC；本地派生任务，非原benchmark官方查询；没有模型执行或K测量。独立专家10位码；前缀目标由同一标签派生

## hscodecomp-Q2-v1

来源：[原件](</Volumes/Element/Github2/semantic-workload-bench/workloads/hscodecomp-batch/queries.json>) · `local_derived` · `registered_not_executed` · `substantive_relational`

```text

按参数化2/4/6/8/10位编码前缀返回商品清单及数量

```

```mermaid
flowchart BT
  n0["R · ResultBundle | 清单和总数"]
  n1["R · Distinct | record_id；一个实体不因多个标签重复计数"]
  n2["R · Project | record_id及原请求字段"]
  n3["R · Filter | status=OK AND label匹配参数（HTS为显式前缀；其他按原契约）"]
  n4["R · Unnest | value中的去重标签"]
  n5["R · Transform | validate_10_digit_code_or_abstain"]
  n6["S · SMap | sem_map_resolve_exclusions_and_classification"]
  n7["R · Lookup | retrieve_hts_tree_and_notes；检索实现尚未指定"]
  n8["S · SMap | sem_map_extract_material_use_unit_facts"]
  n9["R · Scan | hscodecomp public records"]
  n10["R · Scan | hscodecomp frozen public lake / catalog / full references"]
  n11["R · Aggregate | 全局; COUNT(*)"]
  n9 --> n8
  n8 --> n7
  n10 --> n7
  n7 --> n6
  n6 --> n5
  n5 --> n4
  n4 --> n3
  n3 --> n2
  n2 --> n1
  n1 --> n0
  n1 --> n11
  n11 --> n0
  classDef semantic fill:#fff0d6,stroke:#9a5b00,color:#332000;
  class n6,n8 semantic;
```

DEVELOPMENT_INCOMPLETE_INPUT_DIAGNOSTIC；本地派生任务，非原benchmark官方查询；没有模型执行或K测量。Derived from the same Q1 labels; not independent gold

## hscodecomp-Q3-v1

来源：[原件](</Volumes/Element/Github2/semantic-workload-bench/workloads/hscodecomp-batch/queries.json>) · `local_derived` · `registered_not_executed` · `substantive_relational`

```text

按预测完整编码统计商品数；前缀筛选为派生诊断，不是独立专家gold

```

```mermaid
flowchart BT
  n0["R · ResultBundle | 统计和completeness（缺失不是0或负例）"]
  n1["R · Aggregate | label及原请求source_entity; COUNT(DISTINCT record_id)；需要时COLLECT DISTINCT label"]
  n2["R · Unnest | status=OK的去重value；空集合不产生标签行"]
  n3["R · Transform | validate_10_digit_code_or_abstain"]
  n4["S · SMap | sem_map_resolve_exclusions_and_classification"]
  n5["R · Lookup | retrieve_hts_tree_and_notes；检索实现尚未指定"]
  n6["S · SMap | sem_map_extract_material_use_unit_facts"]
  n7["R · Scan | hscodecomp public records"]
  n8["R · Scan | hscodecomp frozen public lake / catalog / full references"]
  n9["R · Aggregate | 全批; COUNT status=ABSTAIN；完成数/总数"]
  n7 --> n6
  n6 --> n5
  n8 --> n5
  n5 --> n4
  n4 --> n3
  n3 --> n2
  n2 --> n1
  n1 --> n0
  n3 --> n9
  n9 --> n0
  classDef semantic fill:#fff0d6,stroke:#9a5b00,color:#332000;
  class n4,n6 semantic;
```

DEVELOPMENT_INCOMPLETE_INPUT_DIAGNOSTIC；本地派生任务，非原benchmark官方查询；没有模型执行或K测量。Derived from Q1; partial groups explicitly marked incomplete

## hscodecomp-Q4-v1

来源：[原件](</Volumes/Element/Github2/semantic-workload-bench/workloads/hscodecomp-batch/queries.json>) · `local_derived` · `registered_not_executed` · `substantive_relational`

```text

返回未完成记录及原因，并报告全量coverage；缺事实和运行失败均需保留原因，不当负例。

```

```mermaid
flowchart BT
  n0["R · ResultBundle | 拒答队列及全量coverage"]
  n1["R · Project | record_id, reason"]
  n2["R · Filter | status=ABSTAIN"]
  n3["R · Transform | validate_10_digit_code_or_abstain"]
  n4["S · SMap | sem_map_resolve_exclusions_and_classification"]
  n5["R · Lookup | retrieve_hts_tree_and_notes；检索实现尚未指定"]
  n6["S · SMap | sem_map_extract_material_use_unit_facts"]
  n7["R · Scan | hscodecomp public records"]
  n8["R · Scan | hscodecomp frozen public lake / catalog / full references"]
  n9["R · Aggregate | 全批; COUNT(status=OK)/COUNT(*)"]
  n7 --> n6
  n6 --> n5
  n8 --> n5
  n5 --> n4
  n4 --> n3
  n3 --> n2
  n2 --> n1
  n1 --> n0
  n3 --> n9
  n9 --> n0
  classDef semantic fill:#fff0d6,stroke:#9a5b00,color:#332000;
  class n4,n6 semantic;
```

DEVELOPMENT_INCOMPLETE_INPUT_DIAGNOSTIC；本地派生任务，非原benchmark官方查询；没有模型执行或K测量。No independent gold; this is execution accounting, not missing-fact correctness 运行管理派生，不新增独立语义问题。

## stard-Q1-v1

来源：[原件](</Volumes/Element/Github2/semantic-workload-bench/workloads/stard-batch/queries.json>) · `local_derived` · `registered_not_executed` · `substantive_relational`

```text

For every question in records.json, return a ranked, duplicate-free list of relevant article IDs from lake/catalog.jsonl. Use the frozen article corpus. This is relevant-article retrieval, not a legal ruling or a complete legal answer. Do not infer that unannotated or unreturned articles are legally inapplicable.

```

```mermaid
flowchart BT
  n0["R · Transform | validate_article_ids"]
  n1["S · SMap | sem_map_relevance_rank"]
  n2["R · Lookup | retrieve_full_catalog；检索实现尚未指定"]
  n3["S · SMap | sem_map_decompose_issues"]
  n4["R · Scan | stard public records"]
  n5["R · Scan | stard frozen public lake / catalog / full references"]
  n4 --> n3
  n3 --> n2
  n5 --> n2
  n2 --> n1
  n1 --> n0
  classDef semantic fill:#fff0d6,stroke:#9a5b00,color:#332000;
  class n1,n3 semantic;
```

DEVELOPMENT_RETRIEVAL_ONLY；本地派生任务，非原benchmark官方查询；没有模型执行或K测量。人工相关法条集合；排名指标可对无序qrels评估，非原gold顺序

## stard-Q2-v1

来源：[原件](</Volumes/Element/Github2/semantic-workload-bench/workloads/stard-batch/queries.json>) · `local_derived` · `registered_not_executed` · `substantive_relational`

```text

返回涉及指定法条的咨询记录清单与数量

```

```mermaid
flowchart BT
  n0["R · ResultBundle | 清单和总数"]
  n1["R · Distinct | record_id；一个实体不因多个标签重复计数"]
  n2["R · Project | record_id及原请求字段"]
  n3["R · Filter | status=OK AND label匹配参数（HTS为显式前缀；其他按原契约）"]
  n4["R · Unnest | value中的去重标签"]
  n5["R · Transform | validate_article_ids"]
  n6["S · SMap | sem_map_relevance_rank"]
  n7["R · Lookup | retrieve_full_catalog；检索实现尚未指定"]
  n8["S · SMap | sem_map_decompose_issues"]
  n9["R · Scan | stard public records"]
  n10["R · Scan | stard frozen public lake / catalog / full references"]
  n11["R · Aggregate | 全局; COUNT(*)"]
  n9 --> n8
  n8 --> n7
  n10 --> n7
  n7 --> n6
  n6 --> n5
  n5 --> n4
  n4 --> n3
  n3 --> n2
  n2 --> n1
  n1 --> n0
  n1 --> n11
  n11 --> n0
  classDef semantic fill:#fff0d6,stroke:#9a5b00,color:#332000;
  class n6,n8 semantic;
```

DEVELOPMENT_RETRIEVAL_ONLY；本地派生任务，非原benchmark官方查询；没有模型执行或K测量。Derived from the same Q1 labels; not independent gold

## stard-Q3-v1

来源：[原件](</Volumes/Element/Github2/semantic-workload-bench/workloads/stard-batch/queries.json>) · `local_derived` · `registered_not_executed` · `substantive_relational`

```text

按法条统计命中的咨询数，生成咨询—法条索引

```

```mermaid
flowchart BT
  n0["R · ResultBundle | 统计和completeness（缺失不是0或负例）"]
  n1["R · Aggregate | label及原请求source_entity; COUNT(DISTINCT record_id)；需要时COLLECT DISTINCT label"]
  n2["R · Unnest | status=OK的去重value；空集合不产生标签行"]
  n3["R · Transform | validate_article_ids"]
  n4["S · SMap | sem_map_relevance_rank"]
  n5["R · Lookup | retrieve_full_catalog；检索实现尚未指定"]
  n6["S · SMap | sem_map_decompose_issues"]
  n7["R · Scan | stard public records"]
  n8["R · Scan | stard frozen public lake / catalog / full references"]
  n9["R · Aggregate | 全批; COUNT status=ABSTAIN；完成数/总数"]
  n7 --> n6
  n6 --> n5
  n8 --> n5
  n5 --> n4
  n4 --> n3
  n3 --> n2
  n2 --> n1
  n1 --> n0
  n3 --> n9
  n9 --> n0
  classDef semantic fill:#fff0d6,stroke:#9a5b00,color:#332000;
  class n4,n6 semantic;
```

DEVELOPMENT_RETRIEVAL_ONLY；本地派生任务，非原benchmark官方查询；没有模型执行或K测量。Derived from Q1; partial groups explicitly marked incomplete

## stard-Q4-v1

来源：[原件](</Volumes/Element/Github2/semantic-workload-bench/workloads/stard-batch/queries.json>) · `local_derived` · `registered_not_executed` · `substantive_relational`

```text

返回未完成记录及原因，并报告全量coverage；缺事实和运行失败均需保留原因，不当负例。

```

```mermaid
flowchart BT
  n0["R · ResultBundle | 拒答队列及全量coverage"]
  n1["R · Project | record_id, reason"]
  n2["R · Filter | status=ABSTAIN"]
  n3["R · Transform | validate_article_ids"]
  n4["S · SMap | sem_map_relevance_rank"]
  n5["R · Lookup | retrieve_full_catalog；检索实现尚未指定"]
  n6["S · SMap | sem_map_decompose_issues"]
  n7["R · Scan | stard public records"]
  n8["R · Scan | stard frozen public lake / catalog / full references"]
  n9["R · Aggregate | 全批; COUNT(status=OK)/COUNT(*)"]
  n7 --> n6
  n6 --> n5
  n8 --> n5
  n5 --> n4
  n4 --> n3
  n3 --> n2
  n2 --> n1
  n1 --> n0
  n3 --> n9
  n9 --> n0
  classDef semantic fill:#fff0d6,stroke:#9a5b00,color:#332000;
  class n4,n6 semantic;
```

DEVELOPMENT_RETRIEVAL_ONLY；本地派生任务，非原benchmark官方查询；没有模型执行或K测量。No independent gold; this is execution accounting, not missing-fact correctness 运行管理派生，不新增独立语义问题。

## udrp-Q1-v1

来源：[原件](</Volumes/Element/Github2/semantic-workload-bench/workloads/udrp-batch/queries.json>) · `local_derived` · `inspection_only` · `substantive_relational`

```text

For each supplied case, apply the frozen WIPO Overview 3.0 to attributed party contentions and recorded facts, and return a singleton list containing RELIEF_GRANTED or DENIED. Missing support is not a denial: ABSTAIN with null value and a reason when unable to complete. These are retrospective pre-analysis case extracts, not original filings. This query is registered for inspection: residual answer leakage and external-fact gaps remain, so it is not an evaluation-ready prediction benchmark.

```

```mermaid
flowchart BT
  n0["R · Transform | combine_decision_or_abstain"]
  n1["S · SMap | sem_map_evaluate_three_elements"]
  n2["R · Lookup | retrieve_overview_elements_and_exceptions；检索实现尚未指定"]
  n3["R · Scan | udrp public records"]
  n4["R · Scan | udrp frozen public lake / catalog / full references"]
  n3 --> n2
  n4 --> n2
  n2 --> n1
  n1 --> n0
  classDef semantic fill:#fff0d6,stroke:#9a5b00,color:#332000;
  class n1 semantic;
```

INSPECTION_ONLY_LEAKAGE_AND_FACT_GAPS；本地派生任务，非原benchmark官方查询；没有模型执行或K测量。正式命令的规则抽取标签；保留正式原文，非新独立人工复核标签

## udrp-Q2-v1

来源：[原件](</Volumes/Element/Github2/semantic-workload-bench/workloads/udrp-batch/queries.json>) · `local_derived` · `inspection_only` · `substantive_relational`

```text

筛出预测驳回案件，生成需复核的少数类清单

```

```mermaid
flowchart BT
  n0["R · ResultBundle | 清单和总数"]
  n1["R · Distinct | record_id；一个实体不因多个标签重复计数"]
  n2["R · Project | record_id及原请求字段"]
  n3["R · Filter | status=OK AND label匹配参数（HTS为显式前缀；其他按原契约）"]
  n4["R · Unnest | value中的去重标签"]
  n5["R · Transform | combine_decision_or_abstain"]
  n6["S · SMap | sem_map_evaluate_three_elements"]
  n7["R · Lookup | retrieve_overview_elements_and_exceptions；检索实现尚未指定"]
  n8["R · Scan | udrp public records"]
  n9["R · Scan | udrp frozen public lake / catalog / full references"]
  n10["R · Aggregate | 全局; COUNT(*)"]
  n8 --> n7
  n9 --> n7
  n7 --> n6
  n6 --> n5
  n5 --> n4
  n4 --> n3
  n3 --> n2
  n2 --> n1
  n1 --> n0
  n1 --> n10
  n10 --> n0
  classDef semantic fill:#fff0d6,stroke:#9a5b00,color:#332000;
  class n6 semantic;
```

INSPECTION_ONLY_LEAKAGE_AND_FACT_GAPS；本地派生任务，非原benchmark官方查询；没有模型执行或K测量。Derived from the same Q1 labels; not independent gold

## udrp-Q3-v1

来源：[原件](</Volumes/Element/Github2/semantic-workload-bench/workloads/udrp-batch/queries.json>) · `local_derived` · `inspection_only` · `substantive_relational`

```text

统计两种预测决定及未完成数量；不得只报多数类准确率

```

```mermaid
flowchart BT
  n0["R · ResultBundle | 统计和completeness（缺失不是0或负例）"]
  n1["R · Aggregate | label及原请求source_entity; COUNT(DISTINCT record_id)；需要时COLLECT DISTINCT label"]
  n2["R · Unnest | status=OK的去重value；空集合不产生标签行"]
  n3["R · Transform | combine_decision_or_abstain"]
  n4["S · SMap | sem_map_evaluate_three_elements"]
  n5["R · Lookup | retrieve_overview_elements_and_exceptions；检索实现尚未指定"]
  n6["R · Scan | udrp public records"]
  n7["R · Scan | udrp frozen public lake / catalog / full references"]
  n8["R · Aggregate | 全批; COUNT status=ABSTAIN；完成数/总数"]
  n6 --> n5
  n7 --> n5
  n5 --> n4
  n4 --> n3
  n3 --> n2
  n2 --> n1
  n1 --> n0
  n3 --> n8
  n8 --> n0
  classDef semantic fill:#fff0d6,stroke:#9a5b00,color:#332000;
  class n4 semantic;
```

INSPECTION_ONLY_LEAKAGE_AND_FACT_GAPS；本地派生任务，非原benchmark官方查询；没有模型执行或K测量。Derived from Q1; partial groups explicitly marked incomplete

## udrp-Q4-v1

来源：[原件](</Volumes/Element/Github2/semantic-workload-bench/workloads/udrp-batch/queries.json>) · `local_derived` · `inspection_only` · `substantive_relational`

```text

返回未完成记录及原因，并报告全量coverage；缺事实和运行失败均需保留原因，不当负例。

```

```mermaid
flowchart BT
  n0["R · ResultBundle | 拒答队列及全量coverage"]
  n1["R · Project | record_id, reason"]
  n2["R · Filter | status=ABSTAIN"]
  n3["R · Transform | combine_decision_or_abstain"]
  n4["S · SMap | sem_map_evaluate_three_elements"]
  n5["R · Lookup | retrieve_overview_elements_and_exceptions；检索实现尚未指定"]
  n6["R · Scan | udrp public records"]
  n7["R · Scan | udrp frozen public lake / catalog / full references"]
  n8["R · Aggregate | 全批; COUNT(status=OK)/COUNT(*)"]
  n6 --> n5
  n7 --> n5
  n5 --> n4
  n4 --> n3
  n3 --> n2
  n2 --> n1
  n1 --> n0
  n3 --> n8
  n8 --> n0
  classDef semantic fill:#fff0d6,stroke:#9a5b00,color:#332000;
  class n4 semantic;
```

INSPECTION_ONLY_LEAKAGE_AND_FACT_GAPS；本地派生任务，非原benchmark官方查询；没有模型执行或K测量。No independent gold; this is execution accounting, not missing-fact correctness 运行管理派生，不新增独立语义问题。
