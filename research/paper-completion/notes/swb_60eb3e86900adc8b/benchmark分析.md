# 评测与边界

**指标**：AUROC 与 F1-max（%）。LogicQA 本身无阈值，分数由 log-prob 派生（§5.2，PDF p.5）。主实验用 GPT-4o，每类跑 3 次取均值。

**实验 1（MVTec LOCO 逻辑异常，Table 1，PDF p.5）**：

| 方法 | 设置 | 平均 AUROC | 平均 F1-max |
|---|---|---|---|
| LogicQA (GPT-4o) | 少样本、可解释、自动提示 | 87.6 | 87.0 |
| LogicAD | 少样本、可解释 | 86.0 | 83.7 |
| WinCLIP | 少样本 | 64.3 | 59.5 |
| PatchCore | 少样本 | 74.0 | — |
| GCAD | 非少样本 | 86.0 | — |
| AST | 非少样本 | 79.7 | — |

LogicQA 在 Screw Bag 上最弱（AUROC 71.5，低于 LogicAD 的 83.8）；在 Splicing Connectors 上提升最大（92.4 vs 73.4）。

**实验 2（SEM，Table 2，PDF p.6）**：GPT-4o 平均 AUROC 90.3、F1-max 92.4；InternVL-2.5 8B 的 F1-max 85.2；PatchCore 为 79.2/77.8。

**实验 3（换 VLM，Table 3，PDF p.6）**：平均 F1-max 依次为 GPT-4o 87.0、Gemini-1.5 Flash 79.7、InternVL-2.5 38B 77.6。Gemini 在 Splicing Connectors 上只有 46.8。

**实验 4（解释的人工核对，§5.4，PDF p.6）**：两位标注者按主问题作答，与模型一致率分别为正常 98%/异常 85% 和 98%/86%。

**边界**：

- 附录 Table 5 中使用标注的 LogiCode（98.8）和 PSAD（98.1）远高于本文结果（PDF p.18）。
- 基线数值是否为作者自行复现，正文未说明。
- 只评测逻辑异常。
- SEM 数据不公开，不能复核。
- 正文没有报告成本或延迟。
- Limitations 承认性能依赖 VLM 视觉能力，且需要图像预处理（PDF p.7）。

阅读者分析：人工核对只说明标注者回答主问题时与模型一致，不等于独立验证每条异常理由的正确性。
