# usecase

原文 Figure 1a 的贷款风控任务（PDF pp.1–3）：输入 input.csv（宽表格式的用户贷款行为记录），要求以 apply_date 为月份，对全部特征逐月计算统计量与预测指标（缺失率 … KS），缺失值填 −1，输出 output.csv（列：col、date、各指标）。标准解先预处理特征与标签列，再逐月逐列计算缺失率并实现 KS（按分数排序后的累计好坏样本差最大值）。评测函数用归一化 MSE 比较逐月、逐用户层面的指标。标注技能包括 “Handling Missing Data” 与 “Efficient Data Structures and Algorithms”。

图中展示的失败：Smolagents 把已填为 −1 的值当缺失计算（缺失处理技能误用）；DA-Agent 用逐阈值循环计算 KS 导致单步超时（效率技能误用）。这说明任务描述中的歧义（缺失值是否已预先填充）和大规模数据都会影响结果（§1，PDF p.1）。

阅读者分析：该用例体现的是“数据处理 + 统计指标计算”型多步任务，评分依赖输出表的数值匹配；若项目要把它映射为语义算子工作负载，需要保留输出 schema、容差和缺失值约定，否则不可比。

依据：[arXiv:2607.01647v1，14 页](https://arxiv.org/abs/2607.01647)，§1、Definition 2.2、Figure 1，PDF pp.1–3。
