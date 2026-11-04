# 具体用例

**层级表格问答（HiTab，Figure 2(c)，PDF p.3）**：输入是一张"美国国防部研发、测试与评估拨款（按机构，2015–18）"的层级表，行层级为 department of defense / defense advanced research projects agency 等机构，再分 rdt&e、total research、basic research。

- instruction：说明这是层级表格问答任务，表格可能是层级的。
- input：`[TLE]` 表题 + `[TAB]` 序列化的多级行列。
- question：DARPA 的 basic research 在 2016 至 2018 年间增加了多少美元？
- response：80.3（即 458.4 − 378.1）。

该任务需要模型理解多级结构、定位单元格并做算术。TableLlama 在 HiTab 上执行准确率 64.71，高于作者列出的 SOTA 47.00（Table 2，PDF p.6）。

**另一用例（列类型标注，Figure 2(a)）**：给定 1958 年日本职棒中央联盟投手榜，模型从 Freebase 候选中为 player 列选出 sports.pro_athlete、baseball.baseball_player、people.person。

若在本项目中把它当作"语义抽取/语义过滤"算子，需要注意原文每次只针对一张表的一列或一个问题，候选池在提示中显式给出（阅读者分析）。
