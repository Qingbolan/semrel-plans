# 评测与边界

**实验 1（零样本 schema 格式，Table 3，p.7）**：GPT-3.5-turbo 下五种格式 EX 在 77.0–79.2、TS 在 66.1–69.4；Table(Column) 类格式 TS 更高，作者认为与 OpenAI 官方示例格式接近有关。

**实验 2（Spider dev 对比，Table 2，p.7）**：

| LLM | 方法 | API/SQL | EM | EX | TS |
|---|---|---|---|---|---|
| Codex | Rajkumar et al. | 1 | — | 67.0 | 55.1 |
| Codex | DIN-SQL | 4 | 57.2 | — | 69.9 |
| GPT-4 | DIN-SQL | 4 | 60.1 | 82.8 | 74.2 |
| GPT-3.5-turbo | ACT-SQL | 1 | 62.7 | 80.4 | 71.4 |
| GPT-4 | ACT-SQL | 1 | 61.7 | 82.9 | 74.5 |
| 微调 | RESDSQL-3B+NatSQL | — | 80.5 | 84.1 | — |

GPT-4 + ACT-SQL 在 extra hard 上 TS 为 44.0，easy 为 91.1（Table 12，p.12）。

**实验 3（鲁棒性变体，Tables 5–7，p.8）**：GPT-3.5-turbo 的 ACT-SQL 与 few-shot 相比，Spider-Syn 上 EX 63.7→67.9、TS 54.5→59.3；Spider-DK 上 EX 68.8→68.2；Spider-Realistic 上 EX 76.4→75.8、TS 62.0→61.2。

**实验 4（多轮，Tables 8–9，p.8）**：SParC 上 ACT-SQL 的 IM-TS 为 29.6，低于 few-shot 的 31.5；CoSQL 上 IM-EM 13.3，远低于 RASAT+PICARD 的 27.0。作者把原因归于改写质量。

**边界**：作者承认 ns、nd 需手工决定，选择策略简单；在鲁棒性变体和多轮数据集上效果较差（Limitations，p.9）。全部结果在 dev 集上，作者用 Table 4 中其他方法的 dev/test 走势推论上下文学习不会过拟合 dev，但没有给出 ACT-SQL 自身的 test 结果；所有结果为单次运行，未报告方差（阅读者分析）。

依据：§4.2–4.4、Limitations、Tables 2–12，PDF pp.6–9、12。
