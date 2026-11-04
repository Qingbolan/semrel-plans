# Chicago食品检查：真实批，但预测与裁定不能混用

**Reject现成目标路线**。下载[原始城市完整项目](https://github.com/Chicago/food-inspections-evaluation)（含原始方法报告Rmd与数据）和[2019独立回顾论文](https://arxiv.org/abs/1910.04906)。后者不是城市原始报告，明确区分。官方API实际取得2014年1月按inspection_id升序的前20条，不是随机样本；这只是字段审查，C完整0/20。

| A/q | B/E | C | D | E/K | F | G | H |
|---|---|---|---|---|---|---|---|
| 原q为检查前预测是否将被记critical violation；不是现场合规裁决 | 天气/历史等是预测特征，不能当复杂规则E；历史完整检查手册未取得 | 0完整依据闭合 | 不存在静态不足证据，原模型为固定统计程序 | 类别不是K，未知 | 真实检查流程成立 | 事前特征不足以决定现场事实；事后备注又有判定泄漏 | 完整官方repo+论文+20API记录已下，完整手册与权利范围仍缺 |

回顾论文使用官方模型17075训练/1637测试（论文统计，未在本轮解码Rds复算）。目标为14种critical代码中至少一项，2018年7月规则更改；不能混合时期。城市CODE/21脚本从Violations计算违例矩阵和严重度，固定代码映射并不是语义推理。

| Query | 数据湖数据1 | 数据湖数据2 | 具体标签 |
|---|---|---|---|
| 预测下一次critical citation | 历史检查/营业执照/天气/周边投诉与sanitarian特征，DATA/*.Rds | 固定模型；不是法规推理环境 | inspection-level critical Boolean |
| 判断本次Pass/Fail | 官方API results、violations | 历史检查标准尚未冻结 | results多类，不能用critical Boolean代替 |
| 备注→违例代码 | Comments事实可能可拆，但夹带裁决及历史引用 | 需要完整同版手册 | 代码在原violations字段，必须私有隔离；未构造 |

真实记录920444，2014-01-15，GALLISTEL LANGUAGE ACADEMY，results=Fail；代码29、32、33、34、35、38，均非1–14 critical范围。备注29说先前小违例未整改、升级serious；38又让读者看29。这个实例足以说明Fail不等价于critical=True，不能用原论文任务结果声称检查合规性能。不能从单例推出一般裁决规则。

| 类Python DAG | 性质 |
|---|---|
| `x=join(history,licenses,weather,complaints)` | 普通数据集成，原预测模型 |
| `p=fixed_statistical_model(x)` | 风险预测，不能当事实gold推导 |
| `facts=sem_map(strip_and_extract,inspection_comments)` | 新任务构造尚未实现；不可凭删代码认定无泄漏 |
| `y=sem_map(apply_manual,facts,E)` | 拟议规则裁定；E/事实完整性未建立 |

| 方法 | 预期结果 | 过程 | operator候选 |
|---|---|---|---|
| LOTUS给原记录 | 直接读出Fail，属于泄漏 | 抽results或明确裁决词 | 无研究意义 |
| LOTUS事前特征+E | 无法保证恢复现场结果 | 风险相关性或固定分类 | 缺现场事实不是推理差距 |
| 逐案Agent给去裁决事实 | 未实测且输入/E未构造 | ==核历史整改要求、卫生手册、当前现场事实== | 历史join→规则适用，需独立充分性验证 |
| 批Agent | 摊销与质量未知 | ==预建规则索引==→按事实匹配→逐案复核 | ρE索引、ρP共同流程、ρG未测、ρR现场事实；K未知 |

十问边界由以上表涵盖：任务必须选择风险预测或法规裁定，不能混用；E未冻结；x是真实检查但原输入有监督输出；gold为检查员发现而非模型；C0、D/E未知；可探索历史不代表可获得未公开现场；未知状态不能填Fail；当前不证明区别于预测分类或固定规则映射。拒绝现成路线，原数据仍可作为另行构造来源。未执行模型/作者脚本，未补造20条专家gold。

[来源/commit/hash/抽样链接](../artifact/evidence/shared-environment-strict-chicagofood/source.json)。


## 输出与信息不足边界补充

预测任务输出critical事件概率或冻结阈值后的Boolean；缺现场事实不自动产生UNKNOWN gold。另行现场裁定任务的输出与不足语义尚未冻结，results里的Fail不能代替UNKNOWN；读取/执行失败应ABSTAIN，不修改源检查标签。
