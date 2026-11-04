# 具体用例

**论文示例**（Figure 1.1 与 Table 1.1，印刷 pp.3–4）：一段新闻写道，一个可能波及 100 万 Gmail 用户的钓鱼活动用伪装成 Google Docs 的应用诱骗收件人点击 "Open in Docs"，再把他们带到真实的 Google 账户页面，要求授权该应用访问 Gmail。

CASIE 的目标输出为 Attack.Phishing 事件框架：

| 角色 | 填充 |
|---|---|
| Attacker | 无 |
| Attack-Pattern | click a blue box that said "Open in Docs." |
| Number of Victims | 1 million |
| Purpose | handover Gmail access |
| Tool | a email；dummy app；Google account page |
| Trusted-Entity | Google Docs |
| Victim | Gmail users；Recipients |

随后 Purpose 可按词相似度归入"未授权访问"等子类型，组织实体链接到 Wikidata（如 Adobe→Q11463），输出 JSON 与 RDF（第 12 章，印刷 pp.134–136；附录 A.1）。

阅读者分析：对语义查询而言，这类框架把新闻变成"事件 × 角色 × 论元"的表格，可支持"列出 2018 年所有针对医疗机构的数据泄露及泄露数据类型"一类查询；但论元必须在触发词前后一句内才被标注，跨句信息（如 GPE、时间）会系统性缺失，作者在 §14.2 也承认这一点。

依据：§1.1、第 12 章、§14.2，印刷 pp.3–4、134–136、149–150。
