# 贡献与评价

论文自述三点贡献（§1，p.2）：

1. 系统比较不同 schema 提示格式与少样本示例选择策略对 LLM 的影响；
2. 提出 ACT-SQL 自动生成 CoT，不需要人工标注，也不需要额外 API 调用；
3. 把方法扩展到多轮 text-to-SQL，在 SParC、CoSQL 上与部分微调模型可比。

**技术核心**（§3.3，pp.4–5）：对 SQL 中每个 `[tab].[col]`，枚举问题的所有连续片段 `q_i..j`，取相似度最高者作为链接依据（忽略 GROUP BY 列）；再处理只出现在 FROM 中的表，最后列出 SQL 中的值。相似度模型为 text2vec-base-chinese（§4.1，p.5）。由于 CoT 可以为每个训练样例离线生成，动态示例也能带 CoT。

**评价**：自动 CoT 带来的增益较小且不稳定。附录 Table 11 中 15 组设置里，ACT-SQL 的 TS 有 5 组低于对应 few-shot（如 Create(EoT)、ns=4/nd=0：69.6→68.5）（阅读者分析）。Spider-DK 和 CoSQL 上 ACT-SQL 的 EM 或 TS 也低于普通 few-shot（Tables 6、9）。GPT-4 + ACT-SQL 的 EX 82.9 与 DIN-SQL 的 82.8 几乎持平，EM 61.7 比 DIN-SQL 的 60.1 高，代价差异主要体现在调用次数（Table 2，p.7）。

所谓 CoT 实际是自动化的 schema linking 说明，并非一般意义的推理链；多轮场景的改写步骤会额外调用 LLM，因此“一次调用”只对单轮成立（阅读者分析）。

依据：§1、§3.3、§4、Tables 2、6、9、11，PDF pp.2–8、12。
