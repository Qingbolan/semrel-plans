# 具体用例

论文 Figure 5 的完整评测流程（PDF p.7）使用泰坦尼克乘客文件 `test_ave.csv`：

1. **问题**：新建特征“FamilySize” = “SibSp” + “Parch”，再计算它与“Fare”的 Pearson 相关系数。
2. **约束**：按行求和生成新列，计算相关系数前不做任何额外清洗或预处理。
3. **智能体执行**：说明思路后写代码，用 pandas 读取 `/mnt/test_ave.csv`、相加两列、调用 `corr()`；沙箱输出 0.20510382556972825；智能体回答“约 0.205，弱正相关”。
4. **重新格式化**：GPT-3.5 按格式要求（保留两位小数、取值在 -1 到 1 之间）输出 `@correlation_coefficient[0.21]`。
5. **判分**：正则抽取后与标签 `@correlation_coefficient[0.21]` 精确匹配，判为正确。

Figure 1 是另一个例子：在 `Happiness_rank.csv` 上对 GDP per capita 与预期寿命做线性回归，答案包含 R² 与拟合好坏两个子问题，`{@coefficient_determination[0.67], @model_fit["poor fit"]}`（PDF p.2）。

舍入位数、取值范围等都写在格式要求里，因此判分对数值精度敏感；多子问题题目必须全部答对才算正确（阅读者分析）。

依据：Figures 1、5，附录 P，PDF pp.2、7、14。
