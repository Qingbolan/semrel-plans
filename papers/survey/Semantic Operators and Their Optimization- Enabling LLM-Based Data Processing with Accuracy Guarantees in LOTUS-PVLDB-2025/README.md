# Semantic Operators and Their Optimization: Enabling LLM-Based Data Processing with Accuracy Guarantees in LOTUS

本文提出“语义算子”：用自然语言参数化的 filter、join、top-k、group-by、aggregation、map，每个算子的正确行为由一个高质量参考算法定义。在此基础上，作者为 filter、join、group-by、top-k 设计了基于代理（小模型或嵌入）的优化，保证以概率 1−δ 达到相对参考算法的准确率目标 γ。系统实现为 LOTUS，提供 Pandas 风格的 API。

主要结果：FEVER 事实核验准确率 91.0%，FacTool 为 80.9%；BioDEX 上优化后的 join 比参考算法少约 1,000 倍 LLM 调用（参考算法成本为估计值）；SciFact 与 HellaSwag-bench 排序的 nDCG@10 是次优基线的 1.03–2 倍。

[原文](https://www.vldb.org/pvldb/vol18/p4171-patel.pdf)

版本：Patel, Jha, Pan, Gupta, Asawa, Guestrin, Zaharia（Stanford、UC Berkeley），PVLDB 18(11):4171–4184, 2025。已通读 §1–8（pp.4171–4182）、Tables 1–7、Figures 1–7，数字已对照全文核查；未复现实验。

| 阅读内容 | 位置 |
|---|---|
| problem | §1–2，pp.4171–4175 |
| method | §3.1–3.4、Algorithm 1，pp.4175–4176；§4 系统，pp.4176–4177 |
| evaluation | §5.0–5.5、Tables 2–7、Figures 4–7，pp.4177–4182 |
| limitations | §7（保证只覆盖单算子、参考算法仍待改进），p.4182 |
