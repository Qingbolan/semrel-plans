# 工作负载

**数据集**（§7.1，Table 4，p.186:16）：原始数据真实，表间关联与查询由作者构建。

| 基准 | 表 | 行数 | 多模态列 |
|---|---|---|---|
| YouTube | Videos | 46,774 | AudioClip（AUDIO，来自 AudioCaps）、Description（TEXT） |
| Craigslist | Pics | 14,674 | FilePath（PICTURE） |
| Craigslist | Ads | 3,000 | Title（TEXT） |
| Netflix | Movies | 17,770 | FeaturedReview（TEXT，取自 IMDb 评论） |
| Netflix | Ratings | 100M | 无 |

YouTube 数据由 AudioCaps 音频片段加上抓取的视频标题、描述、播放量、点赞数组成；Craigslist 为作者抓取的 3,000 条家具广告，每条至少一张图。

**查询**：YouTube 24 个、Craigslist 25 个、Netflix 6 个（Netflix 只有一个多模态列），类型包括 Min、Max、Sum、Avg、Count 聚合及带 LIMIT 的选择查询；每个查询至少一个 NL 谓词，可能是两个谓词的合取或析取；Craigslist 与 Netflix 有连接查询（§7.1）。

**标签模拟**：按人工确定的阈值模拟用户回答；阈值从 −28 到 27 不等，同一模型、同一列也随谓词变化很大（如图片列上 'wooden' 与 'leather sofa' 的阈值在 16 到 27 之间）（§7.1）。

**运行环境**：两颗 Intel Xeon Gold 5218（共 32 物理核）、384 GB 内存、两块 RTX 2080Ti（§7.1）。

**指标**：计算时间、标签数、加权代价、界误差、相对误差；“真值”由全量处理并用足够标签确定精确阈值得到，只在模型完全准确时才是真实答案（§7.4）。

阅读者分析：§7.1 列出的查询合计 24 + 25 + 6 = 55 个，但 §7.2 两处都以“49 个基准查询”为分母，原文口径不一致，这里不自行修正（阅读者分析）。

依据：§7.1–7.2、§7.4、Table 4，pp.186:16–186:21。
