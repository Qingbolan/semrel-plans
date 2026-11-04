# 具体用例

**原文用例：Breakfast Box 的逻辑推理（Logic Reasoner，PDF p.5）**

1. AVLM 对查询图像的描述为："盒子左侧有一个 nectarine 和一个 apple，右侧有一些 nuts……"
2. LLM 将其转为图像规格 Σ_0：`left(nectarine,1); left(apple,1); right(nut,irrel)`，其中 irrel 表示数量无关。
3. 正常规格 Σ_norm 由描述"左侧要么有 apple 没有 nectarine，要么有 nectarine 没有 apple；左侧应有两个 tangerine"得到：`(left(apple,1) ∧ left(nectarine,0)) ∨ (left(nectarine,1) ∧ left(apple,0))`、`left(tangerine,2)`。
4. 补全规则：Σ_na 声明 tangerine = mandarin、tangerine ≠ apple；Σ_dca 规定左侧只能出现正常规格中提到的物体；描述中未提到 tangerine，则按默认值补 `left(tangerine,0)`。
5. Prover9 证明 Γ ⊨ ¬Σ_0，判为异常；最小解释为 Σ_a = {left(nectarine,1), left(apple,1)}，因为单独任一项都不导致矛盾。

原文注明此正常描述只是示例，"不一定是原数据集对正常的定义"（PDF p.5）。

**Guided CoT 示例（Fig. 4，PDF p.4）**：对 splicing connector 用普通问题提问时，GPT-4o 错误回答"线缆接在两个连接器的同一位置"；改用 Guided CoT 后，正确回答左侧插在 top、右侧插在 bottom。

阅读者分析：这个模式相当于"VLM 抽取结构化事实 + 符号规则校验"，可类比于在图像集合上执行可解释的语义过滤；其可靠性取决于 VLM 描述的准确度。
