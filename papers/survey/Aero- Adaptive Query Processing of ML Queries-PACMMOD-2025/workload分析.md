# 工作负载

**数据集**（§7.1，p.14）：

| 数据集 | 规模 | 模态 |
|---|---|---|
| Dog | YouTube 视频，19k 帧 | 视频 |
| Warehouse | YouTube 视频，14k 帧（扩展实验复制为 112,912 帧长视频） | 视频 |
| IMDB | 15k 张演员人脸图片 | 图像 |
| FoodReview | 600 条麦当劳 Google 评论及评分 | 文本 |

**查询**（§7.1，pp.14–15）：6 条作者构造的 SQL。

| 查询 | 数据 | 谓词 | 考察点 |
|---|---|---|---|
| Q1 | Dog | 检测到 dog + 品种 = labrador + 颜色 = black | 谓词重排与路由策略 |
| Q2 | Dog | Q1 + `Area > 0.4` | 谓词数增加 |
| Q3 | Warehouse | person + no hardhat | Laminar 资源利用 |
| Q4 | Warehouse | 同 Q3，但先跑两条探索查询缓存部分结果 | 部分缓存与自适应路由 |
| Q5 | IMDB | 年龄 = 20–29 + 情绪 = happy | 选择率随数据漂移 |
| Q6 | FoodReview | 13B 本地 LLM（Orca，CPU）判断评论关于 food + `rating <= 1` | worker 负载失衡 |

**谓词统计**（Table 1，p.16）：

| 谓词 | 平均选择率 | 平均代价 (ms) |
|---|---|---|
| DogBreedClassifier = labrador | 0.06 | 30.35 |
| DogColorClassifier = black | 0.15 | 0.95 |
| person ∈ ObjectDetector | 0.83 | 21.79 |
| no hardhat ∈ HardHatDetector | 0.25 | 35 |
| AgeClassifier = 20–29 | 0.57 | 12.2 |
| EmotionClassifier = happy | 0.4 | 16 |

**模型**：ObjectDetector 为 YOLOv5；DogColorClassifier 是基于 HSV 范围的启发式；品种、年龄、情绪用 ViT；HardHatDetector 为微调 YOLOv8s（§7.1，p.15）。

**单位与指标**：单位是帧、检测出的对象、图片或评论；主指标为查询处理时间，辅以 GPU 利用率、队列占用和阶段耗时。没有人工标注的准确率实验，只比较与 EvaDB 的结果是否一致（§7.2）。

阅读者分析：谓词都是固定 CV/LLM 模型输出上的确定性判断，与开放语义谓词不同；Q5 的选择率漂移（情绪在前段图片中选择率高、年龄在后段高）是唯一显式的分布漂移场景。

依据：[DOI 10.1145/3725408](https://doi.org/10.1145/3725408)，§7.1、Table 1，pp.14–16。
