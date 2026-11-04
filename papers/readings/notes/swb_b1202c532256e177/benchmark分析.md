# 评测与边界

**实验 1（电子表格主结果，Table 1，p.4）**：基线绝对值（122B 用户 Vrf / 35B 用户 Vrf / Avg）为：No Skill 27.67 / 19.00 / 18.19；Human-Written 48.33 / 9.67 / 26.93；Parametric 26.17 / 20.17 / 19.23。演化行报告相对初始化的增量：

| 作者 | 模式 | 变体 | ΔAvg |
|---|---|---|---|
| 122B | Deepening | +Error / +Success / +Combined | +9.28 / +8.15 / +9.65 |
| 122B | Creation | +Error / +Success / +Combined | +6.79 / +16.96 / +18.62 |
| 35B | Deepening | +Error / +Success / +Combined | +5.64 / +12.44 / +14.04 |
| 35B | Creation | +Error / +Success / +Combined | +15.22 / +5.65 / +13.31 |

摘要中的“+57.65 pp”是 35B 作者 Creation +Error 在 122B 用户 WikiTQ 上相对 Parametric 的增量。

**实验 2（跨家族，Figure 3，p.5）**：Gemma-4 与 GPT-5.5 用自身轨迹深化 skill，或使用 Qwen 写的 skill，均有提升。

**实验 3（数学与 DocVQA，Tables 2–3，p.6）**：相对 No Skill，DAPO 增量最多 +6.0；DocVQA 122B 作者 +Combined 在 122B 用户上 ANLS +0.2534、Acc +22.25。

**实验 4（设计对比，Tables 4–5，pp.6–7）**：122B 用户 Vrf：并行 65.83，Seq-B=1 61.83，Seq-B=4 59.00；耗时约 3 / 60 / 15 分钟。35B 用户的 Soft/Hard 上 Seq-B=1 略高。ReasoningBank（top-1 检索）122B Vrf 56.00，+Combined 69.83；该比较排除 OOD。agentic 错误分析在多数设置下优于单次调用版本（Figure 4）。

**实验 5（补丁选择，§4.3，Table 6）**：贪心选择的曲线低于全量合并；BO 选择使 Vrf 从 65.83 升至 69.83，但验证成本高。

**实验 6（文档 skill，§4.4，p.9）**：PDF 76.9%→85.3%，PPTX 72.5%→88.8%，DOCX 79.7%→87.5%。

**局限（原文）**：默认合并全部补丁；BO 选择成本随验证集与补丁数快速增长，且只用了 32 题验证（Limitations，p.9）。阅读者分析：未报告 skill 演化本身的 token 成本；Table 1 中存在负增量单元，结论主要依赖 Avg 汇总。
