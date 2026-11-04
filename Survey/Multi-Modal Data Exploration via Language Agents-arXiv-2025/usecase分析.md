# 具体用例

**原文示例**（§3，Figure 2，EHRXQA）：

> Was patient 18061894 prescribed acetaminophen, and did a chest x-ray show any technical assessments until 12/2103?

问题同时需要处方表和胸片影像。规划器把它拆成意图表识别、text2SQL、图像分析等子任务；查处方与找出相关胸片可并行，胸片交给 M3AE 做 VQA，最后由决策器合成答案。每个节点的推理和输出都可供用户查看（Figure 2 说明）。

**ArtWork 上的三个演示**（附录 D）：

1. **解释**（Figure 3）：“按世纪统计描绘战争的画作数量并作图”。分为 4 个任务：SQL 取画作与世纪 → 逐图判断是否描绘战争 → Pandas 计数 → Matplotlib 画柱状图；结论为 16 世纪 1 幅、18 世纪 2 幅。
2. **智能重规划**（Figure 4）：“数据库中最早的文艺复兴画作描绘了什么？”。SQL 找到 `images/img_0.jpg`（1438 年）；BLIP-2 第一次回答不具体，决策器拒绝作答并新增 Task 3，把问题改写为 “What is specifically depicted in the painting?”，得到 “umbrellas”。
3. **并行规划**（Figure 5）：“文艺复兴画作中描绘战争和描绘剑的各有多少？”。两个 image_analysis 任务并行，再汇总，答案为 1 幅和 38 幅。

阅读者分析：例 2 中 1438 年的文艺复兴画作被识别为 “umbrellas”，论文未核对其正确性；这些演示说明流程如何运转，不证明答案正确（阅读者分析）。

依据：[arXiv 2412.18428v2](https://arxiv.org/abs/2412.18428v2)，§3、Figure 2，附录 A、D、Figures 3–5，PDF pp.4、7、13–16。
