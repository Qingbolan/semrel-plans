# 评测与边界

**基线**：线性/逻辑回归、Seq2Seq、RNN、Bi-RNN、LSTM、Bi-LSTM、GRU、Transformer、Mamba、决策树、随机森林、XGBoost、BERT、CINO、RoBERTa，以及 CNN/ViT/ConViT 编码器与 RNN/LSTM/GRU/Transformer/Mamba 解码器的组合；LLM 包括 GPT、LLaMA 3.1、Qwen 2.5、DeepSeek、Claude 3.5 Sonnet、Gemini 1.5 Flash，分提示、嵌入 + MLP、带分类头微调三种用法（Baseline Model、Table 5，PDF p.6）。指标为 Precision、Recall、F1。

**实验 1（主结果，Table 6，PDF p.7）**：

| 模型 | Equal Weight F1 | Constraint F1 | Suspected F1 |
|---|---|---|---|
| Logistic Regression | 42.18 | 60.79 | 45.98 |
| XGBoost | 90.17 | 97.65 | 87.28 |
| Mamba | 87.15 | 98.69 | 93.89 |
| BERT | 91.89 | 97.78 | 91.23 |
| ConViT-Transformer | 92.07 | 97.05 | 94.87 |
| MaBoost | 94.79 | 99.47 | 96.76 |

**实验 2（LLM，Figures 1–3，PDF pp.8）**：提示法 F1 多在 25 以下（最好 N-shot 约 70）；微调最佳为 GPT-4o 87.44（Equal Weight）、LLaMA 3.1 405B 90.67（Constraint）、DeepSeek-V3 89.13（Suspected）。

**实验 3（消融，Tables 7–8，PDF p.9）**：去掉时空特征后 Suspected F1 降至 64.79；在决策树/随机森林/XGBoost 上加 Transformer 或 Mamba 编码器均有提升。

**作者承认的局限**：F1>99% 看似过高，作者归因于规则清晰；目前仅覆盖美国市场（Discussion，PDF pp.9–10）。LLM 评测细节称"将在最终版本中完整记录"（PDF p.6）。

阅读者分析：多处 F1 与 P/R 不相容——Seq2Seq（P 76.67、R 74.68、F1 77.02）的 F1 高于两者，MaBoost（94.93、95.48、94.79）的 F1 低于两者，单一调和平均不可能如此，论文未说明是否为跨折平均；未报告方差或显著性；结合标签泄露问题，这些分数不宜作为模型能力的证据（阅读者分析）。

依据：Experimental Result、Tables 5–8、Figures 1–3、Discussion，PDF pp.5–10。
