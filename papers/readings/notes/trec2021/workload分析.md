# 工作负载

各 track 的数量与单位必须分开：

| Track | 原文描述的输入规模与评测对象 |
|---|---|
| Clinical Trials | 2021 年 4 月 registry 快照约 375,000 个试验；75 个由临床人员编写的模拟病例，每个 5–10 句，不是真实患者记录 |
| CAsT | 25 个对话 topic，平均 9 轮；实际完成 19 个 topic 的标注，多数到第 8 问，不能将全部轮次视为已判断 |
| Deep Learning | MS MARCO v2 约 1,100 万文档、1.4 亿段落；477 个测试问题，密集判断文档任务 57 个、段落任务 53 个 |
| Fair Ranking | 英语 Wikipedia、WikiProject topic；协调者输出单排名，编辑者输出排名序列，评价曝光公平性 |
| Health Misinformation | C4 noclean；50 个 topic，35 个完成判断 |
| Incident Streams | 26 个灾害事件，按时间顺序在线逐 tweet 标注，不得看完后续流再回填 |
| News | Washington Post 集合，51 个 topic；背景链接最多返回 100 篇，另有 anchor–link 任务 |
| Podcast | 超过 100,000 个英语节目单集；50 个检索 topic（40 topical、10 known-item）；摘要任务提供 1,000 单集 |

这些是不同输入/评测集合，不能直接相加成同一种“查询总数”。

依据：[NIST TREC 2021 proceedings overview，Ian Soboroff，17 页](https://trec.nist.gov/pubs/trec30/papers/Overview-2021.pdf)，§3.1–3.8，PDF pp.5–16。
