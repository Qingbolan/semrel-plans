# 第十四增量：CLEF TAR逐review协议—批量—gold连接

2026-09-08，Asia/Singapore。仍0/10严格通过。此处保留候选核验记录，不将其列为通过的数据湖。

## 原始材料

已下载[原始2019论文](https://ceur-ws.org/Vol-2380/paper_250.pdf)及[完整官方仓库](https://github.com/CLEF-TAR/tar)，commit `dbc13d02bb3e2f8ebc90e62ff47f5eb591e5ca20`。仓库ZIP334,825,063 bytes，1,919个Git blob逐项一致；包含历年评测和参赛运行产物，绝不把参赛输出当gold。未执行作者代码。

原始下载`data/shared-environment-audit-20260908-v14/`；[收据](../artifact/evidence/shared-environment-audit-20260908-v14/download-receipts.json)、[复算脚本](../artifact/evidence/shared-environment-audit-20260908-v14/audit_data.py)、[逐review连接表](../artifact/evidence/shared-environment-audit-20260908-v14/protocol-review-groups.json)、[统计](../artifact/evidence/shared-environment-audit-20260908-v14/statistics.json)。

2019 Task1中protocols/protocals（上游拼写）共121文件、118个不同review ID。解析文本词数中位564，最大4,519；2个XML解析失败按原字符串计数并标记，不声称成功提取。不同split相同review不自动算独立湖。筛选任务Task2返回PMID清单，完整候选全文没有随仓库发布。

论文§2.3解释gold由最终review的Included/Excluded/Additional参考文献构造：摘要层正例是Included∪Excluded，全文层正例是Included。不是直接发布原始逐条screening日志。论文也明确只提供protocol的相关部分，并指出候选全文版权限制。

## 较强的具体组

`CD012165`：子宫内膜生物标记对盆腔子宫内膜异位症的诊断准确性。关联10,222个不同PMID；摘要层正例308，全文层正例47。协议XML4,519词，但objective字段2,118词，内嵌QUADAS-2偏倚评估表及研究质量判定规则。

这些规则可能服务于风险偏倚/适用性评估，而非纳入筛选本身。比如随机/连续入组、排除不当、失访比例等规则，不能因文本长就宣称每篇纳入判断依赖它们。部分文字描述“没有纳入研究被判为某类”的已完成review观察，也需从预筛选环境中审计隔离。没有直接把原objective字段挂载为无泄漏E。

本轮另实际下载[PMID22230112](https://pubmed.ncbi.nlm.nih.gov/22230112/)及[PMID15733405](https://pubmed.ncbi.nlm.nih.gov/15733405/)的PubMed XML和摘要。两篇都是原content gold正例。前者研究VEGF/sFlt-1并在腹腔镜手术时取得样本；后者研究MMP-9/TIMP-1，摘要报告45位内异症患者和32位子宫肌瘤对照。均为开发暴露例子，不作独立确认。仅下载两篇摘要，未称取得10,222篇全文。[例子数据](../artifact/evidence/shared-environment-audit-20260908-v14/development-papers.json)。

## Query与数据湖表

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold |
| --- | --- | --- | --- | --- |
| 根据CD012165标准，筛选候选进入全文审查 | 协议相关片段4,519词，需剔除不适用内容和事后信息 | 10,222个PMID；本轮取得2篇摘要 | 生物标志物、样本类型、目标病症和参考标准相关字段 | abs正例308；全文正例47另存，不混成一个任务 |
| PMID22230112是否进入本review最终纳入清单 | 目标是子宫内膜标志物的诊断准确性 | 摘要含VEGF/sFlt-1、多组织取样和腹腔镜 | 完整论文证据未取得 | content=TRUE；摘要单独充分性未证明 |
| PMID15733405同一判断 | 同一review标准 | 45病例/32对照及免疫组化检测，摘要已取 | 非完整论文 | content=TRUE；不能从该例直接抽取通用病例对照排除规则 |

## 类Python DAG

| 类python的DAG | 具体数值 | 边界 |
| --- | --- | --- |
| `groups = join(protocols, qrels, review_id, split, type)` | 121文件/118不同review | 本轮实际执行，保留重复与错误 |
| `E = audit_and_freeze(protocol_parts)` | CD012165原文4,519词，objective2,118词 | 审计尚未完成；不能伪称30页protocol PDF |
| `R = fetch_pubmed(pmids)` | 总10,222；本轮仅2篇 | 已保存2篇XML，不推断全文可得 |
| `facts = sem_map(R, study_population_test_reference)` | 病种/样本来源/检测/参考标准 | 未运行 |
| `selected = sem_filter(facts, E, stage='abstract')` | 原gold选中数308 | 拟议；全文stage目标47是另一个契约 |
| `evaluate(selected, private_abs_gold)` | 10,222分母 | 未评分，不能用取到的两正例宣称准确 |

## 多种方法预期表

全部是未实测的目标和过程，不是性能报告。

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent 的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
| --- | --- | --- | --- | --- |
| 两篇例子的原content目标TRUE，但摘要是否足够未核 | 固定标准抽取→样本/检测/病种映射→同资源参考标准核对 | 同目标；若缺全文则不能保证正确 | ==核review目标与多组织样本是否包含目标组织==→==查允许公开的参考标准证据==→缺证据保留不确定 | `StudyFacts → ScopeCheck → ReferenceStandardCheck`，不能写死PMID |
| 摘要筛选预计目标308项，结果未知 | 静态条件拆解可直接使用全部相关标准，允许固定检索和缓存 | 是否改善未知 | ==分清摘要升级判断与最终纳入==→按同阶段规则处理 | 阶段参数与证据充分性约束，避免用全文gold惩罚正常摘要升级 |
| E-only编译可能已足够 | 仅从协议相关字段生成谓词，并与固定工具/Coding Agent比较 | 一次轨迹能带来什么须实测 | ==记录真实执行访问了哪些规则和材料==→自动提取→冻结→独立批次 | 无轨迹编译对照、相同资源和预算；质量评估规则不应人为塞入筛选流程制造复杂性 |

## 决定与范围

此数据实证满足真实文献、大同review批量、构造gold，但未满足所要求的完整长共享环境与必要依赖。最长片段的额外长度部分来自另一任务的质量评估，不以此通过。不能从这种不通过推断公开长protocol绝不存在；下一步可以找实际完整protocol与原始筛选审计记录的绑定来源。

新增工程测试0；执行下载、Git blob/词数/qrels统计、两篇PubMed读取，无模型/提取器/作者代码运行。模型预算、prompt、种子及推理缓存均不适用。许可与全文获取、事后信息隔离、复杂E因果增益均未完成。论文/仓库完整下载已完成且无活跃进程。
