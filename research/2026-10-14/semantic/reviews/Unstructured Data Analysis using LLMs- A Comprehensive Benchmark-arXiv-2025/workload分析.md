# workload分析

| v1数据集 | 表2文件数/属性数 | 平均token | 输入及来源 |
|---|---:|---:|---|
| WikiArt | 1000/19 | 789 | 艺术家文字及画作图片，WikiArt |
| NBA | 225/28 | 8047 | Wikipedia球员、球队、经理、城市文档 |
| LCR/Legal | 566/19 | 5609 | AustLII澳洲判例；正文另说570 |
| Finance | 100/30 | 130633 | Enterprise RAG Challenge公司报告，文本/图片 |
| Healthcare | 100000/51 | 10649 | MMedC文档，疾病、药物、机构及其他类别 |

环境数据：任务数据是上述文档与显式join关系，通常无额外外部知识环境；attribute descriptions/schema属于查询规范，ground truth关系表属于评测环境且不应作为待测系统输入。Finance先用MinerU解析PDF；输入对象含text、image URL、metadata。Healthcare从680000抽100000，三主类别共6100文档由人工标属性，其余NULL来自类别判断，不能称100000全人工属性gold（§3.2–3.3）。

§4.6并发实验为1/2/4/8线程，不是每prompt塞1/2/4/8文档。§4.7的512token块上限、128下限是chunk参数，也不是batch size。正文无通用prompt batch合同；不要用文件总数替代batch。论文240条与本地6个数据集代表query或目录数量不能直接互换。

来源：[原论文](https://arxiv.org/abs/2510.27119v1)。本分析据所列版本全文核读，未复现实验。
