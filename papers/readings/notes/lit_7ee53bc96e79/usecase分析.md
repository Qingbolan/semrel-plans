# 具体用例

附录 D 的 xlong Hi-C 任务：为基因组组装人工校正生成 Hi-C 接触图（test35 中的 “Hi-C contact map for curation”，Table 8 记为 20 个工具、深度 17）。使用 batch-4 tactic 快照的 PRTE Agent 依次：

1. 记录允许的文档与受限来源；加载 Hi-C、组装 QC、live-schema、本地检查等 tactic；建立幂等 notebook；
2. 把任务描述映射为输出义务（单倍型、gap/端粒轨迹、Hi-C 统计、Pretext 接触图、覆盖度）；
3. 写 gxformat2、转换并 lint；在服务器端导入 URL、建立 Hi-C 与 PacBio 集合、导入并调用；
4. 旧版 BWA-MEM 包装器终止失败后保留失败证据，依次改用 minimap2、BWA-MEM2，并在 schema 相关失败后移除可选的 PretextSnapshot；
5. 最终完成 22 个 Galaxy 作业、17 个工作流输出并打包断言轨迹（Fig.9，PDF p.16）。

作者也承认该图并非专家工作流的完美复现，xlong 任务的分支拓扑恢复和可选输出推理仍困难（§D.4，PDF p.17）；Fig.5 中 GEPA 在该案例以更低 token 走完全部里程碑（§4.5，PDF p.6）。

依据：[arXiv 2606.20839v1，18 页](https://arxiv.org/pdf/2606.20839v1)，§4.5、附录 D、Fig.9，PDF pp.6、15–17。
