# Zhou et al. — RuleArena: A Benchmark for Rule-Guided Reasoning with LLMs in Real-World Scenarios

本文提出 RuleArena：用航空行李费、NBA 交易、美国个人所得税三个领域的 95 条真实规则和 816 道题，测试 LLM 是否能按长篇自然语言规则推理并计算。主要结果是最终答案准确率很低：0-shot 下 o1-preview 在航空 Level 1 只有 0.54，其余非推理模型在难题上很少超过 10%；不过规则选择精确率在航空和税务上都是 1.000。已阅读正文、Limitations、附录 B 的数据构造和附录 D.2 的因素分析；未逐条审阅附录 C 的结构化解析模板与附录 E 的提示词。

[原文](https://aclanthology.org/2025.acl-long.27)

版本：ACL 2025 Long Papers（Vol.1）pp.550–572，ACL Anthology 2025.acl-long.27，23 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | §1、§3.1，PDF pp.1–3 |
| 方法 | §3.2–3.4、§4.1、附录 B，PDF pp.4–5、14–15 |
| 评测 | §4.2–4.3、Tables 3–7、附录 D.2，PDF pp.5–9、19–22 |
| 局限 | Limitations，PDF p.10 |
