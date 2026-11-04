# 具体用例

**原文示例**（Figures 3–4、Example 1，§2，p.186:4）：模式为 `Ads(AdID, Created, AdText, Price)` 与 `Pics(FilePath PICTURE, AdID)`。查询：

```sql
SELECT Min(A.Price)
FROM Ads A, Pics P
WHERE Created > DATE'2022-01-01'
  AND P.AdID = A.AdID
  AND NL(P.FilePath, 'Shows wooden chair with blue cushions')
```

**执行过程**：
1. Alice 把标签请求上限设为 5；
2. 预处理：在一小部分图片上用 CLIP 计算与谓词文本的相似度，并请 Alice 标 3 张图，初步缩小“相似度多高才算满足”的阈值区间；
3. 优化器选择按价格升序处理图片：若随机处理，未看过的图片里总可能有更便宜的椅子，最小值无法确定；按价格升序处理时，第一个确定满足谓词的广告就是最低价（Example 2，§4.1）；
4. 每步算一批相似度，必要时再请求标签；
5. 用改写后的 SQL 计算界：下界在“可能满足”（分数高于阈值下界或尚未计算）的行上求最小价，上界在“必定满足”的行上求（Figure 6、Example 3）；
6. 界的距离满足要求或达到约束时停止，返回 [下界, 上界]。

**不利情形**（Example 3，§4.3）：若有 1,000 条比最便宜的椅子还便宜的铅笔广告，而计算上限只允许评估 500 项，部分铅笔广告未被评估，仍计入“可能满足”，下界无法收紧。

依据：§2 Example 1、§4.1 Example 2、§4.3 Example 3、Figures 3–6，pp.186:4–186:12。
