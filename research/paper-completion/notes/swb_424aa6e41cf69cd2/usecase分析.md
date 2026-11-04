# 具体用例

**标注一个系统名与它的商品名**：原文以抗糖尿病药 troglitazone 为例，它有商品名 Rezulin，系统名为一长串 IUPAC 名称（p.4）。在 CHEMDNER 中，troglitazone 标为 TRIVIAL，IUPAC 全称标为 SYSTEMATIC，若文中出现缩写（至少 3 字符）则标为 ABBREVIATION；三者各自是独立的字符区间，语料本身不把它们链接到同一结构（pp.5、11；Fig. 1）。

**需要排除的表达**：同一摘要中若出现 antibiotic、hormone、metabolite 等角色词，或 inactivator 这类泛概念，按负例规则不标注（p.5）。Alkaloid 这类结构类别名原则上不能用单一 Markush 式表示，指南为此提供了可标为 FAMILY 的示例清单（p.7）。

**下游用途**：作者设想用 CHEMDNER 训练的标注器为人工策展生成预标注、构建化学词典、做"是否含化学提及"的文档分诊，或按学科训练子领域标注器（p.14）。

阅读者分析：若作为语义过滤或抽取任务的数据源，CHEMDNER 只提供"哪里有化学实体及其命名类型"，不提供实体身份或性质；任何"找出提及某化合物的摘要"类查询需额外的规范化步骤，本文未提供。

依据：pp.4–7、11、14；Fig. 1。
