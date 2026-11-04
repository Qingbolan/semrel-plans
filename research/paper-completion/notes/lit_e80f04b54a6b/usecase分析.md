# 具体用例

**用例：企业黑话查询"show me the income of TencentBI this year"**（§IV-A，p.5；§IV-C，p.6）

1. 该查询实际涉及三列 `prod class4 name`、`shouldincome after`、`ftime`，列名与用户措辞的语义关系模糊。
2. 离线阶段，Algorithm 1 读取引用这些列的历史 SQL/Python 脚本，为表和列生成描述、用途、标签和派生列计算逻辑，存入知识图谱；"TencentBI"等别名通过 alias 节点关联到正式名称。
3. 在线阶段，系统先改写查询，并把"this year"等时间表达按当前时间标准化；再用词法+向量检索粗召回知识节点，alias 回溯到主节点，按词法、语义、LLM 三项加权打分取 top-K。
4. LLM 把查询翻译为 JSON DSL（MeasureList、DimensionList、ConditionList），经 JSON Schema 校验后按规则转换为 SQL 或 Vega-Lite。
5. 结果写入笔记本单元，用户可在 Chart 单元中用 GUI 调整。

部署反馈（§VIII，p.12）：三个月内平均每月 2,093 名注册用户、10,900 次 API 调用，每周 319 名活跃用户；一位分析师称制图时间从 15 分钟降到 2 分钟（87%）。这些是轶事式用户反馈，没有对照组。

阅读者分析：原文没有给出该示例查询的最终 SQL 或执行结果，用例说明的是流程而非已验证的输出。
