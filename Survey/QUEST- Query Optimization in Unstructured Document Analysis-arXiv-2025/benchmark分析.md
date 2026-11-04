# 评测与边界

**基线**（§5.1，p.9）：ZenDB（语义层次树定位属性）、PZ（Palimpzest 原型）、LOTUS（全文喂给 LLM）、RAG（属性名+描述做相似检索，无文档级索引和证据）、ClosedIE（微调的抽取模型，不用 LLM）、Eva（Evaporate，让 LLM 生成抽取代码）。

**指标**：每条查询的元组级 P/R/F1（元组所有单元格都正确才算对）；每文档平均输入+输出 token（含采样成本）；每文档平均执行时间。

**实验 1（准确率，Table 2，p.11）**：F1 如下。

| 数据集 | ClosedIE | Eva | RAG | PZ | ZenDB | LOTUS | QUEST |
|---|---|---|---|---|---|---|---|
| WikiText | 0.24 | 0.33 | 0.37 | 0.78 | 0.79 | 0.90 | 0.87 |
| SWDE | 0.59 | 0.70 | 0.83 | 0.86 | 0.84 | 0.96 | 0.95 |
| LCR | 0.09 | 0.14 | 0.34 | 0.50 | 0.55 | 0.45 | 0.72 |

正文 §5.2 把 LCR 上 QUEST 的 F1 写成 0.7，精确值以 Table 2 的 0.72 为准。

**实验 2（成本与延迟，Table 3，p.11）**：ClosedIE 不用 LLM、Eva 只花少量 token 生成代码，故不报 token。

| 方法 | token Wiki | token SWDE | token LCR | 秒 Wiki | 秒 SWDE | 秒 LCR |
|---|---|---|---|---|---|---|
| Eva | – | – | – | 0.06 | 0.05 | 0.08 |
| ClosedIE | – | – | – | 0.76 | 0.65 | 1.83 |
| ZenDB | 260 | 280 | 2,530 | 2.08 | 1.77 | 2.73 |
| PZ | 400 | 320 | 2,610 | 2.17 | 2.16 | 2.85 |
| RAG | 440 | 340 | 3,500 | 2.57 | 2.65 | 3.01 |
| LOTUS | 2,520 | 1,150 | 12,480 | 2.66 | 2.78 | 3.36 |
| QUEST | 170 | 190 | 2,030 | 1.12 | 1.21 | 2.68 |

token 和秒均为每文档平均值；2.68 s 不是整批 100 篇 LCR 文档的响应时间。

**实验 3（过滤排序，§5.3，Figure 6，pp.10–11）**：与 Random、Selectivity、Average_cost（样本平均代价）、Exhaust（逐文档穷举）比较。按 token 排名 QUEST ≈ Exhaust < Average_cost < Selectivity < Random；过滤数增多时 Exhaust 的运行时间指数增长，QUEST 缓慢增长。

**实验 4（join，§5.4，Figure 7，p.11）**：两表 join 对比 Pushdown 与已知真实选择率的 Optimal，QUEST 明显低于 Pushdown、略高于 Optimal；IN 过滤选择率高（E3，0.6–1）时会退回下推。多表 join 对比 Random、Pushdown、Optimal（已知选择率并枚举所有顺序）。

**实验 5（消融，§5.5，Figure 8，pp.11–12）**：两级索引对比仅片段级索引；证据增强；阈值 τ 在自动值 0.4 附近变化；采样比例 1%–25%（5% 最平衡）；聚类数 K=1–7。

**边界**：
- 原文：只优化 SPJ，聚合留作未来工作（§2.1）；多查询优化与其基准测试不在范围内（§2.4）。
- 阅读者整理：每个数据集只有 100–200 篇文档；正文未说明所用 LLM、嵌入模型和硬件；ground truth 由 LLM 抽取再人工核验；PZ 为早期原型（作者称其深入优化“仍在进行”）；本轮未重跑任何实验。

依据：[arXiv 2507.06515v2](https://arxiv.org/abs/2507.06515v2)，§5.1–5.5、Tables 2–3、Figures 4–8，PDF pp.9–12。
