# 咨询相关法条批检索 — BUILT 开发构造契约

固定单位：整理后的法律咨询，全量 1543 条。分组：咨询ID；实体与近重复隔离未证。

Q1：For every question in records.json, return a ranked, duplicate-free list of relevant article IDs from lake/catalog.jsonl. Use the frozen article corpus. This is relevant-article retrieval, not a legal ruling or a complete legal answer. Do not infer that unannotated or unreturned articles are legally inapplicable.

| Query | 用途 | 标签来源 |
| --- | --- | --- |
| Q1 | 原任务语义步骤，输出有序label_id列表 | 人工相关法条集合；排名指标可对无序qrels评估，非原gold顺序 |
| Q2 | 返回涉及指定法条的咨询记录清单与数量；参数例 `705` | 同Q1派生，非独立gold |
| Q3 | 按法条统计命中的咨询数，生成咨询—法条索引 | 同Q1确定性聚合 |
| Q4 | 未完成清单与coverage | 无独立gold，只作执行账目 |

输入投影、完整DAG和输出契约见 [queries.json](queries.json)。Q2–Q4 共用Q1中间结果，不伪装成额外语义任务或已发现operator家族。禁止把原gold复制成模型“预期输出”。

资源：[环境卡](../../environments/stard/resource-card.md)。源证据：[严格审查](../../docs/shared-environment-strict-audit-stard.md)。

状态：`DEVELOPMENT_RETRIEVAL_ONLY`。原相关性标签不保证完整依据或回答充分性；全量关联校验不等于语义正确。

衡量指标计划：Recall@k, MRR@k, source-label set F1, coverage。本次只构造与校验，没有模型推理、质量评分、独立确认划分或Strong升级。P/D/X、原排名指标与派生集合/聚合指标不得混用。

复现与实际交付：[五湖构造指南](../../docs/shared-environment-five-lakes-build.md)。
