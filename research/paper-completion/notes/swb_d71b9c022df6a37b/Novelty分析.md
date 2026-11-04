# novelty

原文列出的贡献（PDF p.4）：(1) 新的话语关系与结构标注框架；(2) 扩展 rstWeb 支持次级边与信号标注；(3) 超过 200K token、12 个语体的英文语料；(4) ANNIS 可检索的 XML 格式与转换工具；(5) 新定义的解析任务、指标与官方 scorer；(6) 神经流水线基线。

技术要点：
- 主树与 RST 向后兼容（“primary tree should be the same tree as in plain RST”，PDF p.14），次级边只表达关系不表达显著性，nuclearity 仍唯一。
- 次级边必须由信号授权，以控制标注主观性；复杂度上解析次级边最坏只增加一个二次时间步骤（§3.4，PDF p.17）。
- 信号评测：按 (边, 标签) 分组计数的 SP/SR，以及通过 OPTIMAL-PAIR 最优配对计算的 token 级 WP/WR（PDF pp.29–30）。

阅读者分析：创新主要在于把 RST 层级、PDTB 式连接词锚定与 SDRT 式树外关系统一进一个可标注、可评测的格式，而不是新的解析算法——基线系统明确只是“very rough proof of concept”（PDF p.36）。次级边仅占全部关系约 3.37%，但在 causal-result（14.1%）、explanation-justify（11.7%）、adversative-concession（10.3%）等标签上占比较高（Table 10，PDF p.37），这是其增量价值的主要证据。非 DM 信号大多由规则/金标准句法与共指自动诱导，仅部分人工校正（§4.1.2），因此“信号”层的人工质量与 DM 层不同。

依据：[Computational Linguistics 51(1), 2025，ACL Anthology 2025.cl-1.3，50 页](https://aclanthology.org/2025.cl-1.3)，§1、§3、§5–6，PDF pp.4、10–17、28–37。
