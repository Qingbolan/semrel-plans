# DataSpace 单轨迹算子原型：结果与否定边界

工程链路已跑通：真实来源 → 1条 native Codex 示范 → 1次自动提取 → 冻结Python/applicability → 300条后续记录 → 私有评分与成本分析。当前任务未通过“killer task”筛选，也没有在本次300条整批比较中获得包含学习开销的token收益。

## 300条后续记录

| 系统 | 完成且精确正确 | ABSTAIN | 应选104条元组 | 本次执行tokens |
| --- | ---: | ---: | ---: | ---: |
| Native Codex，整批共享计划/代码 | 299/300 | 1 | 全部正确 | 252,075 |
| 同一单轨迹冻结算子 | 299/300 | 1 | 全部正确 | 0 |
| 手写固定SQL控制 | 300/300 | 0 | 全部正确 | 0（人工构造成本未知） |

两种Agent相关方法在同一条记录上拒绝，公开源的本日基准收益率为NULL；没有把未知值自动改成事实标签。SQL控制按正值筛选排除NULL。原始输出不修改，拒绝计入全量分母。三个系统的选中数均为104，count误差0；下游F1=1不能代替逐记录coverage。

## 16条开发筛选及接口审计

| 系统/传输 | 筛选正确 | 严格名称+范围正确 | Coverage | Token使用 |
| --- | ---: | ---: | ---: | ---: |
| 传统LOTUS sem_map / Chat | 14/16 | 11/16 | 14/16 | 已知156,455，另2次usage未知 |
| 传统LOTUS sem_map / Responses | 16/16 | 13/16 | 16/16 | 242,905 |
| Native LOTUS agentic batched / Chat，修正usage适配后 | 8/16 | 8/16 | 8/16 | 已知120,238，另2次usage未知 |
| Native LOTUS agentic batched / Responses，忠实投影原生结果 | 16/16 | 14/16 | 16/16 | 351,658 |
| Native Codex整批 | 16/16 | 16/16 | 16/16 | 318,587 |
| 冻结算子 | 16/16 | 16/16 | 16/16 | 0 |
| 手写SQL | 16/16 | 16/16 | 16/16 | 0 |

静态/agentic的已完成结果均正确筛选并保留完整投资范围；严格匹配失分来自另一种公开简称字段。Chat静态3条、Responses静态3条、Responses agentic2条属于此类。v1未充分指定多个简称字段中的哪一种，因此这些差异不能证明推理能力或资源增益；不据此宣布静态质量差距。详细可追溯分类保存在[证据目录](../artifact/evidence/dataspace-amortization-20260906)。后续澄清必须另立任务版本，而非悄悄改本轮分数。

Chat静态的1次HTTP403与1次超时导致2条ABSTAIN；agentic的2次HTTP403导致两分片共8条ABSTAIN。更早的agentic适配器还错误累加provider usage中的嵌套dict；保留原始工程失败，不当语义结果。Responses版本没有此类服务失败，但原适配器误丢弃两个原生预算内的最终回答。已使用固定LOTUS原生parser从真实响应重新投影，未发新模型请求、未补写或改写答案。修正前收据全部保留；这不是B6轨迹重放研究臂。原生finalization及占位符/分片ID解析均有回归测试。

## 摊销结论

固定任务与示范选择下的学习路线tokens：

| 阶段 | Tokens |
| --- | ---: |
| 真实示范（11calls） | 144,453 |
| 自动提取（1call） | 36,960 |
| 验证：reference Agent + 冻结算子 | 318,587 |
| 源切分/索引的模型tokens | 0 |
| 合计 | **500,000** |

这500,000高于真正整批300条Codex的252,075，约1.98倍；本次没有完整学习路线的token收益。若错误地把16条Agent批次的单位成本线性外推，会得到26条开始回本、300条约597万tokens的预测；实际300条Agent只用了约25万。代码保留带场景标注的投影，明确它不是测量，不替代整批共享计划的强对照。

完整实验（包括预检、所有比较、失败请求）共111次实际API尝试，已知token下界1,636,745，另4次HTTP403及1次超时没有usage；总tokens与实际金额因此仍有未知部分。不能把500,000当作全部研究开销。重复投影不重复计费。详见[全实验账本](../artifact/evidence/dataspace-amortization-20260906/experiment-cost-ledger.json)。Provider报告了部分cache和reasoning-token计数；请求参数与返回计数分别保留，不将请求none等同服务实现保证。

算子首次执行interval约0.323秒。为修正漏计verification/setup，使用相同冻结代码作一次计时补跑：全runner约0.971秒，其中verification0.228/setup0.415/execution0.329秒；两次预测除计时字段外完全一致。Native300容器运行interval约343.5秒。计时边界不同且多臂重叠，不能据此声称受控端到端加速；CPU/GPU、实际金额、人工研究/构造及独立复现成本未完整测量。

离线测试45项全部通过（包括原生LOTUS适配与结果投影回归），另有10次实际容器隔离检查通过；这些工程检查不构成研究优势验证。

## 证据和范围

- [机器汇总](../artifact/evidence/dataspace-amortization-20260906/comparison.json)、[冻结生成代码与来源](../artifact/evidence/dataspace-amortization-20260906/provenance.json)、[源实体/隔离/计时验证](../artifact/evidence/dataspace-amortization-20260906/validation.json)。无原始数据或完整轨迹进入源码artifact。
- [冻结协议及显式操作修正](dataspace-amortization-pilot.md)、[运行与复现指南](dataspace-artifact-guide.md)、[workload card](../workloads/dataspace-fund/workload-card.md)、[resource card](../environments/dataspace/resource-card.md)。
- DataSpace源ZIP的完整SHA256与task184的19文件/40,624,940bytes校验通过。1/16/300基金和1/4/56管理人组分别互斥；原始总体1048基金。三种文件类型在派生环境中存在，但任务必要证据仅SQLite，无多模态感知或异质资源因果验证。
- 模型为指定服务gpt-5.4别名，未核验官方snapshot。全部为开发实验，近重复、训练污染与独立确认尚未闭合。配对manager-cluster分析保持DEVELOPMENT_ONLY，不自动设置科学VALIDATED。
- 缺少无轨迹合成、同轨迹摘要/简单重放消融、多个独立one-trace episodes与独立团队复现。它们是未来研究主张的门槛，不是本轮已有结果。

结论：实现了可运行、可追溯的单轨迹自动算子原型；当前基金任务保留为工程控制。未找到需要昂贵Agent探索的有效质量差距，未获得本批次包含学习开销的收益。
