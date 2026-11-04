# Dou, Zhu et al. — FinGuard: Detecting Financial Regulatory Non-Compliance in LLM Interactions

本文从 3,120 份中国金融监管文件出发，用 LLM 抽取合规要点、聚类并经专家审定，得到 11 个大类、35 个子类的金融合规风险分类体系；据此合成违规/合规查询与多模型回复，构建训练集 FinGuard-Train 和专家标注的 FinGuard-Bench（1,020 个查询–回复对）。基于 Qwen3-8B 经 SFT 与自博弈 RL 训练的 FinGuard 在基准上查询级/回复级 unsafe 类 F1 为 90.23/85.43，高于 Qwen3.5-397B-A17B（78.68/64.08）和 GPT-5.1。已通读正文、局限、伦理声明与附录 A–I。

[原文](https://arxiv.org/abs/2605.29427)

版本：arXiv:2605.29427v1（2026-05-28），19 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | §1、§3.1，PDF pp.1–2 |
| 方法 | §3.2–3.4、Algorithm 1，PDF pp.3–6；附录 A–H，pp.11–13 |
| 评测 | §4–5、Tables 5–8、Figure 2，PDF pp.6–8；附录 I（Table 11），p.14 |
| 局限 | Limitations、Ethics Statement，PDF p.9 |
