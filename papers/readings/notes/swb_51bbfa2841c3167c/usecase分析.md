# 具体用例

Figure 4（PDF p.4）的例子："Mary walked across the garden. She called for John. He stopped working, and they left together."

- walked(e1)、called(e2)、left(e3) 是有界事件 [B]，依次放在时间线位置 1、2、3。
- working(e4) 标为 {U]：右端点已知（在 Mary 呼叫时停止），左端点不明。它以 e2 为锚点，持续到呼叫时，并延伸到此前某个未指定时刻。
- John 在 Mary 穿过花园时是否已在工作，属于世界知识推断，不在事件顺序标注范围内。

转换为 TimeML 时，e4 与 e2 之间可确定包含关系；与 e1 之间因左端不明，按附录 B 的规则映射为 vague（阅读者分析：此处按附录 B 规则推得，原文未逐条列出该例的转换结果）。

Figure 5 的分支例子：John 读过书（e5）发生在看电影之前，但不知是否在回到 Boston 之前，因此放到挂在电影事件上的 <] 分支。作者指出，是否借常识把读书放到整段观影序列之前，是重要的分歧来源（脚注 7，PDF p.5）。

依据：§3.1–3.3、附录 B，PDF pp.3–5、15–16。
