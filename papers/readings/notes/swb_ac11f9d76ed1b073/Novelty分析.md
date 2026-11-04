# 贡献与评价

**论文自述贡献**（§1，p.2）：

1. 系统比较三种 LLM 实体匹配策略，分析各自适用场景与不足；
2. 提出组合多种策略和多种 LLM 的 ComEM 框架；
3. 在 8 个数据集、10 个 LLM 上做实验验证。

**主要发现**（§4.2–4.4，pp.6–9）：

- 发现 1：引入记录间交互很关键。论文称 comparing 比 matching 平均高 10.7 个 F1 点，selecting 再比 comparing 高 5.32 点；selecting 比同样输入记录数的 6-shot matching 高 7.97 点。
- 发现 2：ComEM 比单一的 comparing 或 selecting 高 2–18 个 F1 点，且花费更少。
- 发现 3：selecting 最具性价比，成本不到 matching 的一半，因为不必反复输入锚记录和任务说明。
- 发现 4：comparing 和 selecting 都受位置偏差影响，匹配记录在候选列表中越靠后，F1 越低（Figure 3）。
- 发现 5–6：没有一个 LLM 在所有策略上都最好；用于排序过滤时 matching 比 comparing 更合适（Figure 5）。

**阅读者评价**：

- 新意在于把实体匹配从二分类改写为列表选择，并用“小模型粗排＋大模型精选”降低成本；列表式重排思路在信息检索中已常见，论文本身也引用了相关工作。（阅读者分析）
- 按 Table 4 的均值核算：selecting 相对 matching 的提升 (17.58+14.46)/2=16.02，与文中一致；但 matching→comparing 为 (2.84+16.56)/2=9.70，comparing→selecting 为 (14.74−2.10)/2=6.32，与文中的 10.7 和 5.32 不符（两者之和仍为 16.02）。（阅读者分析）
- 在 GPT-4o Mini 上 comparing 平均 84.36 反而高于 selecting 的 82.26，所以“selecting 最好”主要由 GPT-3.5 Turbo 的结果支撑。（阅读者分析）

依据：§1、§4.2–4.4，Table 4、Figures 3–5，PDF pp.2、6–9。
