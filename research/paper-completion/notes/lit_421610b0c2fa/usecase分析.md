# 具体用例

Figure 2 的端到端例子（§3，pp.2–4）：用户输入“列出所有产品名称及其收到的投诉数，用柱状图展示”。

1. **processor**：生成数据库描述（如 Products 的 product_id、product_name 及示例值“Chocolate”“Mouse”）；模式过滤只保留 `Products: [product_id, product_name]` 与 `Complaints: [product_id]`，去掉 product_category 等无关列；补充解释“product_id 是连接 Products 与 Complaints 的外键”；把查询分类为 MULTIPLE。
2. **composer**：先确定图表类型为柱状图，构造草图 `VISUALIZE bar SELECT _, COUNT(_) FROM _ JOIN _ ON _`，再填入列名得到完整 VQL。
3. **validator**：把 VQL 翻译成 Python 代码执行；遇到“缺少 GROUP BY”错误时把信息回送 composer，composer 补上 `GROUP BY t1.product_name` 后重新验证，直到渲染成功。

阅读者分析：在语义数据处理流水线中，这对应“自然语言 → 结构化查询（含连接与聚合）→ 可执行产物 → 执行反馈”的闭环；可复用之处在于把修正放在较简单的中间语言（VQL）上，而不是直接改最终代码。该用例只说明流程，不代表此类查询的成功率。

依据：§3.1–3.4 与 Figure 2，PDF pp.2–4。
