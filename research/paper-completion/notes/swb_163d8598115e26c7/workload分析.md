# 工作负载

**数据集**：训练只用 Abt-Buy（AB）。零样本评测 7 个基准：Amazon-Google（AG）、DBLP-ACM（DA）、DBLP-Scholar（DS）、IMDb-TMDb（IM）、IMDb-TVDb（IT）、TMDb-TVDb（TT）、Walmart-Amazon（WA），覆盖电商、学术引文与电影。正文 §4 还提到“餐厅”领域，但列出的数据集中没有餐厅数据集。

**评测单位**：沿用 COMEM 协议，用 Sparkly 对每个锚检索 top-10 候选，blocking recall@10 为 94.89%–99.96%。每个数据集的评测集为 400 个锚：300 个有一个真匹配，其余 100 个没有真匹配。阅读者计算：7 个数据集合计 2,800 个锚。

**监督基线数据**：DITTO 在每个目标数据集额外采样 5,000 个标注对训练。

**后端模型**：Flan-T5-xl（3B，用于 MATCH/COMPARE）、Llama-3.1-8B、GPT-oss-20B、ERNIE 4.5 21B、Gemma 3 27B、Qwen3 30B、GPT-4o mini；Table 1 给出各模型每百万 token 价格。GPU 成本按 4 家云厂商 H100 按需价平均定为每小时 5.98 美元。

**训练量（附录 F，AB）**：MATCH 335,592 token、COMPARE 1,694,532 token、SELECT 2,122,750 token，PPO 训练 2.75 H100 小时。

依据：[ACL 2026 long 1258，13 页](https://aclanthology.org/2026.acl-long.1258.pdf)，§4，PDF pp.4–6；Table 1，PDF p.5；附录 E–F Tables 8、10，PDF pp.12–13。
