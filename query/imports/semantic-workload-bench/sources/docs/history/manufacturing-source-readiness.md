# Manufacturing source readiness — 2026-09-05

状态：一手来源审查与小规模原始材料下载，**未运行检测器、LLM、Data Agent 或性能实验**。本文件不能证明静态算子不足或 Agent 优势。由主任务统一追加 `report.md`。

## 决策

**DeepPCB 最快可以形成“参考模板辅助的 PCB 缺陷筛选/定位”可执行控制场景，已经有 24 对图片和独立人工缺陷标注落盘；但不适合直接作为真实良品/不良品混合批次，更没有返修决策 gold。** Real-IAD 的正常/异常、多视角结构更适合后续质量筛查，但当前图片需要授权且类别压缩包很大。VISION 的最小类别包较小，但制造规格缺失正是官方承认的限制，不能补写一套规格后声称是原始生产标准。

| 候选 | 真实材料 / 可执行性 | 模板、工具、gold | 当前结论 |
|---|---|---|---|
| DeepPCB | 已下载 24 个官方 test 记录、48 张原图、24 份标注，总计 2,349,259 bytes | 每条有对齐无缺陷模板；6 类 bbox gold；无需 checkpoint 即可尝试图像差分工具 | 现在可做缺陷类别筛选/定位控制；全批“是否存在缺陷”退化，不能冒充生产验收或返修任务 |
| VISION | 官方 HF 元数据可读；最小 Electronics 包 11,581,737 bytes；实际文件 HEAD 返回 401 GatedRepo | 14 个领域、COCO 标注；原图 bbox 决策保留，增加 polygon；没有核实到配对模板/完整制造规格/可即用 checkpoint | 合法获得访问后可下载一个小类别做 20–30 条 pilot；当前尚未拿到实际记录/gold |
| Real-IAD | 官方 HF 元数据可读；1024 版全量约 53GB，单类别如 audiojack 1,057,915,816 bytes；实际 split ZIP HEAD 返回 401 GatedRepo | 真实生产线来源、多视角正常/异常图和 mask，官方 UniAD 训练代码 | 更接近质量检查情境；目前未下载图像，不声称已经能运行；只在授权后取 split+单类别选定 ZIP members |

## DeepPCB：已验证的本地材料

一手来源为 [官方仓库](https://github.com/tangsanli5201/DeepPCB)、[冻结 README](https://github.com/tangsanli5201/DeepPCB/blob/08e98c4db5922613fb97176eb3d6497d48260cb1/README.md) 和 [原论文](https://arxiv.org/abs/1902.06197)（2019 年预印本；本次未读取 PDF）。冻结 commit：`08e98c4db5922613fb97176eb3d6497d48260cb1`；这是代码/数据快照标识，不当作数据首次发布日期。

原始集合 1,500 对，官方 trainval 1,000、test 500；640×640 配准图来自 CCD 扫描板图，模板经人工清理。**作者明确说向 tested 图人工增补缺陷**，所以是实际板图背景与增补缺陷混合来源，不能称“全部自然发生的缺陷”。标签 ID 为 1 open、2 short、3 mousebite、4 spur、5 copper、6 pin-hole；文件每行五个整数为 `x1 y1 x2 y2 type`。这些类别与图框不是 IPC 验收标准，也不包含修复动作、修复成功率、严重度或报废成本。

本地目录：`outputs/manufacturing-source-candidates/deeppcb/`。

- `public/images/`：24 tested + 24 temp 原图；Pillow 全部校验 640×640 且可解码。
- `private/gold/`：24 份官方 bbox 标签；禁止提供给模型/工具检索。
- `pilot_manifest.json`：每条官方路径、test split、源 URL、逐文件 SHA256 和字节数。
- `fetch_pilot.py`：可复现小规模获取脚本；`README.md`、`LICENSE`、`PCBData/test.txt`、`PCBData/trainval.txt` 保存来源说明与官方划分。
- 选择规则：按 `SHA256("manufacturing-pilot-v1" + NUL + official_test_line)` 排序取前 24；没有根据 gold 或模型结果选样。
- 24 条跨 7 个 group：12100×6、44000×5、50600×3、90100×6、20085×1、12300×2、12000×1。不是独立生产批次抽样，后续 train/test 要避免同板模板/裁剪相邻图泄漏。

真实样例 `12100147`：`public/images/12100147_test.jpg` 与 `12100147_temp.jpg` 已实际通过 `view_image` 查看；私有标签含 7 框（open×2、mousebite×3、spur×1、pin-hole×1）。样例 `44000013` 有 10 框（open×2、short×2、mousebite×2、spur×2、copper×1、pin-hole×1）。这里只核验材料与标签，不把视觉观察当预测结果。

本 pilot 共 165 个 gold 框：open 38、short 29、mousebite 32、spur 24、copper 19、pin-hole 23。每图类别存在数分别为 24、22、20、17、17、22。**24/24 有 open，24/24 至少一种缺陷**：因此直接“reject any defect”会全拒绝。把 clean template 作为良品输入可做受控检查，但它是人为清理的模板、且不能同时作为自身检索参考来制造满分；不得据此声称真实良品泛化。

## 可以立即交给主任务实现的场景

共享 batch question 可取：**“筛出含有与预期导电图案分离的多余铜（spurious copper）的待检 PCB 区域，并返回位置和模板对比证据。”** 该 24 条按上述规则抽样后有 17 正、7 负，gold 由官方类别 5 的 bbox 是否存在映射，不需新编 gold。此任务是在本轮已见类别分布后选择，因此只能进行探索性诊断，不是预注册确认性评测。此问题是缺陷分型筛查，不能改名为“这些板应返修”。用于复核/分流的业务用途是研究构造，未核实外部客户需求。

固定 DAG：`scan(test_pairs) -> sem_filter(shared_spurious_copper_predicate, evidence_environment) -> project(record_id, locations, evidence_refs) -> group_by(board_group).count()`。若要求完整六类位置，关键步骤应使用结构化 `sem_map`，然后普通 filter/project；不要硬塞进只有布尔值的 filter 输出。

公开环境可以包含未画框的待检图、对应 clean 模板、类别通用定义、模板配准/二值化/连通域工具文档。当前环境已检测到 `cv2`、`numpy`、`scipy` 可导入；**工具尚未实现或验证准确率**。建议第一条 Agent 示范只允许开发 group：读取类别定义 → 比较模板 → 尝试阈值/配准 → 从差分连通域区分多余与缺失铜 → 结合模板连通性区分 spur 与孤立 copper → 返回可审查证据。保存动作/参数/证据、不要保存私人思维链；随后冻结所得流程处理剩余 records。

这也可能完全由固定图像算法或 Coding Agent 一次写出的程序解决。必须保留“模板差分 + 固定分类规则”的对照，并让所有方案获得相同模板和工具。一次示范可复用目前只是待测假设；不能先把现成算法命名为动态算子然后宣布研究目标成立。

DeepPCB 官方树与 releases 已查：没有 `.pt/.pth/.ckpt/.onnx` checkpoint，releases 为空；README 对模型实现仍写未来公开，现有 `tools/` 是标注工具，`evaluation/` 是评分脚本，不能报告“官方预训练检测器已可用”。无需权重的 CPU 图像工具是可尝试路径，但应明确与“调用已训练领域模型”属于不同机制。

许可同时存在 [MIT LICENSE](https://github.com/tangsanli5201/DeepPCB/blob/08e98c4db5922613fb97176eb3d6497d48260cb1/LICENSE) 与 README 的 research-only 数据使用声明；本次按研究使用处理，不把仓库 MIT 概括成图像无限商业许可。

## VISION：规格与测试 gold 要分别核实

[官方数据卡](https://huggingface.co/datasets/VISION-Workshop/VISION-Datasets/blob/bc14e85d80c1ba9fedb7b3e8164d1800a805bf57/README.md) 对应 HF revision `bc14e85d80c1ba9fedb7b3e8164d1800a805bf57`，元数据 lastModified 为 2023-06-15。官方卡说明 train/val 有 COCO 标注，inference 混合测试/弃用图且不公开标签。还明确缺少制造商规格时难以区分标签遗漏与领域决策，故保留原缺陷决策。

小 pilot 首选 Electronics 包（11.58 MB），其次 Wood（23.23 MB）或 Capacitor（35.89 MB），避免先取 Console（1.63 GB）。本次只获得 API 文件大小和卡片，没有获得实际图片、标签条数或记录 ID，因此不能编写真实样例或声称完整 gold 已有。

新增 polygon 为 CC BY-NC 4.0，原始图像仍按各自来源许可；不能把卡片许可覆盖全部上游资产。`gate=auto` 需要账号提交联系信息并接受条件，本次无凭证 HEAD 返回 401，未申请/绕过 gate。未核实到官方可下载检测 checkpoint；可以训练通用检测模型，但这不是“开箱即用已有领域工具”。

## Real-IAD：后续更真实，但不是当前无成本入口

[官方项目页](https://realiad4ad.github.io/Real-IAD/) 与 [数据卡](https://huggingface.co/datasets/Real-IAD/Real-IAD) 描述真实生产线采集，包含 30 类物体、多视角与多种异常。HF revision `6713deac4c5fb286c2139b2d674258a25af5ddde`；数据许可 CC BY-NC-SA 4.0 / research-only，项目网页的 CC BY-SA 是网页许可，不能混同。当前授权 gate 返回 401，未下载样本。

[官方代码](https://github.com/Tencent/AnomalyDetection_Real-IAD)（由旧腾讯仓库重定向说明定位），冻结 commit `98c28ffbe95b380d17a3777d77219152368c19e9`。有 UniAD 数据/训练/评估配置，但树中无权重文件、releases 为空；README 指导先训练，再生成预测/评分，并非提供已验证的 Real-IAD checkpoint。代码有 `LICENSE` 与 `LICENSE_UniAD`，不能用数据许可替代代码依赖许可。

若已有合法授权，优先先取 JSON split，再从一个类别 ZIP 通过严格 HTTP Range 取 20–30 **物理物件**的完整多视角图及私有 mask；不是随便取 20–30 张视图就声称独立样本。当前单类别 archive 大小已核对；Range 支持、JSON 实际字段、每件视图可达性与正常参考选择还未验证。本数据可支持正常/异常筛查及区域定位，不能推导“可返修/应报废”。

## 可复现与尚未验证项

```bash
python outputs/manufacturing-source-candidates/deeppcb/fetch_pilot.py
```

来源 API 快照保存为 `outputs/manufacturing-source-candidates/{vision,realiad}-hf-{metadata,tree}.json`，代码树与 releases 审查也在同目录。没有下载多 GB 文件，没有提交用户身份字段，没有运行模型，没有新写规格或修复标签，没有修改 adapter 或主代码。

仍需主任务实施：工具候选运行、同证据静态与 Agent 比较、一次示范的可复用组件、训练/验证板级隔离、成本与延迟记录。现有证据足够开始 DeepPCB 控制实验，不足以认定它就是开放世界动态能力标杆。
