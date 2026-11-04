# 具体用例

**原文模板**（§3.4，p.7）：根据症状查疾病，再找能治这些病的药物。SQL 类写法如下：

```sql
SELECT {Attribute}(s), {agg_func}({Attribute}(s))
FROM diseases
JOIN drug ON disease.name = drug.disease
WHERE disease.symptoms {operator} {literal}
GROUP BY {group_by};
```

对应的代码写法依次是 `Filter(disease_doc, …)` → `Join(disease_doc, drug_doc, disease_doc.name = drug_doc.disease)` → `Extract(…)` → `Aggregate(…)`。

**输入与 gold**：输入至少包括疾病和药物两个文档集合，系统需要读取文档的 text 字段，并抽取 name、symptoms、disease 等属性。`disease.name = drug.disease` 是评测时在关系 gold 上使用的连接条件，原始文档里并没有现成的这个字段。

**实例化**：`{Attribute}`、`{literal}`、`{operator}`、`{group_by}`、`{agg_func}` 都是占位符，由脚本按 §3.4 的规则随机填充，所以上面是一个模板，不是一条具体查询。具体实例要以官方发布的查询文件为准；本文没有逐条核对官方的 240 条查询。

**各系统执行这类 join 的方式不同**（§2.2，p.4）：
- ZenDB 和 QUEST 先从两组文档中分别抽出疾病表和药物表，再做 join；
- LOTUS 先抽出疾病表并对 join 键做嵌入，再用每种疾病的嵌入检索相关的药物文档，只对检索到的文档抽取药物表。

§4.6 的“with-Search”实验（Figure 11，NBA）显示，这种用 join 键检索的剪枝能降低成本，但会误删本应 join 上的文档，导致准确率下降。

阅读者分析：在 Finance 这样的长报告上，只读相关的块可以省 token，但可能漏掉分散在多段中的信息（如 `Business_cost` 需要按行业汇总多项成本）。先弄清所求属性的证据分布在哪里，再决定读全文还是分块，比对所有查询使用同一种分块策略更合适。

依据：[arXiv 2510.27119v1](https://arxiv.org/abs/2510.27119v1)，§2.2、§3.3–3.4、§4.6、Figure 11，PDF pp.4–7、11。
