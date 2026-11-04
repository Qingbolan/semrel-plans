# 工作负载

| 赛道 / 测试 | 内容 | 命名类型 | 对比系统数 |
|---|---|---|---|
| Conference | 7 个会议本体两两对齐，共 21 个匹配任务；参考对齐用公开的 ra1-M3（含类与属性映射） | Type 1（有意义的名字） | OAEI 2022/2023 共 15 个系统 |
| Anatomy TC1 | 小鼠解剖 ↔ 人体解剖，含大量平凡对应（标签相同） | Type 2（编码） | 12 |
| Anatomy TC2 | 同上，但从 R 和 A 中都去掉平凡对应，只评非平凡对应 | Type 2 | 12 |
| MSE TC1 | MaterialInformation 片段 ↔ MatOnto；参考对齐中故意含包含关系 | Type 1 | 4 |
| MSE TC2 | 完整 MaterialInformation ↔ MatOnto，大量缩写（如 Au=Gold） | Type 1 | 4 |
| MSE TC3 | 完整 MaterialInformation ↔ EMMO（基于 BFO 的上层本体） | MI 为 Type 1，EMMO 为 Type 2 | 4 |

来源：§5.2，pp.8–9。正文未给出各本体的实体数和参考对齐规模；Conference 每个对齐可用的 trial 对应"通常少于 10 个"，作者把它视为少样本任务（§5.2.1，pp.8–9）。

**评测单位**：一条等价对应。用 Precision=|A∩R|/|A|、Recall=|A∩R|/|R| 和 F1 计算（§5.1，pp.7–8）。

**运行设定**：主结果用 gpt-4o，similarity_threshold=0.90，top@k=3，单次运行（§5.2，p.8）。消融中比较了 10 个 LLM（4 个 API 模型、6 个约 7–9B 的开源模型，见 Table 1，p.5）和 3 种 OpenAI 嵌入（§6.1.3，p.10）。作者说明只用 TBox 数据集；出于隐私考虑未评测 ABox（§8，p.12）。

依据：§4–§6、§8，pp.4–12。
