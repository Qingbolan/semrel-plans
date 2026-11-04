# 域名争议回顾性裁决查询 — BUILT 开发构造契约

固定单位：2024 WIPO单域名裁决的前分析章节，全量 1572 条。分组：案件；跨当事人/商标隔离未证。

Q1：For each supplied case, apply the frozen WIPO Overview 3.0 to attributed party contentions and recorded facts, and return a singleton list containing RELIEF_GRANTED or DENIED. Missing support is not a denial: ABSTAIN with null value and a reason when unable to complete. These are retrospective pre-analysis case extracts, not original filings. This query is registered for inspection: residual answer leakage and external-fact gaps remain, so it is not an evaluation-ready prediction benchmark.

| Query | 用途 | 标签来源 |
| --- | --- | --- |
| Q1 | 原任务语义步骤，输出有序label_id列表 | 正式命令的规则抽取标签；保留正式原文，非新独立人工复核标签 |
| Q2 | 筛出预测驳回案件，生成需复核的少数类清单；参数例 `DENIED` | 同Q1派生，非独立gold |
| Q3 | 统计两种预测决定及未完成数量；不得只报多数类准确率 | 同Q1确定性聚合 |
| Q4 | 未完成清单与coverage | 无独立gold，只作执行账目 |

输入投影、完整DAG和输出契约见 [queries.json](queries.json)。Q2–Q4 共用Q1中间结果，不伪装成额外语义任务或已发现operator家族。禁止把原gold复制成模型“预期输出”。

资源：[环境卡](../../environments/udrp/resource-card.md)。源证据：[严格审查](../../docs/shared-environment-strict-audit-udrp.md)。

状态：`INSPECTION_ONLY_LEAKAGE_AND_FACT_GAPS`。仍有4处既有残余instruction-transfer词面标记，语义泄漏未清；外部调查未封存；1513/59严重偏斜；禁止将本构造视为可用预测实验证据。

衡量指标计划：source-label macro-F1, DENIED recall, balanced accuracy, coverage。本次只构造与校验，没有模型推理、质量评分、独立确认划分或Strong升级。P/D/X、原排名指标与派生集合/聚合指标不得混用。

复现与实际交付：[五湖构造指南](../../docs/shared-environment-five-lakes-build.md)。
