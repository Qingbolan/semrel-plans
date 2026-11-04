# 评测与边界

基线：PLM（Sentence-BERT + 多标签输出层，含数据增强版）；LLM 直接提示（GPT-3.5/4、Llama3 8B/70B、Qwen2 7B/72B）；LLM (all knobs)（在提示中列出全部 knob 供选择）；CoT 与任务分解；GPT-3.5 SFT（§6.1，PDF p.10）。检索 top-5；GPT 温度 0。

**实验 1（主结果）**：Table 2，PDF p.11，F1 / SuccessRate。

| 方法 | MySQL SO F1 | MySQL Forum F1 | PG SO F1 | MySQL Run SuccessRate |
|---|---|---|---|---|
| GPT-4 直接 | 0.222 | 0.060 | 0.161 | 0.43 |
| GPT-4 (all knobs) | 0.332 | 0.235 | 0.390 | 0.49 |
| GPT-3.5 SFT | 0.347 | 0.390 | 0.347 | 0.46 |
| Andromeda + GPT-3.5 | 0.348 | 0.382 | 0.321 | 0.79 |
| Andromeda + GPT-4 | 0.441 | 0.449 | 0.398 | 0.76 |
| Andromeda + Qwen72B | 0.437 | 0.412 | 0.410 | 0.60 |

PG SO 上 Andromeda+GPT-4 (0.398) 与 GPT-4 all knobs (0.390) 很接近；Runnable 中 GPT-3.5 优于 GPT-4，作者归因于 GPT-4 不遵守输出格式、推荐 knob 更少（平均 2.63 对 4.85）。

**实验 2（遥测消融）**：Table 7，GPT-3.5 下仅遥测 0.34、仅文档 0.58、二者结合 0.79。

**实验 3（效率、成本与 DBA 对比）**：平均每问 5.37 s（GPT-3.5）/6.79 s（GPT-4），遥测分析 2.85 s（Table 8）；单问成本 $0.006/$0.022。两名 DBA 用 Andromeda 时 SuccessRate 均为 0.76，平均耗时 7.55/3.79 分钟，查手册为 0.42/0.38、14.79/24.51 分钟（Table 9，PDF p.14）。

局限：作者承认 NL 设定以采纳答案为标准、无法验证是否真正解决，因此另设 Runnable（PDF p.9）；值推荐仍有难度，尤其是连续取值（§7）；相似 knob 难以区分（附录）。阅读者分析：未与 Panda、D-Bot 或传统调优器比较；SuccessRate 依赖专家判断且样本仅 100 题；Table 2 中 Qwen72B Forum Recall 印为“.0.171”，属排版错误（阅读者分析）。

依据：§6.2–6.5、Tables 2、7–9、§7，PDF pp.10–14、17。
