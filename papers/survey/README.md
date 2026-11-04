# Paper 阅读库

论文阅读记录快照，接入图册左侧第三个 Paper 入口。

源目录：`../IntentDB-Adaptive-Semantic-Processing-over-Heterogeneous-Data-Environments/Survey/`。
本次导入保留现有研究记录，不代表本次重新核读原文或复现实验。每篇 README 保留版本、阅读范围和获取缺口；四份分析保留事实、分析判断及待验证推断的区别。发表信息沿用阅读记录，未重新联网核验。

每篇包含 `README.md`、`出发点分析.md`、`解决的问题分析.md`、`Novelty分析.md`、`workload分析.md`。Motivation 是首个阅读 tab 和默认打开页。Use case 与 Benchmark 可分别使用独立的 `usecase分析.md`、`benchmark分析.md`；未独立编写的条目从 workload 原段落提取，保留结果边界。Eddies 已根据原文核读并拆分六个阅读方面。中文原稿不自动翻译，界面标签跟随语言切换。没有公开原文链接的四篇保留已有本地 PDF。

`manifest.json` 记录源路径及文件 SHA-256。更新快照：

```sh
python3 scripts/import_survey.py ../IntentDB-Adaptive-Semantic-Processing-over-Heterogeneous-Data-Environments/Survey
npm run build
```

页面构建只读取本仓库快照，不依赖相邻仓库。通过 `#paper/<id>/<aspect>` 定位论文和阅读方面。

## 本次扩展检索

[2026-10-14 Data Agent 与 Semantic Operator 文献清单](../research/2026-10-14/README.md)记录来源、方向、版本和本次阅读范围。新精读按七个栏目组织，并通过 `scripts/collect_literature.py` 合并到现有目录。检索条目保存在 `config/literature-catalog.json`；只有具备独立分析文件的论文才展示相应阅读栏目。
