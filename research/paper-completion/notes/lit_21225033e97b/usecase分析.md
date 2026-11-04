# 具体用例

附录 A.3 Figure 7 的提示：data.csv 是意大利同一产区葡萄酒的化学分析，含 Types 等 14 个属性。任务是画出 Types 与其他属性的堆叠柱状图，处理后数据存为 `processed_data.csv`，图存为 `stacked_bar_chart.png`。

其中一条 TFC 为：T1“数据清洗与预处理”；F1 Data Completeness；C1 读取真值文件与模型输出的 `processed_data.csv`，比较两者非空单元格比例是否完全相等，返回布尔值。

可视化部分另由 F2（Plot Validity）、F4（图像文件是否存在）和 VLM-as-a-judge（GPT-4o-mini）评价（§4.2）。

这种检查输出文件属性是否等于真值的评分，只验证可观测的中间结果，不评价分析结论本身（阅读者分析）。

依据：附录 A.3 Figure 7、§4.2，PDF pp.5–6、11–12。
