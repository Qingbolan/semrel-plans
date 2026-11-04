# Zeldes et al. — eRST: A Signaled Graph Theory of Discourse Relations and Organization

本文提出 Enhanced Rhetorical Structure Theory（eRST）：在保留 RST 单根投射主树（primary tree）与核心/卫星（nuclearity）的前提下，加入受信号约束的次级边（secondary edges，可非投射、可成环、可与主边并存）以及锚定到 token 的分类信号（DM 与 6 类以上非 DM 信号）。作者把 GUM v9（213 篇、12 个语体、203,879 token、26,352 EDU）及 RST-DT 测试集 38 篇扩展为 eRST 标注，定义含信号与次级边的评测指标和官方 scorer，并给出流水线基线：在给定金标准主树时次级边 Full=0.184，换成预测主树（DMRST）后跌到 0.030。已阅读 §1、§3–§7 全文与 §2 相关工作概要；未逐条核对附录 A/B 的关系清单与中文树库说明。

[原文](https://aclanthology.org/2025.cl-1.3)

版本：Computational Linguistics Vol.51 No.1（2025），pp.23–72，DOI 10.1162/coli_a_00538，ACL Anthology PDF 2025.cl-1.3，50 页（下文页码为 PDF 页，期刊页 = PDF 页 + 22）。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| problem | §1、§2.1–2.6，PDF pp.1–10 |
| method | §3（主树、次级边、信号、复杂度），§4.1 标注流程，§5.1–5.2 任务定义与模型，PDF pp.10–22、28–33 |
| evaluation | §4.1 一致性（Tables 3、5），§4.2 语体统计（Table 6），§5.3 Tables 8–9，§6 Table 10，PDF pp.19–27、33–37 |
| limitations | §3.4、§5.3 末、§7，PDF pp.17、34–36、40–41 |
