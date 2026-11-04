# 具体用例

§6.4 与 Figure 3–4 给出一个参考图生成案例（PDF pp.7、20–21），数据库为 journal_committee.sqlite：

**用户请求**："我喜欢这张带危险阈值线的日值图，能否改成按主题显示期刊销量？想看哪些主题超过 2,000，把这些高表现者标成红色，低于阈值的柱保持蓝色，在 2,000 处加一条标注为 'High Sales Threshold' 的虚线，加上标题并正确标注坐标轴。"

**执行过程**（Figure 3）：
1. 协调者调用 DQ Agent 的 generate_sql：依次 find_fields、list_tables、get_table、execute_sql，得到 `SELECT Theme, SUM(Sales) ...`；
2. 调用 Vis Agent：检索图表示例列表与示例代码，生成 Altair 代码并执行调试；
3. VE Agent 评估发现 2 个代码问题（如 SyntaxError），Vis Agent 修改；再评估仍失败时，协调者从 SQL 生成重新开始整个流程，最终得到通过验证的代码。

**结果比较**：MultiVis-Agent 只把超出阈值的部分染红（柱子图层 + 以阈值为下界 y2 的高亮图层 + 虚线规则 + 文本标签）；Instructing LLM 与 LLM Workflow 把超阈值的整根柱子染红；nvAgent 在 VQL→Altair 转换中产生带尾逗号的 `GROUP BY Theme,`，触发 DatabaseError，未生成图表。

阅读者分析：用户原话"把这些高表现者标成红色"其实也可以理解为整根柱子变红，基线的做法未必算错；"只染超出部分"是金标准（Figure 4b）的约定。这说明该基准的正确性部分取决于对参考图风格的具体解读。
