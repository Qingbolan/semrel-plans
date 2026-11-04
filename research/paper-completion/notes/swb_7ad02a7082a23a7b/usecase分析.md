# 具体用例

**用例 1：标注示例（Figure 1，p.2）**

- "Moeller was named CFO in January 2009." 触发词 "named" 为 EMPLOYMENT|START，论元 Moeller（Employee）、CFO（Title）、January 2009（Time）。
- "AbbVie's dividend yield currently stands at 3.9%." 为 DIVIDEND 事件，AbbVie 为 Company，3.9% 为 YieldRatio。
- "American Airlines reports load factor increase in May, shares gain" 同时含 REVENUE|INCREASE 与 SECURITY VALUE|INCREASE 两个事件。

**用例 2：触发词压缩造成的歧义（§5 误差分析，p.7）**

原文 "... organic sales growth projections for this year ..." 中标注的 SALES VOLUME 触发词是 "sales growth"，预处理后只剩 "growth"。而 "growth" 在语料中也常用于 PROFIT/LOSS、REVENUE、EXPENSE 等指标，因此模型难以区分。类似地，"buy" 常是 MERGER/ACQUISITION 触发词，却常被误判为买入/持有/卖出式的 RATING；"Apple made $64.1 billion before taxes in fiscal 2017." 真值为 PROFIT/LOSS，模型预测为 REVENUE。

**用例 3：看似合理的多余预测**："Below is an analysis of Apple's App Store revenue..." 中的 "revenue" 被预测为 REVENUE，但真值中没有，因为它是一个泛指提及，后面紧跟具体事件；作者说明这不是标注质量问题，而是标注方案要求事件具体且相关（pp.7–8）。

阅读者分析：对语义抽取类查询而言，"同一词在不同指标语境下对应不同事件类型"说明只看触发词局部不够，需要更长上下文或事件共指信息，作者也持这一看法（p.7）。

依据：FNP 2020，Figure 1、§5，PDF pp.2、7–8。
