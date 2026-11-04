# HSE-Bench：固定真实案例规模初筛

原论文 https://arxiv.org/html/2505.22959v1 已完整下载464588 bytes；官方仓库当前T-Lab/hse-bench（原mengqiwang1入口），commit511ccbc30a68a30c5ef0e813bb8849e1d016457e，ZIP981326 bytes已解压。数据Joysouo/hse-bench revision4b92a2a45e396b0d2ae533850c073bec82ecf38a，无门控。下载并解析CourtCase_rule-conclusion.csv，实际38条（加header39行）。原文/代码明示法规场景由模型生成，法院案例由原判决转换为QA；四种IRAC问题不是同一固定任务，152法院题不能当152独立结论cases。

论文总1020：法规448、法院152、考试320、视频100。仅以法院结论任务计38，且跨地区/法规，不满足同E数百真实cases的F。不能为凑规模把生成法规场景或四种任务合并。当前不进入20gold深审，不计Strong。

| Query | 数据湖数据1 | 数据湖数据2 |
|---|---|---|
| 判断Company X忽视护栏锈蚀导致坠落的法律结果 | 首条法院结论题，改写矿工事故描述 | reference=[2011] NSWIRComm 13；判决原文未下载核验 |
| 类Python DAG | scan→sem_map(E,case)→legal_outcome | 应独立提供有效法规，不能把当前判决结果当环境 |
| 数据数值 | 38法院结论题；首条gold C=因安全违规被罚 | 未验证原判决与描述的保真性 |

| LOTUS预期结果 | LOTUS过程 | Agent预期结果 | Agent过程 | operator结构 |
|---|---|---|---|---|
| 目标C，未实跑 | 固定法规检索→单次判断 | 目标C，未实跑 | ==核对辖区、雇主职责与已知隐患==→应用条款 | 固定职责/违约/因果检查可作为对照；动态必要性未证明 |

| 比较臂 | 证据 |
|---|---|
| task-only | 未实跑；选择题常识可答不证明E必要 |
| full-E静态 | 未实跑 |
| per-case Agent | 未实跑 |
| batch Agent | 未实跑；RoE提示收益不是单轨迹编译证据 |

本例gold仅为下载标签，不是法律意见或独立已核金标准。源论文有专家检查描述，但当前20原始来源核验未完成。仓库results CSV为输出文件，本轮初步DictReader行数不作为数据计数，避免无header造成少1。正式源CSV确认38。
