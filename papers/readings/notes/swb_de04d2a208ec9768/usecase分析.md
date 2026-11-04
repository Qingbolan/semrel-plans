# 具体用例

**用例：把 LitCovid 的 BioC 标注导入 MMAX2（§2.3，PDF pp.4–5）**

LitCovid 文档由若干 `<passage>` 组成，每段含 `<text>` 和若干 `<annotation>`，标注以字符偏移和长度指向段落文本。步骤如下：

1. 创建空项目：`MMAX2Project` 与 `MMAX2CommonPaths`，并新增 `passages` 和 `entities` 两个 markable 层；两层的标注方案是手工编写的，包含所有取值以及默认值 `none`。
2. 对每个段落，用 `add_basedata_elements_from_string` 生成 basedata，同时在 `passages` 层创建覆盖该段的 markable，并设置 `type` 属性。
3. 用 `render_string(..., mapping=True)` 得到"字符位置 → basedata ID"映射，把每个实体标注的偏移区间转换成 basedata ID 列表，在 `entities` 层创建 markable 并设置 `entity_type`。
4. `add_markable` 遇到完全相同的 span 时返回已有对象而不重复创建。
5. 写出 XML；重新加载项目（此时提供 Java 绑定）时，可得到两层正确的默认值。

本例创建时不提供 Java 绑定，因此不做校验。

阅读者分析：该流程是"异构标注格式 → 统一离位表示"的典型数据集成步骤；字符偏移到 token 的映射依赖 pyMMAX2 的激进分词，若外部标注边界落在 token 内部，会被扩展到整个 token。代码中用 `try/except KeyError` 跳过无法映射的位置，论文未讨论由此可能丢失的边界信息。

依据：§2.1、§2.3，PDF pp.3–5。
