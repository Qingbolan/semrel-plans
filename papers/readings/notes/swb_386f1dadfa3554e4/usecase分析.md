# 具体用例

**NCBI Disease 上的第一轮审核**（§5.4、Figures 2–3、6–7，PDF pp.4、8–9、13）：GPT 用原指南标注 10 篇开发文档，最频繁的差异组是（金标 DiseaseClass，预测无实体），共 7 例。

1. 模式解释：作为 "with/of" 补语或并列"症状列表"出现的病症被当作症状漏标；真阳性则集中在 "X is an autosomal recessive disorder" 这类有疾病中心词的句式。
2. 原则生成：IF 临床病症名词短语出现在依附的特征列表中，THEN 每个并列项标为 DiseaseClass；EXCEPT 修饰非疾病中心词或是笼统过程词。
3. 指南修订：在原指南第 3 节（Modifiers）与第 4 节（Duplicate mentions）之间插入新规则 #4。

结果：该差异组从 7 降到 1，另有 5 例 Modifier→SpecificDisease 误标被顺带纠正。"microcephaly, mental retardation, and short stature" 三项被找回；但 Wilson 病句子中的 "copper accumulation" 成为新的 FP。整个循环 4 轮后停止。

阅读者分析：这一用例说明修订规则是可读、可审计的文本，但也说明单条规则会产生精度-召回的再平衡。
