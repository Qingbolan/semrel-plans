# 评测与边界

**被测对象**：三种开源脚手架 AIDE、MLAB（MLAgentBench 的 ResearchAgent）、OpenHands（CodeActAgent），作者做了少量修改（附录 A.6）；模型包括 o1-preview、GPT-4o（2024-08-06）、Claude 3.5 Sonnet（20240620）、Llama 3.1 405B。Gemini-1.5-Pro 因输出被判为背诵而反复被拦截，未能评测（§3.1 脚注 7）。

**实验 1（脚手架与模型，Table 2，p.6）**：

| 配置 | Valid Sub. % | Above Median % | Gold % | Any Medal % |
|---|---|---|---|---|
| o1-preview + AIDE | 82.8 | 29.4 | 9.4 | 16.9 ± 1.1 |
| GPT-4o + AIDE | 54.9 | 14.4 | 5.0 | 8.7 ± 0.5 |
| Claude 3.5 Sonnet + AIDE | 51.1 | 12.9 | 4.4 | 7.6 ± 1.8 |
| Llama 3.1 405B + AIDE | 27.3 | 6.7 | 1.7 | 3.0 ± 1.0 |
| GPT-4o + OpenHands | 52.0 | 7.1 | 2.7 | 4.4 ± 1.4 |
| GPT-4o + MLAB | 44.3 | 1.9 | 0.8 | 0.8 ± 0.5 |

o1-preview 和 GPT-4o（AIDE）分别跑了 16 和 36 个 seed，其余 3 个。

**实验 2（pass@k，Figure 3）**：o1-preview 从 pass@1 的 16.9% 增至 pass@8 的 34.1%；GPT-4o pass@6 为 17.0%（§1、§3.2）。

**实验 3（硬件，Table 3）**：GPT-4o+AIDE 仅 CPU 9.1%、单 GPU 8.7%、双 GPU 10.2%，日志中未见使用第二块 GPU（§3.3）。

**实验 4（时长）**：给 100 小时、节点上限 5,000，奖牌率从 24 小时的 8.7% 升到 11.8%，且有时因“最佳解”选择不完善而下降（§1、§3.4，Figure 4）。

**实验 5（污染）**：熟悉度与成绩无正相关；描述混淆前后 8.5% 对 8.4%（§4，Table 4）。获奖提交未发现抄袭；日志工具标记的违规经人工复核均为误报（附录 A.3–A.4，Table 6）。

**边界**（§6，p.10）：公开竞赛可能已进入预训练语料（GPT-4 基座能复现 Titanic 数据若干行）；任务都有清晰问题、干净数据和明确指标，不覆盖 AI 研发的全部能力；划分和评分代码与原竞赛不同；资源消耗大。

阅读者分析：附录 Table 9 的总列与 Table 2 略有出入（如 GPT-4o+AIDE 8.6 对 8.7，MLAB 1.3 对 0.8，OpenHands 5.1 对 4.4），文中未解释，引用时应以 Table 2 为主。

依据：§3–4、§6，Tables 2–4、Figures 3–5，PDF pp.5–10；附录 A.3–A.4、A.6，pp.15–19；Tables 9–10，pp.28–29。
