# 评测与边界

**基线**：微调类（Table-BERT、LogicFactChecker、TaPas、SAT、TAPEX、SaMoE、PASTA、ReasTAP、TableFormer、TaCube、OmniTab、T5 等）与 LLM 上下文学习类（直接提示的 Codex、Binder）。

**实验 1（主结果，Tables 1–3）**：

| 设置 | TabFact test-small 准确率 | WTQ dev / test | FetaQA BLEU |
|---|---|---|---|
| Codex（直接提示） | 72.6 | 49.3 / 47.6 | 27.96 |
| Binder | 85.1 | 62.6 / 61.9 | — |
| Codex + Dater | 85.6 | 64.8 / 65.9 | 30.92 |
| 最强微调基线 | PASTA 90.8 | OmniTab 61.3 / 61.2 | T5-large 30.54 |
| 微调模型 + Dater 分解 | PASTA 93.0 | OmniTab 62.5 / 62.5 | — |
| Human | 92.1 | — | — |

**实验 2（消融，Table 4）**：去掉证据分解时 TabFact All 降 3.8、WTQ All 降 2.0、FetaQA BLEU 降 2.46；去掉问题分解时分别降 3.7、4.5、0.19。作者解释 WTQ 更依赖问题分解，FetaQA 更依赖证据分解。

**实验 3（案例）**：Table 5 对比规则法与 Dater 的列选择；Table 6 对比 Codex 思维链与 Dater 子问题。均为挑选案例，无定量错误分析。

**边界**：作者在 §6 承认证据分解一次性整体预测行列索引，未按问题逐步推理。未报告 LLM 调用次数、token 成本或延迟（每个样本至少需证据分解、子问题、SQL、推理四次调用，另加 self-consistency）；Simple/Complex 划分对 WTQ 仅按问题长度；结果依赖已下线的 code-davinci-002，复现受限（阅读者分析）。

依据：§5.4–5.7，pp.8–11；Tables 1–6；§6，p.12。
