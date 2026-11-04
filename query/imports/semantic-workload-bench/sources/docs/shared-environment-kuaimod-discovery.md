# KuaiMod：公开来源初核

原论文https://arxiv.org/html/2504.14904v1 全文HTML已下载209,929 bytes；官方仓库https://github.com/KuaiMod/KuaiMod.github.io commit e3e7124ad9b671c9898a7962ef024a1c4aa67f72，完整ZIP108,821,284 bytes已下载解压，未运行作者代码。官方数据https://huggingface.co/datasets/KuaiMod/KuaiMod revision382bf808505f6b7764fcb3a377b925a8e87760f8，gated=false。

数据README实际字段：tag、title、OCR、ASR、images、pid，图像为封面与最多8帧。标签是当前gold，不得模型可见；title可能含用户身份，实体分组需要审计。许可CC-BY-NC4，不能据项目网页许可证覆盖数据。

HF清单仅README、dataset.py、test/benchmark.jsonl和test/images.tar.gz等，无公开训练历史库条目。论文所述common-law主要以历史反馈训练模型，并不直接证明公开E有可检索历史判例库。训练24,562及测试1,000等规模仍是论文陈述，须实际文件确认。六/十五/十七分类不同口径待核，不能当执行家族K。

标注下载session28010末次poll确认live，README已获取；benchmark JSONL未完成，不推断记录数量。下一轮先poll同handle。当前不能给20gold结论或Strong评级。


## 完整标注实核

session28010已终止：read timeout。改用同一revision的HF raw入口（curl --max-time45）成功下载完整benchmark.jsonl并解析。实际1,000行、1,000唯一pid、578正向/422违规、16个标签（15违规+正向）；README“17 tags”与实际及scorer不一致，不沿用。7,337个图像引用，尚未下载图像，不等于已验证7,337张。

所有记录仅tag/title/OCR/ASR/images/pid；没有comments。论文§3.3称测试记录包括用户评论，§A.2使用top20评论，公开记录未包含。没有逐例理由、规则引用、训练H；不能以论文历史训练24,562条当公开共享环境。标签数据已取得不等于C20闭合，当前不以文本推断视觉gold。

官方evaluation/multi_cls_eval.py对找不到标签字符串的预测直接continue，且以标签子串首匹配判定；这是代码观察，不推断论文实际指标受多少影响。若复现需保留官方分数并另报全量coverage/失败，不能把跳过当正确。

| Query | 数据湖数据1 | 数据湖数据2 | 数据湖数据3 |
|---|---|---|---|
| 按平台标准判断每视频违规类别 | 1,000条title/OCR/ASR+帧引用 | 共享完整规则未取得 | 历史训练案例未公开取得 |
| 类Python DAG | scan→sem_map(rule,video)→classify | 环境缺口 | 不能挂载当前gold当H |
| 已核数值 | 正向578、违规422、16类、7337帧引用 | 未核长度 | 不将24562训练数冒充下载数 |

| LOTUS预期结果 | LOTUS过程 | Agent预期结果 | Agent过程 | operator结构 |
|---|---|---|---|---|
| 未执行，不能给分数 | 完整规则/帧/文本上的固定调用为待测基线 | 未执行，不能预期优胜 | ==核对证据模态、规则适用与事实充分性==→判定；缺失评论不能凭空补足 | 帧/文本抽取→证据充分性检查→固定分类；动态需要性未证明 |

| 比较臂 | 当前状态 |
|---|---|
| task-only | 未运行 |
| full-E静态 | 完整E缺失，未运行 |
| per-case Agent | 未运行 |
| batch Agent | 未运行；历史训练改进不是执行期缓存收益 |

本路线在公开共享环境与证据完整性处未过关；图像规模不补足E，当前不扩展下载大图包，不计Strong。只在规则/历史资料与缺失评论的公开来源明确时再推进20gold。
