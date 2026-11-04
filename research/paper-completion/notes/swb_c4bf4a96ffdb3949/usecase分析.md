# 具体用例

**编码员工作流**（§3.3、§3.1，PDF pp.3–4）：

1. 在 INCEpTION 中打开一份住院病历的全部合规记录。
2. 从头阅读，高亮某个片段（如出院小结中的 "hypotension"），并分配 ICD-10 编码。
3. 编码完成后，对照 MIMIC 原 ICD-9 编码及其可能的 ICD-10 映射复查遗漏；若因缺少手术记录等原因找不到证据，就在编码报告中注明。
4. ICD-10 编码随后自动映射到 ICD-9。

**模型侧**（§6.3，PDF p.9）：监督注意力模型对单 token 证据（如 "hypotension"、"asthma"）的精确片段匹配命中 30/33（90.9%）。多 token 证据只命中 3/17（17.6%），常只抽出 "peptic" 而非 "peptic ulcer disease"，只抽出 "compartment" 而非 "compartment syndrome of left lower extremity"。

阅读者分析：这对应"对长文档做多标签分类，并为每个标签给出可追溯片段"的语义抽取负载；若在项目中使用，需要区分充分证据与完整证据两种标注口径。
