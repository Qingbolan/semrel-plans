# Nie, Xia, Liu, Jermaine & Chaudhuri — Cost-Aware Optimization for Agentic Query Execution

本文把"在 SQL 中混入 LLM 语义算子"的查询处理重新表述为"智能体式查询执行"：规划与执行交替进行，智能体每步观察中间关系后再决定下一个 SQL 或 LLM 算子。相应地，查询优化变为同时权衡答案质量与成本的"智能体工作流优化"。作者提出 EnumGRPO：在学习阶段按五个规划轴枚举候选工作流并执行，用组内相对优势和四阶段 LLM 蒸馏把质量—成本反馈写成自然语言经验池（不更新模型权重）。在 SWAN 80 条评测查询上取得 35.4% 执行准确率，LLM 算子成本为每查询 0.011 美元，比 Agentic BlendSQL 低 317 倍，比 Palimpzest 低 55 倍；经验池还能迁移到 GPT-5.6 主干、SemBench Movie 以及 Spider/BIRD。已阅读全文正文 §1–7（14 页，含参考文献）。

[原文](https://arxiv.org/abs/2606.03152)

版本：arXiv:2606.03152v2（2026-10-07，PVLDB 格式预印本），14 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| problem | §1–2、Figure 1，PDF pp.1–3 |
| method | §3.1–3.4、Table 1、Figure 2、Algorithm 1，PDF pp.3–8 |
| evaluation | §4–5、Tables 2–5、Figures 3–4，PDF pp.8–12 |
| limitations | §5.4 失败分析、§5.5 规模权衡、§5.7 学习成本、§7 未来方向，PDF pp.10–12（原文无独立 Limitations 节） |
