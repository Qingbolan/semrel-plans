# 工作负载

**主数据集：MVTec LOCO AD（只用逻辑异常部分）**（Dataset and Metrics、Table 1，PDF p.6）：5 个类别——Breakfast Box、Juice Bottle、Pushpins、Screw Bag、Splicing Connector；异常包括缺件、多件、颜色与物体不匹配等。原文未给出每类测试图像数。

**辅助数据集：MVTec AD**：重点看 capsule、pill、transistor、toothbrush 四个"含朴素逻辑异常"的物体类别，另有 carpet、grid、leather、tile、wood 等纹理类别（Table 2、Table 6，PDF pp.6–7）。

**设置**：
- 单样本：每类只用一张正常训练图像，完全免训练（Experiments，PDF p.5）；
- 每类重复 5 次实验，报告均值与标准差（Table 1 标题）；
- AVLM 为 GPT-4o、LLaVA 1.6、LLaVA 1.5，部署细节在附录 A.4（本 PDF 未包含）。

**计数探针**（Text Feature Extraction，PDF p.4）：从 CountBench 随机取 250 张；自建 UniformBench 150 张同质物体图像（棋盘上的兵、篮中的啤酒瓶、围棋棋子）。

**指标**：AUROC 与 F1-max；逻辑推理分支只报告 F1-max（Table 3）。
