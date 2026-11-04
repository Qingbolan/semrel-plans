# 工作负载

**训练数据**（§4.2、§5.1，pp.7、10）：默认使用 T-5 到 T-18 共 14 类任务；每类 1,000 个实例，零样本与少样本模板各半。表格从 125K 张网页表和数据库表中采样（由 200 多万原始表激进去重得到）。§4.2 另写爬取了 2.9M 网页表与 188K 数据库表，两处口径不同，正文未说明对应关系（阅读者分析）。

**测试划分**（Table 2、§5.1，pp.6、10）：T-1 至 T-4 为完全未见任务；T-5 至 T-9 为训练见过的任务类型，但测试数据集不同。合成型测试（T-1、T-2、T-8）取自电子表格语料，与训练用的网页表/数据库表语料分开。

| 任务 | 指标 | 数据集（规模） |
|---|---|---|
| T-1 缺失值定位 | F1 | 4 个变体，各 1,000 |
| T-2 列查找 | Acc | Spreadsheets-CF 841 |
| T-3 表格问答 | Acc | WikiTableQuestions 4,344 |
| T-4 列类型标注 | F1 | Efthymiou 594、Limaye 174、Sherlock 971、T2D 367 |
| T-5 行到行转换 | Acc | BingQL-Unit 103、BingQL-other 1,102、FF-GR-Trifacta 132、Headcase 88、Stackoverflow 145 |
| T-6 实体匹配 | F1 | Magellan 7 个（如 DBLP-GoogleScholar 5,742、Beer 91） |
| T-7 模式匹配 | Recall | DeepM 41 |
| T-8 数据填补 | Acc | Spreadsheets-DI 1,000 |
| T-9 错误检测 | F1 | Spreadsheets-Real 870、WebTables-Real 432（作者人工标注） |

表格统一以 Markdown 序列化；附录 A 给出各任务的零样本/少样本提示词及 JSON 输出格式（pp.16–47）。

依据：Table 2、Table 4、§4.2、§5.1、附录 A，PDF pp.6–7、10、12、16–47。
