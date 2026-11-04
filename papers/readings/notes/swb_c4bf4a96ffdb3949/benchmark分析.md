# 评测与边界

**指标**（§6.2，PDF p.8）：均为 P/R/micro-F1，分四类。

- **Token match**：逐 token 比较。
- **Exact span match**：连续证据片段完全重合才算对。
- **两种 position-independent（P.I.）变体**：按字符串匹配，不看位置，用以缓解"充分证据与完整证据"的标注差异。

阈值在开发集上按 token micro-F1 选择。

**实验 1（Inpatient 出院小结测试集，Table 9，PDF p.8；3 次训练均值）**：

| 方法 | Token F1 | Exact span F1 | P.I. token F1 | P.I. span F1 |
|---|---|---|---|---|
| CAML 无监督注意力 | 21.4 | 7.1 | 28.5 | 10.1 |
| EffectiveCAN 无监督注意力 | 36.2 | 25.3 | 47.7 | 34.9 |
| 监督注意力（SA） | 43.0 | 27.8 | 56.8 | 39.2 |
| 线性 tagging | 40.4 | 27.3 | 53.3 | 37.5 |
| CNN tagging | 41.9 | 26.2 | 55.6 | 35.9 |

作者认为 SA 在所有指标上最佳，tagging 方法可能需要更多数据。CAML 的三个种子中有一个明显偏高，因此标准差很大（§6.3，PDF p.9）。

**实验 2（全部可编码文档，SA，Table 10，PDF p.8）**：截断长度从 3,500 提高到 5,000。Inpatient 的 token F1 为 37.2，exact span F1 为 24.5；Profee 分别为 36.5 和 28.1。作者提醒，截断可能丢掉一半以上的 token 和证据。

**实验 3（证据训练量，Table 7，PDF p.7）**：随证据训练数据增加，token-F1 从 32.0 升到 36.8；编码 F1 基本不变，约为 58。

**边界**（§8，PDF p.10）：

- 编码员倾向只标充分证据，因此召回率可能被低估。
- 存在部分漏标修饰词的情况，例如只标了 "effusions" 而非 "bilateral pleural effusions"。
- 标注工具不支持不连续片段。
- 基线只覆盖 CNN 类模型，没有 Transformer 或 LLM 基线（阅读者分析）。
