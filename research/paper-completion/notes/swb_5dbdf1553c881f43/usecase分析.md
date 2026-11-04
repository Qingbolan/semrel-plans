# 具体用例

**用例：为 PubMed/PubTator 全文检索标注化学物质**（摘要；Usage Notes，pp.9–10；p.11）

研究者想找全所有讨论某种化合物的论文，包括只在正文 Methods 或 Results 中提到该物质的论文。NLM 的流程如下：

1. BlueBERT 在全文中识别化学提及。例如同一文章里可能出现 "triphenyl phosphate" 和缩写 "TPHP"。
2. MTCR 先用 Ab3P 从全文中找到缩写定义，把 "TPHP" 还原为全称；再用 MeSH 精确/宽松匹配，或经 ChEBI、UNII 等术语表的交叉引用，得到 MeSH ID。
3. 若某提及在多个候选 ID 之间有歧义，就与文档内无歧义的 ID 求交集来消歧。
4. 结果通过 PubTator API 对全部 PubMed 每日更新。

**为什么需要全文**（Table 5、p.9）：作者原以为 Methods 中多是试剂，但检查后发现 Methods 中也有许多具体化学物质，Methods 独有的不同提及达 1,098 个，因此得出结论：对很多检索与索引任务，处理全文是有用的。

阅读者分析：对语义检索类查询而言，这篇论文支持"只看摘要会漏掉大量实体"的判断；但它评测的是实体识别，没有直接评测检索效果。

依据：摘要、Methods（MTCR）、Usage Notes、Table 5，PDF pp.1、5–6、9–11。
