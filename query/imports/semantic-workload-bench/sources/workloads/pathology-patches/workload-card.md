# 病理切片批分类：Vision-LLM-Integration 转换原型

当前已在本仓库导入并逐图核验历史 PathMNIST 开发批次，可执行固定模型分类和独立评分。原项目保持只读。公开基准模拟医院影像归档任务，不代表医院数据或临床部署。

业务请求：对本批切片逐张识别组织类别，输出分类清单，统计每类切片数量，供影像归档与后续人工复核使用。记录单位是28×28 RGB组织图块，不是完整病理slide、患者或诊断。PathMNIST九分类及官方split见[官方资料](https://medmnist.com/v2)。

```text
scan(patches)
  → validate_image
  → sem_map(classify: image → class_id)
  → project(case_id, class_id, status)
  → group_by(class_id).count
```

固定任务是九类组织分类：脂肪、背景、碎屑、淋巴细胞、黏液、平滑肌、正常结肠黏膜、癌相关间质、结直肠腺癌上皮。不要把类别8直接解释为患者诊断。完整类别映射冻结在public/tasks/pathmnist.json；每张输入显式提供modality。

数据湖public含1,000张待分类切片、32张官方train参考图及标签、模型权重、模型卡、架构和预处理代码。private含当前test gold、源索引及训练重复审计。模型卡说明权重是历史补建的MedicalConvNet：10,000条train、seed42、3epoch、Adam0.001；并非原Vision项目checkpoint。原项目commit ebcb99edbe929fa8b7620171d3013ce569eddb4b，本次检查无.pt/.pth权重或医疗NPZ，原下载脚本合并train/val/test，不用于本次划分。

本批继承历史按SHA256(medical-v1:pathmnist:test:index)取前1,000条的选择，不重新挑例；源NPZ、历史清单及gold均锁hash。逐张核对源像素和官方标签，32参考图也核对train来源。与登记的10,000训练图精确像素重复为0；患者隔离与训练污染未核验。历史模型性能已被查看，本批只能用于开发/控制，不是独立确认。

运行及实际结果见[当前原型指南](../../docs/pathology-batch-pilot.md)。评分包括全量accuracy、九类macro-F1、coverage、混淆矩阵及下游每类计数误差；ABSTAIN保留在分母。没有一次Agent轨迹或自动提取器。

实验顺序：先测传统LOTUS直接视觉sem_map；固定模型程序作为同资源强对照；再比较允许同模型/代码/参考图的Coding Agent与Data Agent。批内计划与模型加载均允许复用。只有观测到质量改善才研究单轨迹提取，不能以CNN差或文件多证明Agent必要。固定程序足够时保留阴性结果。
