# Giannakouris, Trummer — DBG-PT: A Large Language Model Assisted Query Performance Regression Debugger

这是一篇 4 页 VLDB 演示论文。DBG-PT 记录查询的每次执行；当最新执行时间达到先前的 φ 倍时判为性能回退，把高效计划与回退计划（`EXPLAIN` 文本）连同 DBMS 与硬件信息填入提示，让 LLM 输出计划差异、修复用的配置/提示建议及理由。论文只给出系统设计与演示场景，没有定量实验。已通读全文（含图与参考文献）。

[原文](https://doi.org/10.14778/3685800.3685869)

版本：PVLDB 17(12):4337–4340，2024（VLDB 官网 PDF，CC BY-NC-ND 4.0），4 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | §1 Introduction，pp.1–2（4337–4338） |
| 方法 | §2 System Overview，Fig. 1，pp.2–3（4338–4339） |
| 评测 | §3 Demonstration Script（三类场景），p.3（4339）；无定量评测 |
| 局限 | §4 Conclusions and Related Work，p.4（4340）；原文仅称“处于早期阶段” |
