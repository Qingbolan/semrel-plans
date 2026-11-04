# 工作负载

本文没有发布数据集、查询集或训练/测试划分。可视为“工作负载”的是标注方案本身：

| 项 | 内容 |
|---|---|
| 核心关系 | 20 个：Cause、Condition、Negative Condition、Purpose、Manner、Concession、Contrast、Exception、Similarity、Substitution、Conjunction、Disjunction、Exemplification、Elaboration、Restatement、Synchrony、Asynchrony、Expansion、Functional dependence、Feedback dependence |
| 对称性 | Table 1 中 6 个对称（Contrast、Similarity、Conjunction、Disjunction、Restatement、Synchrony），其余 14 个不对称（阅读者按表计数） |
| 论元类型 | 情境（含事件、状态、事实、条件、否定情境）与对话行为 |
| XML 元素 | `dRel`、`drArg`、`explDRLink`、`implDRLink` |
| 映射对象 | 七种分类：RST、RST Treebank、SDRT、DISCOR、ANNODIS、PDTB、Sanders 等/DiscAn |

正文脚注 3 提到 ISO DR-Core 已用于 DialogBank 中对话的篇章关系标注，但本文没有给出该语料的规模或统计。

依据：[Bunt 主页 PDF，10 页](https://let.uvt.nl/general/people/bunt/docs/ISA-12-DR-core-revised.pdf)，§3、Tables 1–5、§4.3，PDF pp.4–8。
