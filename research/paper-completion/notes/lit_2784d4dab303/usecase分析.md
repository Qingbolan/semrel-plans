# 具体用例

**案例研究**（§4.5，p.4871；Fig.1，p.4861）：

1. 用户问："Company A 2024 年的收入是多少？"
2. **对话分析**：查询同时含维度（2024）与指标（收入），语义完整，进入下一阶段。
3. **意图查询**：从知识库召回三元组（"company"，默认未特别说明时指腾讯，示例问题）解释术语；"收入"有歧义（含税或不含税），系统追问用户指 `shouldincome` 还是 `shouldincome_after`。
4. **SQL 生成**：选表并生成 `SELECT SUM(shouldincome_after) AS total_income FROM revenue_by_quarter WHERE YEAR(ftime) = 2024 AND cname = Company A`。
5. **数据洞察**：用户追加"对 Company A 2024 年收入做维度归因分析"，Planner 拆分任务、准备数据、调用归因工具并生成报告（Fig.8）。

**两步法示例**（§3.4.4，pp.4867–4868）："分析 2023 年腾讯云 BI 的消费"先被改写为 SIR：产品中文名 `p_name_zh` 为"腾讯云 BI-高级版"、指标为含税消费收入 `consumeincome`、时间 2023，再由代码 LLM 生成 SQL。

阅读者分析：该用例展示的是"术语映射 + 追问澄清"对歧义列的处理，与语义算子系统中由 LLM 直接判定行级语义不同，这里 LLM 只负责理解问题和生成 SQL，数据处理仍由数据库执行（阅读者分析）。

依据：§3.4.4、§4.5、Fig.1、Fig.8，pp.4861、4867–4871。
