# 具体用例

**论文用例：初学者友好的机器学习课程过滤（Figure 1，p.2；§2.1，p.3）。**

用户对课程表（title、subject、difficulty 列）执行 sem_filter("beginner-friendly courses about machine learning")。

- **解释式：** 对每一行发送“该行是否满足条件？返回 True/False”给 LLM，N 行 N 次调用。
- **编译式：** 一次 LLM 调用，以默认 filter 提示（“You are an advanced database query optimizer…函数必须命名为 compiled_filter，参数 row 为含 {INPUT_SCHEMA} 键的字典，返回布尔值，只输出 Python 代码”）生成函数：把 title 与 subject 拼接后检查是否包含 “Machine Learning / ML / Deep Learning / DL / Artificial Intelligence / AI” 等关键词，且 difficulty == "beginner"；随后本地对全部行执行，不再调用 LLM。
- **在 SemBaker 中的流程：** 优化器估计该 filter 输入行数；若 ≥11（时间代价阈值）且谓词未触发可编码性筛查（没有主观、讽刺、多跳要求），则路由为编译；编译在后台线程池进行，此前的原生算子可同时执行（§2.2–2.3）。

**阅读者分析：** 该例也暴露了编译式执行的语义边界——关键词匹配会把含 “AI” 子串的无关标题判为真，或漏掉以其他措辞描述的 ML 课程；论文用与原生输出的一致性（filter F1 0.890）衡量这一近似，而非人工标注的真值。对本项目，若把此类编译算子纳入语义查询基准，应区分“与 LLM 解释的一致性”和“相对真值的正确性”。
