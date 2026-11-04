# 评测与边界

**设置**（§5，PDF pp.6–7）：编码器为 uncased BERT、SciBERT、MatSciBERT；每个配置训练 5 次（训练折不同），报告测试集均值±标准差。

**实验 1（测量句识别，Table 8，PDF p.7；测试集 F1）**：

| 模型 | MEASUREMENT F1 | QUAL_MEAS F1 |
|---|---|---|
| 随机基线 | 21.9 | 14.7 |
| BERT | 72.5 | 50.6 |
| SciBERT | 75.0 | 52.7 |
| MatSciBERT | 74.9 | 54.7 |
| 人类一致性（子集估计） | 73.8 | 61.7 |

MatSciBERT 总体准确率 78.2%。

**实验 2（NER，Table 9，测试集）**：

| 模型 | 编码器 | Micro F1 | Macro F1 |
|---|---|---|---|
| 依存解析 | BERT / SciBERT / MatSciBERT | 73.0 / 76.5 / 77.3 | 61.7 / 65.8 / 67.6 |
| CRF 标注器 | BERT / SciBERT / MatSciBERT | 75.3 / 78.7 / 79.6 | 63.2 / 69.3 / 70.7 |

**实验 3（关系抽取，金标实体，Table 10）**：

| 模型 | dev Micro | dev Macro | test Micro | test Macro |
|---|---|---|---|---|
| 多数类基线 | 38.3 | 29.4 | 37.2 | 27.4 |
| BERT | 69.5 | 63.4 | 63.5 | 57.7 |
| SciBERT | 72.5 | 65.7 | 67.5 | 62.0 |
| MatSciBERT | 73.2 | 66.5 | 67.6 | 62.0 |

使用预测实体时（span 须精确匹配），micro-F1 降至 dev 42.5 / test 36.5，macro 37.9 / 32.8（§5.3，PDF p.8）。

**实验 4（多任务学习，Tables 11–12，PDF p.8）**：NER 加入 SOFC-Exp/MSPT 无整体提升；关系抽取中加入 MuLMS 使 SOFC-Exp 测试 micro 66.9→68.7、MSPT 84.6→85.6，MuLMS 加 MSPT 为 67.6→68.7。

**边界**：IAA 很不均衡——NE 中 SAMPLE F1 仅 4.7、PROPERTY 40.0（Table 6）；关系总体 κ=0.61，但 usedTogether κ=0.00（Table 7）。作者认为 IAA 低估可复现性，因第二标注者只经过简短培训（Limitations，PDF p.9）。金标实体标签作为关系模型输入使任务明显变易，流水线存在误差传播。阅读者分析：MTL 增益多在 1–2 个点且标准差 0.4–4.3，统计显著性未报告。
