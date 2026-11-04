# 具体用例

论文 Figure 2 的多跳问题：“Never Too Loud 的表演者成立于哪座城市，该城市的城堡叫什么名字？”（§3，PDF p.3）

1. **构图**：从不同文本块中抽取原子事实，例如“Never Too Loud 是加拿大硬摇滚乐队 Danko Jones 的第四张录音室专辑”“Danko Jones 是来自多伦多的加拿大硬摇滚三人组”。关键元素 Danko Jones、Toronto、Canada、Album、Casa Loma 等成为节点。
2. **计划**：先找出与“Never Too Loud”相关的表演者，再确定其成立城市，最后找该城市著名的城堡。
3. **探索**：从相关初始节点读取原子事实，用 `read_chunk` 把块 1、3、5 放入队列；读块后更新笔记，经 `read_neighbor_node` 到达相邻节点，信息足够后调用 `termination`。
4. **作答**：笔记记录“表演者是来自加拿大多伦多的 Danko Jones”“文中提到多伦多的城堡是 Casa Loma”，最终答案为 Casa Loma。

这个流程可看作“文档→实体/事实图→按问题分解遍历”的半结构化检索。若在数据系统中复用，图可按文档预先构建并缓存，查询时只付探索成本；论文在 §4.4 也指出单文档多问题场景下可摊薄成本（阅读者分析）。

依据：§3、Figure 2、§4.4，PDF pp.2–4、8。
