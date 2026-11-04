# 具体用例

**例：商品记录链接**（Figure 1，p.1）。锚记录标题为 “Cruzer Force USB Flash Drive 32GB Type-A 2.0 Chrome”。候选包括：

1. Sandisk USB Flash Drive 32GB Cruzer Glide 2.0/3.0
2. Pendrive Sandisk Cruzer Force - SDCZ71-032G-B35
3. Sandisk Extreme Pro 3.1 Solid State Flash Drive 128GB
4. Kingston DataTraveler G4 32 GB USB-stick

三种策略的提问方式：

| 策略 | 提问 | 图中的 LLM 回答 |
|---|---|---|
| Matching | 锚记录与候选 1 是否指同一实体？ | No |
| Comparing | 候选 1 与候选 2 哪个更符合锚记录？ | Record B（候选 2） |
| Selecting | 从列表中选出与锚记录指同一实体的那条，没有则答 [0] | Record 2 |

（Figure 1；附录 B 的提示模板，Table 5，p.13）

在 ComEM 中，先由 Flan-T5-XL 对 10 个候选逐对打 matching 分并取前 4 个，再交给 GPT-3.5 Turbo 或 GPT-4o Mini 做 selecting（§4.1）。

阅读者分析：这类“锚记录 + 候选列表 → 选一个或都不选”的形式与语义 join 的候选精选步骤对应；把它用在项目中时，需要保留一对一假设和 blocking 候选上限，因为 selecting 依赖“最多一个匹配”。

依据：Figure 1，PDF p.1；§3.4–3.5、§4.1，pp.4–6；附录 B、Table 5，p.13。
