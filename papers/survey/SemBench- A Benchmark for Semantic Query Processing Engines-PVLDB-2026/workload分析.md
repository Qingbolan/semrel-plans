# 工作负载

**场景与输入表**（§4.1–4.5、Table 2，pp.4–7）：

| 场景 | 查询数 | 输入表 | 数据来源与构造 |
|---|---:|---|---|
| Movie | 10 | `Movies(id,title)`、`Reviews(id,reviewId,reviewText)` | Kaggle 烂番茄影评，带人工情感标签 |
| Wildlife | 10 | `ImageTable(image,city,stationID)`、`AudioTable(audio,city,StationID)` | 相机陷阱图片和动物叫声两个 Kaggle 集合；city（5 个）和 station（4 个）随机生成 |
| E-Commerce | 14 | `styles_details(id,productDescription,productImage,…)` | Kaggle 时尚商品集，共 44,446 件；gold 来自结构化列（颜色、类别等） |
| MMQA | 11 | 5 张 Wikipedia 表/文本表，外加 `images` 元数据表 | MultiModalQA |
| Cars | 10 | `Cars`、`ComplaintsText`、`CarImage`、`DiagnostAudio` | 车辆属性为合成数据；投诉文本、诊断音频、损伤图片取自 4 个真实数据集，按共现约束分配损伤 |

**算子分布**（Table 2）：语义 Filter 共 50 个、Join 15 个、Map 7 个、Rank 3 个、Classify 4 个。E-Commerce 用 join 最多（9 个），Wildlife 和 Cars 没有语义 join。

**数据规模**（Table 2–3）：

| 场景 | 文本行 | 图像行 | 音频行 | 可用范围 | 基础规模 | 扩展实验 |
|---|---:|---:|---:|---|---:|---|
| Movie | 1,375,738 | – | – | 1–1,375,738 | 2,000 | 1,000–16,000 |
| Wildlife | – | 8,718 | 650 | 1–8,718 | 200 | 100–1,600 |
| E-Commerce | 44,446 | 44,446 | – | 50–44,446 | 500 | 250–4,000 |
| Cars | 157,376 | 30,131 | 1,387 | 1–157,376 | 19,672 | 9,836–157,376 |
| MMQA | 5,000 | 1,000 | – | 25–1,000 | 200 | 100–800 |
| 合计 | 1,582,560 | 84,295 | 2,037 | | | |

**执行参数**（§5.1–5.2）：每个实验重复 5 次。适用的系统把 LLM 调用并发设为 20，BigQuery 由引擎自行管理并发与 batch。ThalamusDB 的 join batch 为 10，即两侧各 10 行放进同一个提示。并发数和提示内 batch 是两件事，不能混用。

阅读者分析：作者只用了全量数据中很小的一部分（每个场景几百到几千行）。原因是语义处理成本高，而这个规模已足以拉开系统差异（§4.6）。MMQA 的原文编号（Q2a/Q2b、Q3a/Q3f、Q6a–c）应作为 source id 保留。

依据：[arXiv 2511.01716v2](https://arxiv.org/abs/2511.01716v2)，§4.1–4.6、§5.1–5.2、Tables 2–3，PDF pp.4–7。
