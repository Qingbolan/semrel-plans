# Yang, Lan, Jia et al. — HSCodeComp: A Realistic and Expert-level Benchmark for Deep Search Agents in Hierarchical Rule Application

HSCodeComp 用大型电商平台上的 632 条真实商品记录（标题、属性、类目、图片、价格等，描述有噪声）构造任务：要求智能体结合层级关税规则、人工决策规则和海关裁定库，预测完整的 10 位 HS 编码，以测试“分层规则应用”能力。最佳系统 SmolAgents（GPT-5，带图片）的 10 位准确率为 46.83%，远低于原文给出的人类专家 95.0%；加入人工决策规则、访问网页、多数投票和自我反思都没有带来稳定提升。已读正文全部和附录 B–F；附录 G–I 的案例只抽看两页。

[原文](https://arxiv.org/abs/2510.19631)

版本：arXiv:2510.19631v1（2025-10-22 提交，PDF 标注 2025-10-23），38 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| problem | §1、§3，PDF pp.1–5 |
| method | §4.1–4.2、附录 B、F，PDF pp.5–6、16、19 |
| evaluation | §5–6、Tables 1–6、Figures 4–6，PDF pp.6–11；附录 D–E，PDF p.17 |
| limitations | §2.1、§6.3–6.5、§9、附录 F，PDF pp.3、9–11、19；附录 G 失败案例抽看 pp.25–26 |
