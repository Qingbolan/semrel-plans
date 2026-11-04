# Liu et al. — InsLogicBench: An Argumentation Logic Grounded Benchmark for Complex Insurance Claims Adjudication

本文提出一个中文保险理赔裁决基准：给定理赔描述与整份保单，模型要找出相关条款、逐条解释命题并给出“赔付/拒赔”结论。数据由嵌套 Toulmin 模型驱动的可控合成流程生成，共 2,621 个问答对，来自 110 份公开保单。8 个 LLM 中 DeepSeek-R1 的裁决准确率最高（0.82），但例外条款与“缺失条件”场景明显更难。已阅读正文、Limitations 和附录 C；附录 B 的全部提示词与附录 E 的五个案例只做了浏览。

[原文](https://aclanthology.org/2026.acl-long.1035)

版本：ACL 2026 长文（pp.22592–22619），28 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | Abstract、§1、§3.1，PDF pp.1–3 |
| 方法 | §3.2–3.3、Table 1、Algorithm 1，PDF pp.3–5 |
| 评测 | §4–5、Tables 2–6、Figures 6–8，PDF pp.5–8；附录 C Table 7，PDF p.21 |
| 局限 | Limitations、Ethics Statement，PDF p.9 |
