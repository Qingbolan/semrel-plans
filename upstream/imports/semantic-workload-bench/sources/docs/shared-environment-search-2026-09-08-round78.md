# Increment78：RMU/LAM:ECHR法律论证来源审计（未通过长E条件）

仍6/15。本轮从网页论证检索发现法律领域RMU:ECHR/LAM:ECHR，优先核查真实裁决来源；这两个名字来自同项目README/论文，不算两个湖。已下载原论文与完整作者仓库；未找到独立长标注规范，因此不列入合格湖。不能把法律领域知识的潜在复杂性替代所需共享E证据。

## 完整下载

- [作者原论文](https://arxiv.org/pdf/2208.06178)：39页684997bytes，SHA256 `eafe54da3f34b3e7f55bc93be2efb6eaf1f8276ad949656e14dd69383f2f1518`。
- [作者完整仓库](https://github.com/trusthlt/mining-legal-arguments/tree/a1a14832ce55c85f04c9e211f3606e04401d9c0e)：commit `a1a14832ce55c85f04c9e211f3606e04401d9c0e`，ZIP114639467bytes/2018entries，1997Git blobs全部SHA1匹配、CRC通过，tree未截断。SHA256 `bbffa89a63a22f2aae8c9e25d5b5735d44a3b98694553d6763c6f8d6469906b2`。
- 外部约74GB预训练模型未下载；完整repo包含数据/代码/预测，未将predictions当gold，未运行作者代码。
- 全repo树未找到PDF/manual/guideline文件。论文§3.1加Appendix B schema/例子3024words；提取明确锚定章节标题，修正了最初误匹配正文Appendix B引用造成的重复范围。不能把39页方法/实验论文整体当必要环境。

## 全量观察

`gold_data`原生375XMI、21776346Unicode字符、15211LegalArgumentation spans；5演员标签、实际15种argument type。论文说373是作者代码明确删除两个少于5标注的文档后数量，不能将375当下载错误。`article_3_data`20XMI/2064619chars/1210spans，是同项目扩展，不另算湖；跨目录源实体重叠未审计。

全文在UIMA Sofa，span为UTF16坐标，全部范围合法、可解码。没有独立重复的surface文字字段，故不能把“范围合法”声称为独立人工字符正确性证明。类型包括Subsumtion8691、Entscheidung des EGMR1238、比例适当性1959、既往判例2015等（原375数据）。actors为申请人2472、EGMR9953、国家2401、第三方212、委员会/分庭173。

论文§3.2说明法律专家参与标注与裁定，最后阶段部分单人标注；不能说每案都由多人独立标注。当前gold任务是论证类型及论证提出者，不是重新依据Convention预测胜败/合规。许可和方法精确适用仍需核验，不提供法律建议。

## 三张表（未通过候选的明确边界）

| Query | 数据湖数据1：E | 数据湖数据2：items | 数据湖数据3：gold |
|---|---|---|---|
| 按作者法律论证scheme抽取span/论证类型/提出者 | 目前只有论文约3024词schema及示例；独立长规范缺失 | 原生375真实裁决，作者论文口径373；20案另作同项目扩展 | 15211原生人工论证span、type/actor；不是胜败gold |

| 类python的DAG | 具体数值 | 下游目标 |
|---|---|---|
| `scan(judgments).sem_map(extract_legal_arguments,E).explode(arguments).filter(type=='Vorherige Rechtsprechung des EGMR')` | 原375文档15211spans | 2015既往判例类span；不等于2015独立判例 |
| `arguments.groupby(actor,type).count()` | 5actor/实际15type | 作者标注分布；不代表案情真伪或谁胜诉 |

源例001-100469.xmi：UTF16[40335:40574]的申请人关于解雇及Article8的主张标为Subsumtion/申请人；[40950:41208]的法院可受理性判断为Entscheidung des EGMR/EGMR。例子是当前开发阅读，未运行模型。

| 预期LOTUS关键算子结果 | 预期LOTUS过程 | 预期Data Agent结果 | 预期Data Agent过程（==环境探索步骤==） | 预期operator结构 |
|---|---|---|---|---|
| 目标为上例两个span/type/actor；实际未知 | 完整裁决+同scheme固定sem_map→UTF16范围及枚举校验→聚合 | 相同gold目标，未知 | ==查法律论证类型与actor定义==；==核对该段是在转述申请人还是法院自己判断==；输出span并校验 | `extract(text,policy)`→候选span→type/actor→坐标验证→查询；不预设轨迹学习优势 |

缺少长E，不启动这一候选的模型比较或构造来凑15个湖。不同type filter是同一抽取任务的投影。后续如取得作者更完整且实际使用的指南，可重新评估；不能擅加整本法律手册充大上下文。

下载data/shared-environment-audit-20260908-v78；脚本/收据artifact/evidence/shared-environment-audit-20260908-v78。无模型/独立确认/public-private构造。下载session52435正常结束。
