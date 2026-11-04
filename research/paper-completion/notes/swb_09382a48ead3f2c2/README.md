# Zhang et al. — LogiCode: an LLM-Driven Framework for Logical Anomaly Detection

LogiCode 让专家先从正常样本中写出逻辑规则，再由 GPT-4 把规则和任务说明转成调用视觉 API（find、locate、count、determin_color、size）的 Python 代码，执行后输出"正常/异常 + 原因"。作者同时发布 LOCO-Annotations（MVTec LOCO 上的 2,908 张图像，含像素级对象分割和"异常类型：具体原因"标注）与评测协议 LogiBench。论文报告 5 类平均准确率 0.989，但代码生成成功率仅约 0.59，而且 find() 从 LOCO-Annotations 读取对象位置。已通读全文，未复现实验。

[原文](https://arxiv.org/abs/2406.04687)

版本：arXiv:2406.04687v1（2024-06-07，标注为投稿 IEEE T-ASE），11 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | Abstract、§I–§II，PDF pp.1–3 |
| 方法 | §III、Fig. 3、Table I，PDF pp.3–5 |
| 评测 | §IV-A–C、Tables II–V、Fig. 7，PDF pp.5–9 |
| 局限 | §IV-D Discussions、§V，PDF p.9 |
