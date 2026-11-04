# 具体用例

**原文示例**（Figure 2，§3.1，pp.4–5）：

> “This is a dataset featuring sensor readings from water pump, aimed at predicting machine operational status (normal or faulty). Your tasks include conducting a comprehensive data analysis encompassing correlation analysis, causal inferences, data exploration, anomaly detection, and feature engineering.”

**任务图**：LLM 把需求拆成数据探索、相关性分析、异常检测、特征工程、模型训练、模型评估、可视化等任务节点，节点间有依赖边。

**动作图**：以可视化任务为例，它被拆成三个动作，其中混淆矩阵由 sklearn 计算，需要使用前面训练任务产生的预测结果（§3.1，p.5）。

**失败时的修正**（Figure 3，p.7）：某次执行中任务 3.3 失败；重生成的任务图保留已成功的任务，用新的 3.3 替换原任务，并新增任务 4.1、4.2、4.3 和 5。前缀匹配找到分叉点后，分叉前的任务结果直接复用。

**其他类型任务**（§4.2，附录 F.1）：开放任务包括 OCR、网页搜索与爬取、邮件自动回复（需登录邮箱）、网页模仿、图像去背景、文生图、图转 HTML、小游戏生成。它们需要的输入资源和工具各不相同，不能用一个“无数据环境”概括。

阅读者分析：水泵示例是展示性的工作流，论文未给出该例的量化结果；量化结论来自后述四类评测。

依据：[arXiv 2402.18679v4](https://arxiv.org/abs/2402.18679v4)，§3.1–3.2、Figure 2–3、§4.2，pp.4–9。
