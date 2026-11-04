# Zheng, Yin et al. — SGLang: Efficient Execution of Structured Language Model Programs

SGLang 是执行“语言模型程序”（多次 LLM 调用 + 控制流 + 结构化输入输出）的系统，由嵌入 Python 的前端语言（gen、select、fork、join 等原语）和运行时组成；运行时的三项优化是 RadixAttention（以基数树 + LRU 管理跨请求 KV cache 复用）、压缩有限状态机（正则约束解码一次输出多个 token）、面向 API 模型的推测执行。论文报告在 Llama、Mixtral、LLaVA 等模型及 12 类工作负载上吞吐最高提升 6.4 倍、延迟最多降低 3.7 倍（§6.2）。

已阅读正文与附录 A–D；端到端结果多以归一化柱状图给出，未逐柱读数，未复现实验。

[原文](https://arxiv.org/abs/2312.07104)

版本：arXiv:2312.07104v2（2024-06-06，正文标注 “Preprint. Under review”；NeurIPS 2024 正式版未取得），20 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | §1，PDF pp.1–2 |
| 方法 | §2–5、Table 1、Figs. 2–4，PDF pp.3–7；附录 A–B、D，PDF pp.15–20 |
| 评测 | §6、Figs. 5–8、Table 2，PDF pp.7–9；附录 C、Figs. 12–13，PDF pp.18–19 |
| 局限 | §3 末（饥饿问题）、§8 Future Directions、附录 B.3、D.1，PDF pp.6、10、18–19 |
