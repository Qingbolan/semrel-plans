# 工作负载

**数据来源**（§4.1，p.3）：BIRD 中的 5 个数据库：california_schools、debit_card_specializing、formula_1、codebase_community、european_football_2。

**问题构造**：从 BIRD 中选取 match-based、comparison、ranking、aggregation 四类问题，改写为需要世界知识（参数化知识）或 LM 推理才能回答的版本。共 80 题：知识类 40、推理类 40；四种类型各 20 题。真值由人工标注（§4.1）。

**改写示例**（附录 A，p.8）：

| 类型 | 原 BIRD 问题 | 修改后 | 需要 |
|---|---|---|---|
| Match | 经度最高的学校提供的年级范围 | 限定在“硅谷”地区城市中的学校 | 知识：哪些城市属于硅谷 |
| Comparison | 身高超过 180 的球员中凌空球得分超过 70 的人数 | 再加“比 Stephen Curry 高” | 知识：Curry 的身高 |
| Ranking | 热度最高的 5 个帖子的标题 | 按“技术性”从高到低排列这 5 个标题 | 推理：判断标题的技术程度 |
| Aggregation | 列出某帖子下的所有评论 | 总结这些评论以回答原帖问题 | 推理：总结评论文本 |

§4.1 正文举的知识类例子是“只要 Bay Area 的学校”，附录 A 的对应例子是“Silicon Valley”。

**每题的输入**：对应数据库的表与所需列，以 SQLite 数据库或等价的 DataFrame 提供，外加 schema；不需要额外的网页环境。RAG 基线每次检索 10 行，这是候选数，不是数据规模或批大小。

**指标**：match、comparison、ranking 用与标注答案的精确匹配；aggregation 只做定性分析；另报告每题执行时间（秒）（§4.1）。

阅读者分析：80 题规模较小，且改写由作者完成，不代表真实用户问题的分布；论文没有给出统一的记录批大小（阅读者分析）。

依据：§4.1–4.2、附录 A，PDF pp.3–4、8。
