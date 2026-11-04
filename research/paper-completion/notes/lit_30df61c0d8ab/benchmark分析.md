# 评测与边界

**实验 1（经典表格数据，Table 2，PDF p.18）**：把 LAMBDA 采用的分析方法交给作者手工用 R 重做，括号内为 R 结果；差异来自数据处理、超参数与交叉验证划分不同（表注）。

| 数据集 | LAMBDA 最佳 | R 最佳 | 指标 |
|---|---|---|---|
| AIDS | 89.67 | 89.62 | 准确率 % |
| NHANES | 100 | 100 | 准确率 % |
| Breast Cancer | 98.07 | 98.25 | 准确率 % |
| Wine | 98.89 | 98.89 | 准确率 % |
| Concrete | 0.2749 | 0.2755 | MSE |
| Power Plant | 0.0315 | 0.0363 | MSE |
| Abalone | 0.4542 | 0.4408 | MSE |
| Airfoil | 0.2528 | 0.2559 | MSE |

原文据此称 LAMBDA 达到与熟练 R 分析师相当的水平（§4.1.1，PDF pp.18–19）。Abalone 最佳行在原表中排版错位（PDF p.18），上表按两列数值读取（阅读者分析）。

**实验 2（高维、缺失、图像、文本，Tables 4–7，PDF pp.20–21）**：这些结果没有其他智能体或人工基线。

- 高维：三个数据集最佳准确率 56.62%、61.23%、70.63%，LAMBDA 一律先做 PCA。
- 缺失数据：Framingham、StuRecord、Heart Disease 最佳 85.35%、61.05%、60.40%；Table 5 中 Heart Disease 的 XGBoost 为 60.71%，高于标注的“Best” 60.40%（阅读者分析）。
- 图像：MNIST 上 CNN 99.19%、Transformer 97.23%。
- 文本：SMS Spam 上朴素贝叶斯 98.39%、BERT（DistilBERT 迁移）99.37%。

**实验 3（知识整合，Table 8，PDF pp.22–23）**：评分 S=1（代码与执行均成功）、0.8（代码对但环境等原因执行失败）、0.5（代码错但执行成功）、0（均失败或超时）。

| 智能体 | PM | NCM | FPNENN |
|---|---|---|---|
| GPT-4 Advanced Data Analysis | 0.80 | 0 | 0 |
| ChatGLM-Data Analysis / OpenInterpreter / Chapyter | 0 | 0 | 0 |
| OpenCodeInterpreter | 1.00 | 0 | 0 |
| DataInterpreter（工具）/ TaskWeaver（插件）/ LAMBDA（知识） | 1.00 | 1.00 | 1.00 |

除自带模型的平台外，其余均用 GPT-3.5 实现；有工具机制的智能体把代码转成工具，没有的则直接放入上下文。

**实验 4（工具与指令不一致，Table 9，PDF pp.23–24）**：在 FPNENN 上要求把 MSE 损失改为 L1，或把编码器 784→200 改为 784→400。TaskWeaver 与 Data Interpreter 直接调用原工具，LAMBDA（Full 模式）识别出不一致并完成修改。每个案例只有一次定性结果。

**实验 5（检查员消融，Table S.2，PDF p.38）**：454 条指令上执行通过率从 68.06% 升到 95.37%。

**边界**（阅读者分析）：无标准基准、无重复运行或方差；R 对照由作者自己完成；知识整合只有 3 个任务，每格单次打分；执行通过率只衡量代码能否运行，不衡量分析是否正确。原文没有独立局限章节，§6 只列出未来方向：接入更多领域大模型、改进界面、支持流数据和多人协作，并计划以课堂用户满意度评估（PDF pp.27–28）。

依据：§4–6、Tables 2、4–9、S.2，PDF pp.17–28、38。
