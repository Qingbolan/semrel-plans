# 工作负载

**查询集**：SemBench 五个场景共 55 条语义查询，另加 BioDEX 1 条（§7.1.1、附录 B）。附录 J 逐条给出意图和核心代码（省略数据加载等）。Medical 场景因许可问题已从 SemBench 移除。

| 场景 | 查询数 | 查询类型 | 输入表与规模（Table 2） |
|---|---|---|---|
| Movie | 10 | Q1–4 过滤，Q5–7 连接，Q8 分类，Q9–10 排序 | Reviews 20,000 行；ReviewText |
| Wildlife | 10 | 图像过滤、音频过滤、图像+音频组合（见下注） | ImageData 4,000 行（Image/City/StationID）；AudioData 650 行（Audio/City/StationID） |
| MMQA | 11 | 文本过滤/抽取，文本→图像连接，图像连接+抽取 | 四张表各 300 行：LizzyCaplanText、BenPiazzaText、TampaInternationalAirport、Images |
| Cars | 10 | 文本、图像、音频过滤及多模态组合 | CarComplaint 99,929 行（Summary）；CarImage 19,156 行；CarAudio 871 行 |
| E-Commerce | 14 | 过滤、抽取、分类、连接、3/4 路连接、结构化抽取、跨模态过滤-连接、top-k | StyleDetails 5,000 行：ProductDisplayName、ProductDescriptors、Images |
| BioDEX | 1 | 文章 × 反应的语义连接（极端多标签分类） | 1,000 篇文章 × 100 个反应；文章由标题、摘要和相关章节组成 |

注：§7.1.1 把 Wildlife Q8 列为音频过滤，而附录 J.2 的 Q8 是图像或音频的组合查询，以附录代码为准（阅读者分析）。

**质量指标**（§7.1.2）：按查询类型用相对误差（聚合）、F1（检索）、Spearman ρ（排序）、ARI（分组/分类）；BioDEX 用 RP@5。均在 [0, 1] 内与 ground truth 比较。

**执行环境**：给定关系与可访问的图片/音频文件，加上算子/模型目录，不需要开放 Web 搜索。验证集只用于选计划，不并入查询事实表。

**规模与批处理口径**（§6.1–6.2、§7.1.4）：算子输入输出以 DataFrame 传递，支持批量推理，但未给统一的 batch size。并发 20 是请求并发数，验证 50 是样本数，LIMIT 5/10/100 或 top-k 是结果限制。N ≤ 300 时直接用 LLM 执行，近此规模 55 条中只有 16 条更适合纯 LLM。主实验关闭计划缓存。

阅读者分析：查询以单表或少数表上的语义谓词为主，最大的连接（E-Commerce Q8）为 28 条文本 × 4,993 张图片；没有真实用户日志。具体例子见“具体用例”，结果见“评测与边界”。

依据：[arXiv 2606.29151v3](https://arxiv.org/abs/2606.29151v3)，§6.1–6.2、§7.1、Table 2、附录 B、附录 J，PDF pp.8–10、16、24–27。
