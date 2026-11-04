# Yuvraj & Devarakonda — ATLAS: Benchmarking and Adapting LLMs for Global Trade via Harmonized Tariff Code Classification

本文把美国海关 CROSS 裁定转换成“产品描述 → 10 位 HTS 美国税则号”的分类基准（18,731 条裁定，测试集 200 条），并用 SFT 微调 LLaMA-3.3-70B 得到 ATLAS。ATLAS 在测试集上 10 位全对 40%、6 位全对 57.5%，高于 GPT-5-Thinking 的 25% 与 55.5%；成本按假设定价估算约为 GPT-5-Thinking 的 1/5。已读完正文全部章节（正文 8 页，其余为参考文献），没有附录。

[原文](https://arxiv.org/abs/2509.18400)

版本：arXiv 2509.18400v1（2025-09-22），12 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | §1，PDF pp.1–2 |
| 方法 | §2–§3，PDF pp.2–5 |
| 评测 | §4、Tables 2–5，PDF pp.5–7 |
| 局限 | §3.3、§5，PDF pp.5、7–8（无单独局限章节） |
