# AIReg-Bench：原论文与完整仓库核验

判定：Reject；不计入 Strong。真实案例条件不满足，专家评审合成案例不等于真实生产决策。未执行模型，以下执行过程均为预期。

原论文：https://arxiv.org/abs/2510.01474 。官方仓库：https://github.com/camlsys/aireg-bench 。本次完整下载 commit `846d5cc075ad424a2d31dd20e34a7c5fe836f157`，671 个文件；哈希和大小见 [下载收据](../artifact/evidence/shared-environment-strict-aireg/source.json)。未执行作者代码。未发现 LICENSE 文件，不能推定数据许可。

| 证据项 | 本次观察 | 意义 |
|---|---|---|
| 来源 | README 与论文 §3 明确模型生成 fictional systems | F 不满足真实案例 |
| 数量 | documentation 实数 300；论文专家评审 120，每例三人 | 不能将 300 都算专家 gold，360 个评分也不是 360 cases |
| E | articles.txt 实数 2,190 词，Art.9/10/12/14/15 | 不等于完整复杂长 AI Act；单例指定条款 |
| Gold | 1–5 Likert 评分，中位数作比较；附录 I 为 2/3/3 | 不是法院最终二元判决 |
| 资源增益 | 论文表4 GPT-4o κw .775，去条文 .654；MAE .558→.717 | 作者结果，未复现；不能证明固定同资源方法不足 |
| C/D/E | 未做20个真实案例闭合；未见同资源固定程序不足；K未测 | 不升级 Strong |

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 |
|---|---|---|---|
| 对每份技术文档，按其指定 AIA 条款输出合规 Likert 评分 | 120 份被专家评审的合成文档（300份生成池的子集） | 五条法规摘录，2,190词 | human_annotations.xlsx；仅评分器可读 |
| 类python的DAG | `scan(annotated_ids)` | `join(article_id, articles); sem_map(score_and_evidence)` | `compare(prediction, median_gold)`；N=120，不是300 |

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
|---|---|---|---|---|
| 附录I交通安全例：目标中位数3；LOTUS实际预测未知 | 将指定Art.10和完整文档送入sem_map，输出评分与证据 | 同样目标3，实际预测未知，不能预设更准 | ==读取条款并定位数据代表性、地域覆盖与缓解证据==；输出评分，必要时标明证据不足 | `ArticleAssessment(article_id, text) -> {score, evidence, uncertainty}`；固定检查表也可实现，未证明动态结构必要 |

| 具体例子 | Gold与输入核验 | 可支持的结论 | 不能支持的结论 |
|---|---|---|---|
| 论文附录I，交通安全，Art.10 | 三位专家评分2/3/3；数据偏向城市、外围/郊区覆盖不足，缓解措施效果缺证据 | 专家意见存在分歧；应保留有序评分和证据充分性 | 不把score3自行称批准；不将未运行LOTUS/Agent写为正确 |

这里的高质量法律专家参与值得保留为标注设计参考，但不能替代真实批量数据来源。未展开20例审计，因为已确认 F 硬条件失败；C标为未完成而非通过。
