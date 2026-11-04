# 具体用例

原文 Figure 2 给出 Beer 数据集上的实体匹配用例（PDF p.4）：

- **系统消息**：要求模型忠实回答用户问题（推理版要求给出详细解释）。
- **任务描述**：判断下面两个 Product 是否相同，需仔细比较所有属性。
- **注入知识**：缺失值（N/A 或 "nan"）不应作为判断依据。
- **实例内容**：Product A `[name: "Sequoia American Amber Ale", factory: "Wig And Pen"]`；Product B `[name: "Aarhus Cains Triple A American Amber Ale", factory: "Aarhus Bryghus"]`。
- **问题与格式**：A 与 B 是否为同一 Product？从 [Yes, No] 中选择。
- **答案**：任务版直接输出 No；推理版说明名称不同、厂家不同，最后单独一行给出 `Final answer: No`。

推理时用户可进一步做特征工程，例如在 Beer 上只保留 name 与 factory、忽略 style 与 ABV，并可写成数据集特定知识放进提示；也可以加少样本示例，或用 vLLM 前缀缓存批处理共享前缀的实例（§4，PDF p.5）。

这一用例与语义算子中的“成对语义匹配/语义连接”在形态上一致——每次对一对记录输出布尔判断。原文建议先用阻塞（blocking）缩小候选，再交给 Jellyfish 判断（§5.7，PDF p.9），这说明它适合作为匹配算子的逐对判定核心，而非全表连接的完整执行方案（阅读者分析）

依据：§3.2、§4、§5.7、Figure 2，PDF pp.4–5、8–9。
