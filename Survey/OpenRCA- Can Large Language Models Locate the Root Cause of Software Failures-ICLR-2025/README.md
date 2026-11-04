# OpenRCA: Can Large Language Models Locate the Root Cause of Software Failures?

LLM 在软件工程中的研究多集中于写代码，较少关注上线后的故障根因分析（RCA）。本文提出 OpenRCA 基准：来自三个企业软件系统（AIOps 挑战赛数据）的 335 个故障案例，配有 68.5 GB、5.23 亿行的指标、日志与调用链；每个案例给一个自然语言查询，要求输出根因的组件、开始时间、原因中的指定子集。作者还提供 RCA-agent，让 LLM 写 Python 代码分析遥测，而不把原始数据塞进上下文。

结果显示任务很难：Claude 3.5 用平衡采样只解出 3.88%，用工程师预选的 oracle KPI 也只有 5.37%，用 RCA-agent 提高到 11.34%；没有任何方法解出要求全部三个元素的 hard 查询（Tables 2–3）。

[原文](https://proceedings.iclr.cc/paper_files/paper/2025/file/d29b8d53678015079e1d245c023e49d2-Paper-Conference.pdf)

版本：ICLR 2025 正式会议版（香港中文大学（深圳）、微软、清华），PDF SHA-256 `3cd926feb85119dbb0927e856366e36b0f0794a3b16ea0950a8b4c13cd54fe2a`。已通读正文 §1–8、Figures 1–7、Tables 1–4，数字已对照全文核对，未复现实验。
