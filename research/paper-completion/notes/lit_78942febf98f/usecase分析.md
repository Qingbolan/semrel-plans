# 具体用例

**WebQSP 的 KGQA 例子（Figure 2，§5.4，PDF pp.8–9）**：问题 “what highschool did harper lee go to?”
1. 调用 `Extract_Neighbor_Relations(Harper Lee)`，得到 education、birthplace、residence 等关系，线性化后提示 LLM “只给出一个相关关系”，LLM 选择 education；
2. 调用 `Extract_Triples(Harper Lee, [education])`，得到经过 CVT 节点的教育三元组，线性化后让 LLM 给出唯一答案实体；
3. 输出 Monroe County High School。

**Spider 例子（附录 B，PDF p.14）**：问题 “What is the name of the breed with the most dogs?”
1. 先列出全部表名和列名，LLM 选择 Dogs 和 Breeds；
2. 再读取这两张表的列和外键 `Dogs.breed_code → Breeds.breed_code`；
3. 生成连接后分组计数的 SQL。

阅读者分析：这些用例对应“模式裁剪 + 逐步证据选择”，与语义查询中的“先缩小上下文再交给 LLM”相同；但每一步的选择错误会向后传播，错误分析也证明选择错误是 KGQA 的主要失败来源。
