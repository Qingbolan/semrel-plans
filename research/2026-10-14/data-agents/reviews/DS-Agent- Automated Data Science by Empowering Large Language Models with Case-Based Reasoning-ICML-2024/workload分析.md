# workload分析

[论文原文](https://arxiv.org/html/2402.17453v2)

§4.1：30 个任务，文本、时间序列、表格三种输入，分类与回归两类目标；12 个开发任务、18 个部署任务。数据输入为各任务的 train/valid/test，环境知识是 Kaggle 人类经验库与成功代码库。不能将30任务写成一批30行输入；论文没有统一输入记录 batch size。原始自然语言指令应从官方 benchmark 配置逐条提取，本次不将本文概括写入 query JSON。
