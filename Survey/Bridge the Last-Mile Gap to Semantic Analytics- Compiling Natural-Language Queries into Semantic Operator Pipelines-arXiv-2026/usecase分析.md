# 具体用例

**原文示例**（Figure 1–2，§1、§3.3，pp.1–5；HybridQA 题目）：

> “How often does the folk festival in the South Moravian city with fewer people than Boskovice but more than others take place?”

数据：一张“南摩拉维亚城市人口”表（Rank、City、District、Population），以及按城市组织的 Wikipedia 段落。

| Rank | City | District | Population |
|---|---|---|---|
| 1 | Brno | Brno-City | 380,681 |
| 2 | Hodonín | Hodonín | 24,065 |
| 3 | Boskovice | Blansko | 11,622 |
| 4 | Kyjov | Hodonín | 11,218 |

**Phase A**：“Boskovice”是 matched（表第 3 行）；“South Moravian”是 topical（表标题，不能做过滤常量）；“folk festival”是 absent（表里没有，需去文本中找）。

排名推断“比 Boskovice 少中最多”锁定第 4 行，City = Kyjov、District = Hodonín 成为桥接实体，对应段落 `/wiki/Kyjov`（“famous for its folk festival 'Slovácký rok' held every four years”）。

**Phase B**：三步计划：过滤表中人口低于 11,622 的城市 → 把匹配城市与描述民俗节的段落 join → 聚合提取节日举办频率。

**Phase C**：查参考文档 Layer 2 中 `Compose(TextQ, TableQ)` 的示范流水线，代入谓词，生成 Palimpzest 代码（Figure 1）：

```python
filtered = table_ds.sem_filter("select cities whose population is below Boskovice's 11,622")
joined = filtered.sem_join(text_ds, "town name appears in passage")
joined.sem_agg("how often the festival takes place", output="answer")
```

执行返回“Every four years”。

阅读者分析：示例中第一步过滤谓词只写了“低于 11,622”，“其中最大者”这一约束实际由 Phase A 的桥接实体承担，而非出现在生成的流水线里。原始问题应从 Figure 1 逐字引用，不要从中文解释回译。

依据：[arXiv 2606.04641v1](https://arxiv.org/abs/2606.04641v1)，§1、§3.3–3.5、Figure 1–2，pp.1–6。
