# 评测与边界

**设置**：主模型为 GPT-3-175B（text-davinci-003，不微调）；另测 GPT-J-6B、LLaMA2-7B 的轻量微调（§5.1，p.7）。指标：填补和转换用准确率，检错和实体解析用 F1（§5.1，p.8）。

**实验 1（四类任务对比 SOTA，Tables 1–4）**：

| 任务/数据集 | 最强非 UniDM 基线 | UniDM |
|---|---|---|
| 填补 Restaurant | FM(manual) 88.4 | 93.0 |
| 填补 Buy | FM(manual) 98.5 | 98.5 |
| 转换 StackOverflow / Bing | FM 65.3 / 54.0 | 67.4 / 56.0 |
| 检错 Hospital / Adult | FM 97.1 / 99.1 | 99.8 / 99.7 |
| 实体解析 Beer | FM(manual) 100 | 96.3 |
| 实体解析 Amazon-Google | Ditto 75.6 | 64.3 |
| 实体解析 iTunes-Amazon | FM(manual) 98.2 | 96.3 |
| 实体解析 Walmart-Amazon | FM(manual) 87.0 | 88.2 |

（Tables 1–4，pp.8–9）实体解析上 UniDM 在 4 个数据集中有 3 个低于最强基线（阅读者分析）。作者把落后解释为领域词汇罕见，Ditto 用领域数据微调、FM 人工选例（§5.2，p.9）。

**实验 2（模型与成本，Tables 5–7）**：Walmart-Amazon 上微调后的 GPT-J-6B 为 86.6、LLaMA2-7B 为 89.4，未微调 LLaMA2-7B 只有 40.6。换用 GPT-4-Turbo 时 Restaurant 填补为 96.5。每查询 token：FM 174/246，UniDM 6,860/7,323（Restaurant/Buy）（pp.9）。

**实验 3（消融，Tables 8–10）**：Restaurant 填补从无组件 82.6 到全组件 93.0，其中仅属性级检索即到 90.7（p.10）。

**附录**：连接发现在各阈值下 F1 均高于 WarpGate（Figure 5，只给图）；SWDE NBAplayer 信息抽取 UniDM 70.1，低于 Evaporate-code+ 的 84.6（Table 11，p.17）。

**边界**：作者承认领域数据上不可靠、可解释性弱、计算开销增加，且不能完全替代传统方法（§6.1，p.11）。阅读者分析：未报告测试集规模、方差或多次运行；FM 为作者复现；GPT-3 与微调对比使用不同模型。

依据：§5–6.1、Tables 1–11，PDF pp.7–11、17。
