# 贡献与评价

**作者声明的贡献**（§1，PDF pp.2–3）：

1. NL2SQL360：可按 SQL 特征、领域等定制子集的多角度评测平台。
2. 新实验发现：在 Spider/BIRD 上以 15 种设置测试 13 个 LLM 方法与 7 个 PLM 方法。要点包括：微调至关重要（微调 LLM 在 EX 领先，PLM 在 EM 领先）；GPT-4 方法在子查询上更好；微调模型对问法变化更稳定；跨领域无明确赢家，领域内训练数据关键；代码预训练的 LLM 微调后更好。
3. SuperSQL：遗传算法搜索出的组合方案。
4. 三个研究方向：可信 NL2SQL、低成本方案、自适应训练数据生成（§6，PDF p.12）。

**SuperSQL 组成**（§5.3，PDF p.12）：RESDSQL 的 schema linking + BRIDGE v2 的 DB content；DAILSQL 的相似度 few-shot；OpenAI 贪心解码，不用多步与 NatSQL；DAILSQL 的 self-consistency。搜索阶段用 GPT-3.5，最终换为 GPT-4。

**评价**：

- 原文事实：主要价值在系统比较与分场景结论；QVT 是新指标，其余为已有指标。
- AAS 以 Spider 开发集 EX 为搜索目标，SuperSQL 又在同一开发集上报告 87.0% 并称超过其他方法，存在在评测集上选型的偏差；测试集结果（Spider 87.0%、BIRD 62.66%）更能说明问题（阅读者分析）。
- BIRD 开发集上 SuperSQL 与 SFT CodeS-15B 同为 58.5% EX（Table 4），并未领先；正文称其"具有竞争力"，表述与表格一致（阅读者分析）。
