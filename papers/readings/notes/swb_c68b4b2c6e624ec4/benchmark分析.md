# 评测与边界

**实验 1（8 个通用 LLM，困难子集）**（Table 2，PDF p.5；200 dpi 渲染核对）。下表列各领域最高分及对应设置：

| 领域（指标） | 最高分 | 模型 / 设置 |
|---|---|---|
| SARA Numeric（Acc） | 44.4 | O3 / Zero-Shot |
| Airline（Acc） | 90.8 | O3 / Few-Shot |
| SARA Binary（F1） | 70.0 | Claude Sonnet 4.5 / Direct |
| USCIS-AAO（F1） | 71.5 | GPT-5.1 / Direct |
| Housing（F1） | 46.8 | GPT-5.1 / Few-Shot |

置信区间很宽，例如 O3 Zero-Shot 的 SARA Numeric 为 44.4（+15.6/−15.8）。没有模型在所有领域和设置中都最好；开源模型对提示更敏感，Qwen3-235B 在 SARA Numeric 上从 Few-Shot 的 0.7 升到 Direct 的 32.1（§4.1，PDF p.6）。走 Prolog 时弃权率更高，Direct 则减少弃权但错误更多（§4.1、Figure 2，PDF pp.6–7）。

**实验 2（训练 Qwen2.5-32B）**（§4.2、Table 3，PDF pp.7–8）：SFT、DPO+SFT、GRPO+SFT、GRPO+DPO+SFT 在二分类任务上有提升（Few-Shot USCIS-AAO 从基座 10.3 升到 45 以上），但 SARA Numeric 在所有方法与设置下都低于 10。

**实验 3（编码模型与推理强度）**（附录 C.1–C.2、Table 7，PDF pp.21–22）：GPT-5.2-Codex 最强（Airline Few-Shot 95.5、SARA Numeric Zero-Shot 45.8），Qwen 编码模型多处接近 0；提高推理强度并不稳定地提升 SARA Numeric。

**边界**：摘要称最佳困难子集成绩为 SARA Numeric 44.4%、Housing 46.6，但 Table 2 中 GPT-5.1 Few-Shot 的 Housing 为 46.8，Table 7 中 GPT-5.2-Codex 的 SARA Numeric 为 45.8；Table 4 中 USCIS-AAO Few-Shot 一行合计 96.4%，不是 100%（阅读者分析）。困难子集仅 28–80 例，原文无独立的局限性章节；伦理声明强调基准只用于研究、不可作法律建议（PDF p.10）。
