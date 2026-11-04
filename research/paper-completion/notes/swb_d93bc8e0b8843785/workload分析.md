# 工作负载

| 来源 | 原始规模 | 标注抽样 | 倾听者句子数 |
|---|---|---|---|
| CounselChat（专业咨询师） | 2,129 个帖子—回复对，31 个主题 | 随机 1,000 对 | 9,893 |
| RED（Reddit 同伴，8 个心理健康 subreddit） | 约 1.2M 段二人对话，平均 2.66 轮 | 随机 1,000 段 | 7,368 |
| 合计 | — | 2,000 段 | 17,261 |

来源：§3.2，PDF pp.3–4；Table 2，PDF p.6。RED 用 Pushshift API 抓取，经清洗（含去除倾听者回复中的脏话）；8 个 subreddit 为 mentalhealthsupport、offmychest、sad、suicidewatch、anxietyhelp、depression、depressed、depression_help（§3.2，PDF pp.3–4）。

**标注成本与组织**：12 名 UpWork 受训从业者；每批 10 段对话（5 CC + 5 RED 交替），每批两名标注者；共 200 批、400 份分配（§3.3，PDF p.4；附录 A.3，PDF p.11）。第一阶段每批 $10、约 30 分钟，一致性高于平均另付 $5 奖金；第二、三阶段每批 5（原文未写货币符号）、约 15 分钟（§7，PDF p.9）。

**标签分布要点**（Table 4，PDF p.7）：CC 中 Give Information 3,643、RED 中 1,213；RED 中 Self-Disclose 1,216、CC 中 174；Support 在 RED 为 815、CC 为 418。

阅读者分析：数据单位是句子级单标签分类，无官方训练/验证/测试划分，原文未报告任何模型基线。
