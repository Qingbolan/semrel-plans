# 评测与边界

基线：Poirot（InsightBench）、Pandas AI、InfiAgent、MetaGPT、直接 GPT-4o，以及 AgentAda 无技能版（W/O Skill）；附录 E 另比 ECA、EvoR。所有调用为 GPT-4o 与 text-embedding-3-small（§6，p.6）。

指标：六项 rubric（分析深度、目标相关性、persona 一致性、连贯性、充分回答问题、图表结论质量）的成对胜/负/平/均不好比例；QA 精确匹配准确率与 1–5 分 rubric；FactScore 与 LLM 打分的事实性；技能匹配 MRR。

主要结果（原文）：
- 人评（Table 2，p.7）：Depth 48.78 vs 27.67；Relevance to Goal 平局 49.22%，Persona 平局 61.44%。Fleiss κ 0.7658–0.8842（Table 8，p.17）。
- SCORER 在 700 数据集上（Table 4，p.8）：对 Pandas 的 Depth 胜率 63.88%，对无技能版 49.12%。
- QA 正确性（Table 5，p.9），精确匹配准确率（%）见下表；SCORER 的 1–5 分 rubric 上 AgentAda 也最高（如 Depth 4.46，无技能 4.10）。

| AgentAda | 无技能 | Poirot | Pandas AI | InfiAgent | MetaGPT | GPT-4o |
|---|---|---|---|---|---|---|
| 90.6 | 82.6 | 81.2 | 80.4 | 84.2 | 85.5 | 78.8 |

- FactScore（GPT-5 校验，Table 11，p.35）：87.9 vs 无技能 76.1。
- 技能匹配：MRR 0.83，准确率 0.9（§6.5，p.10）。
- 外部基准（Table 14，p.35）：InfiAgent-DABench 准确率 76.5（GPT-4o 版）vs InfiAgent 62.0。

局限与阅读者分析：
- 论文没有独立的局限性章节；§7 只把多表、非结构化与大规模数据列为未来工作。
- 主要比较依赖 SCORER（GPT-4o 评审，提示用本系统的人评数据优化），其“验证损失 0.4”的含义（MSE 量纲）未与其他评审器的数值对照；Table 13 中人评胜率 44.5 与 Table 2 的 48.78 不一致，可能来自不同子集，原文未说明。
- 未报告成本、延迟、方差或显著性检验；基线配置细节有限。§1 提到的“60.01%”在结果表中未找到对应数字（阅读者分析）。

依据：[arXiv:2504.07421v3，41 页](https://arxiv.org/abs/2504.07421)。
