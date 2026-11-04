# 具体用例

**律师检索相似难民案件**：律师准备新申请时，通常按以下要素寻找相似先例：审理组成员、来源国及申请人特征、申请年份对应的地缘政治背景、法律程序、裁决理由、引用的法律、案例和国别报告（§3.1 “Choice of Categories”，p.4）。AsyLex 的实体类型正是据此设计，例如 CLAIMANT_INFO（年龄、性别、国籍、职业，如“citizen of Iran”）、LEGAL_GROUND（公约理由）、LAW_REPORT（如 Amnesty International 的国别报告）（附录 B，p.13）。

Table 2 给出两份文书封面的结构化结果：案件 #123259 的听证地点为 toronto/on，法庭为 refugee appeal division；案件 #100049 记录了视频会议听证和法官姓名（p.4）。附录 A 展示了 #123259 原始封面及标注（p.12）。

在此基础上，研究者可以按 CLAIMANT_INFO 高频短语（如 male、female appellant、roma、citizen of china，Table 5，p.5）做分组，再比较不同群体的结果分布，用于分析潜在偏差（§3.2，p.6）。

阅读者分析：论文没有实现或评测“相似案件检索”本身，只提供可用于检索的实体；检索效果需另行验证。

依据：§3.1–3.2、Tables 2、5，PDF pp.4–6；附录 A–B，pp.12–13。
