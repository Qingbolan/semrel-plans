# SEED: Domain-Specific Data Curation With Large Language Models

实体匹配、属性补全、信息抽取等数据整理任务需要领域定制方案，手写代码或标注训练数据代价高，而逐条调用 LLM 又贵。

SEED（Chen、Cao、Madden、Kraska 等，MIT 等）把 LLM 当作“编译器”：用户用自然语言描述任务、输入输出和少量示例，SEED 生成混合执行流水线，由 LLM 生成的代码（CodeGen）、相似查询缓存（CacheReuse）、用 LLM 伪标签训练的小模型（ModelGen）和直接 LLM 调用（可带工具）组成，优化器在给定效果容忍度下选择调用 LLM 最少的组合。

在 5 类任务、9 个数据集上，SEED 的效果接近或达到 few-shot 最佳水平，实体匹配中只有 2.9–10.4% 的记录交给 LLM（§6，Tables 3–8）。

[原文](https://arxiv.org/abs/2310.00749v3)

版本：arXiv 2310.00749v3（2024-04-24，cs.DB），20 页；首个预印本为 2023 年，目录按本版本归档为 2024。已通读 §1–6 与附录 A、B.1、C，数字已对照全文复核（2026-11）；未复现实验。
