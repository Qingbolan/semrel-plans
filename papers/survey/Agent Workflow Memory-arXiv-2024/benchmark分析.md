# 评测与边界

**基线**：

| 基准 | 基线 | 说明 |
|---|---|---|
| WebArena | WebArena 原论文智能体、AutoEval、BrowserGym、BrowserGym_ax-tree | BrowserGym 同时输入 HTML 和 accessibility tree；作者另跑只用 accessibility tree 的版本以与 AWM 输入一致（§3.1，p.4） |
| WebArena | SteP | 使用 14 个人写、针对 WebArena 的工作流，监督条件不同（§3.1，p.4） |
| Mind2Web | MindAct、Synapse、CogAgent（仅 3.5 下步骤 SR） | AWM 沿用其元素过滤，把 Synapse 的检索样例换成工作流（§3.2，pp.6–7） |

**实验 1（WebArena 主结果，Table 1，p.5）**：

| 方法 | 总成功率 | Shopping | CMS | Reddit | GitLab | Maps | 平均步数 |
|---|---|---|---|---|---|---|---|
| SteP（人写工作流） | 33.0 | 37.0 | 24.0 | 59.0 | 32.0 | 30.0 | – |
| AutoEval | 20.2 | 25.5 | 18.1 | 25.4 | 28.6 | 31.9 | 46.7 |
| BrowserGym | 23.5 | – | – | – | – | – | – |
| BrowserGym_ax-tree | 15.0 | 17.2 | 14.8 | 20.2 | 19.0 | 25.5 | 7.9 |
| AWM | 35.5 | 30.8 | 29.1 | 50.9 | 31.8 | 43.3 | 5.9 |

AWM 比 BrowserGym 高 12.0 分（相对 51.1%），比 BrowserGym_ax-tree 少约 2.0 步，比 AutoEval 少 40.8 步。在 Shopping 与 Reddit 上仍低于 SteP。

**实验 2（WebArena 跨模板子集，Table 2，p.6）**：AWM 33.2，SteP 32.1，AutoEval 23.2，BrowserGym_ax-tree 20.5。

**实验 3（Mind2Web，GPT-4，Tables 3–4，pp.7–8）**：

| 划分 | 方法 | 元素准确率 | 动作 F1 | 步骤 SR | 任务 SR |
|---|---|---|---|---|---|
| cross-task | MindAct | 41.6 | 60.6 | 36.2 | 2.0 |
| cross-task | AWM_offline | 50.6 | 57.3 | 45.1 | 4.8 |
| cross-task | AWM_online | 50.0 | 56.4 | 43.6 | 4.0 |
| cross-website | MindAct | 35.8 | 51.1 | 30.1 | 2.0 |
| cross-website | AWM_offline | 41.4 | 46.2 | 33.7 | 2.3 |
| cross-website | AWM_online | 42.1 | 45.1 | 33.9 | 1.6 |
| cross-domain | MindAct | 21.6 | 52.8 | 18.6 | 1.0 |
| cross-domain | AWM_offline | 36.4 | 41.6 | 32.6 | 0.7 |
| cross-domain | AWM_online | 40.9 | 46.3 | 35.5 | 1.7 |

GPT-3.5 下，AWM 步骤 SR 34.6，Synapse 30.6（Table 3）。收益主要来自元素选择更准；动作 F1 反而低于 MindAct，作者解释为智能体不知道何时该偏离工作流（§3.2.1）。

**实验 4（表示消融，Tables 5–9，pp.8–10）**：
- 规则归纳 vs LM 归纳：WebArena 35.6 vs 35.5（步数 6.3 vs 5.9）；Mind2Web 步骤 SR 43.4 vs 45.1，任务 SR 2.0 vs 4.8；
- 代码 vs 文字工作流：步骤 SR 45.1 vs 45.4，任务 SR 4.8 vs 3.6，差别不大；
- 状态描述（GPT-3.5）：只用自然语言 34.6，只用 HTML 33.8，两者都用 32.9；过滤后的 HTML 有 47% 的情况漏掉全部正确元素；
- 工作流作为动作（AWM_AS）：步骤 SR 46.4，任务 SR 3.6。

**实验 5（工作流质量，附录 A.3，Table 10，pp.15–16）**：每例约 7.3–7.4 个工作流；利用率 WebArena 0.94、Mind2Web 0.91；Mind2Web 覆盖率 0.40。

**边界**：
- 原文承认：在线工作流来自模型预测轨迹，不一定正确，可能降低表现（§3.2.2）；智能体难以判断何时偏离工作流（§3.2.1）；预设动作序列看不到动态弹窗（§5）。
- 阅读者整理：只用 GPT-4/3.5 两个模型；没有成本或延迟核算，步数减少不等于总 token 减少（归纳与评估调用未计入）；任务级 SR 在 Mind2Web 上绝对值很低（≤4.8%）且并非全面提升；未报告重复次数或方差；在线结果依赖任务顺序，论文未测不同顺序。

依据：[arXiv 2409.07429v1](https://arxiv.org/abs/2409.07429v1)，§3–5、Tables 1–10、附录 A.3，PDF pp.4–10、15–16。
