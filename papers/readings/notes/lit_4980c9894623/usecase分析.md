# 具体用例

附录 Fig.17 给出一个作者称仅分治 CoT 能解出的例子（p.23；§3.3 p.4 的说明）：Formula 1 数据库中，问题为"2008 年澳大利亚大奖赛冠军比最后一名车手快多少百分比？"

原文给出的 SQL 用三个 CTE：`time_in_seconds` 用 `CASE WHEN positionOrder = 1` 区分两种 `time` 格式（冠军为完整时长，按时/分/秒换算；其余车手取去掉首字符后的数值），`champion_time` 取冠军秒数，`last_driver_incremental` 取最大名次车手的值，最后计算百分比（Fig.17，p.23）。

阅读者分析：这对应分治 CoT 的"分解子问题 → 子 SQL → 组装"（Alg.1，p.4），但 Fig.17 只展示最终 SQL，未展示该题的具体子问题文本。

**失败用例**：附录 Fig.8 中选择代理挑中 `SELECT DISTINCT T1.*`，而金标准只要 `T1.ID`，属于"错选"（p.17）；Fig.11 中选中的候选语义正确，但因数据列名不一致，执行准确率计 0（p.19）。

阅读者分析：该例说明系统的强项是单库内的复杂计算 SQL，而不是跨表的语义判断。若把 CHASE-SQL 作为语义查询的基线，应注意它依赖 BIRD 的 evidence 提示，Fig.15 就带有 "percentage = DIVIDE(...)" 形式的提示（p.21）。
