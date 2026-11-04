# 具体用例

**原文查询**（§5.2，p.956）：找出指定国家、账户余额较高的客户在指定日期之后发货的明细。

```sql
select *
from customer c, orders o, lineitem l
where c.custkey = o.custkey and
      o.orderkey = l.orderkey and
      c.nationkey = 1 and
      c.acctbal > 9000 and
      l.shipdate > date '1996-01-01'
```

**出错过程**：lineitem 按 shipdate 升序到达。早期到达的 lineitem 几乎都不满足 `shipdate > 1996-01-01`，lineitem 上谓词的选择率看起来远低于 customer，于是 eddy 把 orders 元组送去与 lineitem 连接。这些 orders 元组被存进 lineitem ⋈ orders 的状态里。

**纠正过程**：在 eddy 看到约 55% 的 orders 元组时选择率发生变化；STAIRs 把已存的这批 orders 元组一次性迁移到另一个连接（与 customer 的连接），此后性能几乎等同于一开始就路由正确。EddyJoins 只能改变后续路由，旧状态仍在，因而明显更慢（Fig. 7(i)）。

**迁移成本**（Fig. 7(ii)）：限制 eddy 在看到一定比例的 orders 元组前不得改路由或迁移。在约 55% 处迁移时，迁移成本约占 STAIRs 总执行成本的 7%；推迟越久，要迁移的元组越多、收益越小，但 STAIRs 仍好于 EddyJoins，只有在最后才迁移整个 orders 关系时例外（已无收益）。

**SteMs 的表现**：本查询中间结果复用很少，但 SteMs 仍较差，因为它无法避免让后到的 lineitem 元组与 orders 连接——要避免，就必须物化 customer ⋈ orders 的中间结果（§5.2）。

阅读者分析：这里的“错误”完全来自到达顺序与选择率外推，不是因为数据语义不同；Fig. 7 只以柱状图给出秒数，正文没有列出各方案的具体时间。

依据：[VLDB 2004](https://www.vldb.org/conf/2004/RS24P2.PDF)，§5.2、Fig. 7，pp.955–956。
