# 工作负载

| 集合 | 任务数 | 工具总数 | 平均工具数 | 平均深度 |
|---|---|---|---|---|
| BioWorkflow train26 | 26 | 322 | 12.38 | 10.62 |
| BioWorkflow test35 | 35 | 455 | 13.00 | 11.34 |
| BioAgent Bench full | 10 | 62 | 6.20 | 5.80 |

（Table 1，PDF p.3）test35 按规模分层：small 5、medium 10、long 10、xlong 10（Table 2 表头）；§3.1 称其“balanced across sizes”，实际 small 只有 5 个。

任务来源为 IWC（同行评审的 Galaxy 工作流）和 GTN 教程，主题覆盖 RNA-seq、ChIP/ATAC、Hi-C、宏基因组 MAG、VGP 基因组组装、SARS-CoV-2 变异、蛋白组学、分子对接等（Tables 7–8，PDF pp.9–10）。每个任务记录工具数、最长依赖链深度、输入数和可用断言数；部分任务断言数为 0。

BioAgent Bench 不提供金标准 Galaxy DAG，其工具/深度统计用的是作者 Galaxy 运行的工具数和评测器步骤数代理（附录 B，PDF p.8）。

运行环境：本地沙箱含 Python notebook、BioBlend、gxformat2、Planemo、任务清单、公开文档（Table 9 列 7 个文档仓库）和 usegalaxy 执行后端（§3.1、附录 B）。求解器通过 Codex CLI 使用 gpt-5.5、xhigh reasoning（Fig.6，PDF p.11）。

阅读者分析：这是长时程、带真实外部服务的代理工作负载，单位是“工作流任务”，不是查询或表；结果依赖公共服务器排队、工具版本和数据可得性（Limitations）。

依据：[arXiv 2606.20839v1，18 页](https://arxiv.org/pdf/2606.20839v1)，§3.1–3.2、Table 1、附录 B，PDF pp.3、8–11。
