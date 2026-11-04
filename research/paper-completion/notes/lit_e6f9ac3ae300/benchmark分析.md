# 评测与边界

**基线**：BM25 与 Gemini API 嵌入（models/embedding-001）的神经检索，均复用 ReadAgent 的分页结果并取 top-k 页；全文（QuALITY）或截断前/后 6,000 词（QMSum）；只用要点记忆（GistMem）（§4.2，pp.5–6）。

**指标**：QuALITY 用准确率；NarrativeQA 与 QMSum 用 ROUGE-1/2/L F 值和两种 LLM 评分——LR-1 只计严格匹配，LR-2 计严格或部分匹配，由 PaLM 2-L 按严格与宽松两个提示判定（§4.1，p.5）。

**实验 1（QuALITY，Table 1，p.6，3 次运行均值）**：

| 方法 | CR | 准确率 |
|---|---|---|
| 全文 | 0% | 85.83% |
| BM25 top-4 | 58.57% | 84.42% |
| 神经检索 top-4 | 60.68% | 84.88% |
| GistMem | 85.53% | 77.52% |
| ReadAgent-P 回查 1–2 页 | 72.17%（约 3.5 倍有效上下文） | 86.16% |
| ReadAgent-S 1–6 页 | 58.53% | 87.17%（最高） |

与直接用全文相比，ReadAgent 回查 1–2 页总处理词数节省 20.4%（§3.3，p.4）。

**实验 2（NarrativeQA 测试集，Table 2，p.7）**：

| 子集 | 最好检索 LR-1 | GistMem LR-1 | ReadAgent 最好 LR-1 |
|---|---|---|---|
| Gutenberg | 53.60%（BM25 top-4） | 55.79% | 60.55%（S，1–3 页） |
| 电影剧本 | 52.13%（神经 top-4） | 54.68% | 64.53%（S，1–3 页） |

Gutenberg 上 ReadAgent-P 回查 1 页的 CR 为 94.84%，约 20 倍有效上下文（阅读者核算）。

摘要称 Gutenberg 测试集 ROUGE-L 比最好检索基线高 31.98%；按 Table 2 中 ReadAgent 最高 ROUGE-L 0.226 与 BM25 top-4 的 0.197 计算约为 15%，未能复现该数字；0.260/0.197≈1.32 恰好对应电影剧本测试集 ReadAgent-P 回查 1 页的 ROUGE-L 与 Gutenberg 测试集 BM25 top-4 的 ROUGE-L，疑为跨子集混用（阅读者分析）。LR-1 的“提升 12.97%”则是相对提升（60.55/53.60）（阅读者分析）。

**实验 3（QMSum，Table 3，p.8）**：ReadAgent-S 1–6 页 LR-1 46.57%、LR-2 91.54%、ROUGE-L 21.15，均为最高；截断前 6k 词 LR-1 仅 14.71%。作者指出要点会使回答变长、压低 ROUGE 精度，因此认为 LLM 评分更有参考价值。

**实验 4（GPT-3.5，附录 B，Table 7）**：趋势相同，ReadAgent-S 与全文相当；ReadAgent-P 平均只回查 1.0 页。

**边界**：作者承认不能提供无限上下文，要点记忆过长时不保证效果；常规检索可处理比本方法大得多的库；使用要点时 LLM 可能更易幻觉出被省略的细节，但未加研究；LLM 评分难以与其他工作横向比较（§2、§4.3.3、§5、Impact Statement，pp.2、8–9）。阅读者分析：评分器与被评模型同为 PaLM 2-L，存在自评偏差风险；QMSum 只有 272 题。

依据：§4、Tables 1–3，PDF pp.5–9；附录 B，PDF p.13。
