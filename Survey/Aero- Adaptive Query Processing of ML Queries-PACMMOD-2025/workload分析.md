# workload分析

**验证什么。** 已知ML谓词执行时，动态顺序、部分缓存和worker资源调整能否在不换模型的前提下提高吞吐。

**数据、单位与gold。** 正式论文§7.1：Dog为YouTube19k帧，Warehouse14k帧，IMDb15k人脸图片，FoodReview600条麦当劳Google评论；6个作者构造SQL查询。单位是帧、检测对象、图片或评论。主要指标处理时间、GPU利用率、队列/worker负载和路由开销；没有独立人类gold准确率实验，保持的是固定UDF与谓词结果，不是模型绝对正确。

**最有说服力用例（原文Q4重述）。** 仓库安全检索需要person与no-hardhat两个检测结果。使用前已有探索查询分别缓存帧1000–7000的ObjectDetector和8000–14000的HardHatDetector，但固定路由不能充分利用这种局部性；使用后记录根据已有结果和当前成本走不同顺序，避免重复UDF。预热查询费用应与后续查询一起看，不能当冷启动免费缓存。

**baseline及公平性。** EvaDB含静态Cascades式优化、缓存和重排；VIVA用3%输入估计，仅开启重排，关闭会影响质量的过滤/模型替换；资源实验比Ray Serve autoscaling。统一AMD EPYC/256GB/NVIDIA A40；不同功能对比在§7对应实验说明。

**效果范围。** 论文摘要及§7最高6.4×是所测工作负载上限。Q1–Q2测犬种/颜色/面积，Q3–Q4测仓库及缓存，Q5测年龄/情绪，Q6测LLM与rating过滤；不是开放数据源探索或LLM规划收益。

来源：[正式27页PACMMOD3(3)，Article174，2025，DOI10.1145/3725408](https://upenn.ferric.systems/dbscholar/sigmod_papers/2025/3725408.pdf)。本分析为原文重述与比较边界判断，未复现实验。
