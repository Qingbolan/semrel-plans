# 评测与边界

**基线**：RAMS 上为 Seq 与 Two-step（当时 SOTA，先检测中心词再扩展）；WikiEvents 上为句子级 BERT-CRF、句子级 BERT-QA 与文档级 BERT-QA-Doc；零样本中另有把 TapKey 换成 Prototype Network 的变体（§4.2–4.4，PDF pp.6–7）。

**实验 1（RAMS）**（Table 4，PDF p.7）：BART-Gen 的 Span F1 / Head F1 为 48.64 / 57.32，Two-step 为 41.8 / 49.7；摘要中的 7.6 F1 对应 Head F1 差值。

**实验 2（WikiEvents 常规与信息量论元）**（Tables 5–6，PDF p.7）：

| 模型 | 常规 Arg-C Head | 常规 Arg-C Coref | 信息量 Arg-C Head | 信息量 Arg-C Coref |
|---|---|---|---|---|
| BERT-CRF | 54.48 | 56.72 | 43.29 | 47.70 |
| BERT-QA | 56.16 | 59.36 | 43.44 | 46.45 |
| BERT-QA-Doc | 34.77 | 45.96 | 24.46 | 29.26 |
| BART-Gen | 64.57 | 65.11 | 51.03 | 57.04 |

所有模型在信息量论元任务上都明显变差；CRF 识别片段较好但分类受长尾角色拖累；QA 模型识别差、易重叠过度生成；直接把 BERT-QA 用到文档级反而大幅下降（§4.3，PDF p.7）。摘要的 5.7 与 9.3 分别对应常规与信息量 Arg-C Coref F1 的差值（阅读者分析）。

**实验 3（ACE 零样本）**（Table 8，PDF p.9）：见 10 个最频繁类型时 TapKey + BART-Gen 的 TC F1 / AC Head F1 为 69.23 / 44.19，全监督为 71.13 / 53.71，即约 97% / 82%；0 个已见类型时 TapKey 的 TC F1 为 52.10，Prototype 仅 2.22。

**边界**：作者列出两类剩余问题：本体约束（如互斥角色同时填为“Japan”）和常识知识缺失（如引渡案中错判 Destination/Source）（§4.6，PDF pp.8–9）。完全新的模板可能让模型改动模板结构（§4.4，PDF p.7）。阅读者分析：结果为单次运行，无方差或显著性检验。
