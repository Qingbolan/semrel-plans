# ScienceAgentBench: Toward Rigorous Assessment of Language Agents for Data-Driven Scientific Discovery

在宣称智能体能端到端自动化科研之前，应先严格评估它能否完成科研流程中的单个数据任务。本文从 4 个学科的 44 篇同行评议论文中提取 102 个任务，由 9 位领域专家验证；每个任务要求智能体根据指令、数据集信息和可选的专家知识，生成一个可独立运行的 Python 程序，并用可执行率、成功率、CodeBERTScore 和 API 费用评测。

5 个 LLM × 3 种框架中，最好的 Claude-3.5-Sonnet + self-debug 在 3 次尝试下只解出 32.4% 的任务，加专家知识后 34.3%；单独列出的 OpenAI o1 + self-debug 达 42.2%（Table 3）。

[原文](https://arxiv.org/abs/2410.05080v2)

版本：arXiv 2410.05080v2（2024-10-24，俄亥俄州立大学等；PDF 标为 "Under review"，正式发表于 ICLR 2025，以官方仓库信息为准）。已通读 §1–5、Figures 1–4、Tables 1–3，数字已对照全文核对，未复现实验。官方仓库后来发布了 2026 verified 数据，其结果不能与本版本数字混用。
