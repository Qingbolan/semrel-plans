# 第二十六增量：UDRP可行性审定与前部脚注修正

**计入第1个结构与来源已核验、可构造开发实验的数据湖。** 本结论限定为从公开裁决中的程序背景、已记载事实和双方主张，按共享UDRP环境预测投诉是否应获转移或撤销救济的回顾性任务。不是原始诉状预测、临床/司法部署、方法优势或已完成独立确认。十湖目标仍缺9个，不把多个UDRP版本算多个湖。

## 对原始要求的证据

| 要求 | 已核验证据 | 未据此声称 |
|---|---|---|
| 长/复杂共享E，判断确实依赖它 | 官方WIPO Overview3.0及政策/细则152页；1543/1572案原始专家分析明确引用同一Overview；包含三要件、证明责任、注册时间、合理利益和具体例外 | 不声称每案需要全部152页，也不声称轨迹学习优于E-only规则编译 |
| 同一任务、大批量真实cases | 作者发布的真实WIPO D2024案件，单域名1603条中1572条满足公开标题构造条件；§1–§5输入与§6–§7结果分离 | 31条格式未覆盖，不称1603全量就绪；不是合成案件 |
| 每条case有独立gold | 正式专家裁决的救济结果，统一提取为1513 RELIEF_GRANTED、59 DENIED；原Decision和metadata另存，已保留已知细粒度差异 | 提取程序不是新的专家意见；本轮8条复核不代表逐案人审全部完成 |
| 原论文和完整作者仓库下载 | [原论文18页](https://astrolavos.gatech.edu/articles/Manuscript_UDRP_final.pdf)及[完整作者代码/数据归档](https://doi.org/10.5281/zenodo.16954717)843037756bytes，MD5/size和57条目CRC均已通过、完整解压 | 作者MIT软件许可不自动覆盖上游文书/官方指引重新发布权利 |

作者归档SHA256 `cc5a666db9f6097e3e1ed73a30afb4c62ec50130e077db0fcdc4a7aea76306b4`。第22–25轮有原始下载与统计依据。本轮没有新下载、没有模型运行。

## 本轮审核和修正

全1572份public输入检查未见保留的§6/§7标题，也未见整个正式决定开头的精确回显；但这两个检查**不足以排除泄漏**。进一步读取42个非标准程序措辞命中，发现前部脚注会提前透露“执行转移指令附件”，因此原v25输入不能直接用于比较。

新增public-only统一规则识别本案Panel attached/authorized Annex1、Registrar及transfer/order的执行公告句，v2删除35案69句，保存精确删除内容/位置及输入输出hash；不读取gold选择删除项、不删除整案。第一版留下删除标记，标记本身可能成为线索，因此另建v2直接删除，未覆盖旧版本。v2仍命中4个instructions/transfer上下文，逐条读取为历史域名转移及资金转账，合法事实保留。不能将当事人引用旧案判词、请求救济或程序认定全部删掉。

公开v2：`data/shared-environment-audit-20260908-v26/public-v2/`。对应private v2 gold：`data/shared-environment-audit-20260908-v25/gold-extraction-v2.jsonl`。审计脚本、8条确定性gold抽样、42语言命中、原39执行指令命中、v1/v2删除收据均在`artifact/evidence/shared-environment-audit-20260908-v26/`。8条按每类SHA256排序取4条，全部正式裁决与粗标签一致，属于研究者读取检查而非新增法律专家标注。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | 私有gold |
|---|---|---|---|---|
| 为品牌保护案件批量筛选按UDRP应获得域名转移或撤销救济的投诉 | [官方152页共享解释环境](https://www.wipo.int/amc/en/docs/2023_overview3.pdf) | 1572真实单域名案，经过已知执行公告移除的§1–§5 | 具有归属的事实、主张、程序背景；原文的事实认定已给定，非从原始证据重新认定事实 | 1513获救济/59驳回，正式裁决独立保存 |
| D2024-0001 vs D2024-0061，均为开发例 | 相似性、合法利益、恶意需分别判断 | 前者冒充车队网站；后者存在广泛第三方使用和是否针对商标的争议 | 当事人主张与已记载事实不能混淆 | 前者Transfer→True；后者denied→False；不是预先判定两方法能答对 |

| 类python的DAG | 具体数值 | 说明 |
|---|---|---|
| `scan(public_v2.queries).read(case_path)` | 1572条，与private记录ID对应 | 不挂载当前gold/专家分析或允许检索本案裁决 |
| `sem_map(apply_udrp, frozen_E)` | 输出RELIEF_GRANTED/DENIED/ABSTAIN | 无模型运行收据，不造指标 |
| `sem_filter(label==RELIEF_GRANTED).project(id).count()` | gold参考1513，非预测结果 | 强偏斜，必须报告负类/清单质量及常量获救济对照 |
| `evaluate(private_v2, frozen_predictions)` | 开发暴露，尚无独立split | 全量成本及质量需后续实验 |

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
|---|---|---|---|---|
| 示例目标分别True/False，实际正确性未知 | 同样完整E与输入，固定检索、事实抽取、三要件及例外判断；可共享E编译/缓存 | 同目标，不预言Agent更准 | ==定位与事实相关的规则及例外==→==核对时间、程序、证据归属和缺口==→输出决定/ABSTAIN；不得读取本案专家分析 | `UDRPReliefOperator(E_hash, attributed_facts, elements, exceptions, procedural_conditions, abstain)`；与E-only编译、固定工具、Coding Agent、批Agent公平比较 |

**可行性与科学有效性分开**：原始结构、真实来源和共享规范依赖已有证据，因此本轮可计为可构造湖；当前开发包仍需更广的语义泄漏审核、近重复/主体分组、源文书事实选择偏差分析、正式标签独立复核和实验隔离。这些限制不能被“本轮正则通过”掩盖，也不因尚未证明Agent更优而否认该工作流存在。这里没有将任务登记为仓库VALIDATED workload。
