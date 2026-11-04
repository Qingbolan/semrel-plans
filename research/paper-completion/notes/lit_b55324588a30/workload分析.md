# 工作负载

| 任务 | 数据集 | 来源 | 说明 |
|---|---|---|---|
| 数据填补 | Restaurant（目标属性 city）、Buy（目标属性 manufacturer） | Mei et al., 2021 | 人工遮盖目标属性值，有真值 |
| 数据转换 | StackOverflow、Bing-QueryLogs | TDE 基准 | 涵盖 ip、地址、电话等多种转换类型 |
| 错误检测 | Hospital、Adult | 数据清洗文献常用 | 错误约占数据 5%，所有单元格有真值 |
| 实体解析 | Beer、Amazon-Google、iTunes-Amazon、Walmart-Amazon | Magellan 基准 | 同 schema 两表的候选记录对，正/负标签 |

（§5.1，pp.7–8；Table 4，p.9）

附录追加两类负载：连接发现用 NextiaJD 的子集，4,404 个属性对（2,239 正、2,164 负，质量标为 Good/High）；信息抽取用 SWDE 的 NBAplayer（NBA 球员 Wikipedia HTML 页面，封闭 schema）（附录 D–E，p.17）。

**规模缺口**：正文没有给出各数据集的测试记录数、被遮盖单元格数或候选对数量；只给出微调用的 Walmart-Amazon 训练划分 6,144 条（§5.2，p.9）。默认检索设置为从数据集中随机抽 50 条记录，取 top-3 记录和 1 个属性（§5.1，p.7）。

阅读者分析：以上都是逐单元格/逐记录对的短输入任务，与长文档语义查询不同；若在本项目中复用，应注意结果对单表、小上下文的依赖。

依据：§5.1–5.2、附录 D–E，PDF pp.7–9、17。
