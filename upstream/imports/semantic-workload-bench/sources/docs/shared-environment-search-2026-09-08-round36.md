# 第三十六增量：IFD交易披露来源核验

**仍1/10；IFD暂不计入。** 下载原论文、完整作者仓库与官方规则后，发现批量数据未发布，标签生成与长环境依赖也未得到验证。本轮从金融申诉检索进入证券披露路线；未把FOS聚合统计当作逐案数据。

| 下载对象 | 实际证据 |
|---|---|
| [IFD原论文v1](https://arxiv.org/abs/2507.20162v1) | 12页、554,978 bytes；完整PDF已取得 |
| [作者仓库](https://github.com/CH-YellowOrange/MaBoost-and-IFD) | commit `1230fae1d6f6bcb727c405c65b3fa3bb2353da87`；3个blob全部Git SHA1验证、ZIP CRC通过 |
| 仓库内容 | README、attention-xgboost.ipynb、xgboost.ipynb；README明确接受后发布数据代码。两个notebook读取的identify_delay.csv不存在；完整下载仓库不等于取得完整数据 |
| [官方2002规则](https://www.govinfo.gov/content/pkg/FR-2002-09-03/pdf/02-22301.pdf) | 161,807 bytes已下载；两营业日变更适用于2002-08-29起交易，不能直接覆盖所有2002年旧交易 |

论文报告4,051,143条，却同时写17.4%即21,482条；按所报分母计算仅0.53027%，口径未解释。来源为WRDS，原交易和日历未释放，无法本地核验全部计数或重新计算标签。论文使用LLM生成的营业日日历并以程序计算延迟，不等于独立监管执法判定。

本次静态读取notebook：特征保留delay、gap_days及营业日字段，而只删除id标签列。对日期型标签而言这些可能直接携带判定信息；没有数据及生成器，尚不能量化泄漏或断言论文全部实验无效。未运行notebook、未训练模型；历史notebook输出不属于本次结果。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | 私有gold |
|---|---|---|---|---|
| 按适用版本判断内部人Form4交易申报是否逾期 | 已下载2002修订规则；完整历史例外、营业日及生效版本尚未构造 | 论文声称4,051,143交易；仓库实际CSV数量0 | WRDS字段及生成日历未取得；不能把52个字段名当作数据湖 | 程序派生id标签，逐条未取得；独立裁决gold未见 |
| 论文Table3的DCN02720220 | 交易日期早于2002-08-29，不能直接套新两日规则 | TRANDATE=2002-08-01，SECDATE=2002-08-06；FDATE=2012-05-29，字段含义/修订来源需核验 | 表内Delay=1、Gap Days=-3589，不能从名称自选正确申报日期 | Table3 id=0；仅论文示例，未取得源记录，不擅自改gold |

| 类python的DAG | 具体数值 | 当前边界 |
|---|---|---|
| `scan(identify_delay_csv)` | 可读取交易0条；论文声称4,051,143 | 必要CSV缺失，默认路径不可运行 |
| `bind_rule(trade_date).resolve_filing_date()` | 示例2002-08-01在新规则生效前28天 | 应先绑定历史规则，不能将表中2012日期当作已核验申报日期 |
| `business_day_deadline(rule, calendar, transaction)` | 两营业日只是部分时段的规则 | 日历和例外须外部可核验，不将LLM生成日历当gold |
| `filter(filed_after_deadline).project(dcn).count()` | 实际输出与计数未知 | 未完成构造或评分，延迟不自动等于故意违规 |

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
|---|---|---|---|---|
| 示例参考id=0，但源字段未核验时应ABSTAIN；没有实际模型预测 | 固定解析适用日期和申报字段，确定规则后调用日历计算器；共享预处理与缓存均允许 | 同样需要正确历史版本与字段；不能保证优于固定日期程序 | ==核对日期字段来源与修订含义==→==识别交易早于新规则生效==→==检索当时期限及例外==→在证据充分后计算，否则ABSTAIN | `FilingDeadlineOperator(rule_version, effective_date, transaction_type, filing_date_resolver, business_calendar, exceptions, abstain)`；固定程序、仅E编译和Coding Agent均须比较 |

当前不能以“百万交易+金融合规”计为合格湖。即使后续取得CSV，还须验证共享规范实际复杂性、标签与日历独立性及真实字段来源。原材料在data/shared-environment-audit-20260908-v36，下载收据、哈希验证和统计在artifact/evidence/shared-environment-audit-20260908-v36。无模型成本、准确率或单轨迹提取结论。
