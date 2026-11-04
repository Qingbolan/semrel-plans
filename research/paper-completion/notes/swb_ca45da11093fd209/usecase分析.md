# 具体用例

**用例：合同条款审查（cuad_audit_right）**。律师需要判断一份合同中某条款是否赋予一方审计对方账簿、记录或场所的权利。LegalBench 把 CUAD 原本的长文档片段抽取任务改写为二分类：

- 提示：“Does the clause give a party the right to audit the books, records, or physical locations of the counterparty to ensure compliance with the contract?”
- 输入条款：“We shall have the right at all times to access the information system and to retrieve, analyze, download and use all software, data and files stored or used on the information system.”
- 输出：Yes

论文报告，在 38 个 CUAD 条款任务上，GPT-4、GPT-3.5、Claude-1 的平均平衡准确率均 ≥88%，说明短条款二分类对大模型较容易；但输入变成 1–2 页的供应链披露时，三者平均降到 74–75%，MAUD 并购协议多选题中 GPT-4 只有 47.8%。

对语义过滤类查询，这一对比提示“条款级短文本 + 是/否判断”与“长文档 + 多选”是难度差异很大的两种负载；但 LegalBench 的输入是预先切好的条款，不包含从整份合同中定位条款的步骤（阅读者分析）。

依据：§3.2，p.6；§4.1，p.7；§5.3，p.10。
