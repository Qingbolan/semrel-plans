# usecase分析

斑马/羚羊共现属于Wildlife Q7：输入是一张包含图片列和city/station列的表，语义调用读图片，关系逻辑判断同一city是否同时存在两类动物。不能把“统计斑马照片”写成输入数据本身；那是任务意图，输入是照片记录表。§5.4解释更多行让系统更容易找到每个city的支持证据。

Movie Q7是真实的评论语义join测试。表4(a)给LOTUS费用$1.81、Quality .21、431.8s；Palimpzest$7.72/.68/1056.1s；ThalamusDB$.15/.57/636.9s；BigQuery$3.31/.70/198.3s。应关联作者具体SQL文件及其输入表，不能只显示两个SCAN节点替代输入说明。

MMQA航空公司logo匹配（例4.5）把airlines文本与image配对，输入两列跨模态；本地英文自然语言描述若从SQL翻译而来，应另列description而非覆盖source_query。

来源：[原论文](https://arxiv.org/abs/2511.01716v2)。本分析据所列版本全文核读，未复现实验。
