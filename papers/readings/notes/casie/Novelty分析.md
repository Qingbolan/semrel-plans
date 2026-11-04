# 贡献与评价

除领域事件模式和标注语料外，方法将词表示、句法与外部实体类型特征输入 BiLSTM-CRF，分别识别触发片段和论元；论元检测使用注意力，角色分类按事件类型约束候选，现实性分两次二分类。DBpedia/Wikidata 在此提供输入特征，不意味着输出已形成经过实体消歧的知识图谱。

依据：[AAAI 2020, pp.8749–8757](https://ebiquity.umbc.edu/get/a/publication/1312.pdf)，CASIE’s Design and Architecture，PDF pp.2–5。
