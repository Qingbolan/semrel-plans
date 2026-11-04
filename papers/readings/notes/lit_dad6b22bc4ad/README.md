# Wang, Li et al. — DSMentor: Enhancing Data Science Agents with Curriculum Learning and Online Knowledge Accumulation

DSMentor 是一个推理时优化框架：Mentor agent 仅凭题目描述给数据科学题目打难度并排成由易到难的课程，Student agent 按此顺序逐题生成代码，并从不断增长的在线长期记忆（历史题目、生成代码、对错标签）中检索相似示例。用 Claude-3.5-Sonnet 时，QRData 通过率 0.543，比最佳基线 GPT-4 (PoT) 高 5.2 个百分点，因果题高 8.8 个百分点。已阅读 arXiv 正文全部 5 节与 Tables 1–7；正文多处引用的"补充材料附录"不在该 PDF 中，未能阅读。

[原文](https://arxiv.org/abs/2505.14163)

版本：arXiv:2505.14163v1（2025-05-20），13 页（正文 pp.1–11，参考文献 pp.11–13）。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| problem | §1、Figure 1，PDF pp.1–3 |
| method | §3.1–3.2、Figures 2–3，PDF pp.4–6 |
| evaluation | §4.1–4.4、Tables 1–7、Figure 4，PDF pp.6–11 |
| limitations | §5 结论的未来方向，p.10；正文无局限章节，附录不在 arXiv 版本中 |
