# 公共部门综述驱动候选发现

下载原论文Agent Benchmarks Fail Public Sector Requirements（arXiv2601.20617），读取方法及§5。其六项标准不同于本项目A–H；不能用其“无benchmark全部满足”作为本项目无解证明。论文宽检索1300余篇，经分阶段筛选图示640→518 agentic→308 realistic→94 process→8 public-sector→0 metrics；不可将1300当作逐一满足我方筛选的公开数据。尚未取得完整筛选清单/仓库。

从其原始参考定位两条线索：LawReasoningBenchmark（cocacola-lab官方repo；论文2025.findings-acl.887）及AI for Climate Finance（最终论文2026.eacl-demo.34已下载）。前者待原材料审计，不直接计候选。

气候金融最终论文附录E称500文档/20000专家片段、350train文档；主任务按项目计算EWS总预算及pillar预算。短taxonomy与长原始项目报告的角色须分开，不能把报告长度当共享E。脚注写将开放代码/标注，附录称CSV/PDF随supplement发布，尚需取得实际附件核对版本/数量；不采用旧稿298行作为现版计数。没有本次数据运行、20gold审计或Strong升级。

下一步优先确认最终论文附件是否实际包含数据，再判断固定预算抽取任务是否满足共享环境必要性。论文作者的准确率不等于本次复现或同资源LOTUS不足。

来源：https://arxiv.org/abs/2601.20617；https://aclanthology.org/2026.eacl-demo.34/；https://github.com/cocacola-lab/LawReasoningBenchmark 。


## 气候金融发布入口核验

已下载ACL官方源元数据2026.eacl.xml并抽取demo论文34记录。该记录没有supplement/附件条目；论文网站也只列PDF。论文附录称数据在supplement中，与当前可观察发布入口不一致，记录缺口，不推断作者从未发布。论文正文及元数据仍写“将开放”代码与标注。部署站点本轮web工具返回Internal Error，不能用该错误证明网站永久下线。搜索未定位匹配官方仓库；同名Climate Finance Bench（Pladifes）是其他论文，不混用。

| Query | 数据湖1 | 数据湖2 | 数据湖3 |
|---|---|---|---|
| 按项目识别EWS活动并汇总各pillar预算 | 500报告为论文所称规模；实际未取得 | 20000标注片段为论文所称，非已下载gold | 附录四pillar及cross-pillar分类定义；不是47页报告本身 |
| 类Python DAG | parse → align(amount,activity) → classify → groupby(project,pillar).sum | evaluator-only | 固定定义可供所有方法使用 |

| LOTUS预期结果 | LOTUS过程 | Agent预期结果 | Agent过程 | operator结构 |
|---|---|---|---|---|
| 未执行、未知 | 固定文本表格解析、检索、分类与聚合 | 未执行、未知 | ==检查跨行金额归属、重复预算、活动范围== → 分配与聚合 | 待真实案例，不从87%作者结果推断动态必要性 |

四臂状态：task-only缺报告不能执行；完整E固定流程、逐案Agent、共享批Agent均无本次匹配实验。暂保留线索，不继续以论文数量增加Strong计数；所缺为实际报告/标注资产、长共享E必要性与同资源D/E证据。
