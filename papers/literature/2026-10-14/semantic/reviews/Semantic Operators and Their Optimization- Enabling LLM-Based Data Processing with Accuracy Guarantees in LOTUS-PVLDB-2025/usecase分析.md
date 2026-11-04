# 具体用例

| 用例 | 查询输入 | 需要的数据环境 | 输出 |
|---|---|---|---|
| FEVER事实核验 | claim文本列 | Wikipedia语料及ColBERT索引 | supported/not-supported标签 |
| BioDEX药物反应匹配 | 医学论文文本表 | 不良反应标签表 | 每篇论文的反应标签排名 |
| SciFact检索排序 | scientific claim | 论文语料和检索索引 | top-k相关论文 |
| HellaSwag-bench排序 | 含实验accuracy的摘要表 | 无独立外部证据库 | 按报告accuracy排序 |
| ArXiv主题分析 | 647篇论文文本/摘要 | 无独立外部证据库 | 5个发现的主题及文档归属 |

“数据环境”在这里表示查询所需辅助语料、标签和索引，不是 GPU。Figure 1 是示例程序：检索相关摘要，过滤声称优于指定baseline的论文，再做摘要。它不是论文中某条已编号 benchmark question。

HellaSwag-bench 的200份摘要由Llama生成并注入随机accuracy值（§5.3脚注7），是论文作者构建的合成任务，不能标成真实论文摘要。

来源：[Semantic Operators and Their Optimization: Enabling LLM-Based Data Processing with Accuracy Guarantees in LOTUS](https://www.vldb.org/pvldb/vol18/p4171-patel.pdf)。
