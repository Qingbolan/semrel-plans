# 第三十二增量：企业ESRS指标人工验证集

**不新增合格湖，累计1/10。** 找到真实企业报告上的ESRS指标抽取研究，但完整人工gold仅10家公司年×21指标，不能把数百万模型输出或重复标注算成大批量gold。这里只登记阴性核验，不列入合格清单。

## 下载与核验

- [Nature Communications原论文](https://www.nature.com/articles/s41467-026-75160-z)，2026-07-07发表，17页PDF已下载，1,336,723 bytes；web PDF工具重定向失败，但常规HTTP下载取得有效PDF并成功提取正文。
- [完整作者仓库](https://github.com/forsterkerstin/corporate-sustainability-tracker)，commit `3d8ccb1d0f0e6f212924b372f2da8510ee457d3b`，31个blob逐项Git SHA1验证、ZIP CRC通过并完整解压；软件MIT，不能扩展为全部公司报告许可证。
- [作者OSF数据](https://osf.io/q2jpv/)通过公开OSF API取得完整目录清单，下载manual_validation_set.csv 58,282 bytes、第二标注者CSV 37,463 bytes、indicator_metadata.csv 325,660 bytes、report_ids.csv 421,969 bytes。未下载约1.5GB的两份模型输出文件，未声称下载整个数据湖或9,173份报告PDF。

收据/URL/SHA256在`artifact/evidence/shared-environment-audit-20260908-v32/downloads.json`；原始资产在data同名目录。已核原论文Methods Validation、作者README数据契约及实际CSV，未执行作者模型或R分析。

## 数量和语义

实际第一/第二标注文件各210行，代表同一批10个公司年、10家公司、21个指标，每指标10行。第二标注者是复核，不增加独立cases。501条指标metadata对应短context（空白切词min15/median51/max165），不等于完整长ESRS文本。9,173个报告ID是来源登记，不等于9,173有人工gold报告。

原论文主结果为2,880,249次模型请求/847,835次返回数值，不是人工逐项验证。作者明确某指标未返回值可能由于不适用/非重大性，也可能抽取失败，不能直接作违规gold。人工CSV有75个字符串NaN，不能未经标注语义核验将它们当FALSE、违规或执行ABSTAIN。

原论文对2014–2023报告按ESRS指标做回顾性透明度衡量，不是当年依法合规裁决。即使另行下载完整ESRS，也不能把这个缺少合规判定的标签集变成监管合规gold。原PDF报告尚未本轮取得，具体数值以下仅作为作者gold条目说明，不冒充独立核实报告事实。

## 三表

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | 私有gold |
|---|---|---|---|---|
| 固定ESRS定义，从每家公司年报告中抽取Scope1排放及单位 | metadata的指标/披露要求与短context已下载；完整长规范未下载 | 人工集对应10公司年，报告文件名已列，PDF未取得 | 年报/可持续报告可能共同供证；不能仅用搜索关键词代替完整证据 | 每指标10条；210条跨21指标不能称210个同指标独立cases |
| 公司年`3ab3f5ac-9724-44f3-ae2e-ebb12dd69afd_2022` | Gross Scope1 greenhouse gas emissions定义 | 登记的同公司年AR.pdf和SR.pdf | 全部边界、单位与年份需查原文 | 作者gold=13,698,169 tCO2eq；本轮未独立对PDF核验 |

| 类python的DAG | 具体数值 | 边界 |
|---|---|---|
| `scan(manual_gold_metadata).groupby(company_year)` | 10公司年/21指标/210格 | 私有标注用于审计，不给模型 |
| `load(reports).sem_map(extract_scope1, frozen_definition)` | 固定指标N=10，报告待取得 | 未达到大批量；没有模型执行 |
| `sem_filter(disclosed).project(company_year,value,unit)` | NaN语义未冻结 | 不自动判未披露/不合规 |
| `evaluate(private_values)` | 210含75NaN，数值条目135 | 第二标注者210为相同实例复核，不是另210测试 |

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
|---|---|---|---|---|
| 本例参考13,698,169 tCO2eq；实际未运行/未读取原PDF | 固定检索Scope1表格及说明，校验公司/报告期/边界与单位，再结构化抽取；可固定跨AR/SR检索 | 同参考，不能预言更准 | ==定位排放表和计量边界==→==核对年份、Scope1与Scope2/3区别==→==检查重述或跨报告冲突==→输出值/缺证据状态 | `ESRSIndicatorOperator(definition_version, report_bundle, period, unit_rules, boundary_checks, abstain)`；不同指标可参数化，但不能用参数数目增加独立报告样本数 |

本轮满足原论文/完整作者仓库下载与可追溯核验，未达到长E＋大批量同任务gold门槛。缺口不是必须证明Agent胜出，而是只有10个公司年及原gold并非合规决定。工程测试新增0；脚本`audit_data.py`是来源统计，不构成科学有效性验证。
