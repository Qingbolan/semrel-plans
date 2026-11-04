# Lao et al. — GPTuner: A Manual-Reading Database Tuning System via GPT-Guided Bayesian Optimization

GPTuner 用 LLM 读取 DBMS 手册、论坛和 GPT 自身知识，整理成每个 knob 的结构化提示，再用于选 knob、收缩取值范围和两阶段贝叶斯优化。论文在 PostgreSQL/MySQL 上调优 TPC-H 延迟和 TPC-C 吞吐，称平均以 16 倍更少时间找到更好配置，相比最佳基线最多提升 30%。已阅读正文 §1–9；PDF 第 2、4、5、10、11 页无文本层，已渲染核对（含 §8 实验页）。消融研究正文未给出，仅指向技术报告，未阅读该报告。

[原文](https://vldb.org/pvldb/vol17/p1939-tang.pdf)

版本：PVLDB Vol.17 No.8，pp.1939–1952，2024，14 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | §1–3（含 Table 1–2、Figure 2），PDF pp.1–4 |
| 方法 | §4–7（Figure 3、Algorithms 1–3），PDF pp.5–9 |
| 评测 | §8.1–8.5（Figures 4–9、Table 3），PDF pp.10–12；pp.10–11 已渲染核对 |
| 局限 | §8.4 知识质量实验、§9 Outlook，PDF pp.11–12 |

注：`text/lit_973e61bae430.txt` 由 `pdftotext` 提取，缺少 PDF pp.2、4、5、10、11 的正文（原 PDF 这些页无可提取文本），这些页的内容来自渲染图像阅读（阅读者说明）。
