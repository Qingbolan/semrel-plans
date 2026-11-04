# 工作负载

**训练数据 Doc-750K**（§3.2、Table 2–3，PDF p.5–6）：758K 问题、251K 对话（87K 多轮、164K 单轮）、3,103,494 张图像、约 5.2B 文本 token；平均每段对话 11,245 个文本 token、6,178 个图像 token，平均约 4 张图。学术论文约占 32.6%、多模态数据约占 88.8%（这两个比例指整个 SFT 数据配方，见 Fig.4）。

**SFT 混合配方**（§3.3，p.5–6）：多页文档 QA（Doc-750K、MP-Docmatix、MP-DocVQA、DUDE、Taesiri-ArxivQA）、多图通用 QA（MMDU-45K）、单页文档 QA（DocVQA、DocReason、InfoVQA、ChartQA）、纯文本长 QA（LongAlpaca、LongQLoRA、LongCite、LongAlign、LongReward 等）。

**评测基准**（§5，p.7–8）：

| 类别 | 基准 | 指标 |
|---|---|---|
| 多页 VQA | MP-DocVQA、MMLongBench-Doc、DocGenome | ANLS；Acc/F1；分类 Acc、标题/摘要编辑距离、单页/多页 QA Acc |
| 交错长上下文 | MM-NIAH | 按长度分 Short [0,8K]、Medium (8K,32K]、Long (32K,64K] |
| 单页 VQA | DocVQA、ChartQA、InfoVQA | 各自官方指标 |

正文未给出各评测基准的题目数或划分，此处不补数；Doc-750K 未报告自身的留出测试集。

阅读者分析：工作负载是“整份文档 + 一个问题 → 文本答案”的文档问答，与本项目中文档级抽取/问答类查询相关，但没有结构化输出或跨文档聚合任务。

依据：[CVPR 2025 Open Access，12 页](https://openaccess.thecvf.com/content/CVPR2025/papers/Duan_Docopilot_Improving_Multimodal_Models_for_Document-Level_Understanding_CVPR_2025_paper.pdf)，§3.2–3.3、§5，Tables 2–5，PDF pp.5–8。
