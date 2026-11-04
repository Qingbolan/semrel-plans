# 具体用例

**原文示例**（Figure 1，p.2）：

> “An election has been held in Excelstan. Excelstan is a small country including 9 Districts. There are 1000 voters. Each voter is assigned a District Code based on where they live. The District Code is a number between 105-194 and determines what District the voter votes for.”

输入包括：一张区号与选区的对照表（Table 1）、一个记录选民信息及其所投选区的 Excel 文件，以及问题“How many voters are there in the Delta District?”，选项 A. 113 到 E. 117。

**agent 的工作流程**：读题与数据文件 → 生成可执行代码（按区号范围把选民映射到 Delta 选区并计数）→ 根据执行结果给出答案：“There are 115 voters in Delta district, the answer is C.” → 评测函数把答案与标准答案做语义比较。

**建模任务的对应流程**（§2.2）：读竞赛描述、字段说明、训练集和测试集，训练模型，输出与示例提交文件格式相同的预测文件，再由执行脚本按竞赛原指标打分。工具可以用 Python 或 Excel，benchmark 不限定唯一解法。

阅读者分析：这个例子只需一次查表和计数；实际 ModelOff 题目平均有约 750 词的背景和多张工作表，难度远高于此例。

依据：[arXiv 2409.07703v2](https://arxiv.org/abs/2409.07703v2)，§1–2、Figure 1，pp.2–6。
