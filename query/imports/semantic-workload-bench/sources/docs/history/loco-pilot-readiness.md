# LOCO 制造质检 pilot：数据可达，样本尚未就绪

2026-09-05 核查。**官方包可直接获取，无须填写身份表单；但本次受限下载未得到20–30张测试图，不能宣布pilot已构成。** 已保存机器可读证据至 [loco-readiness.json](../outputs/loco-readiness.json)。未运行模型或构造人工阈值。

## 官方来源与实际下载

[官方数据页](https://www.mvtec.com/research-teaching/datasets/mvtec-loco-ad)当前展示表单；[anomalib维护者源码](https://github.com/open-edge-platform/anomalib/blob/main/src/anomalib/data/datasets/image/mvtec_loco.py)仍公开列出[原始分发包](https://www.mydrive.ch/shares/48237/1b9106ccdfbb09a0c414bd49fe44a14a/download/430647091-1646842701/mvtec_loco_anomaly_detection.tar.xz)。HEAD返回200，Range返回206。包内实际读取的README具有MVTec作者、2022版权与CC BY-NC-SA 4.0声明。

包大小6,126,996,224 bytes，Last-Modified为2022-03-09；这表示分发包时间，不是论文发表时间。首尾各64KiB下载后，`xz --list --verbose`确认只有一个压缩块。不能像多块ZIP一样跳取指定类别；未核验到官方按类别包。

随后仅请求前128MiB，流式读取tar，计划最多保存前30张test图并即刻停止。实际取得176个文件：官方README、首类别`breakfast_box`掩码及缺陷配置；**测试图0张**。到达截断压缩流后以EOF终止，这是预算边界，不是完整包损坏。数据和日志在`/tmp/loco-review/prefix`，可复现脚本为`/tmp/loco-review/prefix_probe.py`。未下载完整6GB，未提交表单或发送消息。

另外取得官方[评测代码](https://www.mydrive.ch/shares/48245/a4e9922c5efa93f57b6a0ff9f5c6b969/download/430648014-1646847095/mvtec_loco_ad_evaluation.tar.xz)，21,616 bytes；实际README版本2.0。它消费模型输出的异常图来评测分类及定位，并不是现成检测器。

## 规则足以构造哪些任务

[原论文](https://link.springer.com/article/10.1007/s11263-022-01578-9)发表于IJCV，2022-02-22。Section3.1给出的规则可以作为独立于预测的规范依据：

- `screw_bag`：每袋2个垫圈、2个螺母、1根长螺丝、1根短螺丝；本文不追加长度阈值。
- `splicing_connectors`：两只夹位数相同的连接器由一根线连接；线色与夹位数一一对应；两端接入相同相对位置，形成镜面对称。

**Section3.1没有逐项列出线色—夹位数映射。** 一个正常示例只能提供一个组合，不能自动给出所有未见变体规范。应取得完整、独立选定的正常示范或权威映射，再冻结规则；不能从待测异常标签反推规范。

可固定批任务为“筛出违反指定装配逻辑的组件”，DAG为读取工单图片→获得对应规范与正常参考→语义检查计数/匹配/位置→输出异常记录及证据。固定程序或直接VLM也可能完成，必须实际比较，不能由规则复杂推断Agent必要。

## gold边界

原数据提供正常、逻辑异常和结构异常类别，以及像素标注；完整类别包还包括缺陷配置。它们是独立于本次预测的既有标注，可用于异常检测/定位。逻辑筛选宜先限定正常与逻辑异常；结构异常并不自动意味着某条逻辑约束失败。

原论文没有提供返修动作、可维修性、停线决策或电气功能测试gold。不能把异常标签扩写成这些目标。定位评测的饱和参数也不是制造验收阈值。

## 镜像与当前决策

检查了[公开Hugging Face副本](https://huggingface.co/datasets/zhaolutuan/0423/tree/58ed6284ed45eed7741f13f2fddc305d32603af2/MVTec-LOCO/splicing_connectors)目录API：正常119项、逻辑108项，但结构目录列出158文件，论文为85图，尚未解释额外文件。API结果还存在分页，未做完整目录审核或与官方逐图hash比对；没有下载或采用镜像图片。它只能标为未验证候选来源，不能称官方副本已到。

本轮状态是**受限下载条件下尚未完成样本落地**。完整官方包在技术上可取，后续若选择LOCO需要承担6.13GB下载，或证明可验证的按类别分发路径；当前可以先运行已经取得真实材料的其他质检pilot，保留LOCO为后续候选。
