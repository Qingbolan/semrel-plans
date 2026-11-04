# Hartig, Bizer, Freytag — Executing SPARQL Queries over the Web of Linked Data

开放的 Linked Data Web 上无法预先列出回答一个查询所需的全部数据源。本文提出“链接遍历式”查询执行：从查询中的 URI 和部分结果中的 URI 出发，在执行过程中通过 HTTP 解引用取回 RDF，不断扩充被查询的本地数据集；实现上用迭代器流水线做基本图模式（BGP）匹配，并加入 URI 预取和可暂时“拒绝”输入解的非阻塞迭代器。

在 4 个真实 Web 查询上，系统在 46 秒到 3 分 47 秒内返回 2–27 个结果（Table 1）；在模拟的 BSBM Linked Data 服务器上，预取把查询混合执行时间降到约 80%，非阻塞迭代器约减半（§6.2，Fig. 6a）。

[原文](https://olafhartig.de/files/HartigEtAl_QueryTheWeb_ISWC09_Preprint.pdf)；[出版信息](https://doi.org/10.1007/978-3-642-04930-9_19)

版本：作者预印本（TeX 生成于 2009-08-13），16 页；正式版 ISWC 2009，LNCS 5823，pp.293–309。阅读范围：2026-11-04 对照预印本全文重读 §1–8 并核对数字；§3 形式化未逐式证明，未复现实验。
