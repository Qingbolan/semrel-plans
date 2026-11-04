# 工作负载

| 领域 | 演化数据 | 测试数据 | 指标 |
|---|---|---|---|
| 电子表格（ID） | SpreadsheetBench-Verified 前 200 题 | 后 200 题（Vrf）；完整 SpreadsheetBench 去除演化题后 2,529 例（Soft/Hard） | 官方判定，3 个种子均值 |
| 表格 QA（OOD） | — | WikiTQ 2,810 例、HiTab 1,585 例，均转为表格操作任务 | 通过率 |
| 数学 | 400 道 DAPO 题 | 100 道不相交 DAPO 题；AIME 2026 30 题 avg@8 | 通过率 |
| DocVQA | 50 例 | 其余 5,299 例 | ANLS、Acc（ANLS≥0.5） |
| PDF / PPTX / DOCX | VRDU / TSBench / 合成 DOCX 任务 | VAREX / TSBench 按幻灯片不相交的 OOD 划分 / OfficeBench DOCX 子集 | 本地验证器通过率 |

来源：§3.1、§3.4–3.5、§4.4，附录 A（pp.4–5、8–9、13–14）。

**模型与配置**：Qwen3.5-122B-A10B 与 Qwen3.5-35B-A3B 同时作为 skill 作者与使用者；跨家族实验使用 Gemma-4-31B-it 与 GPT-5.5-high（§3.3，p.5）。Stage 1 每题一条轨迹；Stage 2 并行 128 个子 agent，合并批大小 32；不设单独工具调用上限；总计约 20,000 GPU 小时（附录 A，pp.13–14）。

**补丁选择实验**：从 200 题演化集中抽取 32 题作为验证集（§4.3，p.8）。

阅读者分析：所有基准都有可自动判定的正确性信号，这是 Stage 1 区分成功/失败轨迹的前提；没有明确判定器的开放式任务不在本文范围内。
