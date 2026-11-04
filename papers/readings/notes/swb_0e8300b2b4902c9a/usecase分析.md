# 具体用例

**四种因果标签示例**（§3.4、Figure 1，PDF p.5）：句子 "The ouster of Morsi and the subsequent suppression of the Brotherhood has enraged the groups members and led to a spate of scapegoating attacks by Muslim extremists" 被标为：

| 事件对 | 标签 |
|---|---|
| ouster → enrage | BEFORE/CAUSES |
| ouster → attacks | BEFORE/PRECONDITION |
| suppression → enrage | OVERLAP/CAUSES |
| suppression → attacks | OVERLAP/PRECONDITION |

**两遍标注示例**（§3.5、Figures 2–3，PDF p.6）："their escape from prison during the uprising that toppled his predecessor, Hosni Mubarak"。第一遍标实体与 SET/SUBSET、APPOSITION（predecessor 与 Hosni Mubarak）；第二遍标 uprising CONTAINS escape，uprising 与 toppled 之间为 BEFORE/CAUSES。

**共指支持的时序推理**（§3.3，PDF p.5）：若某次 "chant" 是 "protest" 的子事件，而 protest 的某个提及在激起它的 "speech" 之后，则 chant 与 speech 的关系可推出，不必另标。

阅读者分析：这类标注可支撑"哪些事件导致了 X、在 X 之前发生"等跨句事件图查询，但原文没有评测查询或问答任务。
