# CAB发现阶段：不展开为Strong候选

完整下载官方commit `37670134e2cd1d1e74bf54a8e3e5042feaee7001`，6文件ZIP55666 bytes。用标准库zipfile/XML读取两个工作簿；无宏、公式或作者代码执行。

| 核验 | 本次观察 |
|---|---|
| 真实规模 | README15类情景；gold工作簿4行含表头，实际3组成对提示；规则工作簿同样3条规则 |
| 搜索摘要规模 | 6483移民裁定等数字出现在README的Existing Benchmarks介绍，不是CAB本身 |
| gold语义 | 第一组是同一补助申请更换政治言论倾向后询问Approve/Deny；列名Compliant/Non-compliant不能替代逐案批准/拒绝gold |
| 结论 | 不满足数百真实case批量；无必要继续20例或模型运行。不加入正式38候选计数 |

| Query | 数据湖1 | 数据湖2 |
|---|---|---|
| 判断申请是否批准（原表提示） | 3组成对情景提示 | 3规则条目 |
| 类Python DAG | scan → sem_map(decide) → compare_pair | rule lookup；真实正确决定数量未知 |

| LOTUS结果预期 | LOTUS过程预期 | Agent结果预期 | Agent过程预期 | operator结构 |
|---|---|---|---|---|
| 未知；缺完整资格条件 | 固定规则/反事实比较 | 未知；不能从禁止歧视规则单独推出申请合格 | ==识别不允许使用的属性及缺失资格条件== → 输出证据不足 | 反事实一致性检查与实际资格判断应分别定义 |

这里不作现行法律解释或提供资格建议。只说明数据任务和gold契约缺口；原始规则链接指向HB00149I草案，是否现行法规未核验，不能冒充冻结生效规则。

来源：https://github.com/xai-privacy/compliance-audit-benchmark 。
