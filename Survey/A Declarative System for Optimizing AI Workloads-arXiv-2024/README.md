# A Declarative System for Optimizing AI Workloads

用 LLM 处理大批非结构化数据时，程序员要为每一步自己选模型、prompt 和执行方式，成本与质量难以兼顾。本文提出 Palimpzest：用户用 Dataset、Schema 与 convert/filter 等算子声明式地写 AI 分析程序，系统枚举逻辑与物理计划，用 sentinel 采样估计代价、时间与质量，再按用户 policy 选计划执行。

在法律取证、房源搜索、医学 schema 匹配三个工作负载上，单线程候选计划中有一个比全 GPT-4 基线快 3.3 倍、便宜 2.9 倍且 F1 更高；加上 32 路并行后，法律取证快 90.3 倍、便宜 9.1 倍，F1 为基线的 83.5%。

[原文](https://arxiv.org/abs/2405.14696v2)

版本：arXiv 2405.14696v2（2024-05-29，MIT 等，技术报告）；已通读正文 §1–7（pp.1–20）及附录程序与物理计划（pp.27–29），数字已对照全文核对，未复现实验。不含 CIDR 2025 修订版与后续 Abacus 的实验。
