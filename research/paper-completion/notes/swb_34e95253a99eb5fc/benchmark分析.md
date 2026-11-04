# benchmark

**基线**（§5.1，PDF pp.6–7）：14 个不带工具的 LLM/VLM（GPT-5、Gemini-2.5-Pro、GPT-4o、Claude Sonnet 4 同时测文本版和带图版）；6 个以 GPT-5 为骨干的开源智能体框架（SmolAgents、Aworld、Agentorchestra、OWL、WebSailor、Cognitive Kernel）；3 个闭源智能体（Manus、Gemini Deep Research、Grok DeepSearch）。

**主要结果**（Table 1，PDF p.7）
- 不带工具：最好为 GPT-5 VLM，10 位准确率 29.27%（2 位 82.12%）；Qwen2.5-72B、Nemotron-32B 接近 0。
- 开源智能体：SmolAgents VLM 46.83%、SmolAgents LLM 42.72%、Aworld 与 Agentorchestra 41.30%、WebSailor 35.44%、Cognitive Kernel 26.42%。
- 所有方法的准确率都随位数增加而下降；较强的模型与智能体 2 位准确率约 72%–83%，差距主要拉开在 6 位及以后。
- 49 条子集（Table 2，PDF p.7）：Gemini Deep Research 40.81%、Manus 30.61%、Grok DeepSearch 26.53%；SmolAgents 与 Aworld 均为 42.86%。

**消融与分析**（§5.2、§6，PDF pp.8–11）
- 加入人工决策规则：SmolAgent 46.83→43.83，Aworld 41.30→42.95，WebSailor 35.44→35.43（Table 3）。
- 图片：GPT-5 骨干 42.72→46.83，其他骨干变化很小（Table 4）。
- 访问网页：42.72→42.09。
- 思考深度：WebSailor 从 Overthink 35.44 到 No-Think 40.82（Table 5）。
- 骨干模型：SmolAgents 用 GPT-5 为 42.72，Qwen-MAX 为 17.43（Table 6）。
- 测试时扩展：多数投票 K=1–16 几乎无提升；自我反思 42.72→42.57（Figure 6）。
- 失败类型：智能体主要减少了编码过时和不存在编码这两类错误，剩余错误以“编码有效但不正确”为主（Figure 4）。

**边界**：人类 95.0% 的测法在已读部分没有说明；闭源系统只评 49 条；公开数据删除了图片和 URL；没有置信区间或多次运行方差（多数投票除外）；国家特定后 4 位以哪国税则为准没有明确说明（阅读者分析）。

依据：[arXiv:2510.19631v1（2025-10-22 提交，PDF 标注 2025-10-23），38 页](https://arxiv.org/abs/2510.19631)。
