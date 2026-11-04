# 工作负载

**LOCO-Annotations**（§IV-A，PDF p.6）：在 MVTec LOCO 基础上重新标注，共 2,908 张图像，其中训练 1,772 张、测试 1,136 张。覆盖 5 个类别：breakfast box、screw bag、pushpins、splicing connectors、juice bottle。

| 特点 | 说明 |
|---|---|
| 测试集范围 | 只标注逻辑异常，不同于 MVTec LOCO 同时包含结构与逻辑异常 |
| 标注格式 | 每张图配 JSON：像素级对象分割 + `Anomaly Type: Specific Reason` |
| 异常类型 | Quantity、Size、Position、Matching |

原文没有给出每个类别的图像数、正常/异常比例，也没有说明训练集 1,772 张在 LogiCode 中如何使用（阅读者分析：从方法看，正常样本用于专家归纳规则）。

**评测重复次数**（§IV-C，PDF pp.7–8）：
- 二分类：每个类别 5 组实验取均值；
- 代码生成：每个类别分别生成 20 次代码；
- 推理准确率：每个类别取 5 组成功执行的代码。

所有实验使用 GPT-4，原文未给出具体模型版本、温度或调用成本（§IV-C，PDF p.7）。
