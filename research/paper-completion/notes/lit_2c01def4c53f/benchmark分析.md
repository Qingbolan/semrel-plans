# 评测与边界

**基线**：GPT-4 零样本、Palm-2、ChatGPT+CoT、Claude-2、DIN-SQL+GPT-4、DAIL-SQL+GPT-4、C3+ChatGPT。实验使用 GPT-4-32k 与 GPT-3.5-Turbo-16k。

**实验 1（BIRD，Table 1，已渲染核对）**：

| 方法 | Dev EX | Dev VES | Test EX | Test VES |
|---|---|---|---|---|
| GPT-4 | 46.35 | 49.77 | 54.89 | 60.77 |
| DIN-SQL + GPT-4 | 50.72 | 58.79 | 55.90 | 59.44 |
| DAIL-SQL + GPT-4 | 54.76 | 56.08 | 57.41 | 61.95 |
| SQL-Llama（7B） | 32.87 | 55.67 | — | — |
| MAC-SQL + SQL-Llama | 43.94 | 57.36 | — | — |
| MAC-SQL + GPT-3.5-Turbo | 50.56 | 61.25 | — | — |
| MAC-SQL + GPT-4 | 59.39 | 66.39 | 59.59 | 67.68 |
| MAC-SQL + GPT-4 + Oracle Schema | 70.28 | 62.63 | — | — |

**实验 2（Spider EX，Table 2）**：MAC-SQL+GPT-4 dev 86.75、test 82.80；DAIL-SQL+GPT-4 为 84.40 / 86.60，DIN-SQL+GPT-4 为 82.80 / 85.30。

**实验 3（消融，BIRD dev，Table 3）**：完整 59.39；去 Selector 57.28、去 Decomposer 55.54、去 Refiner 54.76。Challenging 档从 40.28 分别降到 35.14、38.89、33.33。

**实验 4（示例数，Table 4）**：0/1/2-shot 下 BIRD EX 为 55.54/57.26/59.39，Spider EX 为 74.22/78.35/86.75。

**错误分析（Figure 5）**：BIRD 与 Spider dev 上“标准答案错误”占 30% 与 22%，“语义正确”（与标准不同但合理）占 14% 与 22%。

**边界**：作者承认提示未必最优、只微调了 7B 模型；Refiner 不修正可执行且非空的错误 SQL。

- Spider test 上 MAC-SQL+GPT-4（82.80）低于 DAIL-SQL 与 DIN-SQL，正文“泛化”论断只依据 dev。（阅读者分析）
- §5.5 写“Schema Linking Error 在 BIRD（2%）比 Spider（8%）更多”，数字与文字方向相反。（阅读者分析）
- Oracle Schema 使 dev EX 升到 70.28，说明 Selector 仍是主要差距来源。（阅读者分析）
- 未报告延迟与每题调用成本。（阅读者分析）

依据：§5.1–5.5，pp.5–8；Tables 1–4；Limitations，p.9；附录 A.3，p.11。
