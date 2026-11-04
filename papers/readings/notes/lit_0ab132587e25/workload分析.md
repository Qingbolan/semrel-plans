# workload

**偏好语料（§3.2–3.3、Table 1、附录 B）**
- 来源：AIDE 与 AutoMind（底座 DeepSeek-V3.1、o3-mini）在 MLE-bench 上的真实轨迹，共 1,329 个有效方案，覆盖 26 个 Kaggle 任务；经去重、分类打标与专家抽样（限制主导方法占比）保留 895 个方案。
- 将同一任务内方案穷举两两组合，丢弃难区分的对，并平衡正确答案位置，得到 18,438 对。
- 领域分布（Table 1）：CV 9 任务/289 方案/5,952 对；NLP 8/303/6,682；数据科学（回归、时序、音频、表格、评分）9/303/5,804。
- 主指标：18,438 对上的微平均准确率，三次运行取均值±标准差。
- 分析子集：RQ2–RQ3 每任务至多 15 个方案（2,292 对）；排序实验每任务抽 105 例（§5 开头）。
- 附录 C.2 把对拆为同轨迹/跨轨迹两类，DeepSeek 在同轨迹对上 60.4%、跨轨迹 61.7%，作者据此认为没有"早期半成品 vs 成品"带来的虚高。

**智能体评测（§6.3、Table 5、附录 B.3）**：MLE-bench 中 5 个 AI4Science 任务（Stanford Covid Vaccine、Ventilator Pressure、Statoil Iceberg 为 seen；Aerial Cactus、Histopathologic Cancer Detection 为 unseen，即未出现在主实验语料中），12 小时预算，每任务 3 次独立运行。

阅读者分析：这里没有训练/测试划分——预测器是零样本提示的 LLM，"seen/unseen"只表示任务是否出现在偏好语料里。工作单元是"代码方案对 + 数据报告"，而非数据库查询或文档记录。

依据：[arXiv:2601.05930v2，34 页](https://arxiv.org/abs/2601.05930)，§3、§5、§6.3、Tables 1、5，附录 B、C.2，PDF pp.2–8、15–24。
