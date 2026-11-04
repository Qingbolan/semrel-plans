# 工作负载

**要验证什么**：LLM 能否为混合表、图像、文本的自然语言分析问题生成正确的逻辑计划和物理计划。实验不评价数据发现，§4.2 直接跳过 Discovery、假定检索完美（p.4）。

**数据集**（§4，p.4）：作者称尚无对应基准，因此自建两个。

| 数据集 | 模态 | 构成 |
|---|---|---|
| Artwork | 表 + 图像 | 从 Wikidata 抽取所有"绘画"实体的元数据（标题、创作时间、流派等）及其图像 |
| Rotowire | 表 + 文本 | Rotowire 篮球比赛文字报道，加上从 Wikidata 构建的球队表和球员表 |

**规模**：正文未给完整导入行数；Figure 3 的示例 prompt 中 `paintings_metadata` 与 `painting_images` 均写作 `num_rows=7912`，可视为 Artwork 规模的线索，但非正式说明（阅读者分析）。

**查询集**（§4.2，p.4）：每个数据集 24 个，共 48 个；16 个单值、16 个表、16 个图；一半需要多模态数据，一半只需关系数据。这些查询未用于开发期调 prompt。论文未说明标注者或一致性流程。

**工具**（§4，p.4）：VisualQA 与 Image Select 基于 BLIP-2，TextQA 基于 BART，Python UDF（由 GPT-4 把描述翻译成代码），SQLite 关系算子，seaborn 绘图。生成的 SQL 被限制为只读 SELECT（§5）。

依据：[arXiv 2308.03424v1](https://arxiv.org/abs/2308.03424v1)，§3–5、Figure 3，pp.3–6。
