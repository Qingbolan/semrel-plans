# benchmark

- **比较对象**：15 个 LLM 配置，同一 harness；没有人类分析师或非 LLM 基线。
- **指标**：ms（平均 Jaccard）、CV、平均耗时、Business utility；条件敏感性用 MWU 与 KW 检验（探索性）。
- **总体（Table 3）**：ms 全体 0.3562；Exp1 0.4088、Exp2 0.3972、Exp3 0.3936、Exp4 0.2253。汇总层面只有 Exp1 vs Exp4（MWU p=0.000908）与 KW（p=0.000251）在 0.05 下显著（Table 5）；冗余汇总表与无歧义提示未实质改变汇总 ms。
- **排名（Table 4，实验平均）**：GPT-5.4 xhigh ms 0.8748、CV 0.1202、折扣 0.7665、utility 0.6952；Gemini 3.1 Pro high utility 0.3533（ms 0.4991）；GPT-5.2 xhigh 0.2815（ms 0.6501，CV 0.3739）；Claude Sonnet 4.6 low 0.2506。末位 GPT-5.4 mini low ms 0.0027。Gemini 3.1 Pro high 因 CV 较低排在 ms 更高的 GPT-5.2 xhigh 之上。
- **模型级敏感性（Table 6）**：Exp1 vs 2 无配置显著；vs 3 有 3 个、vs 4 有 2 个；KW 有 6 个。
- **结论**：平均 utility 0.1511 仅为平均 ms 的约 42%；主要风险是同条件下重复运行的不稳定，而非条件变化。更高推理档位在若干家族（GPT-5.4、GPT-5.2）显著提升，但不普遍。
- **局限（§8）**：每条件仅 5 条轨迹，检验功效低、方差估计不确定；只有一个业务问题和一个仿真家族；utility 依赖所选参数化；ms=0 时 CV=0 的约定使折扣无信息。
- **阅读者分析**：CV 在 ms 很低时极不稳定（如 Gemini 3.1 Pro low CV=2.0），而 ms≈0 的配置折扣反而很高（GPT-5.4 mini low 0.754），说明折扣项单独解读会误导，应和 ms 一起看——作者对 ms=0 的情形已作提示。

依据：[arXiv:2606.00051v1，16 页](https://arxiv.org/abs/2606.00051)，§5–6、§8、Tables 3–6，PDF pp.8–14。
