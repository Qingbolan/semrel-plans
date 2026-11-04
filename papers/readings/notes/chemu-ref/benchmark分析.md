# 评测与边界

使用提及和关系 P/R/F1，并区分 surface 与 atom 共指评分。Table 2 联合模型总体关系 F1=68.6，Table 4 加入 ChELMo 后为 73.1；结果取三次随机运行平均。Table 3 的 oracle mention 设置为 82.1，不能与自动提及检测结果混列。Table 2 bridging 从 70.3 到 71.1，表值相差 0.8 个百分点，正文所写 +1.2 不一致，本解析采用表列值（阅读者分析）。长距离、多先行词和不连续提及仍存在系统性错误。

依据：[EACL 2021, pp.1362–1375](https://aclanthology.org/2021.eacl-main.116.pdf)，§6、Tables 2–4，PDF pp.7–9。
