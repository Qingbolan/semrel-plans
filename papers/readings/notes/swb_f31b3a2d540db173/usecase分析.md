# 具体用例

**原文示例**（Tables 4、6，PDF pp.6–7）：句子"There shall be a horizontal landing with a length of at least 1,500 millimetres at the lower and upper end of the ramp."（坡道上下两端应设长度不少于 1,500 毫米的水平平台。）

| 实体对 | 关系 |
|---|---|
| `horizontal`（quality）— `landing`（object） | `selection` |
| `landing` — `length`（property） | `part-of` |
| `length` — `1,500 millimetres`（value） | `greater-equal` |
| `landing` — `lower and upper end`（property） | `necessity` |
| `lower and upper end` — `ramp`（object） | `part-of` |

另一例"The gradient of the passageway located in an outdoor space may not exceed five per cent."被标为：gradient part-of passageway，passageway part-of outdoor space，gradient less-equal five per cent。

**下游场景**（Background p.1）：把这些实体—关系图转为机器可读规则后，ACC 工具即可在 BIM 模型中查找所有坡道，检查平台长度是否不小于 1,500 毫米。原文只提供到实体—关系这一步。

阅读者分析：在语义查询的语境下，这相当于对法规句做结构化抽取，产出 (对象, 属性, 比较符, 数值) 元组，再与建筑数据做连接比较；`value` 中的单位和数量词（如 "five per cent"）需要额外归一化，数据集本身不提供归一化后的数值（阅读者分析）。
