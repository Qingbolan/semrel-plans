# 具体用例

**芝加哥食品检查（CFI）**（Figure 2，p.3）。目的：“Identify the main facility types that have been inspected at the highest risk level.”

在原始表上执行该目的，得到的答案是“SCHOOOL, RESTUARANT, school, GROCRY STORE”，原因是拼写错误、大小写不一致，风险等级写法也不统一（如 “Risk 1 [High]”）。

清洗过程：
1. 选出 Facility Type、Risk 两列；
2. 质量报告指出准确性和简洁性为 False；
3. 生成 `mass_edit`，参数如 `{"from": ["SCHOOL","SCHOOOL"], "to": "School"}`；
4. 迭代后得到正确答案“SCHOOL, RESTAURANT, GROCERY STORE”。

**§7 案例**（pp.8–9）：目的是找出在最近日期被多次检查的设施类型。对 Facility Type 列，人工工作流用了 trim、upper 和 3 次 mass_edit；Llama 3.1-8B 用 trim 和 2 次 mass_edit；Gemma 2-9B 只用 1 次 mass_edit。三者都得到答案“RESTAURANT”。

阅读者分析：这说明工作流维度的 F1 低，并不一定意味着清洗失败；不同操作组合可以达到同样效果。

依据：[arXiv:2412.06724v3，15 页](https://arxiv.org/pdf/2412.06724v3)，Figure 2，PDF p.3；§7、Figure 4，pp.8–9。
