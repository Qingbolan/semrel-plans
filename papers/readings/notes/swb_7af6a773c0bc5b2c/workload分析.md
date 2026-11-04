# workload

**语料**：GENIA 事件语料，1,000 篇 MEDLINE 摘要，36,858 个事件，其中 44% 为复杂事件（Results：KT）。标注工作：
- 2 名外部标注者，一名是生物学专家，一名是语言学专家；
- 先用 GENIA pathway 语料中的 70 篇摘要做练习；
- 方案可行性试验中，两位作者在同样的 70 篇上取得 Kappa 0.89–0.95；
- 标注指南共 66 页；
- 随机抽取 104 篇（10%）由两人都标注，用于计算一致性。

**各维度分布**（% 均为占全部事件的比例）：

| 维度 | 分布 |
|---|---|
| KT（Table 3） | Observation 12,821（34.7%）、Other 11,537（31.3%）、Analysis 6,578（17.8%）、Fact 2,998（8.1%）、Investigation 1,948（5.3%）、Method 976（2.6%） |
| CL（Table 5） | L3 33,876（91.9%）、L2 2,216（6.0%）、L1 766（2.1%） |
| Polarity（Table 7） | Negative 2,263（6.1%） |
| Manner（Table 10） | High 1,392（3.8%）、Low 323（0.8%） |
| Source（Table 13） | Other 545（1.5%） |
| 超维度（Table 15） | New Knowledge=Yes 15,985（43.4%）、Hypothesis=Yes 4,924（13.4%） |

**线索词**（Table 4）：Analysis 常见 suggest、show、demonstrate；Investigation 常见 examined、investigated；Observation 常见 found、observed。Fact 事件中只有 4.6% 带线索词，Observation 事件中只有 7.3% 带线索词。

与图谱查询的关系：图谱查询"事件标注：KT、CL、极性、方式与来源"与本文的五个维度直接对应。阅读者分析：各类别分布高度偏斜，评测时应使用按类别计算的指标。

依据：[BMC Bioinformatics 12:393，PMC3222636 全文 XML](https://doi.org/10.1186/1471-2105-12-393)，Methods、Results，Tables 3–15。
