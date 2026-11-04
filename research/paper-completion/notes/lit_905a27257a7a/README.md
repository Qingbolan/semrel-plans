# Zheng et al. — Efficient Serving for Dynamic Agent Workflows with Prediction-based KV-Cache Management

本文提出 PBKV：在 SGLang（Radix Tree + HiCache 两级缓存）上，为多智能体工作流预测未来 K 步将被调用的 agent，据此给 KV-Cache 节点打分，用于驱逐与预取。核心结果：三个工作负载上相对 LRU 端到端延迟最多降低 1.85×、命中率最多提升 2.55×；在唯一可与 KVFlow 公平比较的静态工作流上最多快 1.26×。已阅读正文 §1–8 及附录 A–F，附录 G 的证明只读了定理陈述与假设，未逐步核对。

[原文](https://arxiv.org/abs/2605.06472)

版本：arXiv:2605.06472v1（2026-05-07），24 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| problem | §1–2，PDF pp.1–3 |
| method | §3–5，Figures 2–4，PDF pp.3–6；附录 B，pp.12–14 |
| evaluation | §6、Table 1、Figures 5–6，PDF pp.6–9；附录 A（Table 2）、C（Table 3）、E、F（Table 4），pp.12–19 |
| limitations | §5 “Limitations”，PDF p.6；§6.2 “Remark on Static Workflows”，p.8；附录 E，pp.17–19 |
