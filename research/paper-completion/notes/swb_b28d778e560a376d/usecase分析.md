# 具体用例

**Wildlife 场景 Q5**（Example 4.2，§4.2、§5.4，PDF pp.5、11）：找出出现大象的城市，证据可来自图像或音频：

```sql
SELECT DISTINCT city
FROM (SELECT city FROM ImageTable I
      WHERE AI.IF(I.image, 'the picture shows an elephant'))
UNION (SELECT city FROM AudioTable A
      WHERE AI.IF(A.audio, 'this sounds like an elephant'));
```

数据表为 `ImageTable(image, city, stationID)` 与 `AudioTable(audio, city, StationID)`，真值来自原数据集的物种标签。

执行差异：ThalamusDB 一旦确认某城市满足条件就不再评估该城市其他行，因为额外求值不会改变 `DISTINCT city` 结果，所以费用明显更低；其他系统会评估全部相关行（§5.4，PDF p.11）。LOTUS 不支持音频，Wildlife 十条只支持四条（§5.3）。

阅读者分析：这个例子说明语义查询的成本优化可以利用查询语义（去重、LIMIT、存在性），而不仅是算子级优化；对本项目而言，它是“跨模态语义过滤 + 关系去重”的典型 pattern（阅读者分析）。

依据：§4.2、§5.3–5.4，PDF pp.5、8–11。
