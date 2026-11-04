# 具体用例

原文附录 A.5 的示例 rollout（p.15）：指令为"若 Sheet1!B1 与 Sheet2!B1 相同，则把 Sheet2!D1 填入空白的 Sheet1!D1"。智能体先用 inspect_range 读两个 B1（都是 "124 bent street"），再读 Sheet2!D1（15100），然后用 code_interpreter 写入并重新打开工作簿核对写入值，最后保存 data.xlsx。奖励由验证服务在 Excel 中重算后比对操作区域。

Domain-Spreadsheet 的金融示例（Fig.3，p.7）：在场外衍生品 CSA 抵押品监控场景中，要求在 Summary 表的 B2:B6 填写 Total Posted、Total Received、Net Collateral 等 KPI。

附录 A.6 说明了工具设计的动机：仅有 code_interpreter 时，模型删除列时边遍历边删导致索引错位；用 Python 拼接含 IFERROR(VLOOKUP(...),"") 的公式字符串时转义出错。fill_formula 与 delete_columns 把这些语义交给工具处理。

阅读者分析：该用例的输出是"被修改的工作簿"而非文本答案，评测只看指定区域的单元格值，不评估公式写法或格式是否合理（正文提到可做公式/结构检查，但 A.10 的实际比较只用重算后的值）。
