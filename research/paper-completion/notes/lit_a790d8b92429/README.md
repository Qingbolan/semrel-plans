# Qi, Miao & Wang — CleanAgent: Automating Data Standardization with LLM-based Agents

本文是一篇 4 页的工作坊/演示性论文：先提出 Dataprep.Clean，用统一的 `clean_type(df, column_name, target_format)` 接口把单列格式标准化压缩为一行代码（目前 142 个类型函数），再用四个 LLM agent（Chat Manager、Column-type Annotator、Python Programmer、Code Executor）自动完成列类型标注、代码生成与执行重试。

唯一实验在 Flights 数据集的日期时间列上，CleanAgent 单元格匹配率 42.5%，GPT-4o 直接提示 22.0%、Cocoon 21.5%。已阅读全文 4 页。

[原文](https://www.vldb.org/2025/Workshops/VLDB-Workshops-2025/DATAI/DATAI25_8.pdf)

版本：VLDB 2025 Workshop: Data Driven AI（DATAI25_8），4 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| problem | §1，p.1–2 |
| method | §2–§3，p.2–3，Figure 2 |
| evaluation | §4，p.3，Table 1 |
| limitations | 无独立章节；§4 实验设置与 §5–6，p.3–4 |
