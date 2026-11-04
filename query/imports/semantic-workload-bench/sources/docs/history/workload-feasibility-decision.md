# Workload framing and evidence gate — 2026-09-05

目标 workload：在共享异质数据环境中，对大量记录执行同一语义判断，但每条记录所需的证据路径、工具组合或停止条件取决于中间观察；批内又存在可复用的知识、工具及执行策略。

这不是 Data Agent 独占的任务类别。Coding Agent 也能探索、写脚本、调用模型并复用结果。研究应检验运行时自适应及批内复用的增益，而不是按产品名称定义能力差异。固定的是关系输入、谓词、输出语义和外层 DAG；内部取证流程是否需要自适应是待验证变量。

比较至少包括：直接静态算子；固定检索/工具/DAG 加语义算子；允许一次探索并生成可复用程序的 Coding Agent；允许批内缓存和规划复用的 Data Agent；最后才是由 discovery 轨迹提取的受控动态算子。共享模型、完整可访问证据、预算及评分协议，计入环境探索、编译、索引、缓存预热和摊销成本。时间、token/金额与质量分别报告，不直接相乘；比较达到同一质量时的成本及延迟。

## 当前证据

- MMQA 场馆湖：保留为候选环境，尚不通过第一标杆门槛。32 条分层抽样产生 64 个谓词判断；两位 AI 审查者共同未决 57 个、分歧 2 个、暂时一致可判定 5 个。没有新增 gold，也不是模型准确率实验。图像可能是城市拼图、logo 或无法回答谓词的外景。多场馆单元格还存在量词/实体映射歧义。
- 固定检索审计：32 条都有额外候选命中，但命中不等于相关或充分。未证明固定检索无法解决任务。容量冲突审查也未建立可核验的同时间、同配置冲突正例。
- FEVEROUS：完整文本—表格库 5,421,406 页；按 ID 哈希抽取 train/dev 各 1,000 条官方标注样本。全部 16,985 个逐记录 content/context 引用可访问；其中 train/dev 各有 270/251 条含文本与单元格混合证据集。两组共享 3 个黄金证据页面，因此 dev 不能宣称为来源隔离的 confirmatory split。它是文本—表格候选/对照，不是视觉多模态目标的替代品。
- AVerImaTeC：本地有声明图像和标签，但缺独立 knowledge store。不能把标注者选定的问答图片直接作为公开证据环境。

## FEVEROUS 复现与边界

完整源数据库：`external/repository/FEVEROUS/data/feverous_wikiv1.db`；SHA256 `a980581f55d46a252090b29269954503735b6f00274d05225476a650ab940276`。解压校验收据见 `outputs/feverous-lake-feasibility.json`。

```sh
python scripts/build_feverous_pilot.py --source external/repository/FEVEROUS/data --wiki external/repository/FEVEROUS/data/feverous_wikiv1.db --corpus-sha256 a980581f55d46a252090b29269954503735b6f00274d05225476a650ab940276 --output outputs/feverous-batch-v1
```

已有输出不可覆盖，复现请指定新目录。公开输入只有 claim、共享谓词及完整 corpus 引用；gold、annotator operations 和证据检查结果独立保存在 private。尚未创建运行时文件访问隔离。读取器支持只读页面、原始元素和标题前缀检索，保留 Unicode NFD、表头及跨度；当前没有全库 ranked/full-text 检索，不构成强静态基线。

外层 DAG 是 scan → sem_filter → project → count。当前仅完成数据与契约准备；没有执行模型、没有静态—Agent gap、没有运行成本结论、没有已验证动态组件。下一实验门槛是建立强固定取证基线和可审计 Agent 执行器，再检查是否存在证据充分且可复现的动态优势。
