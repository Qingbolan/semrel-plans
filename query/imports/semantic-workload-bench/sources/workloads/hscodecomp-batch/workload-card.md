# 商品HTS编码及批量归类表 — BUILT 开发构造契约

固定单位：发布商品记录，全量 632 条。分组：商品ID；来源按类别及标签平衡，非自然流水频率。

Q1：For every product in records.json, use its published title, attributes, price, currency and marketplace categories with frozen HTS 2025 Revision 15 to return one 10-digit HTS code as a singleton string list. Consult hierarchy, unnumbered parent rows and full notes. Do not assume price is per item, invent photos, convert currency without evidence, or reconstruct missing product facts. If a supported classification cannot be completed, ABSTAIN with null value and a concrete reason. The source-label task supplies no independent UNKNOWN gold.

| Query | 用途 | 标签来源 |
| --- | --- | --- |
| Q1 | 原任务语义步骤，输出有序label_id列表 | 独立专家10位码；前缀目标由同一标签派生 |
| Q2 | 按参数化2/4/6/8/10位编码前缀返回商品清单及数量；参数例 `70` | 同Q1派生，非独立gold |
| Q3 | 按预测完整编码统计商品数；前缀筛选为派生诊断，不是独立专家gold | 同Q1确定性聚合 |
| Q4 | 未完成清单与coverage | 无独立gold，只作执行账目 |

输入投影、完整DAG和输出契约见 [queries.json](queries.json)。Q2–Q4 共用Q1中间结果，不伪装成额外语义任务或已发现operator家族。禁止把原gold复制成模型“预期输出”。

资源：[环境卡](../../environments/hscodecomp/resource-card.md)。源证据：[严格审查](../../docs/shared-environment-strict-audit-hscodecomp.md)。

状态：`DEVELOPMENT_INCOMPLETE_INPUT_DIAGNOSTIC`。图片、单位价格、外部裁定及汇率事实未闭合；不可用缺事实造成的失败证明Agent优势。

衡量指标计划：source-label exact 10-digit accuracy, prefix diagnostics, coverage, input-gap audit。本次只构造与校验，没有模型推理、质量评分、独立确认划分或Strong升级。P/D/X、原排名指标与派生集合/聚合指标不得混用。

复现与实际交付：[五湖构造指南](../../docs/shared-environment-five-lakes-build.md)。
