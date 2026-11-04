# BLM-Guard：公开资产资格初筛

原论文 https://arxiv.org/html/2602.18193v1 全文已下载至data/shared-environment-blmguard/paper.html（204188 bytes）。AAAI正式PDF https://ojs.aaai.org/index.php/AAAI/article/download/40914/44875 下载因RemoteDisconnected失败，未冒充成功。来源收据artifact/evidence/shared-environment-blmguard/source.json。

论文描述5–45秒真实商业广告，来源包括专家审核、规则触发和低投诉高曝光广告。给定视频和平台政策集合做逐条违规判定；与目标任务形式相关。但未取得冻结政策全文、逐案视频与独立gold。论文“release”措辞不等于可下载；本次GitHub repository搜索BLM-Guard只返回无关GuardBotuv12，HF dataset搜索为空；这些搜索不证明全球不存在发布。不能采用二手文章的private判定作为事实。

论文框架主要是规则引导训练与GRPO优化，测试提升不能直接证明同模型同资源LOTUS/固定工具流程不足。七风险场景属于类别，不自动形成中间规模执行家族K。无20gold审计条件、无已核验共享环境长度，无许可确认；不计Strong，不加入正式38审计计数。

| Query | 数据1 | 数据2 |
|---|---|---|
| 按共享平台政策判定广告违规 | 作者称真实短视频，未下载cases | 平台政策全文未取得 |
| 类Python DAG（任务形式推断） | scan → sem_map(policy,video) → violation set | 共享policy；不得以分类树替代完整规则 |

| 预期LOTUS结果 | 预期LOTUS过程 | 预期Agent结果 | 预期Agent过程 | operator结构 |
|---|---|---|---|---|
| 无法给具体值：无case/gold | 完整输入上的固定视频抽帧/转录/规则判定可作对照 | 无法给具体值 | ==识别相关模态与条款==→核对视频证据→判定；仅设计推断 | 未验证，不宣称动态必要 |

| 比较臂 | 当前证据 |
|---|---|
| task-only | 未运行 |
| full-E静态 | 同资源对照缺失 |
| per-case Agent | 未运行 |
| batch Agent | 未运行，政策缓存收益未知 |

后续仅在官方数据/政策发布入口出现时继续，不能用论文性能表代替下载审计。
