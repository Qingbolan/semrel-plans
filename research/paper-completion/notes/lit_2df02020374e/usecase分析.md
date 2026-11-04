# 具体用例

Figure 9 的 DSB 10x Query081：查询含 CTE `customer_total_return`，外层用相关子查询比较 `ctr_total_return > AVG(...)*1.2`，原始延迟 300 s。

| 方法 | 选用规则 | 改写后延迟 |
|---|---|---|
| LearnedRewrite | FILTER_SUB_QUERY_TO_JOIN、AGGREGATE_PROJECT_MERGE 等多条 | 19.46 s |
| GPT-4 | 无 | 300.00 s |
| R-Bot (GPT-4) | FILTER_INTO_JOIN、FILTER_SUB_QUERY_TO_JOIN、AGGREGATE_PROJECT_MERGE | 2.83 s |

R-Bot 下推了只涉及单表的过滤条件，并去掉了耗时的子查询；作者认为 LearnedRewrite 在错误代价引导下选了过多规则。

第二例 Calcite `TestJoinConditionPush6`：R-Bot 选 JOIN_CONDITION_PUSH，推导出额外条件 `e.deptno = e.empno` 下推到 `emp` 一侧，15.50 s 降至 1.66 s，其他方法无改进。

依据：[arXiv:2412.01661v2](https://arxiv.org/pdf/2412.01661v2)，§7.4、Figure 9，PDF p.12。
