# 具体用例

原文 Figure 2（PDF p.4）给出一个解析示例：驳回书写道"权利要求 1–2 依 35 U.S.C. 103 被驳回，因相对于 Rebmann（US Pub No 2018/0179985）结合 Wang 等（US Pub No 2018/0298842）显而易见……'travel-permitted region setting unit 25 is configured to set…' 见 ¶[0038]–¶[0039]、[0074] 与 Fig. 5 步骤 S501–S517"。

GPT-4o 将其转为每条权利要求一个 JSON：`isRejected: True`、`sectionCode: 103`、`citedPatents` 中 `patentNum: "20180179985"`、`text: [38, 39, 74]`、`img: [5]`，以及另一件被引专利与理由文本。

这一条记录可以派生三道题：
- PAR4PC：给出权利要求 1 和 8 个候选，应同时选中 Rebmann 与 Wang（§103 可多选）；
- PI4PC：在 Rebmann 的 5 个候选段落中选出 ¶38 / ¶39 / ¶74 这类被引段落；
- NOC4PC：给出权利要求和被引段落，判定为 "103"。

阅读者分析：在项目语境中，这对应"对每条权利要求，在文档集合里找证据文档→定位证据段落→做三分类判定"的多步语义查询链；原文把三步作为相互独立的基准分别评测（§3，p.5），并未评测串联后的误差累积。
