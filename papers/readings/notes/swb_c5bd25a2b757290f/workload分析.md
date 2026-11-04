# 工作负载

**构建漏斗**（Data Records，p.7）：

| 步骤 | 数量 |
|---|---|
| 2017 年 7 月 PubMed 检索（Box 1 中基于 MeSH 的查询） | 86,520 篇摘要，657,538 句 |
| 过滤格式错误句及不同时含药物与遗传因素的句子 | 176,704 句 |
| 随机抽取人工标注 | 1,897 句（来自 1,813 篇摘要） |
| 标注者丢弃（非 PGx、残缺、歧义等） | 952 句 |
| 最终语料 | 945 句，来自 911 篇摘要（发表于 1952–2017 年） |

**标注人力**（pp.5–7）：共 11 名标注者（药师 3 名、生物学者 3 名、生物信息学者 5 名），其中 5 名为资深标注者。第一阶段约 4 个月，人均 344.73 句；第二阶段约 4 个月，每位资深者复核 258.6 句。标注均为志愿完成。

**实体统计**（Table 2）：共 6,761 个，其中简单实体 4,414 个、嵌套 1,938 个、不连续 265 个、既嵌套又不连续 144 个。主要类型为 Chemical 1,718、Gene_or_protein 1,708、Limited_variation 919、Phenotype 699、Disease 635、Pharmacodynamic_phenotype 632。

**关系统计**（Table 3）：influences 937、isAssociatedWith 733、isEquivalentTo 293、decreases 263、increases 243、treats 238、causes 168。metabolizes 和 transports 在同质化阶段被并入 influences。

**数字差异**：Table 3 合计为 2,875，正文 Statistics 段与 p.2 的比较段均写 2,871 个关系，原文未解释这一差额（阅读者分析）。

**划分**：基线采用 10 折交叉验证（pp.10–11），没有固定的训练/测试划分。覆盖面方面，语料包含 PharmGKB 所列"非常重要药物基因"（VIP genes）的 81.8%（p.4）。

依据：Data Records、Statistics、Tables 2–3、6–7，PDF pp.3–4、7、10–11。
