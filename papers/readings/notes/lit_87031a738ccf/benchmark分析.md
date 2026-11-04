# 评测与边界

**设置**（§3.1）：模型包括 GPT-5、o3、Gemini-2.5-Pro、DeepSeek-V3.1、Qwen3-Coder、Qwen3-235B-A22B、Qwen3-8B、Kimi-K2、Doubao-Seed-1.6。框架为 OpenHands（CodeAct）与作者的 DA-Agent（Bash+文件系统，执行 Python/SQL）；DE 表格称使用 DE-Agent 框架（App. B.2）。DA 分数 α=0.6（rubric 60%、GSB 40%），评审为 Gemini-2.5-Flash。DE Score = 各 DE 任务均值（Impl/Evol 用 CFS）。

**实验 1（DE，英文版，Table 3，PDF p.6）**：

| 模型 | Arch | Impl CFS | Impl CS | Evol CFS | Evol SR@8 | DE Score |
|---|---|---|---|---|---|---|
| GPT-5 | 63.93 | 30.79 | 61.98 | 38.75 | 20.00 | 43.45 |
| Gemini-2.5-Pro | 51.96 | 27.66 | 55.32 | 23.97 | 8.00 | 32.88 |
| Qwen3-Coder | 51.43 | 23.64 | 54.21 | 27.12 | 12.00 | 32.80 |
| DeepSeek-V3.1 | 52.66 | 22.33 | 50.04 | 24.11 | 10.00 | 31.41 |
| o3 | 48.32 | 15.07 | 35.55 | 24.42 | 6.00 | 28.39 |
| Qwen3-235B-A22B | 50.73 | 2.43 | 20.15 | 12.43 | 2.00 | 20.15 |
| Qwen3-8B | 45.12 | 1.31 | 15.33 | 15.89 | 2.00 | 19.89 |

**实验 2（DA，英文版，Table 5，PDF p.7）**：DA-Agent 框架下 DA Score 为 GPT-5 50.84、Kimi-K2 41.89、Gemini-2.5-Pro 34.70、DeepSeek-V3.1 34.33、o3 28.20、Qwen3-Coder 25.13、Doubao-Seed-1.6 20.74、Qwen3-235B-A22B 13.25、Qwen3-8B 4.47；OpenHands 框架下 GPT-5 为 46.99。

**实验 3（评审可靠性，Tables 7–10）**：

| 表 | 结果 |
|---|---|
| Table 7（评审一致性） | 人工间 Item κw 0.906、Case ICC 0.925；Gemini-2.5-Flash Item κw 0.834、Case ICC 0.890、模型级 τb 1.000 |
| Table 8–10 | 换评审或换 α∈{0.5,0.8,0.9} 时排名 τb 0.90–1.00；8 次重复打分标准差 <0.35 |

**分析结论**：

- CS→CFS 大幅下降（GPT-5 Impl 61.85→30.49，zh 表），作者解读为编排瓶颈。
- core 层局部错误最多、存活率下降最陡，完成全部 marts 的任务不足 20%（Figure 5）；中等规模编辑（5–10 行）最难（Figure 4）。
- 依赖错误占 DE 错误 41.5%（Figure 7）；DA 错误中执行/计算失败平均 59.05%（Figure 9）。

**文本与表格不一致**：

- §3.2 写"As shown in Tab. 4"引用 DE Score 42.88%，该值来自中文版 Table 4，英文 Table 3 为 43.45（阅读者分析）。
- §3.2 称 DA 最高总分 56.14%，Tables 5–6 中最高为 50.84 / 49.49；56.14 只出现在 Table 8 的"Primary"列，o3 的 Accuracy 40.99、Readability 24.63 等数值在 Table 5 中也找不到对应（阅读者分析）。
- 摘要称 DE 成功率 "under 20%"，§1 称 "under 10%"，Table 3 最高 SR@8 恰为 20.00（阅读者分析）。

**局限**：正文无专门局限章节。App. F 承认路径无法穷举（用三层锚点/原则缓解）、DE 需求需人为消歧、各阶段目前解耦评测。阅读者补充：DE 数据为合成；LLM 评审的绝对分数随评审模型变化明显（Table 8）；未报告成本/token 与运行时间。

依据：[arXiv:2512.04324v1](https://arxiv.org/abs/2512.04324)，§3、Tables 3–10、Figures 4–9，PDF pp.6–11；摘要 p.1、§1 p.3；App. F，pp.40–41。
