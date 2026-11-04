# 具体用例

**原文示例：ClinTox 药物毒性预测**（Figure 2，p.3；Table 1，p.5）。

- 任务指令："在 ClinTox 数据集上训练多任务模型，预测药物的毒性和 FDA 批准状态。把测试集预测（含药物 SMILES 和正标签概率）存到 `pred_results/clintox_test_pred.csv`。"
- 数据集信息：目录 `clintox/` 下有 `clintox_train.csv`、`clintox_test.csv`；预览显示列为 `smiles, FDA_APPROVED, CT_TOX`。
- 专家知识：解释 ClinTox 数据集的含义；建议用 deepchem 的 ECFP（扩展连通性指纹）做分子特征。
- 标注程序：用 deepchem 自定义 loader 以 ECFP 特征加载训练、测试集，训练 `MultitaskClassifier`，预测后写出 CSV。
- 成功标准：测试集 ROC-AUC ≥ 0.77。

**其他代表任务**（Table 1，p.5）：不同学科的产物和判定方式不同，不能统一当成文本分类。

| 任务 | 子任务 | 成功标准 |
|---|---|---|
| 用 DAVIS 数据集建药物–靶点相互作用模型，为 COVID 重定位抗病毒药 | 特征工程、深度学习 | 前 5 个重定位药物与金标准前 5 一致 |
| 分析睡眠期间的 IMU 数据，计算入睡时间、醒来时间、总睡眠时长 | 计算分析 | 各端点与金标准答案 `math.isclose` |
| 分析多伦多消防站及其服务覆盖，可视化覆盖缺口 | 地图可视化 | GPT-4o 评判得分 ≥ 60 |

依据：[arXiv 2410.05080v2](https://arxiv.org/abs/2410.05080v2)，§2.1、§2.3、Figure 2、Table 1，pp.3–5。
