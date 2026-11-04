# 评测与边界

**实验 1（MVTec LOCO AD 逻辑异常，Table 1，PDF p.6，已渲染核对）**：

| 方法 | 设置 | 平均 AUROC | 平均 F1-max |
|---|---|---|---|
| LogicAD（GPT-4o） | 单样本、免训练 | 86.0 | 83.7 |
| AnomalyMoE | 少样本 SOTA | 67.9 | 79.1 |
| WinCLIP | 单样本 | 64.3 | 59.5 |
| GCAD | 全样本 | 86.0 | – |
| PatchCore | 全样本 | 74.0 | – |
| ComAD | 全样本 | 87.7 | – |
| AST | 全样本 | 79.7 | – |

LogicAD 各类 AUROC：Breakfast Box 93.1、Juice Bottle 81.6、Pushpins 98.1、Screw Bag 83.8、Splicing Connector 73.4。AnomalyMoE 只有平均值、没有分类别结果。全样本 ComAD 平均 AUROC 高于 LogicAD，GCAD 与之持平（阅读者分析）。

**实验 2（MVTec AD，Tables 2、6，PDF pp.6–7）**：四个逻辑相关物体类别上 AUROC 86.5，WinCLIP 80.9、AnomalyCLIP 89.1、VAND 71.5；纹理类别 96.9，低于 WinCLIP 98.1。

**实验 3（消融，Table 3，PDF p.6）**：

| 模块组合 | AUROC | F1-max |
|---|---|---|
| 无任何模块 | 23.4 | 9.5 |
| + Guided CoT | 48.5 | 51.3 |
| + Guided CoT + ROI | 60.4 | 65.3 |
| + Guided CoT + ROI + 格式嵌入 | 86.0 | 83.7 |
| + Guided CoT + ROI + 逻辑推理器 | N/A（只输出 0/1） | 83.3 |

**实验 4（不同 AVLM，Table 5，PDF p.7）**：

| AVLM | AUROC | F1-max |
|---|---|---|
| GPT-4o | 86.0 | 83.2 |
| LLaVA 1.6 | 76.2 | 78.1 |
| LLaVA 1.5 | 73.3 | 71.0 |

Table 5 中 GPT-4o 的 F1-max 83.2 与 Table 1 的 83.7 不一致，原文未解释（阅读者分析）。

**实验 5（结构异常，Table 4，PDF p.7）**：MVTec LOCO 结构异常 AUROC 81.5，高于 WinCLIP 64.6、GCAD 80.7，低于 AST 87.7、PatchCore 89.3。

**边界**（Limitations，PDF p.7）：不同 AVLM 结果不一致；推理每张图平均需数秒；失败案例主要由逻辑不一致导致（附录 A.3，本 PDF 未包含）；仍需每个任务定义一次人工提示。阅读者补充：没有报告 API 成本；单样本选择对结果的影响只体现在 5 次重复的标准差中。
