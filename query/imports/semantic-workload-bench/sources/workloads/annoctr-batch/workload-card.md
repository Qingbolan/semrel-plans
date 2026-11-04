# 威胁报告指定提及的技术链接 — BUILT 开发构造契约

固定单位：已给定且有ATT&CK正链接的技术提及，全量 3348 条。分组：本批覆盖112份原报告，湖共120报告；不是3348篇独立报告。

Q1：For every supplied mention and its context, use its complete report and frozen definitions to return the ATT&CK technique ID(s) it denotes. Boundaries and technical-mention selection are given. This is conditional linking of published positive annotations, not end-to-end detection, negative detection, or a complete report inventory. Preserve subtechnique specificity: use Txxxx.xxx, without collapsing to the parent. Return a duplicate-free list.

| Query | 用途 | 标签来源 |
| --- | --- | --- |
| Q1 | 原任务语义步骤，输出有序label_id列表 | 专家技术URL映射为ATT&CK ID；不按父技术折叠，粒度与论文部分实验不同 |
| Q2 | 返回链接到指定技术的提及清单，并关联所属报告；参数例 `T1140` | 同Q1派生，非独立gold |
| Q3 | 对本批给定提及按报告归并技术集合，同时区分提及数与报告数 | 同Q1确定性聚合 |
| Q4 | 未完成清单与coverage | 无独立gold，只作执行账目 |

输入投影、完整DAG和输出契约见 [queries.json](queries.json)。Q2–Q4 共用Q1中间结果，不伪装成额外语义任务或已发现operator家族。禁止把原gold复制成模型“预期输出”。

资源：[环境卡](../../environments/annoctr/resource-card.md)。源证据：[严格审查](../../docs/shared-environment-strict-audit-annoctr.md)。

状态：`DEVELOPMENT_CONDITIONAL_LINKING_ONLY`。正例条件选择不评价发现率；18条原链接缺KG定义；原文存在明示ID捷径；无跨报告实体独立性保证。

衡量指标计划：source-label exact set match, micro/macro set F1, report-clustered analysis, coverage。本次只构造与校验，没有模型推理、质量评分、独立确认划分或Strong升级。P/D/X、原排名指标与派生集合/聚合指标不得混用。

复现与实际交付：[五湖构造指南](../../docs/shared-environment-five-lakes-build.md)。

构造实测：3348条中11条源TECHNIQUE行指向软件实体，另18条技术链接缺KG；29条原gold不在技术输出目录，全部保留并在private/gold-outside-catalog.json登记，不改gold、不删输入、不把这类不可达目标算作模型机制失败。
