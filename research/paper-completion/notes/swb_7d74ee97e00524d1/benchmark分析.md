# 评测与边界

**指标**：图像级 AUROC（§4.3，PDF p.6）。

**实验 1（MVTec LOCO，Table 1，PDF p.6）**：平均 AUROC 如下。

| 方法 | 平均 AUROC |
|---|---|
| SALAD | 96.1 |
| PUAD | 93.1 |
| EfficientAD | 90.7 |
| SAM-LAD | 90.7 |
| 使用监督或按类别调参掩码的 PSAD | 94.9 |
| 使用监督或按类别调参掩码的 CSAD | 95.3 |
| 改用 PSAD 掩码的 SALAD† | 97.2 |

**实验 2（按异常类型，Table 2，PDF p.6）**：SALAD 的逻辑异常 AUROC 为 96.5，结构异常为 95.7。在不使用监督掩码的方法中，两项都最高；PSAD 的逻辑异常为 98.1，更高。

**实验 3（纯结构异常，Table 3，PDF p.6）**：MVTec AD 98.8，VisA 97.9，两者平均 98.3。TransFusion 的平均为 98.9，高于 SALAD。

**实验 4（消融，Table 4，PDF p.8）**：

- 去掉组成分支后，逻辑异常下降 3.5，平均下降 2.3。
- 全局分支改用 ResNet50 特征后，平均下降 3.4。
- 每种合成异常策略都有贡献，单项去除后下降 0.4–0.9。

**推理速度（Table 5，PDF p.8）**：A100 上每张 64.6 ms；EfficientAD 为 6.2 ms。

**边界**：没有独立的局限章节。阅读者核对到以下不一致（阅读者分析）：

- MVTec AD 的分数在 Table 3 中为 98.8，摘要和结论中为 98.9。
- Table 3 中 TransFusion（98.9）和 EfficientAD（98.6）的平均分都高于 SALAD，正文却称 SALAD 的 98.3 为 state-of-the-art；从下一句看，可能只是在逻辑异常方法内比较。
- Table 4 中“4 clusters”行的差值与基线 96.5/95.7 不符。
- 定位结果仅在补充材料中给出。
