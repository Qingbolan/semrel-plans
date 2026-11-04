# benchmark

**标注质量**：DM 预处理工具（DisCoDisCo + 对齐脚本）相对人工：untyped F=83.74%，sourced F=43.46%（Table 3，PDF p.19）。人工一致性：RST-DT DM 识别 mutual F1=95、关系关联 88.8；GUM 92.3 与 90。次级边一致性第一轮 S/N/R=.311/.279/.223，修订指南后 .529/.49/.412，作者对比的主关系人类 R 约 .571（PDF pp.19–20）。非 DM 信号：人-人 anchored micro F1=0.805，系统-人 0.879（Table 5，PDF p.23；两者文档子集大小不同，作者说明不可严格比较）。

**解析基线**（§5.2–5.3，Tables 8–9，PDF pp.31–35）：主树用 DMRST（top-down）或 G&C（bottom-up）；连接词用 DisCoDisCo（DD）或词典基线（LX）；句法与共指用 AMALGUM；DM 归属/次级边用 Electra-base 二分类器。指标为 Parseval 风格 S/N/R/F（次级边的 N 实为方向）及信号检测/锚定。
| 设置 | 主树 R / F | 次级边 S / F | 信号检测 all |
|---|---|---|---|
| gold RST + gold NLP（上界） | 1.000 / 1.000 | 0.389 / 0.184 | 0.925 |
| gold RST + DD+AM | 1.000 / 1.000 | 0.369 / 0.174 | 0.824 |
| DMRST + DD+AM | 0.492 / 0.482 | 0.101 / 0.030 | 0.483 |
| G&C + DD+AM | 0.470 / 0.457 | 0.055 / 0.028 | 0.459 |

结论（原文）：给定正确主树时，次级边与信号可做；预测主树会导致级联错误（“catastrophic”）；LX 基线约使次级边分数减半。orphan 检测即使在金标准设置下也仅 0.176。

**边界**：基线明说是粗略概念验证，未做端到端联合模型；所有实验假设给定 EDU 切分和分词；只覆盖英语；非 DM 信号部分依赖金标准句法/共指自动诱导，评测中 gold NLP 行实际偏乐观。阅读者分析：Table 8 中 gold 行的“主树 1.000”是输入而非预测结果，不应当作系统成绩。

依据：[Computational Linguistics 51(1), 2025，ACL Anthology 2025.cl-1.3，50 页](https://aclanthology.org/2025.cl-1.3)，§4.1、§5，Tables 3、5、8、9，PDF pp.19–23、31–36。
