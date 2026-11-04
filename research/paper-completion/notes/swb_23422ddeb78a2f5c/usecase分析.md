# 具体用例

**用例（原文 Figure 1 与 §3.2 示例）**：案例描述“Alice 和 Bob 于 1993 年 1 月 24 日结婚……”，提示“第 7703(b)(3) 条适用于 Alice 在 2018 年维持其住所”。系统需判断蕴含或矛盾。另一类问题是“Alice 2017 年应缴多少税？”，需要综合全部法条并做算术。

**符号路径**：事实被转写为 `marriage_(alice_and_bob).`、`agent_(alice_and_bob, alice).`、`start_(alice_and_bob, "1993-01-24").` 等谓词，问题转为 `s7703_b_3(alice,home,2018).` 或 `tax(alice,2017,Amount).` 查询（§3.2，Figure 3，p.4）。

**神经路径**：BERT 输入 `[CLS] + s + [SEP] + q + c + [SEP]`，在 [CLS] 上做 sigmoid 分类；数值题因法条超长，只输入 `[CLS] all [SEP] + q + c + [SEP]` 并回归 μ+σθ·r（§5.1）。

阅读者分析：这一用例展示了“自然语言规则 + 结构化事实 + 精确计算”的组合。若要用语义算子处理此类工作负载，需先把事实抽取为关系（人物、婚姻、收入、时间），再由可执行规则计算；论文证明了手工转写后可 100% 求解，但没有评测自动抽取的准确率。

依据：[NLLP@KDD 2020，CEUR Vol-2645 paper5，8 页](https://ceur-ws.org/Vol-2645/paper5.pdf)，§2–3、§5.1、Figures 1、3，PDF pp.2–5。
