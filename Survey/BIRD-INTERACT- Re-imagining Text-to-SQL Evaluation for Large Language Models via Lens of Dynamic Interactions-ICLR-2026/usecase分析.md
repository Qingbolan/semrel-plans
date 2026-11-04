# 具体用例

**原文示例**（Figure 1 与 Figure 2，§1、§3.2，PDF pp.2–4）：文物保护数据库。

**子任务 q1**：“Build a function to calculate and rank all artifacts to identify which need urgent care.”

**被注入的歧义**：“need urgent care”实际意为按 AVS（Artifact Vulnerability Score）降序排序；知识链 “urgent care” → “AVS” → “IF / CPI” 中，中间节点 AVS 的定义在知识库里被遮蔽。IF = 历史评分 × 文化评分，CPI = (10 − 保护状态) / 30，AVS = IF × CPI。

**交互过程**：
1. 系统读取 schema 与列含义，在知识库中搜索 “AVS”，找不到定义；
2. 系统问：判断“urgent care”用什么评分指标？模拟器答：按 AVS 排名；
3. 系统再问 AVS 的精确公式，模拟器答：AVS = IF × CPI；
4. 系统提交创建函数 `rank_urgent_care()` 的 SQL，报语法错误（`/ 30.0` 附近），按反馈修正后再次提交，通过测试用例；
5. 模拟器发布 q2：“对最紧急的文物，给出其最近一次风险评估等级与保护优先级分数”，系统用调用 `rank_urgent_care()` 的 LATERAL 子查询作答并通过测试。

这个例子同时包含知识链断裂、执行调试和对前一步新建函数的状态依赖。

阅读者分析：示例中的信息缺口是作者有意遮蔽的，用来测试系统是否会问；它不说明现实中同类缺口有多常见（阅读者分析）。

依据：§1 Figure 1、§3.2 Figure 2，PDF pp.2–4。
