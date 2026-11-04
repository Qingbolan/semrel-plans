# Shen et al. — A Law Reasoning Benchmark for LLM with Tree-Organized Structures including Factum Probandum, Evidence and Experiences

本文提出“透明法律推理”任务 TL：输入案件描述，输出以待证事实（中间/最终）、证据、经验法则及推理边构成的树状结构。作者从中国裁判文书网收集 453 个案件做众包标注（训练 253、验证 100、测试 100），并提出基于 GPT-4o-mini、带法律知识检索和多角色检查的 TL Agent；在测试集综合分 Sc 上，TL Agent 为 31.50，GPT-4o 为 25.74，Qwen-max 为 30.94。已阅读正文 §1–6、局限及附录 A–D、F–G，渲染核对了 Table 2 与 Tables 4–5。

[原文](https://aclanthology.org/2025.findings-acl.887)

版本：Findings of the Association for Computational Linguistics: ACL 2025, pp.17252–17274，ACL Anthology 2025.findings-acl.887 PDF，23 页（PDF 页码 = 论文集页码 − 17251）。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题（problem） | 摘要、§1、§2，PDF pp.1–4 |
| 方法（method） | §3 数据构造、§4 TL Agent，附录 B（质量控制）、E（工具提示），PDF pp.4–6、13–17 |
| 评测（evaluation） | §5、Table 2（已渲染），附录 A（指标）、F（Table 4）、G（Table 5，已渲染），PDF pp.7–8、12、16–18 |
| 局限（limitations） | Limitations 节、附录 D、H，PDF pp.9、14、17 |
