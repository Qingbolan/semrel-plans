# 具体用例

**原文示例**（Fig. 1，§1 p.2；Example 1，§2 p.3）：查询 ESWC'09 中与 ontology engineering 相关论文的作者电话。

```sparql
SELECT DISTINCT ?author ?phone WHERE {
  <http://data.semanticweb.org/conference/eswc/2009/proceedings> swc:hasPart ?pub .
  ?pub swc:hasTopic ?topic .
  ?topic rdfs:label ?topicLabel .
  FILTER regex(str(?topicLabel), "ontology engineering", "i") .
  ?pub swrc:author ?author .
  { ?author owl:sameAs ?authAlt } UNION { ?authAlt owl:sameAs ?author }
  ?authAlt foaf:phone ?phone
}
```

**执行过程**（据 §2 Example 1 与 §4 组合）：
1. 解引用查询中的会议论文集 URI，从 Conference Corpus 取回数据，匹配第 2–3 行，得到每篇论文的 `?pub` 绑定；
2. 对每个 `?pub` 先解引用其 URI（Requirement 1），再匹配 `?pub swc:hasTopic ?topic`；
3. 主题也是 URI，继续解引用，取得 `rdfs:label` 并按正则过滤；
4. 沿作者 URI 和 `owl:sameAs` 链接到作者的 FOAF 资料，取得 `foaf:phone`；
5. 预取让后续迭代器需要的图多半已经到达；仍未到达时，非阻塞迭代器先拒绝该输入解、处理其他解。

**结果**（Table 1，p.12）：Q1 返回 2 个结果，取回 297 个 RDF 图，访问 16 个服务器，平均耗时 3 分 47 秒。数据来自 Conference Corpus、DBpedia 和个人 FOAF 资料。

阅读者分析：这是 2009 年网络环境下的一次运行，今天的链接与服务器状态不同，不能当作可复现结果；论文也没有给出“只查预先已知来源”的对照，无法说明遍历带来了多少额外结果。

依据：[作者预印本](https://olafhartig.de/files/HartigEtAl_QueryTheWeb_ISWC09_Preprint.pdf)，§1–2、§4、§6.1、Fig. 1、Table 1，pp.2–3、7–9、12。
