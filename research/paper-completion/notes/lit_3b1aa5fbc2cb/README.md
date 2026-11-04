# Son et al. — Kalypso: Relational LLM Serving

本文提出“关系型 LLM serving”：在语义查询处理系统（Lotus、Palimpzest 等）与 vLLM 之间加一层感知查询计划的服务层，把语义算子按流水线执行，使同一元组的 KV cache 前缀在上下游算子之间复用，并用自适应、内存感知的阶段预算调度避免前缀被驱逐。在 FEVER、MEDEC、BioDEX、ContractNLI 四个工作负载上（Llama-3.3-70B，4×RTX Pro 6000），端到端延迟相对 Lotus 最高加速 4.57×，LLM 调用数相近。已通读正文 §1–9；论文无附录。

[原文](https://arxiv.org/abs/2607.23815)

版本：arXiv 2607.23815v2（2026-08-14，cs.DB），14 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| problem | §1、§2（Figure 1–2），PDF pp.1–3 |
| method | §3–6（Table 1、Figures 3–6、Algorithm 1），PDF pp.3–8 |
| evaluation | §7、Table 2、Figures 7–12，PDF pp.8–12 |
| limitations | 无独立 Limitations 节；§6 末（死锁仅在压力测试出现）、§7.1–7.2（各系统级联配置不同）等处的限制由阅读者整理 |
