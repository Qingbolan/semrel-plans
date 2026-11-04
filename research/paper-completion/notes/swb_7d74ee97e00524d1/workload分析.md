# 工作负载

论文使用三个数据集（§4.1，PDF p.5）：

| 数据集 | 图像数 | 类别 | 异常类型 |
|---|---|---|---|
| MVTec LOCO | 3,644 | 5 类（breakfast box、juice bottle、pushpins、screw bag、splicing connectors） | 逻辑 + 结构 |
| MVTec AD | 5,354 | 10 个物体类 + 5 个纹理类 | 结构 |
| VisA | 10,821 | 12 类 | 结构 |

三者都为测试图像提供像素级标注。

**划分与设置**（§4.2，PDF p.6）：采用各类别预定义的训练/测试划分。MVTec AD 和 VisA 没有验证集，作者取训练集的 10% 作为验证集，用于分数标准化。所有图像缩放到 256×256；按 EfficientAD 的方案训练 70,000 次迭代；组成图以 50% 概率加入合成异常；所有数据集和类别使用同一组超参数。

**组成图生成器**：SAM-HQ-h 加 DINO ViT-B/8；UNet 用 AdamW 训练 15 个 epoch，学习率 5e-4，批量 8。

阅读者分析：论文未给出 LOCO 各类别的训练/测试图像数，需要查阅 MVTec LOCO 原论文。
