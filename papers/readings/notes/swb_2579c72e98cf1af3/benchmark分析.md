# 评测与边界

**设置**：SLM 为 MPNet，LLM 重排为 GPT-4o-mini；margin m=0.5，GDC 训练 30 轮、Valentine 10 轮；A100 GPU（规模实验用 CPU）。基线：COMA、COMA++、Distribution、SimFlooding（Valentine 实现），ISResMat，Unicorn（预训练模型）；Jaccard-Levenshtein 与 Cupid 因明显更差而未画出（§6.1，PDF p.8）。

**实验 1（GDC 端到端）**：四个 Magneto 变体在 MRR 和 Recall@GT 上都高于所有基线，Magneto-ft-llm 最高（Figure 6）。原文正文未给出图中各柱数值；渲染图显示 ft-llm 的 MRR 约 0.85 左右，最好基线约 0.4（阅读者读图估计，非原文数字）。

**实验 2（Valentine）**：各法准确率普遍远高于 GDC；Magneto 与基线持平或更优，唯一例外是 Unicorn，作者认为其训练用了 Valentine 构造数据而存在泄漏；在未用于训练的 Magellan 上 Unicorn 反而较差（Figure 7，§6.2，PDF p.9）。

**实验 3（规模）**：GDC 上 Magneto-zs-bp 运行 11–33 s，zs-llm 545–589 s 且随列数基本稳定；ISResMat 在 GDC 最小列数也未完成，Unicorn 只能处理前 100 列（§6.3、Figure 8，PDF p.9）。

**实验 4（消融）**：

| 消融 | 关键结果 | 位置 |
|---|---|---|
| 抽样（zs-bp + Srepeat） | Priority 在 GDC 上 Recall@GT 0.344、MRR 0.591，四个数据集多为最好或次好 | Table 4，p.10（已渲染核对） |
| 合成数据 | GDC 上 ft-bp MRR：mixed-aug 0.761、llm-aug 0.754、struct-aug 0.731；ft-llm MRR：llm-aug 0.866、struct-aug 0.798 | Table 5，p.11（已渲染核对） |
| 重排 | k=5 时 LLM 重排较二分图 MRR 0.731→0.780，Recall@GT 0.375→0.475 | §6.4，p.11 |
| 全模式直送 LLM | 准确率低于所有 Magneto 变体，单表可超 6,000 s | Figure 11，p.11 |
| 模型 | LLaMA3.3-70B 重排 MRR 0.837 对 GPT-4o-mini 0.815；配微调 MPNet 达 0.860 | Table 6，p.12 |

**边界**：作者承认若正确匹配不在 SLM 的 Top-k 中，重排无法补救；重排质量依赖提示；LLM 重排带来成本（§8，PDF p.12）。阅读者分析：GDC 只有 10 个表对且目标只有一个，标准差较大（Table 4–6 中常见 ±0.1–0.3），结论的统计稳定性有限；规模实验只用了 zs 变体（阅读者分析）。

依据：§6、§8、Tables 4–6、Figures 6–11，PDF pp.8–12。
