# Dutch DSO legal-text-to-decision-model — Reject

已下载[原论文](https://arxiv.org/abs/2604.17153)和[完整官方仓库](https://github.com/opengov-lab/legal-text-to-decision-model)，commit6a4844fb235d4f958d0810bba7089a2e9078099e，2135文件。[来源哈希](../artifact/evidence/shared-environment-strict-dso/source.json)。真实的是部署模型，测试cases是枚举输入组合，不满足数百真实案例条件。

| 条件 | 原论文/本地证据 | 结论 |
|---|---|---|
| 来源真实性 | 荷兰Omgevingsloket部署决策模型及对应法律XML | 真实规则程序；不是生产申请case日志 |
| F | §3.6穷举布尔输入、从gold规则提取字符串类别，形成2712+10368=13080组合 | 构造测试，不计真实cases |
| 数量 | 论文95模型；本地gold_models99个JSON | 差异未闭合，不把99称论文实验数量 |
| D | gold是固定DMN逻辑；生成模型的结果与它比较 | 固定执行器可生成该测试gold，不能证明动态探索必要 |
| G | Text+IO显式使用oracle输入输出规范；类别枚举读取gold | 不能作为未知环境探索自然得到的资源 |
| H | 仓库声明CCBY4；上游政府数据许可仅README推定 | 不把该推定写成已核验法律许可 |

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 |
|---|---|---|---|
| 停车库活动在规则下产生什么义务？ | 模型输入为结构化变量，如机械通风、超过20个车位 | 对应法律文本及DMN规则，实际下载 | gold程序；原任务是生成决策模型而非执行真实审批批 |
| 类python的DAG | `enumerate_boolean_inputs()`：构造组合 | `execute(generated_model, inputs)` | `compare(execute(gold_model, inputs))`；论文总13080组合，非真实N |

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
|---|---|---|---|---|
| 机械通风=True且超过20车位=False时，所查看的局部判定表输出True；整项审批结果未计算 | 若已给结构化输入和gold规则，直接固定执行；语言模型预测未知 | 同一局部规则目标；未运行Agent | ==定位活动对应条文、检查变量与规则映射==；形成可执行决策表 | `DMNGraph(inputs)->outcome`；确定性DAG即可，不把生成质量缺口等同执行适应性必要 |

| 具体审查 | 已做 | 未做 |
|---|---|---|
| 源内容 | README、论文§3.6、全部文件下载和gold数量统计；看停车库与屋顶围栏局部规则 | 不声称全部法律到DMN映射已核验 |
| C20 | F失败后未开展20真实case核验，0完成 | 不把程序穷举的20个组合冒充20个真实gold |
| 实验 | 未执行作者代码、生成模型、LOTUS或Agent | 所列过程是预期；未产生实测费用/优势 |

[本地统计](../artifact/evidence/shared-environment-strict-dso/data-audit.json)。这项材料可作为法条编译为固定程序的基线参考，不能满足当前Strong准入。
