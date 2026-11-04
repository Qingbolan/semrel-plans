# 具体用例

论文给出的具体记录示例：BlackBerry 2022 年报告中，2019 年 Scope 1 排放为 6748 metric tons CO2e，构成一条“报告 × 年份 × scope”记录。Table 1 的正例是“Allianz 集团按 GHGP 的 Scope 1 总排放 2019 年为 42 kt CO2e”；虚构的反例“南亚工厂排放较上年下降 2%”在四项规则上都不合格（非全公司、非 scope 边界、非绝对量、非总量）。

具体流程：报告按页向量化，以查询 “What are the total CO2 emissions in different years? Include Scope 1, Scope 2, and Scope 3 emissions if available.” 取余弦相似度最高的 3 页及其前后页，交给 GPT-4 输出各 scope、各年份的数值和单位（Fig.4），再由正则解析成表；非专家逐行勾选对错、选择错误原因、补录遗漏值。

阅读者分析：对本项目而言，这可视作“对长 PDF 做语义抽取并输出结构化表”的工作负载，带有可操作的判定规则和页码证据；若派生查询（如按 scope 聚合、跨年比较），属于项目派生任务，原文未评测。

依据：[Scientific Data 12:1497 (2025)，9 页](https://www.nature.com/articles/s41597-025-05664-8)，Methods（Fig.4、Table 1，pp.4–5）、Data Records（p.7）。
