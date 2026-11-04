# 具体用例

**原文场景**（§3，pp.4644–4645）：在 1,000 条匿名评论上提问“summarize the top complaints about our products and identify which attributes drive negative reviews the most.”

**场景 1：执行前检查计划**。Carnot 返回逻辑计划，同时以 chat 中的嵌套摘要和 DAG 显示。用户在执行任何算子之前检查过滤条件、group-by 字段等参数，确认数据来源、过滤标准和聚合逻辑符合预期。

**场景 2：通过 chat 纠偏**。用户发现过滤算子只看了 ratings 字段，于是在 chat 中补充：“Be sure to also consider any negative comments left in the ‘review text’ field.” 规划器把这句话当作约束，只重新规划受影响的算子并给出新 DAG，执行结果逐算子流式返回。

**场景 3：在 notebook 中直接改单元格**。用户执行前几个单元格后发现语义过滤器有假阴性（把真实投诉判为中性反馈），直接修改该单元格的提示。保存后优化器重新优化该算子的实现，上游仍有效的单元格不重跑，从修改点继续执行。

**成本约束**：用户在界面设置成本与延迟约束，规划器会替换算子实现，例如对低精度过滤用更小更便宜的模型代替大模型（§3）。

**Figure 2 的会话**：问题“Which of these papers is about AI?”，中间是计划与 DAG，右侧 notebook 单元格显示语义过滤的条件和语义 map 的字段说明，左侧是逐算子结果、成本标注（如语义 map 一步 $0.0087）、最终答案和可下载的 CSV。

阅读者分析：以上是作者的演示脚本，不是本项目复现的运行痕迹；若转为图册中的 DAG，应标为演示实例。它提示页面应把查询、可读数据、实际输入列、算子输入输出作为并列可检查的对象。

依据：[PVLDB 19(12)](https://www.vldb.org/pvldb/vol19/p4642-russo.pdf)，§1、§2.1、§3、Figure 2，pp.4642–4645。
