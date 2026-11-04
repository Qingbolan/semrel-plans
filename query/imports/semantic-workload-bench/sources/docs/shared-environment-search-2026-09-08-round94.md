# Increment94 — CRAFT排版输入审计与公开/私有检查包

仍7/15，CRAFT尚未新增资格。本轮复用round56已下载原论文、47页指南和完整作者仓库commit `2abe82b8bb8089448b84937d5f61d8c218011322`，没有用新近摘要代替原始数据。来源：[原论文](https://doi.org/10.1186/1471-2105-13-161)、[完整作者仓库](https://github.com/lhunter-lab/CRAFT)、[作者当前规则](https://github.com/lhunter-lab/CRAFT/blob/2abe82b8bb8089448b84937d5f61d8c218011322/concept-annotation/README.md)。原下载哈希见v56收据。

排除指南明确引用46篇后，51篇均有sections-and-typography结构，类型为section906/italic7225/sup2725/bold376/sub513/underline14。逐项跨度与正文检查发现15328538有3处不一致，其中Author contributions跨度从uthor开始，不能只称空格差异。该文在本开发构造中排除，不修原始数据。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold |
|---|---|---|---|---|
| 建立全文CHEBI概念及出现位置索引 | 50篇完整源文本 | 47页指南＋当前作者规则＋冻结CHEBI扩展本体 | 11647个给定人工上游排版/章节跨度 | 8621概念提及，30不连续；concept gold完全私有 |
| PMID14723793开发示例：识别N末端与共享尾词 | N-与后文terminals及完整上下文 | 协调短语、不连续跨度和扩展概念定义 | 可给定格式结构，不公开概念跨度 | N-[19619:19621]＋terminals[19628:19637]构成同一概念提及 |
| 按文档生成概念集合或出现次数 | 同提及预测 | 固定集合/计数定义 | 确定性投影聚合 | 从同原生gold派生，不算第二独立湖或新的人工任务 |

| 类python的DAG | 具体数值 | 下游gold |
|---|---|---|
| `docs.attach(given_typography).sem_map(chebi_mentions,E)` | 50全文＋11647给定结构→目标8621提及 | 50个源实体，不是8621篇独立文档 |
| `mentions.validate_spans().groupby(doc).collect(concept_id,spans)` | 30不连续提及 | 保留多个跨度组合，不能用平坦BIO标签覆盖任务 |
| `mentions.groupby(doc,concept).count()` | 未运行模型 | 真值可由私有mentions确定性计算，未建立额外独立聚合标注 |

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
|---|---|---|---|---|
| 开发例输出N-和共享terminals两个跨度、相应N末端扩展概念；未测 | 同全文/排版/本体/指南的固定检索与sem_map，验证跨度后聚合 | 同目标，不预设优势 | ==查协调结构规则与扩展概念定义，核对共享尾段==→输出多跨度提及 | `protocol_lookup→ontology_candidates→context_match→discontinuous_span_binding→validation`；未提取/冻结 |
| 完整50篇索引输出未知 | 固定程序可缓存协议与本体索引，必须包含E-only编译对照 | 同等资源与预算下输出未知 | ==按公开资料处理边界/定义歧义==→输出 | 不能使用private源映射、未使用类别列表或gold候选集 |

已构造data/shared-environment-audit-20260908-v94/inspection-v2，57资产含公开文档/规则/本体/task及私有gold/source-map/exclusions；公开文档字段严格为record_id/text/provided_upstream_typography。独立读取检查50个ID对应、全部目标跨度范围与57资产哈希，0错误。尚未做此包逐原生gold tuple一致性复核、完整示例泄漏或协议裁剪，故保持检查包状态。

输入条件显式为ANNOTATION_GIVEN_UPSTREAM_TYPOGRAPHY。字体间边界来自给定人工结构，不能宣称是模型从PDF感知出的结果。它不含当前目标概念标签，但这种上游监督量必须报告。与raw-PDF端到端任务不等价，不用缺排版的弱输入制造Agent优势。

构造v1因假设存在CHEBI/README.md失败，已写FAILED.json保留，禁止使用；原扩展规则实际位于concept-annotation/README.md，纠正后发布到全新v2，未覆盖原产物。原文/本体/注释许可分别遵循源，不因本地检查包取得新再发布权利。脚本audit.py/build.py、typography-audit.json/build.json/verify.json在artifact同v94；无模型、无成本、无独立确认结论。
