# BioDEX reactions — BUILT / DEVELOPMENT PILOT

身份：BioDEX: Large-Scale Biomedical Adverse Drug Event Extraction for Real-World Pharmacovigilance；2023-05-22预印本arXiv2305.13395，Findings of EMNLP2023来源。官方：https://github.com/KarelDO/BioDEX ；任务数据：https://huggingface.co/datasets/BioDEX/BioDEX-Reactions 。本轮已固定revision `01a5dacdabd144a120af04931a11a99febd48432`，获取8篇开发样本并构造公开/私有快照。

原始资源约65k摘要、19k全文和256k关联专家药物安全报告。不能把原始报告数当作BioDEX-Reactions独立样本数；任务卡报告test 4249、train 11543、validation 2886；本轮只从test固定选择8篇，不将其作为确认集。全文许可按article.fulltext_license逐文检查；代码MIT不覆盖全部数据，术语表版本/使用权另查。

真实任务：批量将文献报告的反应映射到标准术语，输出article-reaction关系和排名。拟固定DAG：scan全文→sem_map反应候选→术语搜索→sem_filter核验→输出关系→每文献/术语汇总。默认输入完整，不能靠截断关键证据制造失败。

gold沿用任务发布的反应列表，原始专家报告只在private。未标注反应不能未经审查就等价医学上绝对不存在；明确采用benchmark标签口径并审计漏标。若转成二分类article-term任务，须预定义负例生成与审核，否则保留原多标签/排名任务。

真实来源示例：作者README的raw_dataset索引1展示“Case Report: Perioperative Kounis Syndrome in an Adolescent With Congenital Glaucoma”，关联报告列Kounis syndrome和Hypersensitivity。仅用于说明真实全文—报告映射；不是本仓库载入的稳定record ID，也不是LOTUS失败例。正式冻结应记录源文章ID而非依赖行号。

候选环境资源：全文/章节、固定标准术语目录、文档和术语检索工具、公开解释及工具说明；每项需通过可达性/泄漏/增益核验，不能凭可构想就宣布已具备。临床治疗、诊断或新因果判断不属于任务。

主要指标RP@k及原官方评分；另测抽取/候选召回、错误类型和下游关系完整性。Agent可能逐步发现遗漏与改写查询，尚无本地实测。单示范可复用项假设为章节定位/候选生成/证据核验策略；不声称一个病例教会全部领域知识。

冻结协议见 `docs/biodex-gap-pilot.md`；来源/许可/索引见 `environments/biomedical/sources.lock.json`。本轮使用完整原始全文、24,369项公开术语表及冻结向量检索资源；固定程序也有LLM排序，不能称复现旧余弦排序表。运行/评分收据在 `runs/biodex-gap-pilot-v1/`，本轮结论见report.md。没有单轨迹提取或独立确认。

本轮终态：PILOT_SCORED_NOT_VALIDATED，未通过Agent主指标优势筛选；完整数值及任务有效性边界见根目录docs/pilot-results-2026-09-05.md。

Actual Codex CLI same-model development result: RP@10 **0.3393**, coverage8/8, no out-of-catalog labels or unsupported quotations. Primary agreement did not improve; frozen patient-ADR prompt/gold scope risk remains. [Evidence and limits](../../docs/codex-cli-results-2026-09-05.md).
