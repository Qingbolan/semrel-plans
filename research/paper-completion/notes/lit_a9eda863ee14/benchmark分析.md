# 评测与边界

**实验 1（微调，SOTAB-91，Micro-F1）**：Table 3，p.10。

| 模型 | 训练数据 | Micro-F1 |
|---|---|---|
| ArcheType-LLAMA+ | LLAMA + SOTAB-91 | 85.97±0.6 |
| DoDuo | VizNet + SOTAB-91 | 84.82±0.6 |
| ArcheType-LLAMA | LLAMA + SOTAB-91 | 82.9±0.6 |
| TURL | TURL-Tables + SOTAB-91 | 78.96±0.7 |

**实验 2（零样本，加权 Micro-F1）**：Table 4，p.10，摘录 ArcheType 与较好基线。

| 架构 | 方法 | SOTAB-27 | D4-11 | Amstr-54 | Pubchem-15 |
|---|---|---|---|---|---|
| UL2 | ArcheType | 58.0 | 70.8 | 32.8 | 61.1 |
| T5 | ArcheType | 60.8 | 74.5 | 25.6 | 63.3 |
| T5 | C-Baseline | 50.0 | 75.0 | 8.5 | 59.0 |
| GPT-3.5 | ArcheType | 64.3 | 83.0 | 22.5 | 60.2 |
| GPT-3.5 | K-Baseline | 57.2 | 80.9 | 7.9 | 55.8 |

基线说明：C-Baseline 仿照 Chorus，使用 C 提示、相似度重映射和随机采样；K-Baseline 仿照 Korini & Bizer，使用 K 提示、不重映射、取前 k 个样本（§5.1）。两者都由作者改造，并非原系统。T5 上 C-Baseline 在 D4-11 上为 75.0，略高于 ArcheType 的 74.5，属于误差范围内的"持平"（阅读者分析）。

**实验 3（已有基准，Table 5）**：在 T2D 上，ArcheType-ZS-GPT4 的加权 F1 为 95.3，Chorus-ZS-GPT 为 92.3；在 VizNet-Chorus 上，Sherlock-FT 为 93.0，ArcheType-ZS-GPT4 为 90.5。

**消融**：
- ArcheType 采样优于随机采样和取前 k 个（Fig. 4）。
- 样本数从 3 增到 10 时性能上升，CONTAINS+RESAMPLE 在每个样本规模下都最好（Fig. 5）。
- 增加表名、统计、其他列等特征对微调有益，对零样本有害（Fig. 6）。
- 提示效果因模型而异（Table 6）。
- 参数量不能预测性能，编码器-解码器架构优于仅解码器（§5.4.3，细节在另一份技术报告中）。

**局限**（§5.5，pp.12–13）：上下文窗口限制了样本数和类数；参数量大，带来延迟和能耗；零样本难以利用额外特征；对纯数值列意义有限；标签集变大时性能下降（Fig. 7）。

阅读者分析：新基准是合成的独立列，缺少表级上下文，Amstr 上所有方法都很低。GPT 结果对应特定日期的版本，作者自己也强调闭源模型不可复现。

依据：§5，Tables 3–6，Figures 4–7，pp.9–13。
