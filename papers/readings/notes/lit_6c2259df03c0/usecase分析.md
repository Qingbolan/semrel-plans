# usecase

附录 D 的完整例子（Figure 11）：问题为"有多少行代表取消订单，占全部行的百分比是多少？"。环境 /data/community_0/ 下有 154 个数据集、441 个文件，包括英国交通流量、信用卡申请、欺诈检测、另一份 ecommerce-data 等同主题干扰。目标文件是 onlineretail/source/OnlineRetail.csv（45.6 MB、541,909 行、8 列），该任务 SNR 0.002、干扰相似度高。期望解：先在文件系统中识别 OnlineRetail.csv；用 latin-1 编码读取；以 Quantity<0 识别取消记录；计数并计算占比保留两位小数；按"count; percentage%"格式输出。真值为"10624; 1.96%"。

这个例子说明难点：agent 必须先排除同样是电商/交易类的 ecommerce-data/data.csv 等干扰，再知道"取消"在该数据中以负数量表示——两步分别对应 DA 与 EA。

阅读者分析：对语义查询/数据湖项目，这是"表发现 + 单表聚合"的典型形态；若迁移为项目任务，应保留社区内干扰与只读文件系统设定，而不是只给出目标表。

依据：[arXiv:2606.15300v1，37 页](https://arxiv.org/abs/2606.15300)，附录 D、Figure 11，PDF pp.25–26。
