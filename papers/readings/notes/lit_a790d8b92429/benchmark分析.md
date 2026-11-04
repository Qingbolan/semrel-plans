# 评测与边界

**基线**：(1) GPT-4o + Prompting（直接提示生成标准化代码）；(2) Cocoon（基于 LLM 的一次性数据清洗系统，用官方 Colab notebook 运行，只评测其标准化能力）。RetClean 因依赖用户提供的检索数据源而未纳入（§4）。所有方法使用 gpt-4o-2024-08-06；实验在 MacBook Pro M1、16GB 内存上进行。

**指标**：所有列平均的单元格级匹配率（标准化结果与真值表逐单元格相等的比例），以及延迟（秒）。

**实验 1（Flights 日期时间标准化，Table 1）**：

| 系统 | 单元格匹配率 (%) | 延迟 (s) |
|---|---|---|
| GPT-4o | 22.0 | 19.76 |
| Cocoon | 21.5 | 636.62 |
| CleanAgent | 42.5 | 29.57 |

作者解释：CleanAgent 约为两基线的 2 倍，归因于类型专用 API；Cocoon 延迟高是因为它为所有列生成一次性 SQL，无法针对特定列（§4）。

**局限（阅读者分析）**：单一数据集、单一列类型；真值由 GPT-4o 生成且未人工核验；未报告重复运行次数或方差（LLM 输出有随机性）；未做消融（如去掉 agent、只用 API）；42.5% 的绝对值仍较低，论文未分析失败单元格。论文本身没有局限章节（阅读者分析）。

依据：[Qi, Miao & Wang，VLDB 2025 Workshop DATAI，4 页](https://www.vldb.org/2025/Workshops/VLDB-Workshops-2025/DATAI/DATAI25_8.pdf)，§4，Table 1，p.3。
