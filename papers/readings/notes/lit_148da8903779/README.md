# Pan et al. — KVFlow: Efficient Prefix Caching for Accelerating LLM-Based Multi-Agent Workflows

KVFlow 是面向多智能体工作流的 KV 缓存管理框架：用 Agent Step Graph 估计每个智能体距下一次执行还有几步（steps-to-execution），据此替代 LRU 做节点级驱逐，并在后台把下一步要用的前缀 KV 从 CPU 预取到 GPU。基于 SGLang v0.4.4 实现，相对开启分层缓存的 SGLang，单工作流大提示场景最高 1.83× 加速，高并发场景最高 2.19×。已阅读 arXiv v1 全文（§1–6）；Figures 5–8 经渲染 pp.7–8 核对。

[原文](https://arxiv.org/abs/2507.07400)

版本：arXiv:2507.07400v1（2025-07-10），12 页。批次信息标注 NeurIPS 2025，但所读 v1 正文未标注会议，也未核对会议定稿版。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| problem | §1–2，Figures 1–2，PDF pp.1–3 |
| method | §3.1–3.3，Figures 3–4，PDF pp.3–6 |
| evaluation | §4.1–4.2，Figures 5–8，PDF pp.6–9；pp.7–8 已渲染核对 |
| limitations | 无独立局限章节；§4.1–4.2 中的适用范围说明，PDF pp.8–9 |
