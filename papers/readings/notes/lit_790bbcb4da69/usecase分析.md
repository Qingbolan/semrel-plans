# 具体用例

Listing 5 给出了 BIRD 医院数据库中的一个例子（PDF pp.5–6）。问题是"How many patients with a normal Ig A level came to the hospital after 1990?"，证据说明"normal Ig A level refers to IGA > 80 AND IGA < 500"。Info Alignment 给出 SELECT 内容为"[How many patients]"。

模型按顺序输出：

- 理由：要统计满足条件的不同患者数；
- 列：`Patient.ID`、`Laboratory.IGA`、`Patient.First Date`；
- 值：IGA 范围条件，以及 `strftime('%Y', First Date) >= '1990'`；
- SELECT：COUNT(DISTINCT Patient.ID)；
- SQL-Like：不写 JOIN 的骨架；
- 最终 SQL：在 SQL-Like 基础上补出 `Patient` 与 `Laboratory` 按 ID 的 INNER JOIN。

Listing 6（p.6）给出三类对齐的小例子：把 `name = 'John'` 改成库中实际存储的 `'JOHN'`；把 `ORDER BY MAX(score)` 改为 GROUP BY 形式；在 `ORDER BY score DESC LIMIT 1` 前加 `score IS NOT NULL`。

阅读者分析：Style 对齐的规则是为了贴合 BIRD 标注风格（如 MAX 与 LIMIT 1 的取舍），属于针对数据集的调整，迁移到其他数据库时可能需要重写。

依据：[arXiv:2502.14913v1（2025-02-19，ACM 模板会议信息未填写），15 页](https://arxiv.org/pdf/2502.14913v1)，§3.5、Listings 5–6，PDF pp.5–6。
