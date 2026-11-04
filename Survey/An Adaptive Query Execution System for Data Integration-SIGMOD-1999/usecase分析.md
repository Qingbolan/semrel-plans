# 具体用例

**原文示例 1：同一查询在三种条件下的不同处理**（§1.3、Figure 1，p.2）。查询为：

```sql
SELECT * FROM A, B, C, D, E
WHERE A.ssn = B.ssn AND B.ssn = C.ssn AND C.ssn = D.ssn AND D.ssn = E.ssn
```

假设传统优化器会给出 Figure 1b 的连接树。Tukwila 的行为取决于掌握的信息：

| 条件 | Tukwila 的做法 |
|---|---|
| 来源大小未知 | 不做完整优化，先启发式算一个部分结果（如 A⋈B），再决定下一步 |
| 表都很小 | 全部使用双流水连接、整条查询流水；内存超出时由溢出机制处理 |
| 表很大 | 用标准哈希连接，在 A⋈B 后断开流水 |

**大表情况下的两种运行时调整**：

- 重调度：若来源 A 超时，先执行 D⋈E；若 D⋈E 也超时，带着这一信息调用优化器，生成先用未阻塞来源的计划（类似 query scrambling）。
- 再优化：A⋈B 完成并物化后，若实际基数与估计差距大，唤醒优化器换成更便宜的计划（Figure 1c）。

**原文示例 2：collector policy**（§4.1，p.5）。同时联系来源 A、B，谁先送达 10 条元组谁胜出并停掉另一个；若 A 超时，则启用 C 并停掉 A、B。该 policy 写成事件-条件-动作规则，例如 `when threshold(A,10) if true then deactivate(coll1,B)`。

依据：[原文](https://www.cis.upenn.edu/~zives/research/adaptive_exec.pdf)，§1.3、§4.1、Figure 1，pp.2、5。
