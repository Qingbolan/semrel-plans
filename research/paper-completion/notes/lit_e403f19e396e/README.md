# Fan, Fan, Zhang, Zhang, Du, Song, Li, Jiang, Zhang, Chen — DeepPrep: An LLM-Powered Agentic System for Autonomous Data Preparation

DeepPrep 研究自主数据准备（ADP）：给定多张源表和目标 schema 的自然语言描述，生成由 31 种算子组成、可执行的流水线，产出目标表。方法上，智能体在保存中间表状态的“推理树”上执行 plan/expand/execute/answer 动作，可以回溯到更早的状态。

训练上，采用冷启动课程（算子语法 + 教师轨迹蒸馏）加多轮 GRPO 强化学习与混合奖励，并把 Spider/BIRD 的 NL2SQL 样本合成为带可逆噪声的 ADP 任务。Qwen3-14B 版在 Synth-Spider 上精确匹配准确率 67.18，与 GPT-5（gpt-5-mini）上 ReAct 的 67.03 相当，作者称成本约低 15 倍。已阅读全文正文（13 页）；论文无独立局限性章节，提示词与超参放在外部技术报告 [1]，未阅读。

[原文](https://arxiv.org/abs/2602.07371)

版本：arXiv 2602.07371v1（2026-02-07，cs.DB），PVLDB 格式稿（卷期页码为占位），13 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| problem | §1、§2.1，PDF pp.1–3 |
| method | §2.2–§5、Figs.3–4，PDF pp.3–8 |
| evaluation | §6、Tables 1–3、Figs.5–8，PDF pp.9–12 |
| limitations | 无独立章节；§6 实验设置与 §7 相关工作，pp.9–12（阅读者推断） |
