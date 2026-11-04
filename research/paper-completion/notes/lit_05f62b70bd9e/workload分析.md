# workload

**数据**（§3.1，p.3）：Amazon Reviews 2023，限定“Arts, Crafts and Sewing”类，使用 Hou et al. 提供的 5-core 抽样；要求 product_title、features_json、description_json、details_json、images_json、review_title、review_text 非空且至少 5 个字符；每个商品抽取“main”图像，无图像的商品丢弃，图像随数据集分发（main_image_local 列）。处理后 45k 商品、936k 评论。另有布尔列记录嵌入时文本是否被截断（仅 siglip2 会截断，p.4）。

**文本长度**（Figure 3，p.4）：各文本列最大长度分别为 product title 495、features 4,470、description 74,165、details 3,632、review title 227、review text 20,158 字符。

**语义倾斜**（Figure 2，p.4）：用 Qwen3 嵌入对商品描述做 BERTopic 聚类，类别分布明显不均；最大类大致为“珠宝制作所需一切”。作者说明聚类结果依赖嵌入模型及 UMAP/HDBSCAN 超参数。

**查询**（§3.2，pp.4–5）：102 条手写查询。

| | 单列谓词 | 多列谓词 | 合计 |
|---|---|---|---|
| 过滤 | 37 | 25 | 62 |
| 连接 | 23 | 17 | 40 |

连接若恰好引用每表一列，记为单列连接。谓词类别见 Table 1（Equality 52、Negation 23、Ordinal 17、Temporal 11、Spatial 4、Lexical 10，可重叠）。选择率覆盖约 10^-4 到 10^0（Figure 4，以 gpt-5.4-nano 评估，过滤 SF 1000、连接 SF 100），确切选择率随模型而变。

**评测规模**：过滤 scale-factor 1000（约 1,000 商品、约 2 万评论，阅读者按“每商品约 20 条评论”推算），连接 scale-factor 100（p.5）。不存在训练/测试划分；论文未说明 learned 估计器应如何训练。

**与本项目查询的关系**：本 atlas 引用该论文的 102 条查询（semceb/amazon-reviews/*）来自作者仓库 benchmark_queries/queries.jsonl，数量与论文的 102 条一致（阅读者推断，逐条对应未核对）。
