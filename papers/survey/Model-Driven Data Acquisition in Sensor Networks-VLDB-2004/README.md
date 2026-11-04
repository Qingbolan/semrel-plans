# Model-Driven Data Acquisition in Sensor Networks

把传感网络当作“数据库”会带来两个问题：读数只是物理世界的离散、非随机样本，并不完整；而主流做法（如 TinyDB）每次都尽量读取所有传感器，能耗远超得到可靠近似答案所需。Deshpande、Guestrin、Madden、Hellerstein、Hong 提出 BBQ：用历史数据学到的随时间变化的多元高斯模型回答查询，查询带误差容限 ε 和置信度要求；只有当模型本身不够确定时，才选择一组读数去实际获取，选择时权衡置信度的提升与采集、通信能耗。

在 Garden 真实轨迹上，要求 95% 置信度、误差 0.5°C 时，每次查询的期望能耗从 5.4 J 降到不足 150 mJ，约 40 倍；错误率基本控制在设定的 5% 以内。

[原文](https://ai.stanford.edu/~guestrin/Publications/VLDB04/vldb04.pdf)（[作者站点副本](https://ai.stanford.edu/~guestrin/Publications/VLDB04/vldb04.pdf)）

版本：VLDB 2004（Toronto），pp.588–599。2026-10-07 初读；2026-11 按 VLDB 官方 PDF 全文核对 §1–6 与 Figures 4–8；未复现实验。

另见：[出版方版本](https://www.vldb.org/conf/2004/RS16P1.PDF)。
