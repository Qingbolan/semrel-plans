# 贡献与评价

论文声明（PDF p.2）：(1) 首个大规模、高质量文档级多模态理解数据集，758K 问答、3 个来源、9 类代理任务，其中 31.6% 为直接从文档抽取的真实问答；(2) 不依赖检索的原生文档级 MLLM Docopilot；(3) 多个文档级基准上显著优于现有方法。

阅读者分析：
- 模型侧没有新架构，贡献在数据与训练工程（打包、Ring Attention、Liger Kernel 均为已有技术的集成）。论文自己也把模型定位为“基线”（§4 标题 “Enhanced Baseline”）。
- 数据侧的主张需要区分几个比例：31.6% 为真实问答，75.4% 来自 OpenReview 与 arXiv（“可靠标注”），4.8% 为 LLM 生成。三个比例口径不同，正文没有给出它们如何相加成 100%，其余部分应是依文档结构构造的代理任务（如写标题、写摘要）。
- “首个”这一说法依据 Table 3 与 Docmatix、DUDE 等的规模对比；Docmatix 问答对（9.5M）更多，Doc-750K 的优势在 token 数（5.2B）与跨页结构。
- 数据来源包括 Sci-Hub，论文未讨论版权或数据许可问题。

依据：[CVPR 2025 Open Access，12 页](https://openaccess.thecvf.com/content/CVPR2025/papers/Duan_Docopilot_Improving_Multimodal_Models_for_Document-Level_Understanding_CVPR_2025_paper.pdf)，§1、§3.2、Table 3，PDF pp.2、5–6。
