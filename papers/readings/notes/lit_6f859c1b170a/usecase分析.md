# 具体用例

**例 1：美国众议院前议员表**（Example 1、Figure 1）

不完整元组来自"美国众议院在世前议员名单"：`Bob Riley | Alabama | District=NA | Birth Date=NA | Party=NA`。

- 数据湖中 T1"第 107 届国会众议员名单"有 400+ 元组，只有 Bob Riley 那一行给出 District=AL-3、Party=R。
- T2"阿拉巴马州在世前州长"给出 Bob Riley 出生日期 1944 年 10 月 3 日。
- T3"2002 年州长选举"提到 Bob Riley（共和党）得票 49.2%，与党派相关但不是填补所需的主要证据。

这说明单个元组的缺失值可能分散在多张表、多个元组里，表级检索会带入大量无关行（阅读者分析：这正是 LakeFill 选择元组级索引的直接理由）。

**例 2：两阶段填补**（Figure 4）

球员 Julius Peppers 缺 2013 team 与 position。Stage 1 严格模式下，检索证据支持 position=Defensive end（置信度 0.95），但对 2013 team 拒绝填补；Stage 2 宽松模式结合模型自身知识给出 2013 team=New York Giant，置信度 0.5 并标记为宽松结果。

**例 3：重排标注清单**（Figure 3）

不完整元组为北约克郡博物馆表中的 National Railway Museum（town/city、region 缺失），候选来自澳大利亚维多利亚州博物馆表。GPT-4o 判定"存在性=Yes、相关性=Somewhat Relevant、一致性=Partially Consistent"；作者用该例说明清单仍可能把不相关候选标为正例，因此再用分层训练组降低标签噪声。

依据：PVLDB 18(10)，§1、Figure 1，pp.3354–3355；§4、Figure 3，pp.3357–3358；§5、Figure 4，pp.3359–3360。
