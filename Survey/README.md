# Paper 阅读库

46 篇论文的阅读记录快照，接入图册左侧第三个 Paper 入口。

源目录：`../IntentDB-Adaptive-Semantic-Processing-over-Heterogeneous-Data-Environments/Survey/`。
本次导入保留现有研究记录，不代表本次重新核读原文或复现实验。每篇 README 保留版本、阅读范围和获取缺口；四份分析保留事实、分析判断及待验证推断的区别。发表信息沿用阅读记录，未重新联网核验。

每篇包含 `README.md`、`出发点分析.md`、`解决的问题分析.md`、`Novelty分析.md`、`workload分析.md`。界面中的 Use case 从 workload 原段落提取，保留结果边界。中文原稿不自动翻译，界面标签跟随语言切换。没有公开原文链接的四篇保留已有本地 PDF。

`manifest.json` 记录源路径及文件 SHA-256。更新快照：

```sh
python3 scripts/import_survey.py ../IntentDB-Adaptive-Semantic-Processing-over-Heterogeneous-Data-Environments/Survey
npm run build
```

页面构建只读取本仓库快照，不依赖相邻仓库。通过 `#paper/<id>/<aspect>` 定位论文和阅读方面。
