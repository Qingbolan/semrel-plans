# 具体用例

**Fig.1 与 Fig.3 的电动车表（pp.1、3）**：表中有四列，列名部分缺失，样例行如 `Nissan, Leaf, 98112, JN1AZ0CP4C`。

| 步骤 | 提示要点 | 输出 |
|---|---|---|
| ① 表类别检测 | 给出 DBpedia 类别列表和"以 https://dbpedia.org/ontology 开头"的前缀 | ElectricVehicle |
| ② 列类型标注 | 一个"作家表"示例，要求为每列给出 `dbo:` 属性 | Make、Model、Zip、VIN Prefix 等 |
| ③ 连接列预测 | 给出两个 DataFrame，补全 `pd.merge(df1, df2, left_on=` | 与另一表 `car_registration(name, vehicle_id_number)` 连接时，输出 `(VIN_prefix, vehicle_id_number)` |

由于三步共享上下文，第一步得到的 ElectricVehicle 有助于第二步推断 Make、Model（§1，p.2）。

**Anchoring 示例（Fig.4，p.4）**：模型给第 1 列输出了本体中不存在的 `iucnStatus`。没有 anchoring 时，后续又产生不存在的 `animalName`，最近邻修正也只能给出错误的 `animal`。有 anchoring 时，系统改写历史为合法的 `conservationStatus` 后重开对话，第 2 列得到正确的 `binomial`。

阅读者分析：这类任务可作为语义数据湖查询的前置步骤（为无名列加类型、推荐连接键）；但 Chorus 的连接预测只输出列对，不评估连接后的结果质量。
