# Vision-LLM-Integration → 医疗图像 batch 原型

已构造可执行研究原型：给定医院影像资源环境，对一批病例图像执行共享分类任务。环境包括分类代码、模型权重、类别说明和带标签的训练参考图；测试标签在 private。当前使用公开基准模拟医院任务，不是医院部署数据。

## 实际产物

`outputs/vision-medical-batch-v1/public/`：

- `batches/pathmnist.jsonl`：1,000 张结直肠组织病理切片，9类组织分类。
- `batches/breastmnist.jsonl`：156 张乳腺超声图，恶性 vs 正常/良性。
- `models/`：两个本次新训练的 MedicalConvNet 权重及完整 model card。
- `tool_code/`：可阅读的模型、预处理、批推理代码。
- `legacy_code/`：原项目的 Python/config 资源快照及已知问题说明。
- `references/`：每数据集32张官方 train 参考图及标签。
- `tasks/`：固定输入、类别字典和 DAG。

`private/` 保存原test标签、训练来源index和重叠审计；`public_manifest.json` 保存1265个公开文件的SHA256/大小。模型推理过程不读取private，但当前未配置OS级沙箱，实验运行时仍需显式只挂载public。

原项目 `/Volumes/Element/Github2/Vision-LLM-Integration` 保持只读，commit `ebcb99edbe929fa8b7620171d3013ce569eddb4b`。该checkout没有.pth权重，也没有BreastMNIST/ChestMNIST原图。raw目录是原混凝土裂纹任务，不混称医疗病例；上传图及解释图未纳入有gold批任务。新增权重是bootstrap模型，不是恢复的原项目模型。

## 任务与比较

固定DAG：`scan → validate_image → sem_map(classify) → project(case_id,class_id) → group_by(class_id).count`。这里分类用sem_map；“仅保留恶性图像”可接过滤或定义等价sem_filter。输入显式提供modality，不通过隐去已知元数据制造路由难题。

最小有意义比较：直接视觉语义算子；固定专业模型调用；Coding Agent探索一次后生成整批程序；支持批内复用的Data Agent；最后才是从独立discovery轨迹提取的动态算子。所有系统同样可访问模型/代码/参考资料，分别记录探索、模型加载、批推理、LLM tokens、实际工具耗时和质量。不能把禁用专业模型的静态算子作为唯一对照。

若只需选定一个模型后处理全部切片，固定程序很可能足够；这是待接受的研究结论。动态机制需要由实际错误恢复、不同证据路径或工具选择的收益证明，不能由湖里资源多推出。

## 运行与实测

```sh
python scripts/build_medical_batch.py --source outputs/vision-medical-source --project /Volumes/Element/Github2/Vision-LLM-Integration --output outputs/vision-medical-batch-v1
python scripts/run_medical_fixed.py train --lake outputs/vision-medical-batch-v1 --source outputs/vision-medical-source
python scripts/run_medical_fixed.py predict --lake outputs/vision-medical-batch-v1 --output outputs/vision-medical-fixed-v1
python scripts/run_medical_fixed.py score --lake outputs/vision-medical-batch-v1 --output outputs/vision-medical-fixed-v1
```

复现使用新输出目录。依赖 `pip install -e '.[medical]'`。下载源固定为 [MedMNIST v3.0 / Zenodo 10519652](https://zenodo.org/records/10519652)，两个NPZ经官方MD5核验，SHA256在construction.json。使用28×28版本，仅作为轻量研究原型。

| 任务 | 测试数 | 准确率 | 批推理秒 | 模型训练秒 |
|---|---:|---:|---:|---:|
| 病理9分类 | 1000 | 45.7% | 0.486 | 12.531 |
| 乳腺超声2分类 | 156 | 73.08% | 0.095 | 1.283 |

CPU/PyTorch2.8.0，4线程，batch128，seed42；train按ID哈希取Path10000/Breast546，3epoch，Adam0.001，无调参/重试/增强，未使用test训练。推理计入读PNG/预处理/前向，加载分别约0.002/0.008秒另计；未含进程启动，训练成本单列。两个固定模型均0LLM调用/0LLM tokens，计算金额未估算。分类置信度未校准。

乳腺模型全预测正常/良性，恶性类召回为0，73.08%只是多数类水平。训练—测试像素审计发现乳腺test index76与选定训练集精确重复；保留官方划分并显式报告，尚未按患者去重。Path选定批次无训练像素精确重复，不等于患者/语义无泄漏。所有逐例预测及混淆矩阵在`outputs/vision-medical-fixed-v1/`。

## 原工程中需避免的语义错误

- BreastMNIST是乳腺超声，不是胸片或病理切片；原data_info误拷贝ChestMNIST描述和规模。
- 官方Breast类别0=恶性、1=正常/良性；不能把文件夹Positive解释成恶性阳性。
- 原下载脚本合并train/val/test再随机拆分，不能用于独立测试评估。当前保留官方划分。
- PathMNIST是本次新增的切片来源，原项目没有已验证的该域模型。临时小模型性能不代表成熟专业模型上限。

下一步需要原项目成熟权重的训练来源及准确预处理/类别映射，或另选有可核验checkpoint的病理模型；在质量达标前，本原型不作为静态失败—Agent成功的第一标杆。
