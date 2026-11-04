# 具体用例

**病例时间线**（§2，PDF p.2）：GDUC 病例中，症状在就诊前 2 周出现；结肠镜早于胃镜；治疗持续半个月；随后 26 个月无复发。作者说明症状、检查、观察、治疗、疾病都是病史中的相关事件，把它们按时间排序可以理解病情演变。

**两级标注互补**（§3–§4，PDF pp.2、4）：示例片段 “2020-09-01. The patient enters the ER due to abdominal pains. He reports chest pain 5 days ago.”

- 分类体系标注可以推出 abdominal pains 与 chest pain 在 SNOMED-CT 中同为 [pain of truncal structure] 的子概念，因此相关；
- THYME 标注可以推出两件事的先后。

Table 3（PDF p.6）把该片段逐 token 标为 IOB2：2020-09-01 为 B-TIMEX3，The patient 为 ACTOR，enters/pains/reports/pain 为 EVENT，chest 为 BPART，“5 days ago” 为 TIMEX3；分类列中 “abdominal pains” 和 “chest pain” 为 ENTITY。

作者计划的目标应用：自动构建临床时间线和临床病例问答（§5，p.6）。

阅读者分析：此例中 “chest pain” 在 THYME 层被拆成 BPART + EVENT，在分类层是一个实体——这正是 §4.4 所说的跨度不匹配，下游若做实体级连接需先定义映射。
