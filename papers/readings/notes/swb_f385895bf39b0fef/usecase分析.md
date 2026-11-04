# 具体用例

**政策 10（Tier 1，Certain Objects：把受保护群体比作物品的去人性化言论）的构建流程**（Figure 2，PDF p.3）：

| 步骤 | 例子 |
|---|---|
| 匹配仇恨样本 | "Women are objects" |
| GPT 扩充仇恨样本 | "Women are the objects of men" |
| 验证 | 删除不匹配的条目 |
| 检索非仇恨样本 | "Women are not sexual objects" |
| GPT 扩充非仇恨样本 | "Black people should not be treated as objects" |
| 验证非仇恨样本 | 删除"Some men are sexist"（与政策无关） |

**测试发现**：多数模型检测不到 Certain Objects、Change Sexual（宣传改变性取向/性别认同的服务）、Economic Exclusion、自认对受保护特征不宽容等政策下的仇恨言论。例如多数模型漏掉了"MAKE WOMEN PROPERTY AGAIN!!!!"（§4.2.1，PDF p.7）。

对 Change Sexual 政策，标注者最初只在现有数据集中找到 3 个匹配样本，只能靠人工编写或 GPT 生成补足（§3.1，PDF p.4）。

阅读者分析：若把内容审核当作带政策条款的语义过滤，本例说明需要为每条条款单独准备正例与"相似但不违规"的反例，否则检测器在冷门条款上的漏检会被整体指标掩盖。这是项目派生解读。

依据：[Findings of NAACL 2024，pp.2691–2710](https://aclanthology.org/2024.findings-naacl.172)，§3.1、§4.2.1、Figure 2，PDF pp.3–4、7。
