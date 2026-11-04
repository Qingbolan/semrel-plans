# Lin et al. — Parrot: Efficient Serving of LLM-based Applications with Semantic Variable

Parrot 是面向多次调用 LLM 的应用的服务系统：用 Semantic Variable 标注提示中的输入/输出占位符，让服务端看到请求之间的数据依赖和提示结构，从而在服务端串接依赖请求、从最终输出反推调度目标、按前缀哈希共享 KV cache 并做应用感知调度。在长文档摘要、Bing Copilot/GPTs 共享系统提示、MetaGPT 多智能体编程和混合负载上，相对 FastChat+vLLM/HuggingFace 基线最高 11.7× 加速，或在 GPTs 场景下最高可承受 12× 请求率。已读正文 §1–§9；未复现实验。

[原文](https://www.usenix.org/conference/osdi24/presentation/lin-chaofan)（论文页）；全文 PDF 见 [原文](https://www.usenix.org/system/files/osdi24-lin-chaofan.pdf)。

版本：OSDI 2024 会议论文集 pp.929–946，USENIX 开放获取 PDF 18 页（含封面页）。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。（PDF 页码 = 论文集页码 − 927）

| 阅读内容 | 位置 |
|---|---|
| 问题 | §1、§3、Figures 1–5、Table 1，PDF pp.2–5 |
| 方法 | §4–§5、§7、Algorithm 1、Figures 6–9，PDF pp.5–10 |
| 评测 | §8、Table 2、Figures 10–19，PDF pp.10–14 |
| 局限 | §6 Discussion、§8.1 末段，PDF pp.8–9、11 |
