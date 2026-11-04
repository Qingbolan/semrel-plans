# Adapting to Source Properties in Processing Data Integration Queries

数据集成系统对远程来源的基数、顺序和可预聚合程度几乎一无所知，静态优化常选到产生巨大中间结果的计划。Ives、Halevy、Weld 在 Tukwila 中提出自适应数据分区（ADP）：把来源数据切成若干区段，交给不同的互补计划执行，切换计划时复用已建好的状态，最后用 stitch-up 阶段补齐跨区段的连接组合。

论文把 ADP 用于三件事：执行中纠正错误的基数/选择率估计（corrective query processing）、推测并利用来源的有序性（互补 merge/hash join 对）、按窗口自适应预聚合。在 TPC-H/偏斜 TPC-D（100MB）上，无统计信息时纠错执行通常能恢复到较好计划，每个查询只切换 1–4 个阶段，stitch-up 几乎完全复用先前中间结果；自适应窗口预聚合在无收益时只增加约 1.5% 开销。

[原文](https://repository.upenn.edu/bitstreams/4e226484-c748-49a8-bea6-5c2793285197/download)

版本：SIGMOD 2004（Paris），DOI 10.1145/1007568.1007613，PDF 12 页。2026-10-07 初读，2026-11 按全文（§1–8、Tables 1–3、Figures 1–6）重新核对数字；未复现实验。
