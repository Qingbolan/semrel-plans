# 具体用例

论文用电影数据集说明歧义和派生属性（§3.2–3.3，PDF pp.4–5）：

1. 用户输入“Correlate budget, gross, and rating”。数据中“rating”可指 `Content Rating`、`Rotten Tomatoes Rating` 或 `IMDb Rating`。按提示中的歧义规则，模型为每种解释各生成一张图，并在 `attributeMap` 中记录“rating”对应的候选属性。
2. 对欠指定查询，提示要求按检测到的属性类型推断最合适的任务，再按任务 JSON 中的推荐生成图表。
3. 用户可以接着追问，例如增加一个属性或替换图表类型，此时把上一轮规格附在提示末尾，模型按追问分类修改规格。
4. 论文也记录了失败方式：查询“Show total profit across genres”时，y 轴标为“Total profit”，实际却用了 `Worldwide Gross` 字段，图表会误导用户。

这个例子说明中间规格的价值在于可以检查。用户或程序能对照 `attributeMap` 与 Vega-Lite 的实际字段，发现标签与字段不一致（阅读者分析）。

依据：§2.1.3、§3.2–3.3，PDF pp.2、4–5。
