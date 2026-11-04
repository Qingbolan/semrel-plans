# 贡献与评价

原文声称的贡献（§1、§3、§7，PDF pp.2、4–5、14）：

1. RoBIn 数据集，作者称是第一个公开的 RoB 数据集（GitHub phdabel/robin，经 Cochrane 许可发布）；
2. 作者称首个基于 Transformer 的 RoB 评估模型：RoBIn_Ext（Biomed RoBERTa 编码器 + 起止位置预测 + 分类器）与 RoBIn_Gen（BioBART 编码器-解码器，解码输出平均池化后接二分类，损失为 L_G + L_BCE）；
3. 与 SVM、LR 及三种 LLM 的 0/1/few-shot 比较。

阅读者分析：

- 数据集公开是最实在的贡献。远程监督流程（索引句子、余弦相似度 >0.5 取最高匹配）与 Marshall et al. 的思路一致，作者也承认沿用了已有技术。
- RoBIn_Ext 的分类器是用金标证据单独训练、再作用于抽取证据的（§5.1，PDF pp.8–9），不是端到端联合模型。
- SVM/LR 的输入是"问题 + 期望答案"（§6.2，PDF p.11），即金标证据；LLM 则需自己从上下文找证据。三类系统的输入条件不同，比较不完全对等。
- "超越 SOTA"指的是本数据集上的基线，作者也说明不能与 Table 1 中先前工作直接比较（PDF p.14）。
