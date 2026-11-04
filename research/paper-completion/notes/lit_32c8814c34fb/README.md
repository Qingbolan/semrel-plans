# Deng, Zhang, Fan, Du — DataEvolver: Automatic Data Preparation for Large Language Models through Multi-Level Self-Evolving

DataEvolver 是一个面向 LLM 训练数据的自动数据准备系统：输入原始数据与约 20 条高质量 seed 样例（可选任务描述），自动生成逻辑算子 DAG、实例化为代码并在样本上试运行，用“算子级 + 流水线级”两层自进化修正流水线，最后在全量数据上执行。论文在 7 个基准、3 个骨干模型上以 SFT 后的下游分数评测，报告相对原始数据平均约 +10 分、相对 DataFlow 约 +2 分，单条训练样本的准备 token 成本宏平均降低约 40%。已阅读正文、局限性与附录 B–G（数据、seed、配置、流水线统计、鲁棒性、人工核验）；未审阅附录 H 的全部提示词。

[原文](https://arxiv.org/abs/2606.07001)

版本：arXiv 2606.07001v3（2026-10-13，cs.DB），29 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| problem | §1、§3.1，PDF pp.1–3 |
| method | §3.2–3.4、Fig.2，PDF pp.3–4；附录 D.1、E，pp.16–18 |
| evaluation | §4–5、Tables 1–5、Figs.3–4，PDF pp.4–8；附录 B、C、F、G，Tables 6–19，pp.12–24 |
| limitations | Limitations 节，PDF p.9；附录 G.3 |
