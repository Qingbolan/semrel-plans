# 具体用例

**用例：给一段文本中的子句逐一打 SE 标签**（Figure 1、§2，pp.1757–1758）。

| 子句 | SE 类型 | 判断线索 |
|---|---|---|
| The colonel owns the farm. | STATE | 主动词 own 为静态 |
| John won the race. | EVENT | 动态、一次性 |
| “...”, said Obama. | REPORT | 引语动词 |
| The lion has a bushy tail. | GENERIC SENTENCE | 主指称为类别 |
| Mary often fed the cat last year. | GENERALIZING SENTENCE | 特指主语、惯常 |
| John might win. | STATE | 情态把事件转为状态 |
| Elephants are not small. | GENERIC SENTENCE | 否定不改变类指句类型 |

系统流程：CoreNLP 分词、词性与依存分析；抽取主动词（时态、语态、WordNet 义类、Gigaword 统计的语言学指示特征等）、主指称（限定词类型、数、可数性、是否光杆复数等）与子句特征（情态、否定、条件、副词）；再由 CRF 联合输出整篇文档的标签序列（§5，pp.1760–1761）。

**难例**：“You must never confuse faith” 被不同标注者分别标为 IMPERATIVE 和 GENERIC SENTENCE（§4，p.1760）。

阅读者分析：在语义算子语境中，这类标签可作为“筛选描述一般规律的句子”或“区分事件与状态”的前置分类器；本文只评测分类本身，不涉及下游应用效果。
