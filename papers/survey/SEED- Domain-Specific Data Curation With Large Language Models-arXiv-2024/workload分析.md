# 工作负载

**任务与数据**（Table 2，§6，p.10）：

| 任务 | 数据集 | 内容 | 使用的模块 | 指标 |
|---|---|---|---|---|
| 实体匹配 | Amazon-Google、Abt-Buy | 判断两条商品记录是否同一商品；沿用 MatchGPT 的测试划分 | 全部四类 | F1 |
| 属性补全 | Buy、Restaurant | 分别遮盖制造商与城市属性后补全 | 全部四类 | 匹配准确率（完全匹配或非平凡包含） |
| 信息抽取 | Wiki NBA | 从 NBA 球员 Wikipedia HTML 页抽 19 个属性 | CodeGen、LLM | token F1 |
| 数据标注 | OS | 推文是否为仇恨言论的二分类 | CacheReuse、LLM | 准确率 |
| 数据发现 | Spider、OTT-QA、KaggleDBQA | 为自然语言问题找相关表 | LLM（带工具） | 表集合 F1 |

**标准答案**：沿用原数据集标签；Spider 与 KaggleDBQA 以参考 SQL 涉及的表作为相关表，OTT-QA 用其表检索标注（只有一张正确表）（附录 B.1）。

**参数设置**（§6，p.10）：LLM 为 GPT-4，温度 0；ModelGen 用 t5-small，在 1,024 条未标注验证数据上用 LLM 伪标签微调；CacheReuse 用冻结的 t5-small；CodeGen 分支数取 1 或 4；补全任务用 3 个示例，抽取任务每个属性 1 个示例。

**单位**：一条记录（一对商品、一行表、一个网页、一条推文、一个问题）。论文未逐一给出各主实验的测试条数，不能用源数据集的完整规模代替（阅读者分析）。

依据：[arXiv 2310.00749v3](https://arxiv.org/abs/2310.00749v3)，§6、Table 2、附录 A、B.1，pp.10–17。
