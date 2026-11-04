# 具体用例

**IPF 急性加重事件的检索与网络化**（pp.10–11、19）：语料中 ‘Exacerbation acute’ 作为 Biological_process 触发词出现 72 次，其中 49 次 Theme 为 IPF；‘surgical lung biopsy’（Artificial_process）作为 Cause 仅出现 1 次。‘Disease Progression’ 出现 35 次，其中 IPF 作为 Theme 9 次。

结论部分设想的使用方式（p.19）：用此语料训练的文本挖掘系统，从大量文献中抽取与急性加重、进行性呼吸衰竭或炎症—纤维化相关的分子，画出它们的关系，并进一步找出上游调控分子，以辅助寻找治疗方法。

一个标注层面的例子：Regulation 事件以诱导者为 Cause、作用对象为 Theme；`disorder` 论元把例如“IPF 中某基因表达上调”与普通（非疾病相关）基因表达事件区分开（Fig. 1e–j，pp.3–5）。

若在本项目中把这类语料用于语义抽取或过滤查询，查询单位应是摘要内的事件结构（触发词+论元+疾病上下文），并要考虑事件抽取 F1 只有约 45 的现实上限；本文没有提供任何查询级或问答式评测（阅读者分析）

依据：Results and discussion、Conclusion、Fig. 1，PDF pp.3–5、10–11、19。
