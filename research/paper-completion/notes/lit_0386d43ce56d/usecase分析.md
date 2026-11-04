# 具体用例

IoT 数据集的例子贯穿全文：

1. **输入**：原始一行（温度 T1，CO2 浓度 C1，位置 L1，时间 t1）。
2. **列映射**：LLM 把列映射到元模型概念。
3. **传感器拆分**：这一行变成（Temp, T1, L1, t1）与（CO2, C1, L1, t1）两行，位置和时间各自复制（§3.1 “Sensor Splitting”）。
4. **补列**：如果数据只有 “value”“location”“timestamp” 三列，系统会补出 System、Device、SensingDevice、Sensor 列并填入合成值，再补 MinValue/MaxValue 以支持能力依赖（§3.1 “Column Generation”）。

**抽出的 OFD**（Table 1，IoT 数据）：

- 拒绝依赖 `Device → System`、`SensingDevice → Device`；
- 设备链接 `ds18b20_1 → device_in_1`；能力依赖 `ds18b20_1 → MaxValue/MinValue`；
- 位置依赖 `ds18b20_1 → Room1`；时间依赖 `device_in_1 → device_main`。

**检测输出**：规则 `t1&t2&EQ(t1.SensingDevice,t2.SensingDevice)&IQ(t1.Device,t2.Device)` 要求同一 SensingDevice 对应同一 Device，偏离组内众数的 Device 值被标为错误单元格（§5）。

依据：[arXiv:2404.18681v1](https://arxiv.org/pdf/2404.18681v1)，§3.1、§5、Table 1，PDF pp.4、6–7。
