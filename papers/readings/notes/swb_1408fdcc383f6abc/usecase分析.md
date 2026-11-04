# 具体用例

**原文示例（Fig.1，PDF p.3）**：某人持续收到 Rossi Carta S.r.l. 的未经请求的广告邮件，行使数据主体权利后公司仍未处理。

1. GPT-4o 按 CI 模板抽取：sender = Rossi Carta S.r.l.，subject = Individual，receiver = Individual，attribute = Emails，purpose = Advertising。
2. 借助角色/属性层级图，把具体参数对齐到 GDPR 术语：Controller、Data Subject、Personal Data、Marketing。
3. 依据对齐后的参数匹配可能适用的条款（Art.6、7、12、21 等）。
4. 判定模块推理后给出结论：被 GDPR 第 21 条（反对权，直接营销）禁止。

**AI Act 合成例（Table 11，p.14）**：问答链为“提供者 / 实质修改 / 在欧盟上市使用 / 不属豁免 / 含生物特征分类与社会评分”，标签由问答链决定为“禁止”；GPT-4o 据此写出名为 EmotionSense 的情绪识别系统情境，并标注 CI 参数。

阅读者分析：若作为语义查询，可表述为“对每个案例抽取信息流五元组，再与法规叶子规范连接并判定合规”，即“抽取 → 实体规范化 → 规则匹配 → 判断”的多步管线。原文消融表明，中间步骤若用金标准替代（DP+CI+LAW），准确率显著提升，瓶颈在检索与对齐（阅读者分析）。
