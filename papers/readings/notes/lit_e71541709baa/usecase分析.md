# 具体用例

原文 Fig.3（PDF p.8）的定性示例之一来自 AITQA 合成图表。问题为“What was the peak share price for ALK in 2016?”，回答为“The peak share price for ALK in 2016 was $91.88.”。

ChartLens 的处理流程：
1. 用 Otsu 二值化、轮廓过滤和 SAM 掩码切出每根柱，并打上编号。
2. 把带标记图像、少样本示例和 QA 对交给 GPT-4o。
3. GPT-4o 先验证回答是否与图表一致，再输出支持回答的柱编号。
4. 输出的柱区域与真值区域按 IoU ≥ 0.9 匹配，计算 P/R/F1。

同一图中的其他例子有饼图问题“What's the share of top 3 countries?”，以及“经济活动儿童在服务业中最高与次高比例之差”的柱状图问题。

作者观察到，零样本 GPT-4o 用文本坐标表达框，定位不稳；LISA 和 KOSMOS2 倾向于框住整个饼图或大片区域，对问题不敏感（§7，PDF p.8）。
