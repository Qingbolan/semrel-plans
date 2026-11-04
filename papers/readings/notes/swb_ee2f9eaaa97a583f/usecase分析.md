# 具体用例

附录 D 的例子（PDF p.13）：规则为 EU AI Act 第二章第 5 条第 1 款 (h)——禁止为执法目的在公共场所使用"实时"远程生物识别系统。代理检索到的案例为"EU-Funded ROBORDER Project Restrictions"：2017–2020 年欧盟 Horizon 2020 资助的项目开发了用于边境监控的远程生物识别（面部、步态识别），但伦理准则把使用限制在例外情形，避免在内部公共场所用于执法；relation_to_rule 标为 COMPLIES，适用法规还列出了欧盟基本权利宪章。

评测时模型读到案例背景，回答 PERMITTED 或 PROHIBITED；该例的正确答案对应 COMPLIES→PERMITTED（阅读者分析：论文未写出 COMPLIES/VIOLATES 到 permitted/prohibited 的映射规则，此处按字面推断）。

Figure 1 的另一例：GitHub 隐私声明中"未经同意不访问私有仓库"一条，代理生成"GitHub private repository unauthorized access incidents…"等查询，找到 2016 年 GitHub 数据库连接 bug 导致私有仓库信息外泄的事件报告，标为 VIOLATES。

依据：Figure 1、附录 D，PDF pp.4、13。
