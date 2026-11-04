# SecAlertBench — 源发布核验，未计入Strong

[官方仓库](https://github.com/Dxsssu/SecAlertBench)已完整下载，commit42a84889fda912ca432c994924a1ccd4b9df6274，144文件、ZIP41487195bytes。原论文标题检索尚未定位可下载全文，仓库无PDF；未读原论文故不计入35项已判定清单。[下载收据](../artifact/evidence/shared-environment-strict-secalert/source.json)。

| 核验项 | 本次事实 | 边界 |
|---|---|---|
| 真实数量 | 8322条；Attack2496/Non-Attack5826；rule_name241种 | 不把告警类型直接当语义执行家族K |
| 环境B/C | 发布物为告警、少量原始示例、脚本与模型结果；完整企业日志不公开（README声明） | 未取得可探索共享企业环境或判定SOP，C20=0 |
| G执行泄漏 | RQ1 API脚本46–48整条dict序列化；251–268读取带Label分集并原样放record；166送模型 | 当前源码+当前发布数据路径泄漏Label；未运行模型，不推断历史论文运行是否如此 |
| 来源H | 仓库已下载；未找到LICENSE文件与论文全文 | 不宣称许可闭合；不能满足Strong |

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 |
|---|---|---|---|
| 告警是否为攻击尝试/安全威胁 | normalized请求/响应字段，8322条 | 缺失：企业资产、行为基线、调查规则的共享快照 | Label是私有gold；现行调用路径错误地保留在输入 |
| 类python的DAG | `scan(alerts)` | `sem_map(classify)`，无已获取E | `compare_private_label`；应先隔离gold才能实验，但本轮不改上游数据 |

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
|---|---|---|---|---|
| 未运行；输入含Label时结果不具有效测量意义 | 先用公开字段allowlist，再固定语义分类；同E缺失 | 未运行；不能承诺因Agent而提升 | ==检查请求内容、响应和行为背景是否充分==；缺少企业背景应报告未知 | 可能是固定分类/证据提取，未证明按家族探索，不能编造operator |

| 具体实例边界 | 可读信息 | 不可推出 |
|---|---|---|
| README的Log4j例 | 明示攻击payload，响应400，gold Attack | Attack定义含attempt，不等于入侵成功；不能用HTTP400当Non-Attack |
| 20gold | 暂不做：共享E/论文未取得且输入路径存在gold泄漏 | 不把标签实数或20JSON能打开当依据闭合 |

[源码路径与计数证据](../artifact/evidence/shared-environment-strict-secalert/data-audit.json)。未执行作者代码、攻击内容、模型调用或测试，也未修改源文件。
