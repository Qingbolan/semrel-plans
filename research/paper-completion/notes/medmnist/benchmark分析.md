# 评测与边界

比较 ResNet、auto-sklearn、AutoKeras 和二维 Google AutoML Vision；使用 AUC、ACC，实验至少重复三次。论文同时报告逐子集与跨子集平均值；不同 AutoML 方法预算不同，不能只比较一个总分。

Organ 二维切片与三维体块的样本构造不同，原文专门限制直接比较。Usage Notes 明确说明降分辨率后的数据不用于临床应用。

依据：[Scientific Data 10, 41 (2023), DOI 10.1038/s41597-022-01721-8](https://www.nature.com/articles/s41597-022-01721-8.pdf)，Technical Validation、Tables 3–7、Usage Notes，PDF pp.6–8。
