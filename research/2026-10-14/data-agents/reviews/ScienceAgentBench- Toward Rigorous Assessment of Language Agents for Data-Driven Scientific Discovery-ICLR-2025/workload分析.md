# workload分析

[论文原文](https://arxiv.org/html/2410.05080v2)

输入包含细胞图片、分子、地图和EEG等异构数据。任务的目录预览帮助定位文件；可选领域知识是环境上下文，不能放入硬件栏。Table 1原文示例：“Train a multitask model on the Clintox dataset to predict a drug’s toxicity and FDA approval status.” 对应输入为Clintox数据，输出模型预测，成功阈值ROC-AUC≥0.77。未逐条获取数据文件前，不编造列名或记录数。
