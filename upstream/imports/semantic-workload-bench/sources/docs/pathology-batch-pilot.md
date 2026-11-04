# 医疗切片 batch 原型：当前仓库入口

本次将历史病理开发批次导入当前仓库并实际复跑固定分类。原Vision-LLM-Integration只读；没有恢复原模型或新训模型，没有调用LLM。任务见[workload card](../workloads/pathology-patches/workload-card.md)，资源见[resource card](../environments/pathology/resource-card.md)。

当前产物：`data/pathology-batch-v1/public/` 是数据湖运行视图；`private/` 是独立gold；`runs/pathology-batch-v1/` 包含预测、可观察固定动作、时间/版本收据及评分。两个snapshot采用现有Snapshot清单校验，缺失/额外/篡改文件拒绝。build暂存后发布，run拒绝已存在目录，score拒绝覆盖metrics。

复现需显式提供历史bundle与NPZ，二者校验[sources.lock.json](../environments/pathology/sources.lock.json)，无旧仓库Python包依赖。任意兼容Python环境可用；本次已存在的 `/opt/anaconda3/bin/python3` 为Python3.12，torch2.8.0、numpy1.26.4、Pillow10.4.0。未安装或修改共享pilot环境。

```sh
export PYTHONPATH="$PWD/src"
python artifact/pathology-pilot.py build --source /path/to/vision-medical-batch-v1 --npz /path/to/pathmnist.npz --lock environments/pathology/sources.lock.json --output data/pathology-new
python artifact/pathology-pilot.py run --public data/pathology-new/public --output runs/pathology-new
python artifact/pathology-pilot.py score --private data/pathology-new/private --run runs/pathology-new
```

`python`须指向含上述依赖的环境。历史bundle不是自动下载的发行资产；缺少bundle/权重时不能仅凭原Vision checkout执行此命令。NPZ来源为[MedMNIST固定Zenodo记录](https://zenodo.org/records/10519652)。所有数据/权重本地保留在忽略目录，未外发。

先锁定整批输出再独立score。批大小128、CPU4线程、模型加载一次、0自动重试、无结果缓存；文件系统冷热缓存未控制。run收据分别保存模型加载、读图/前向和整个运行时间，不包括进程启动。历史训练时间12.5307秒仅来自模型卡；本次未重训。实际金额及历史构造/审核成本未知，不填0。

此批已暴露的1,000图只能作为开发/工程控制。临时CNN质量不是成熟专用模型上限，不能据此宣称传统LOTUS不足或Agent改善。后续需可信强模型、同资源对照及独立确认数据；当前没有Agent示范、自动提取或临床验证。

本次独立评分：accuracy **45.7%**，macro-F1 **0.3721**，coverage **100%**。固定模型加载0.0114秒，读图/前向0.3014秒，run总时间0.6233秒（不含进程启动）。例如平滑肌预测338张、gold74张，绝对误差264；可执行性并不意味着归档质量足够。19项离线契约测试通过，含4项新增病理评分边界测试。
