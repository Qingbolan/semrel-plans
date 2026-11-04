# CADENZA: Compiling Natural-Language Intent into Task-Specific Operator DAGs for Semantic Query Processing

[arXiv 2606.29151v3](https://arxiv.org/abs/2606.29151v3)

Jaehyun Ha、Yongjoo Park、Wook-Shin Han；2026-07-13版本。2026-10-14阅读本地27页PDF：正文§1–9，附录A–J，算法1、表1–20及query附录；视觉核对物理计划构造页。首页仍有SIGMOD’27与2018/占位DOI混用，不能据模板认定会议录用。

对象是已绑定输入关系的一个semantic operator instance，将其拆解为带类型的任务DAG，再联合调参。它支持按记录路由、批量推理、相同意图的计划缓存；跨多个语义算子联合优化不属于本文主目标。
