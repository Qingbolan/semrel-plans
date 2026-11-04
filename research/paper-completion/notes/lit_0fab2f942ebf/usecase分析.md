# 具体用例

**论文示例**（Fig.1，p.1）：指令为"删除第五列中以数字开头的元素，然后把该列所有元素大写；统计包含 'Q2' 的元素数，存入 B4"。

1. **Manager** 拆成三个子任务：S1 删除第 5 列以数字开头的元素；S2 将第 5 列大写；S3 统计含 "Q2" 的元素存入 B4。
2. **Action Agent** 逐步发出调用：
   - S1：`ApplyFormulaColumn(col=5, formula="=IF(ISNUMBER(VALUE(LEFT(E{r},1))), \"\", E{r})")`
   - S2：`ApplyFormulaColumn(col=7, formula="=UPPER(G{r})")`——列号写错（应为 5）。
   - S3：`SetCellValue("B4", "=COUNTIF(E:E, \"*Q2*\")")`
3. **Reflection Agent** 每步后重新读取保存的工作簿：S1 判定通过；S2 判定"第 7 列被大写，第 5 列未变"，给出修正 `ApplyFormulaColumn(col=5, formula="=UPPER(E{r})")` 并要求重生成。

这个例子体现了"步级反思"：判断的是刚执行动作是否达成其自述目的，且被拒的步骤仍保留在历史中（因为它已经执行并保存）（§3，p.2）。

依据：Fig.1，p.1；§3、Algorithm 1，p.2。
