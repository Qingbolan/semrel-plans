# Zhang et al. — Jellyfish: Instruction-Tuning Local Large Language Models for Data Preprocessing

本文把错误检测（ED）、数据填补（DI）、模式匹配（SM）、实体匹配（EM）四类数据预处理任务序列化为指令数据，并加入知识注入和 Mixtral 蒸馏的推理数据，对 Mistral-7B、Llama 3-8B、OpenOrca-Platypus2-13B 做指令微调，得到可在单张本地 GPU 运行的 Jellyfish-7B/8B/13B。

Jellyfish-13B 在 19 个已见任务数据集上的平均分为 86.02，高于 GPT-4 的 84.17 和非 LLM 最佳值 80.44；在未见任务列类型标注（CTA）和属性值抽取（AVE）上也有竞争力。已阅读正文 §1–7、Limitations 及附录 C.3–C.4；未逐条审读附录 D–F 的全部提示与知识文本。

[原文](https://aclanthology.org/2024.emnlp-main.497/)

版本：EMNLP 2024 主会，ACL Anthology 2024.emnlp-main.497，正文 pp.8754–8782，PDF 29 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | §1–2，PDF pp.1–3 |
| 方法 | §3–4、Figures 1–2、Tables 1–2，PDF pp.2–5 |
| 评测 | §5、Tables 3–7、Figures 3–4、附录 C.4 Table 13，PDF pp.5–9、18 |
| 局限 | Limitations，PDF p.10 |
