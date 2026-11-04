# 具体用例

问题“2023 年涉及 Cessna 飞机的所有事故的经纬度”在 Luna 中被规划为一个 queryDatabase（按年份与机型过滤元数据）接一个 llmExtract（从文本抽取经纬度）。界面显示 JSON 计划和对应的 Sycamore 代码，用户可以编辑后重跑，也可以逐个算子查看流出的记录并链接回原 PDF；之后还能追问“那么没有严重损坏的事故呢”或“只显示加州”。

另一个 ETL 用例（Figure 4–5）：读取 NTSB PDF，partition(DocParse())，用 gpt-4o 按模式 {us_state, probable_cause, weather_related} 做 llmExtract，再 explode 为块并嵌入，最后写入数据库供查询。

阅读者分析：这是“先缩小候选、再在候选上调用 LLM 抽取”的典型语义查询计划，适合映射为语义 filter/extract/aggregate 算子组合；但原文没有给出该类计划的成本或延迟数字。

依据：[arXiv:2409.00847v3，CIDR 2025，10 页](https://arxiv.org/abs/2409.00847)，§5.2、§6.2、Figures 4–6，pp.5–7。
