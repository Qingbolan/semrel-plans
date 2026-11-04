# 具体用例

**原文示例**（Listing 2，§4.2，p.9；评测中的 Q4，§7.1，p.15）：仓库监控视频的探索式分析。用户先跑两条探索查询，再跑最终检索。

```sql
SELECT ObjectDetector(frame).labels FROM Warehouse WHERE id > 1000 AND id < 7000;
SELECT HardHatDetector(frame).labels FROM Warehouse WHERE id > 8000 AND id < 14000;
-- Q4
SELECT * FROM Warehouse
WHERE ['person'] <@ ObjectDetector(frame).labels
  AND ['no hardhat'] <@ HardHatDetector(frame).labels;
```

**为什么固定顺序不行**：帧 1000–7000 的 `ObjectDetector` 结果已缓存，这段应先跑它；帧 8000–14000 的 `HardHatDetector` 已缓存，这段应先跑它。任何单一全局顺序都只适合一半视频（§4.2）。

**Aero 的做法**（§4.2，p.10）：Eddy 对每个批次查缓存命中率，估计代价 = (1 − 命中率) × 实测代价，把批次先送到估计代价最低的谓词。

**结果**（§7.3，Fig. 9–10，p.18；Laminar 关闭）：

| 配置 | 处理时间 (s) |
|---|---|
| 基线（静态固定顺序） | 498.2 |
| + Eddy cost-driven | 545.0 |
| + Eddy reuse-aware cost-driven | 386.8 |

reuse-aware 相对基线快 1.29×。不考虑缓存的 cost-driven 反而更慢：它在后半段视频仍优先 `ObjectDetector`，且启动画像阶段把数据送给所有谓词，产生额外代价（§7.3）。

阅读者分析：两条探索查询本身的计算代价未计入 Q4；Q4 端到端时间（Aero 116.0 s）还略高于 Q3（104.4 s），作者解释为缓存降低 GPU 利用率并带来查找开销（§7.2）。

依据：[DOI 10.1145/3725408](https://doi.org/10.1145/3725408)，§4.2、§7.1–7.3、Fig. 6、Fig. 9–10，pp.9–10、15–19。
