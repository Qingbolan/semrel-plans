# workload

**金标准（Table 1）**
- 5,000 篇 PubMed 摘要（2005–2014 年发表），训练/开发/测试 = 3,500/750/750，随机划分，但先前 ChemProt 的摘要全部放在训练或开发集。
- 关系 17,274/3,761/3,491，共 24,526；分布极不均衡：inhibitor 7,589 条，而 agonist-inhibitor 18 条、substrate_product-of 37 条、agonist-activator 39 条（测试集中为 0）。
- 实体：gene 61,775、chemical 65,561。249 对实体有两个关系标签；659 个提及同时被标为 CEM 和 GPRO。
- 一致性：化学物标注在 100 篇上的 IAA 为 91%（精确匹配）；关系层因标注者多，未计算传统 IAA，而由更资深的第二标注者抽检。

**大规模语料（Table 2）**：按 10 条选文标准（MeSH 查询、NER 结果、文档分类器、元数据）从 PubMed 选出 3,966,792 篇，过滤空标题/空摘要或无同句 CEM+GPRO 的文档后余 2,366,081 篇，含 33,578,479 个 GPRO 和 20,415,123 个 CEM 自动提及；于 2021-06-17 下载。M 赛道背景集 10,000 篇含 291,856 个自动实体。

与图谱查询的关系（阅读者分析）：图谱把本文列入"共享环境批处理语义任务"证据；原文可直接支撑的是同一套关系指南被套用到数百万摘要上做批量抽取，其他推断原文未讨论。

依据：[Miranda-Escalada et al., Database 2023, baad080，JATS 全文](https://doi.org/10.1093/database/baad080)，Materials and methods；Results：Tables 1–2。
