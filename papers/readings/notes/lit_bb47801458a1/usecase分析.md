# 具体用例

论文运行示例（Fig.2–3，pp.4–5）：Google Play 应用数据中，统计 ART_AND_DESIGN 类别、Free 类型的每个应用里"有效且正面"的评论数。查询为普通 JOIN + 两个关系谓词 + 两个 SemFilter（`{translated_review} is a valid user review`、`… is a positive user review`）+ GROUP BY。

处理流程：表达式压缩把两句改写为 "valid?" / "positive?"；谓词推导利用元数据（translated_review 约 41.8% 为 'nan'）推出 `translated_review != 'nan'` 并下推，大量元组无需调用 LLM；执行时两个 SemFilter 因共用同一列可融合为一次调用 "valid and positive"（Example 4.1、5.1）。

另一个案例 Q6（Fig.8，Table 5，p.11）：在 coins 描述上判断"供应量大""仍在流通""价格上涨"三个条件。样本估计选择率 0.66/0.77/0.22，MCC(σ1,σ2)=0.755。候选路径中融合路径 p2 相对重排路径 p1 延迟约降 49%、成本降约 9%，相对精度 100%；批处理路径在本地反而更慢。τacc=0.80 时 p_b1 与 p2 在帕累托前沿上，延迟优先选 p2、成本优先选 p_b1。

阅读者分析：这一用例展示的是"关系谓词 + 多个文本判断"的混合过滤，是语义算子系统最典型的负载；但融合时保留一致性靠的是提示指令，原文没有给出跨模型的稳定性验证。
