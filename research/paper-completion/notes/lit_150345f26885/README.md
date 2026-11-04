# Chen, Wu et al. — InterChat: Enhancing Generative Visual Analytics using Multimodal Interactions

InterChat 是一个“自然语言 + 图上直接操作”（点选、框选、套索、手绘）的生成式可视分析系统：两个 LLM 智能体把直接操作转成文字描述并与提示中的指代短语对齐，第三个智能体用思维链提示生成 D3.js 代码，数据本体只在本地注入，不发给模型。评估包括两个使用场景、10 人用户研究和 2 位工业专家反馈；多模态交互使简单/复杂任务完成时间分别下降 18%/15%。已阅读正文 §1–7 与附录 III（任务分配），附录 I/II 的提示与对话记录仅浏览。

[原文](https://doi.org/10.1111/cgf.70112)

版本：arXiv:2503.04110v2（2025-04-16，作者版，页眉标注 EuroVis 2025 / Computer Graphics Forum，CC BY 开放获取），24 页（正文 pp.1–10，参考文献 pp.10–12，附录 pp.13–24）。DOI 落地页（Wiley）对脚本访问返回 403，故保存 arXiv 版本。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| problem | §1、§3，PDF pp.1–4 |
| method | §4（工作流、意图推断、可视化生成、响应处理），Figures 2–4，PDF pp.4–7 |
| evaluation | §5（使用场景、用户研究、专家反馈）、Figure 7、附录 III，PDF pp.7–9、21–24；p.9 已渲染核对 |
| limitations | §6.2 失败分析、§6.3 局限与未来工作，PDF p.10 |
