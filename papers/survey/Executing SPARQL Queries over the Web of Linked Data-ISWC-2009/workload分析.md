# 工作负载

**两类工作负载**（§6，pp.11–13）：

| 工作负载 | 内容 | 规模 | 用途 |
|---|---|---|---|
| 真实 Web 查询 Q1–Q4 | 作者电话（ESWC09）、Tim Berners-Lee 认识的人的兴趣、药物 Varenicline 的天然替代、Peter Jackson 电影原声封面 | 每查询 28–442 个 RDF 图、6–46 个服务器 | 可行性演示 |
| BSBM 查询混合 | Berlin SPARQL Benchmark 的 12 个查询，改写为访问模拟服务器 | scale 10–60，4,971–26,108 三元组 | 预取与非阻塞的受控比较 |

**真实查询的数据来源**（§6.1，p.12）：Q1 用 SW Conference Corpus、DBpedia 与个人 FOAF；Q2 用 Tim Berners-Lee 及其认识的人的数据；Q3 用 DrugBank、Diseasome、Traditional Chinese Medicine 数据集；Q4 用 LinkedMDB 与 MusicBrainz。查询的 SPARQL 写法只放在作者的演示页上，论文正文只给 Q1（Fig. 1）。

**模拟 Web**（§6.2，p.13）：用 RAP Pubby 搭的 Linked Data 服务器按 Linked Data 原则发布 BSBM 生成数据。每个规模把查询混合运行 6 次，第一次作热身不计。

**单位**：一个“查询执行”= 从种子 URI 开始、边遍历边匹配直到结束；Table 1 报告的是多次执行的平均值。

阅读者分析：两类工作负载都没有“全网应答”的完整 gold，无法衡量召回；BSBM 服务器规模很小，且没有真实 Web 的延迟分布与不可用情况。

依据：[作者预印本](https://olafhartig.de/files/HartigEtAl_QueryTheWeb_ISWC09_Preprint.pdf)，§6.1–6.2、Table 1，pp.11–13。
