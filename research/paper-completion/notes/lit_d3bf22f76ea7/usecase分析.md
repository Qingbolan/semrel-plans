# 具体用例

**WikiTQ 赛车结果表（Fig.1–2，pp.1–3）**，问题为“Which country had the most competitors?”：

1. 预处理识别出车手列，并生成列描述；
2. 计划的 SQL 步建立去重后的车手中间表 `unique_drivers`；
3. LLM 步根据车手姓名（借助预训练知识）推断并追加 `country` 列；
4. SQL 步按 country 分组计数并排序；
5. 答案提取阶段从最终中间表读出国家名。

计划验证步骤会修订原计划，例如补充缺失的格式化步骤（Fig.2 step D）。

**筛选示例（App. D，Listing 25，p.24）**：问题“what number of games were lost at home?”对应的 Binder SQL 含两个 `QA("map@...")` UDF 条件，因此被判定为混合问题。

阅读者分析：在这个用例中，LLM 步依赖模型对车手国籍的记忆，而不是表内证据。用来作语义算子参照时，应把这种“外部知识补列”与“从表内文本抽取”区分开。

依据：§1–§2、Figs.1–2、Appendix D，PDF pp.1–3、24。
