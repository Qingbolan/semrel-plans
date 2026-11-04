# benchmark

**设置**：SVMhmm 序列标注，以句子为单位，上下文窗口 C=4；特征集 FS0 n-gram、FS1 结构/句法、FS2 LDA 话题与情感、FS3 语义角色/共指/篇章关系、FS4 词向量求和；指标为 token 级 11 类 Macro-F1（§5.1.1–5.1.3，PDF pp.33–36）。基线包括随机、全部预测为 O、只用 FS0。

**主要结果**
- 全数据 10 折（Table 9，PDF p.37）：人类 Macro-F1 0.602（去掉 rebuttal/refutation 为 0.707）；随机 0.071；全 O 0.065；FS0 为 0.156；最佳为 FS01234 与 FS234，均为 0.251（与其他组合差异 p<0.001）。Rebuttal 与 Refutation 的 F1 接近 0。
- 话题内部（Table 10，PDF p.38）：汇总最佳为 FS01234，0.236。
- 跨领域（Table 11，PDF p.38）：只用 FS4 词向量的汇总值为 0.209，其他组合不超过 0.122。
- 其他指标（Table 13，PDF p.42）：最佳系统 αU 为 0.30（人类 0.48，只在部分数据上测）；边界相似度为 0.32（人类 0.70）。
- 句子级近似的上限：一个总能给出正确句子标签的 oracle 在 token 级评测下 Macro-F1 为 0.906（PDF p.34）。

**边界**：token 级 11 类评测非常严格，边界错误与类型错误同等扣分；预处理工具在新闻语料上训练，迁移到用户生成内容会掉点；每篇文档一个论证、只做 logos、句子级近似都是简化（§5.1.7，PDF pp.41–42）。错误分析显示，各类别约一半样本被误判为 O，backing 与 premise 易混淆（§5.1.5，PDF p.39）。

依据：[Computational Linguistics 43(1):125–179, 2017（ACL Anthology J17-1004），55 页](https://aclanthology.org/J17-1004)。
