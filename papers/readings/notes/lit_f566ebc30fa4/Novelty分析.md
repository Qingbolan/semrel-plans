# 贡献与评价

论文声明的贡献（p.4）：

1. 把 Text-to-SQL 重构为 SDLC 式可验证流程；
2. 用不同推理策略的独立生成器替代同 prompt 高温采样的自一致性（N-version programming）；
3. 以确定性检查器（Syntax/Logic/Quality，含 JOIN、ORDER-BY、时间函数、SELECT *、NULL、空结果检查）取代 LLM 自我反思，提供明确修复指令；
4. 在 BIRD/Spider/Spider 2.0 上取得 SOTA 级结果。

还提出“反向模式链接”（先生成 SQL 再解析其模式），Table 6 显示列召回 94.0% 比直接链接 80.9% 高 13.1 个百分点。

阅读者分析：
- 真正可检验的新意集中在反向/值链接组合、检查器链和“执行置信先验 × 成对胜率”的选择规则；每一项都能在消融里看到 0.8–2.5 个百分点的贡献（Table 10），没有单一决定性组件。
- 检查器是手写规则，覆盖的错误类型由 Table 2 固定，其泛化到其他方言（Spider 2.0 的 BigQuery/Snowflake）的方式论文未细说。
- 论文标题中“~3B 激活参数”只对 Qwen3-Coder-30B-A3B（MoE）成立；Gemma3-27B 与 Qwen2.5-Coder-32B 是稠密模型。

依据：[arXiv v3，PACMMOD Article 158，28 页](https://arxiv.org/abs/2510.17586)，§1、§3、Tables 6、10，pp.3–4、10–11、17、21。
