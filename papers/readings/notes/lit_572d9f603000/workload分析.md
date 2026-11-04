# 工作负载

| 项目 | 原文描述 |
|---|---|
| 数据集 | Amazon-2014 评论基准中的 Baby、Beauty、Pet 三个子集（§4.1） |
| 预处理 | 去除交互少于 5 次的用户和物品；留一法（leave-one-out）划分 |
| 骨干 | SASRec、HSTU |
| 指标 | Recall@K、NDCG@K，K∈{5,10}；模型选择统一用验证 NDCG@10 |
| 预算 | 网格搜索枚举全部 729 个配置；贝叶斯优化 500 次试验；VirtualMLE/OPRO 的预算上限正文未明说 |
| LLM | 主实验 VirtualMLE 与 OPRO 均用 GPT-5.4；§4.5 另试 Kimi 2.6、DeepSeek V4 Pro |
| 重复 | 所有方法结果为三次独立运行平均 |

论文未给出三个数据集的用户数、物品数、交互数等统计表。大型生成式推荐器（Tiger、ReaRec、Lc-Rec、OpenOneRec）的数值沿用 OpenOneRec 技术报告 [18] 的实验设置。

阅读者分析：工作负载是“模型调参任务”，而非查询或文档处理负载；与本项目语义查询优化的关系在于“LLM 驱动的、带反馈的配置搜索”，不能当作语义算子数据集。

依据：[arXiv:2606.03221v1，7 页](https://arxiv.org/abs/2606.03221)，§4.1、§4.5，PDF pp.3、6。
