# 贡献与评价

原文声明的贡献（§1，PDF p.3）：

1. 提出 InsightBench，称其为首个专门评测 LLM 智能体端到端、多步数据分析的基准。
2. 比较开源与闭源模型及不同评测策略，表明 AgentPoirot 优于 Pandas Agent，且 LLaMA-3-Eval 可替代闭源 G-Eval。

**构建方法**：选取 ServiceNow 系统表（incident、sys_user、fm_expense、alm_hardware、sn_gf_goal）的列定义 schema；对“可控列”用回归等数学模型植入趋势，例如 TTR=1+slope·(开单日期−起始日期)；非可控列用随机采样或 GPT-4 生成文本；最后由专家写参考 notebook（§2.1、附录 B.1–B.2，PDF pp.3–5、14–15）。质量控制为 20 名具基础数据科学技能的志愿者问卷评审，平均 4/5 分（§2.4，PDF p.6）。

**AgentPoirot**：抽取 schema 统计 → 生成 k=3 个高层问题 → 每题写代码并解读 → 每题再生成 n=4 个跟进问题，共 (n+1)×k=15 条 insight → 汇总（§3.1，PDF pp.6–7）。

阅读者分析：贡献主要在“植入式 capture-the-flag 评测协议”（源自同组 Laradji et al. 2023）与业务主题覆盖，AgentPoirot 只是提示工程基线。数据为合成，原文自承可能缺失真实企业数据的复杂性（附录 A，PDF p.14）。此外原文有若干自相矛盾：难度称为 1–4 级，却写 Hard 为 Level 4–5（§2.3，PDF pp.5–6）；Figure 3 的五主题百分比与正文七类计数口径不同；§3.2 说 LLaMA-3 用 4 张 A100，复现声明写 2 张（PDF pp.7、10）。

依据：§1–3、附录 A–B，PDF pp.1–7、10、14–15。
