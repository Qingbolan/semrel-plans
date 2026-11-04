# 评测与边界

**基线**（§4，PDF p.5）：开源模型包括 Code Llama Instruct（CLI）7B/13B、Llama 3 Instruct（L3I）8B、StarCoder-15.5B、Instruct CodeGen-16B、Llama 2 Chat（L2C）；闭源模型包括 GPT-3.5-turbo、GPT-4-0613、GPT-4-turbo、GPT-4o、Claude 3 Opus。

**指标**：任务 1 用执行错误率（总体及按图类别）、METEOR、CodeBLEU；任务 2 用推荐图类型的 Jaccard 与 Hit Rate、描述的 ROUGE-L/BERTScore，以及把描述交给 SFT L3I-8B 或 GPT-3.5 生成代码后的错误率；任务 3 用 ROUGE-1/2/L、BERTScore，以及描述经 GPT-3.5 生成代码后的错误率（§4，PDF pp.5–6）。

**实验 1（Description-to-Chart，Table 2，PDF p.7）**：

| 模型 | 总错误率 % ↓ | METEOR | CodeBLEU |
|---|---|---|---|
| L3I-8B | 35.91 | 0.519 | 0.437 |
| [SFT] L3I-8B | 16.09 | 0.562 | 0.464 |
| [SFT+RLpref] L3I-8B | 14.55 | 0.567 | 0.461 |
| CLI-13B | 39.14 | 0.489 | 0.413 |
| [SFT] CLI-13B | 9.49 | 0.581 | 0.481 |
| [SFT+RLpref] CLI-13B | 9.21 | 0.566 | 0.467 |
| GPT-3.5-turbo | 18.62 | 0.524 | 0.453 |
| GPT-4-0613 | 19.26 | 0.535 | 0.441 |
| GPT-4o | 13.00 | 0.552 | 0.450 |
| Claude 3 Opus | 14.90 | 0.515 | 0.435 |

**人工评测（Figure 3，PDF p.8）**：每种图类型抽 5 例共 155 例，每例 3 名众包标注者，Krippendorff's α=0.519；SFT+RL L3I-8B 对 GPT-3.5 的胜/负为 25.2%/20.6%；SFT CLI-13B 对 L3I-8B 的胜/负为 47.7%/4.5%。

**实验 2（Raw Data-to-Chart，Table 3，PDF p.7）**：作者称微调后的 L3I-8B 在全部指标上优于开源模型，并在错误率与描述相似度上超过 GPT-3.5-turbo 和 GPT-4-turbo。

| 模型 | 错误率 w/ GPT % ↓ | 错误率 w/ SFT % ↓ | HitRate | Jaccard | R-L | BERTScore |
|---|---|---|---|---|---|---|
| L3I-8B | 27.25 | 38.48 | 0.269 | 0.406 | 0.196 | 0.800 |
| [SFT] L3I-8B | 15.53 | 15.62 | 0.413 | 0.432 | 0.389 | 0.905 |
| GPT-3.5-turbo | 21.00 | 29.10 | 0.239 | 0.412 | 0.232 | 0.816 |
| GPT-4-turbo | 27.05 | 37.01 | 0.313 | 0.461 | 0.184 | 0.808 |
| GPT-4o | 15.82 | 31.64 | 0.339 | 0.436 | 0.170 | 0.786 |
| Claude 3 Opus | 15.62 | 27.34 | 0.294 | 0.451 | 0.188 | 0.813 |

同表中 GPT-4-turbo、Claude 3 Opus、GPT-4o 的 Jaccard 均高于 SFT L3I-8B，"超过闭源模型"只在错误率与描述相似度上成立（阅读者分析）。

**实验 3（Code-to-Description，Table 4，PDF p.7）**：SFT+RLalgn L3I-8B 的 R-L 为 0.440、BERTScore 为 0.884，相似度为全表最高；经 GPT-3.5 生成代码后错误率 20.31%（SFT 为 21.36%）。

同表 GPT-4o 的该错误率为 11.81%、Claude 3 Opus 为 19.33%，均低于本文模型，因此"全面领先"只适用于相似度指标（阅读者分析）。

**边界**：作者列出依赖 Matplotlib 3.8、仅英文、未涉及图表问答（Limitations，PDF p.9）。

执行无错误不等于图正确；正确性只在 155 例人工评测中检查，指标仍以与 GPT 生成真值的相似度为主（阅读者分析）。
