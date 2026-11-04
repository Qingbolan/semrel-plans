# 第142轮：INS-MMBench完整代码与理赔分区核验

仍8/15，本候选不合格。上一轮141提供真实评分/环境范围证据，属于进展。本轮回到保险来源检索；HICRIC与InsLogicBench已检索过，未重复计数；新INS-MMBench实际下载与核验如下。

[原论文](https://arxiv.org/abs/2406.09105)12页2917344bytes，SHA256 `bc32157f35ba612a2fe2775dca5b4ba17f542776c7b5d822b3591236a5c3a3af`。[完整作者代码仓库](https://github.com/FDU-INS/INS-MMBench)commit `2805d3efa2cb16e43e9693e1c9c97748c9423679`，ZIP30417710bytes、122members、CRC通过，SHA256 `d7b2bc52ed4c5f369945269640055f679ed6a822931c0a27099c0c76d0c5bb30`。作者[HF数据仓库](https://huggingface.co/datasets/FDU-INS/INS-MMBench)锁revision `b77ea65c18c61108a32b811ca344308941ff8046`，完整理赔分区multi_step_claim.tsv36738707bytes，SHA256 `6a26cc520d351ba5d091411c0ca13496d767191496bead1954ccd1ba36b4fe39`。收据在artifact/evidence/shared-environment-audit-20260908-v142/，原件在data同名目录。

下载边界：完整代码工作树已取得；HF只取得.gitattributes和完整claim分区，不声称取得整个多模态数据集。最初启动全HF下载，在发现fundamental单文件1544148629bytes、其余无关分区总计约1.3GB后主动终止，进程exit130；没有把未完成fundamental算作成功。之后单独完成37MB claim下载。没有因观察超时重启同一个下载。

实际TSV400行/400唯一index/12字段：index,image,Cost_of_vehicle,Min_coverage,Expiry_date,Max_coverage,Condition,Amount,Severity,expired,claim,question。400图片base64严格解码及Pillow实际解码通过，395个不同字节图像；5条超出唯一图像数，不当作独立场景。全部Condition=1；Severity minor150/moderate150/severe100；expired=1有170条、0有230条；claim=0恰170条，未过期且零赔款0条。这是当前发布分区统计，不是论文10,372总问题数。论文Table2的auto claim列270条/1350images与当前400行单图分区不一致，尚未建立版本/任务对应，不能混用论文结果。

缺少共享E：代码和该分区没有完整保单、适用版本、事故日期/评估日期、定价表或真实理赔单ID。question只是每行车辆价格、expiry和min/max金额加五步指令。论文§3说明scenario参考答案在专家指导下人工构造；图像来源于已有视觉数据集，不因此成为真实保险公司的逐案裁决。上游图像许可及金额来源未逐项核验，不宣称真实保单赔案绑定。

具体原生index0：图像是左前方受损车辆（本轮已查看）；车价44900、min1122.5、max11303、expiry2021-11-12；gold Condition1、minor、Amount4043、expired1、claim0。本轮看图只确认可见受损，不能确认minor等级或维修费4043正确。index2：车价32700、min817.5、max8253、expiry2026-04-30；gold Amount459、expired0、claim459。没有min的合同定义，不能自行将它视作免赔额或起赔门槛。尝试“expired或Amount<min则0，否则min(Amount,max)”仅为开发诊断，31行不一致，不能把该自拟公式当规则或据此改gold。

作者scorer源码vlmeval/evaluate/multi_step_claim.py将资格gold直接定义为expired取反；最终金额误差只计算prediction!=0且gold!=0的行，预测0可能被排除。这来自源码阅读，未运行原论文实验，不断言历史成绩受影响。金额和资格的现行评分不能直接替代完整合同理赔评测。坏输出也可能被解析为0，这不是明确ABSTAIN协议。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold |
| --- | --- | --- | --- | --- |
| Q1 批量判断车损及等级，生成维修核查清单 | 400图，395unique；index0为左前部损伤 | 每行车辆价格和五步问题 | 共享等级标准/维修定价规则未提供 | index0损伤Yes、minor、维修费4043；损伤Yes全400，不能当平衡筛选任务 |
| Q2 依据保单判定是否赔偿并计算赔款 | 同一图和车辆价格、Expiry_date、min/max | 应有保单条文与事故日期，本分区缺失 | Amount/expired/claim为private，不能作为公开事实偷渡 | index0 expired1/claim0；index2 expired0/claim459；没有完整裁决依据 |

| 类python的DAG | 具体数值 / 关键中间结果 | 下游边界 |
| --- | --- | --- |
| `images.sem_map(assess_damage,E).project(id,level,repair_cost)` | 400条；gold150minor/150moderate/100severe | 缺完整等级/价格规范，不保证精确费用可由图推导 |
| `assessments.join(policy_metadata).sem_map(adjudicate,E).aggregate(sum_claim)` | index0目标0；index2目标459 | 需要policy/date；不能先读private Amount/expired再称Agent完成端到端 |
| `predictions.filter(claim_eligible).project(id,amount)` | 作者expired取反给230“eligible” | 与完整保单保障资格不是同一语义，暂不构造正式任务 |

以下均未执行模型；给出的是发布gold目标及方法假设，不预言哪个系统成功。

| 预期关键语意算子直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期关键语意算子直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索步骤== | 预期产生的operator结构 |
| --- | --- | --- | --- | --- |
| index0目标Yes/minor/4043，实际输出未测 | 图+短prompt固定sem_map→格式检查；费用可能无充分依据 | 同目标，不能保证获得未提供的定价信息 | ==查公开字段及维修计价依据==→读取损伤图→依据不足时显式ABSTAIN，不能借private费用补全 | `DamageAssessment(image,pricing_rules)->level,cost,evidence/status`，pricing_rules当前缺失 |
| index2发布目标赔459；实际输出未测 | 固定规则解释min/max及expiry，缺参考日期时契约不完整 | 同样缺信息，不能假定搜索任意当前保单可补齐 | ==定位保单ID/版本/损失日期==→当前未提供→记录缺口 | `PolicyResolver→CoverageDecision→AmountCalculator`目前只能是接口草案，不能称已学operator |

同资源固定程序、Coding Agent、E-only编译与整批Agent均应保留；没有用视觉困难或零输出过滤机制制造Agent优势。

决定：不合格，保留原论文/完整代码/真实分区证据，停止本分区当前构造。不能从保险场景名称推出长共享环境，也不能把专家设计scenario标签描述成真实理赔流水。审计脚本audit.py/audit.json/example.json、原图查看记录可追溯；无模型/快照/正式评分/测试套件/commit。下一轮寻找新独立来源。
