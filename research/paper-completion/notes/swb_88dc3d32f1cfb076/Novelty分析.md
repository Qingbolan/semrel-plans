# 贡献与评价

论文自述三项贡献：

1. CSMeD 元数据集：9 个公开数据集、325 篇综述，基于 BigBio 数据加载器，可通过 Hugging Face datasets 和 LM Evaluation Harness 调用；同时给出现有筛查数据集综述。
2. 扩展元数据：从 Cochrane Library 抓取综述最新开放版本的标题、摘要、纳入标准、检索策略和参考文献，使数据可用于问答或文本对分类。
3. CSMeD-FT：作者称是首个专门用于系统综述长文档全文筛查的数据集，文献平均 4,000 词以上。

阅读者分析：贡献主要是数据整合、去重、统一接口与新的全文切分，不是新模型。CSMeD 没有设测试集，作者明确建议另建无偏测试集合，因此它更像训练/开发资源；CSMeD-FT 有按时间切的规范测试集，是更直接的评测贡献。

阅读者分析：扩展版用 Cochrane 全文阶段的纳入/排除列表近似标题/摘要阶段正例，所以平均纳入率（Table 2 约 20%）与原始数据集（Table 1 约 4.4%）口径不同，不能直接比较。

依据：[NeurIPS 2023 D&B，17 页](https://proceedings.neurips.cc/paper_files/paper/2023/file/4962a23916103301b27bde29a27642e8-Paper-Datasets_and_Benchmarks.pdf)，§1 贡献列表，PDF p.2；§4.1–4.2、Tables 1–2，PDF pp.6–7；§5.1，PDF p.8。
