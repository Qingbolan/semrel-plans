# Zhang et al. — CoDA-Bench: Can Code Agents Handle Data-Intensive Tasks?

本文（中国人民大学，ICML 2026）提出 CoDA-Bench：在基于 Kaggle 的数据密集型 Linux 沙箱中，agent 只拿到一句分析问题，须在平均约 981 个文件（10–8,158）的"社区"目录里自行找出目标数据并写代码求出封闭答案。共 1,009 题、31 个数据社区，另有 119 题的 CoDA-Hard。最好的系统 Mini-SWE-Agent + GPT-5.5 执行准确率 61.1%（Hard 上 49.6%）；在 Hard 上提供 oracle 文件路径可提升 24–28 个百分点。已读正文与附录 A–E、H，案例与提示词（F–G）略读。

[原文](https://arxiv.org/abs/2606.15300)

版本：arXiv:2606.15300v1（2026-06-13），ICML 2026（PMLR 306），37 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| problem | §1、§4.1，PDF pp.1–2、5 |
| method | §3（Table 1、Fig.2）、附录 B–C（Algorithm 1），PDF pp.2–5、16–22 |
| evaluation | §4.2–4.4、§5–6、Tables 2–4、Figs.4–7、附录 E，PDF pp.5–9、27 |
| limitations | 附录 H，PDF p.37 |
