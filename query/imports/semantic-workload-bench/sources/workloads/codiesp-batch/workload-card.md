# 西语病例操作编码批处理 — BUILT 开发构造契约

固定单位：西班牙语病例报告，全量 1000 条。分组：来源论文前缀代理，936组；不是患者身份确认。

Q1：For every complete Spanish case report, return a ranked, duplicate-free list of procedure codes under the supplied CodiEsp guidelines and frozen 2018 coding resources. Use lowercase codes and preserve allowed four- or seven-character specificity; do not invent missing axes. Code mention scope under the task guidelines, not whether a procedure actually occurred. Include all reports; an empty completed list means no selected codable mentions, not absence of real procedures. This task is P, not D or X.

| Query | 用途 | 标签来源 |
| --- | --- | --- |
| Q1 | 原任务语义步骤，输出有序label_id列表 | 源P病例-code集合，保留全部标签；原排序预测任务主指标MAP，集合为补充 |
| Q2 | 返回含指定操作代码提及的报告清单；不解释为患者接受该操作；参数例 `bn39` | 同Q1派生，非独立gold |
| Q3 | 按操作代码统计报告数；不把重复提及或同论文病例算成独立患者 | 同Q1确定性聚合 |
| Q4 | 未完成清单与coverage | 无独立gold，只作执行账目 |

输入投影、完整DAG和输出契约见 [queries.json](queries.json)。Q2–Q4 共用Q1中间结果，不伪装成额外语义任务或已发现operator家族。禁止把原gold复制成模型“预期输出”。

资源：[环境卡](../../environments/codiesp/resource-card.md)。源证据：[严格审查](../../docs/shared-environment-strict-audit-codiesp.md)。

状态：`DEVELOPMENT_SOURCE_LABEL_REPRODUCTION_ONLY`。原标签已有侧别及词义冲突；119份无P标注只作原集合空集；SEDOM历史资源未闭合；X不与P混评。

衡量指标计划：source-label MAP, supplemental set P/R/F1, coverage, separate rule-consistency audit。本次只构造与校验，没有模型推理、质量评分、独立确认划分或Strong升级。P/D/X、原排名指标与派生集合/聚合指标不得混用。

复现与实际交付：[五湖构造指南](../../docs/shared-environment-five-lakes-build.md)。
