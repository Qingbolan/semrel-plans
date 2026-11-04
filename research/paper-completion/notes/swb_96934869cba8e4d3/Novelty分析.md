# 贡献与评价

**原文贡献**（Introduction，PDF p.2）：构建"首个、最大的公开"内部人申报数据集 IFD；定义检测策略性披露违规的二分类任务；提出 MaBoost；在传统模型、深度序列模型和 LLM 上做基准比较。

**数据构造**：从 WRDS 抽取交易记录，用 SAS 处理；保留有效清洗码（R/H/C/L/I），排除修正申报和期权相关交易，只保留公开市场买卖（P/S）；删除交易日晚于申报日的记录；与"LLM 生成的 SEC 工作日历"合并，用 Python 计算两日期限（Dataset，PDF p.3）。

**阅读者分析（评价）**：

- 规模与比例自相矛盾：4,051,143 条交易中"约 17.4%（21,482 条）"违规，但 21,482 只占 0.53%；按 17.4% 应约为 70 万条。Table 2 四类角色合计仅 61,132 条交易；Related Work 又称"超过一百万条记录"（PDF pp.2、4）。
- 标签泄露风险：标签由申报延迟决定，Table 3 的 52 个属性含 Gap_Days、SEC_Business_Day、Delay，特征消融中 "Trade Characteristics" 组也包含 Delay（Table 3、Table 7，PDF pp.5、9）。作者把 F1>99% 解释为规则结构清晰，而未讨论这一泄露。
- 文中称 Id 字段既是"内部唯一标识"又是"标签（1 表示违法）"（PDF p.4）；消融用到的 InsiderRatio、HHI、ROA、Tobin's Q、Ln(Distance) 不在 52 个属性列表中，来源未说明。
- 工作日历由 LLM 生成，未报告人工核对；"co-attentive design""adaptive weighting"在方法部分没有对应描述（PDF pp.3、5）。

依据：Introduction–Experimental Setup、Tables 2–3、7，PDF pp.1–5、9。
