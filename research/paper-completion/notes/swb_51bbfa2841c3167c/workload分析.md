# 工作负载

**TimeBankNT**（§4，PDF p.6）：重标 TimeBank-Dense 使用的 36 篇 TimeBank 新闻（同时也用于 MATRES 与 TDDiscourse），美式英语。含原有 1,715 个事件、289 个 timex。两套独立标注，每套包含：

| 项 | 数量 |
|---|---|
| 事实性标注 | 1,715 |
| 事件–事件 tlink | 79,001 |
| 事件–timex tlink | 23,979 |
| timex–timex tlink | 1,770 |
| 合计（不含逆关系） | 102,313；含逆关系 204,626（脚注 2） |

注意：§4 正文另称每位标注者的 tlink 总数为 207,496，与脚注 2 的 204,626 不一致，原文未解释（阅读者分析）。

**密度**（Table 4，PDF p.8）：tlink/(事件+timex) 比值为 51.05，MAVEN-ERE 9.43，TimeBank-Dense 7.40。

**建模划分**（§5）：30 篇训练、6 篇测试；无开发集说明。文档最长约 2,000 token（正文另处称最长约 4K），整篇输入编码器。关系分布：Before/After 约 30%、Vague 约 15%、Includes/Is_included 与 Simultaneous 各约 8%、Overlap 约 0.2%（脚注 14）。

**标注成本**：项目后期每篇 TimeBank 文本约 20–30 分钟（§4，PDF p.8）。
