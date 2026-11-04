# workload分析

| 场景 | 论文查询数 | 输入组织 | 环境数据 |
|---|---:|---|---|
| Movie | 10 | Movies(id,title)、Reviews(id,reviewId,reviewText) | 无额外外部语料；两表为任务输入 |
| Wildlife | 10 | ImageTable(image,city,stationID)、AudioTable(audio,city,stationID) | 无；city/station由benchmark随机生成，图片/音频列指向媒体 |
| E-Commerce | 14 | styles_details含id、productDescription、productImage及结构字段 | 无；标签只给gold，不能暴露给系统 |
| MMQA | 11 | 5张Wikipedia文本/表格来源表加images元数据表 | 这些表就是查询输入，不是外部搜索服务 |
| Cars | 10 | Cars、ComplaintsText、CarImage、DiagnostAudio | 合成车辆属性与真实媒体关联，不代表自然观测到的跨模态关系 |

表2全量为1582560文本、84295图像、2037音频行；表3基础scale按上述场景为2000/200/500/200/19672。论文55queries不能直接用本地60条catalog覆盖；MMQA原编号Q2a/Q2b等应保存为source id，UI1、2、3编号另存。

§5.2明确ThalamusDB join batch=10，两侧表各10行整合进同一prompt。各适用系统LLM并发20；并发不是prompt batch，BigQuery两者均由引擎管理。benchmark规模轴是输入行数，并未评测多用户或并发多query吞吐（§3.3）。

来源：[原论文](https://arxiv.org/abs/2511.01716v2)。本分析据所列版本全文核读，未复现实验。
