# Semantic operator 文献检索与核读

检索日期：2026-10-14。范围是使用模型实现数据操作、以关系/文档/多模态集合为输入的语义查询系统及其优化；不把语义分割、知识图谱本体上的传统semantic query、泛用SQL hint生成自动视为同一研究问题。

## 检索方法

首先核对现有Survey目录和项目已关联的论文，再以LOTUS、Palimpzest、DocETL、Abacus、QUEST、ThalamusDB、CAESURA、Aero为种子，结合前向关键词检索和论文related work追踪。关键词包含semantic operators、semantic query processing、semantic join、cost-based optimizer、unstructured analytics、LLM-native query optimization、LLM batch data analytics及2026年份限定。

使用arXiv原站、PVLDB/CIDR/NeurIPS正式论文、作者项目页与代码仓库验证身份。搜索结果中的二手介绍只作线索，结论回到原站。当前arXiv标题PLOP与旧索引标题Horrila共用2604.09944，不拆成两篇。`aliases.json`记录正式出版/预印本身份关系，技术报告与短会议稿保留版本区别。

检索不代表可证明覆盖所有全球文献；本目录提供可追踪的候选集和实际阅读状态，便于后续按引文增量扩展。

## 阅读结果

四篇本轮逐节阅读全文正文，并渲染关键实验表格核对：

| 论文 | 版本 | 核对位置 |
|---|---|---|
| LOTUS | PVLDB18(11),2025 | §1–8、表1–7、图1–7；实验页4179 |
| DocETL | PVLDB18(9),2025 | §1–7、表1–6、图1–5；实验页3043 |
| Abacus | arXiv2505.14661v3，对应PVLDB19(5),2026 | §1–7、表1–3、图1–8；PDF第9页 |
| QUEST | arXiv2507.06515v2,2025 | §1–6、表1–3、图1–8；PDF第11页 |

原PDF、提取文本、渲染页在`pdfs/`，哈希在`review_index.json`与catalog。七部分分析分别为README、出发点、问题、Novelty、用例、workload、benchmark。本轮未复现实验、未逐行审计四个系统实现、未读取外链技术报告的所有额外附录；此处“全文核读”明确指下载版本的正文。

其他候选以`abstract_only`或`metadata_only`记录，没有生成假装精读完成的七份模板。已有Survey阅读状态不自动计入本轮完成量。

## 影响当前图册的数据结论

- LOTUS的64是模型inference batch，OpenAI实验64是线程并发，FEVER1000是输入数；不能共用batch字段。
- DocETL BlackVault的41是fold batch，Steam104652是chunk token数，CUAD41是条款种类数。
- Abacus的k=6、j=4是物理候选与优化输入采样数；不是用户输入表6列4行。
- QUEST主表50查询，另有60双表与30多表join实验；本地83记录来自源artifact版本，不应写成论文全部查询的精确枚举。
- Abacus v3摘要与结果叙述存在百分比不一致，DocETL BlackVault类别数正文与表格也不一致；分析保留表格原值和位置，不擅自消除证据差异。

所有“环境需求”按辅助语料、标签、索引或数据表解释；GPU/模型配置放在复现实验设置中。原始英文query仅在有明确原文位置时引用，不从中文总结生成伪原query。


## 补充全文核读
2026-10-14追加Palimpzest技术报告v2、SemBench v2、UDA-Bench v1三篇，共7篇全文分析，每篇7节。当前catalog共28条，7 full_text_reviewed、19 abstract_only、2 metadata_only。版本规模分别保留：SemBench55query、UDA5数据集240query；未声称逐条核验官方全部query文件。新增三篇关键表格均已PDF渲染核对。
