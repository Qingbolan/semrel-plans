# 评测与边界

**基线**（§4.1，p.6）：通用推理（End-to-End QA、Few-Shot QA、Chain-of-Thought）和程序辅助推理（Text-to-SQL、Binder、Dater），均改用 PaLM 2 / GPT 3.5 重跑（§6，p.9）。

**实验 1（主结果，Table 1，p.6）**：

| 方法 | PaLM 2 TabFact | PaLM 2 WikiTQ | GPT 3.5 TabFact | GPT 3.5 WikiTQ |
|---|---|---|---|---|
| End-to-End QA | 77.92 | 60.59 | 70.45 | 51.84 |
| Chain-of-Thought | 79.05 | 60.43 | 65.37 | 53.48 |
| Binder | 76.98 | 54.88 | 79.17 | 56.74 |
| Dater | 84.63 | 61.48 | 78.01 | 52.81 |
| Chain-of-Table | 86.61 | 67.31 | 80.20 | 59.94 |

**实验 2（链长，Fig.3，p.7）**：PaLM 2 / WikiTQ 上，各链长下均优于 CoT 和 Dater，最大差距分别为 11.6 和 7.9 点。

**实验 3（表格大小，Table 3，p.8）**：WikiTQ 小/中/大表上，Chain-of-Table 为 68.13/52.25/44.87，Dater 为 62.50/42.34/34.62，Binder 为 56.54/26.13/6.41。

**实验 4（生成样本数，Table 4，p.8）**：每题 Binder 50、Dater 100、Chain-of-Table ≤25。

**实验 5（FeTaQA，Table 6，p.14）**：PaLM 2 下 BLEU 32.61，End-to-End QA 为 28.37、Dater 为 29.47；ROUGE-1/2/L 仅比两者高 0.03。作者认为 ROUGE 对风格差异不敏感，并举出答案正确但 ROUGE 很低的例子（Fig.5）。

**实验 6（表格编码，Table 10，p.16）**：End-to-End QA 下 PIPE 60.6、HTML 56.1、TSV 58.1、Markdown 58.0。

**边界**：无独立局限章节；FeTaQA 只用 PaLM 2；未报告运行方差或显著性；"样本数"不等于 token 成本（阅读者分析）。
