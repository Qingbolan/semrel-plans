# 具体用例

**用例：电商商品实体匹配**（Figure 1，p.1；§3.2，p.3；§4.2.2，p.5）

两张商品表中各有一行：表 1 "Macbook Pro，$1,999.00"，表 2 "Macbook Air，$899.00"。系统把两行序列化为

`Product A is Title: Macbook Pro Price: $1,999. Product B is Title: Macbook Air Price: $899. Are Product A and Product B the same?`

FM 生成 "No"。少样本时，提示前面还会放入约 10 个人工挑选的已标注记录对作为示范。

**失败案例**（§4.2.2，p.5）：Amazon-Google 中 "pcanywhere 11.0 host only cd-rom xp 98 nt w2k me, manufacturer: symantec, price: NULL" 与 "symantec pcanywhere 11.0 windows, manufacturer: NULL, price: 19.99" 未被正确匹配。作者归因于大量产品专用标识符等行话，模型缺乏语义理解。

**错误检测示例**（Figure 2，p.2）：提示为 "Is there an error in Country?"，少样本示范 "Country: USA, City: Miami? No"、"Country: Spain, City: Paris? Yes"，待判输入 "Country: England, City: Kyoto?"，期望输出 "Yes"。

阅读者分析：这些例子体现的是逐记录对/逐单元格调用 LLM 的"语义过滤/判断"算子形态；原文没有涉及 blocking 后候选对数量带来的调用成本规划。

依据：Figure 1–2、§3.2、§4.2.2，PDF pp.1–3、5。
