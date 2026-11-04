# Deshpande, Hellerstein — Lifting the Burden of History from Adaptive Query Processing

Eddy 可以逐元组改变算子顺序，但早先的路由决定会以中间结果的形式留在连接算子的状态里，之后即使改了路由，新到的元组仍要按旧顺序与这些状态连接——作者称之为“路由历史的负担”。本文提出 STAIR 算子：把连接内部的状态暴露给 eddy，并提供 promotion（提升）与 demotion（降级）两个状态操作，使 eddy 能迁移状态、撤销过去的路由决定；附录 A 证明任意施加这些操作后结果仍然正确。

在 PostgreSQL 7.3 中实现后，475 组随机合成实验里 STAIRs 几乎在所有设置中快于静态 SHJ 和 SteMs，许多设置差一个数量级以上；与 EddyJoins 相比约 66% 的设置差距在 10% 内，其余多数 STAIRs 更快（最多约 10 倍），最坏慢 2.25 倍（§5.3）。

[原文](https://www.vldb.org/conf/2004/RS24P2.PDF)

版本：VLDB 2004（第 30 届，多伦多）论文集 pp.948–959，12 页（vldb.org 链接直接下载返回 403，本轮使用 Wayback Machine 存档的同一官方 PDF）。阅读范围：2026-11-04 重读 §1–7 与附录 A 并核对数字；附录证明未逐步验证，未复现实验。STAIRs 是本文方法，SteMs 是对照架构，两者不要混称。
