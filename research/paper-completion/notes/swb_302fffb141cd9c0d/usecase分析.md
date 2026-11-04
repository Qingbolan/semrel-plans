# 具体用例

Figure 1 以“1972 年美国众议院选举”表为例（列：District、Incumbent、Party、Result、Candidates）。

| 陈述 | 标签 | 所需推理 |
|---|---|---|
| John E. Moss 和 Phillip Burton 都连任 | ENTAILED | 两行查找 |
| John J. Mcfall 竞选无对手 | ENTAILED | 单元格语义 |
| 有三位来自民主党的现任 | ENTAILED | 条件过滤 + 计数 |
| John J. Mcfall 尽管无对手却未能连任 | REFUTED | 语言理解 |
| 共有五名候选人，两名民主党、三名共和党 | REFUTED | 复合事实，需验证三个子问题 |

Figure 3 演示 LPA 对“民主党人比共和党人多”的程序：`Greater(Count(Filter(T, incumbent==democratic)), Count(Filter(T, incumbent==republican)))`，执行返回 True，判为 ENTAILED。

阅读者分析：该用例对应一种“在表上判定自然语言断言真假”的语义谓词；若用于语义查询系统，可把它看成对（表，断言）对的布尔过滤，其中一部分可下推为聚合程序，另一部分仍需语言模型判断。

依据：[ICLR 2020 会议版，arXiv:1909.02164v5（2020-06-14），25 页（含附录）](https://arxiv.org/pdf/1909.02164v5)，§1、§3.1，Figures 1、3，PDF pp.2、6。
