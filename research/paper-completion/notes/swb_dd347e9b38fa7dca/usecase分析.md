# 具体用例

原文场景：药物警戒人员需要从大量文献和药品说明类文本中尽早发现相互作用，并为临床管理提供三类信息——如何发生（mechanism）、后果是什么（effect）、如何规避（advice）（§3.2，PDF p.5）。

原文例句（§3.2，pp.4–5）：

- “Grepafloxacin may inhibit the metabolism of theobromine” → mechanism；
- “Chlorthalidone may potentiate the action of other antihypertensive drugs” → effect（PD 机制并入 effect）；
- “UROXATRAL should not be used in combination with other alpha-blockers” → advice；
- “The interaction of omeprazole and ketoconazole has been established” → int。

Fig. 3 中 fenfluramine 与药物类别 antihypertensive drugs 及其成员（guanethidine、methyldopa、reserpine）分别形成 effect 关系，说明 group 实体参与关系，且类别与成员会各自成对标注（p.5）。

难点示例（§5，p.7）：“Fenofibrate should be taken at least 1 h before or 4–6 h after a bile acid binding resin to avoid impeding its absorption” 被一名标注者判为 advice、另一名判为 mechanism；指南用优先级规则处理一句多类的情况，但标注者常误用为“取句中第一个出现的类型”。

阅读者分析：若把它当作“从说明书中抽取所有需避免联用的药物对”的语义过滤任务，advice 类在 MedLine 子集只有 15 条，跨来源泛化的证据很弱。
