# Zhang, Li, Luo, Tang — SketchFill: Sketch-Guided Code Generation for Imputing Derived Missing Values

SketchFill 处理“派生缺失值填补”（DMVI）：缺失的数值可由同行其他列或相邻行通过公式算出（如 BMI、含税总价、5 期移动平均）。方法用用户给的通用 Meta-Sketch（七步伪代码模板）引导 LLM 生成针对该表的 Domain-Sketch，再转为 Python 代码；在抽样遮蔽的干净行上验证，失败则由 Reflector 修正（最多 3 次），成功后由 Summarizer 泛化为函数批量执行。

GPT-4o 后端下，作者报告在 5 个领域数据集上总体准确率 84.2%，比 CoT 高 56.2%、比 MetaGPT 高 78.8%（§5）。已阅读正文与附录 A–D；Fig. 4 柱状图标签过小，主要依据 Table 2 数值与正文陈述。

[原文](https://arxiv.org/abs/2412.19113)

版本：arXiv:2412.19113v1（2024-12-26，Preprint），19 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | §1、§3.1，PDF pp.1–5 |
| 方法 | §3.2–3.6、Algorithm 1、Fig. 3，PDF pp.5–7；附录 B 提示模板，pp.16–17 |
| 评测 | §4、Table 1–2、Fig. 4，PDF pp.8–10；附录 A、C、D，pp.14–19；p.9 已渲染核对 |
| 局限 | §5 Conclusion 末段，PDF p.10；附录 C.3，p.18 |
