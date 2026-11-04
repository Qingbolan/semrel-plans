# 顶会正式论文检索：发现方证据及攻击后收敛

时间：2026-09-05，Asia/Singapore。限定：正式录用来源优先；不以arXiv、作者README徽章或第三方文章代替proceedings。继承已读仓库契约；本轮只写本文，不修改report/实现/实验产物。未运行付费模型、下载原始影像数据集或模型权重。下载了少量正式论文PDF到/tmp以读取表格，不执行作者程序。

## 结论与检索方式

先从CVF、NeurIPS、AAAI正式出版入口查录用，再反查论文表格和代码实物。针对“直接整体判断可能漏细节”，搜索固定分解、真实裁剪、局部比较、领域知识；并反查增益是否只是训练、标签输入、缺必要上下文或不同评分方式。

本轮发现 **STAR、OralGPT-Plus、Ano-NAViLa、BLINK-Twice、MIRAGE** 五个此前未深入核验的正式候选，并将 **LogicAD** 从此前预印本线索升级为正式AAAI论文证据。不是五条全部推荐：新增视觉中，**OralGPT-Plus提供最具体的领域工具机制；STAR提供最清楚的同backbone工具增益与真实工具实现**，二者仍有批任务构造缺口。真正符合共享规则批任务的优先级，应与另两方核查的 **RuleArena、Chain-of-Table、Magneto** 比较；不能为了覆盖视觉而硬选。

| 论文 | 正式来源与层级 | 可检验共享语义步骤 | 攻击后状态 |
|---|---|---|---|
| LogicAD | AAAI2025技术主轨，39(4):4129–4137 | 同产品的组件/数量/空间关系判断→规则违例筛选 | 有固定分解依据；公平direct及代码端到端仍待验证 |
| OralGPT-Plus | CVPR2026主会，正式CVF PDF，起页35373 | 批全景牙片中指定异常/器械的牙位级提取→清单/数量 | 新增视觉首要资源审计对象；MMOral-X完整发布及客观gold需确认 |
| STAR / VideoTool | NeurIPS2025 Main Conference Track | 批视频中一个固定动作/时间关系判别→筛选/计数 | 方法桥梁；未统计足量同predicate视频 |
| Ano-NAViLa | ICCV2025主会，22066–22076 | 淋巴结WSI中转移灶存在性→阳性病例清单 | 冻结专家工具候选；不作为无需训练的文档增益证据 |
| BLINK-Twice | NeurIPS2025 Datasets and Benchmarks Track | 视觉错位/遮挡的某固定关系判断 | 诊断集合；合成编辑、异质任务、强模型收益有限 |
| MIRAGE | NeurIPS2025 Datasets and Benchmarks Track | 同作物/同病害的图文症状判断→病例分组 | 真实咨询来源线索；输入欠定、资料增益与共享family未证实 |

## 1. LogicAD：正式camera-ready核验

正式[文章页](https://ojs.aaai.org/index.php/AAAI/article/view/32433)和[出版PDF](https://ojs.aaai.org/index.php/AAAI/article/download/32433/34588)确认AAAI2025。**本轮重新读取正式PDF Table3**：Guided CoT AUROC48.5，加ROI60.4，加格式嵌入86.0；逻辑证明路径F1-max83.3。该表与此前arXiv线索一致，但23.4的“无模块”不是现代VLM直接异常分类的公平baseline；也没有LOTUS调用实验。

固定DAG建议：scan同产品图 → sem_map组件/位置/数量 → 执行同一完整装配规范 → filter IDs → count。全图、正常参考与完整规则给所有臂；GroundingDINO ROI必须从图像计算，人工组件标注只能评分。

[官网](https://jasonjin34.github.io/logicad.github.io/)说明真实ROI、重复描述、文本表示及Prover9逻辑；[官方代码](https://github.com/jasonjin34/logicAD)实际master分支含formal_prompts_spec.py/formal_reasoner_all.py和logicad模型目录，不再将此前误查main分支404解释为没有代码。没有本轮端到端执行，因此代码存在≠论文完全可复现。完整规则公开范围、感知路径及标签隔离交协调方进一步核验。每种产品是独立共享谓词，五类平均不能替代单产品效果。SALAD应作为强固定视觉baseline，不因其强而淘汰环境。

## 2. OralGPT-Plus：镜像对侧检查是否纠正真实局部判断

正式[CVF camera-ready](https://openaccess.thecvf.com/content/CVPR2026/papers/Fan_OralGPT-Plus_Learning_to_Use_Visual_Tools_via_Reinforcement_Learning_for_CVPR_2026_paper.pdf)已通过urllib下载并pdftotext读取；web打开403未被当作论文不存在。官方仓库同时记录2026-02-22 CVPR录用，但录用依据采用CVF正式PDF。

原始物理对象是全景牙科X光。论文MMOral-X有300幅图对应300开放问题、686框；Simple/Moderate/Complex各100图。工具Zoom-In与Mirror-In读取同一幅图：选定区域与中线对侧区域组成比较视图，1.5倍padding容纳偏移。具体机制是用对侧近似对称结构检查阴影/低对比异常，不是从另一个标签目录查询答案。建议批任务固定为“提取指定异常类别及牙位”，下游展开病灶→按图/牙位去重→病例清单/计数。不能将“全面诊断所有疾病”自动视为唯一共享任务。

正式Table2无Mirror-In为34.68/14.26/14.30，完整为43.16/20.60/24.96。**这些是GPT-5-mini开放回答连续评分，经5次运行平均，不是客观二分类准确率**；正文另写43.22，与表43.16有小差异，采用表值。实验使用Qwen2.5-VL3B/7B、4k SFT及1k RL，移除工具的消融是否只在推理时改变可用工具尚未确证，不能把训练+资源改动称same-model causal gain。

[官方仓库](https://github.com/isjinghao/OralGPT)锁至`32af894365525cc007ea03edc164c55502384748`。`OralGPT-Plus/README.md`、四种源处理器、proposal/filter/rewrite脚本、`training/mini-o3-rl.tar.gz`实际存在；README说明`mirror_grounding`由`mirror_image`处理。这里只读README与树，未解压执行RL代码。MMOral-OPG已有公开[数据入口](https://huggingface.co/datasets/OralGPT/MMOral-OPG-Bench)，不能据此称MMOral-X已完整可取。本轮未找到锁定的MMOral-X全量manifest/gold下载。

构造侧proposal利用上游病灶gold bbox来生成训练轨迹，属于有监督构造，**不能挂入测试工具**。本项目若做同模型比较，应独立实现纯图像crop/mirror，在完整原图上直接判断/固定全牙位裁剪/固定对侧比较/Agent之间对齐资源；官方SFT轨迹和训练费用不可计零。附录病灶描述来自wiki/google检索，并非正式诊断手册，不应冒充临床SOP。影像可见征象与最终疾病诊断亦需区分。

## 3. STAR：真实工具可用，整套视频QA不等于批workload

[正式NeurIPS页面](https://proceedings.neurips.cc/paper_files/paper/2025/hash/bbdd9525c5ecd3a03fee43d8fd64bd83-Abstract-Conference.html)确认Main Conference Track；[正式论文](https://proceedings.neurips.cc/paper_files/paper/2025/file/bbdd9525c5ecd3a03fee43d8fd64bd83-Paper-Conference.pdf)报告GPT-4o配工具在VideoMME提高8.2个百分点、LongVideoBench提高4.6个百分点。这是同backbone多步骤相对于其视频处理配置的结果，不是任意固定predicate的预测。

输入攻击方核查[代码](https://github.com/fansunqi/VideoTool)commit `e252f8b9433b1b02aba3f59ef2200f3d91cff74e`：frame_selector选未采样时间段并加入真实帧；patch_zoomer通过cv2裁四象限+中心后resize；temporal_grounding解码96帧后调用Grounded-Video-LLM。没有发现这些路径读取人工答案。也发现`tools/python_generator.py`为空，不能称所有公布工具均实现；数据loader缺视频时continue，需要保留coverage而非删失败。

研究攻击成立：唯一testcase的人类演化QA及通用NextQA/VideoMME loader未证明同业务predicate数量。下一步只能先统计，例如固定动作先后关系或某事件出现次数，在独立视频上形成同一任务；若没有足够样本就降为工具单元验证。必须比较同帧预算的固定均匀采样、固定多尺度视图和Agent选帧，避免“少给direct输入”制造效果。字幕/音频若必要所有臂均可用，局部gold timestamp不得作为检索输入。

## 4. Ano-NAViLa：知识确有实物，但不是直接调用LLM加文档

正式[ICCV页面](https://openaccess.thecvf.com/content/ICCV2025/html/Song_Normal_and_Abnormal_Pathology_Knowledge-Augmented_Vision-Language_Model_for_Anomaly_Detection_ICCV_2025_paper.html)确认主会。[补充材料](https://openaccess.thecvf.com/content/ICCV2025/supplemental/Song_Normal_and_Abnormal_ICCV_2025_supplemental.pdf)TableS2在GastricLN的max聚合AUROC：CONCH-class .9068，CONCH-pool .7619，CONCH视觉项 .9902，完整 .9967。因此“给更多词语就更准确”被原表直接反驳；完整方法含训练MLP及表示构造。

[官方代码](https://github.com/QuIIL/ICCV2025_Ano-NAViLa)commit `569caac3b6f24dc697a18f09215ccf747d45b71b`包含normal/abnormal词库、真实图像dataloader、模型、训练/测试器及Camelyon16输出CSV。README明确GastricLN训练WSI不能公开；提供冻结权重及重训权重。原表用100/50词（含重复），论文声称92/48；去重词权重为之后重训，不能混用原表。词库是术语/形态短句，不是详细分支手册。

建议仅将冻结模型当可获取的外部视觉专家候选，输入Camelyon16原始WSI、输出patch分数；public只保存图像/坐标，文件名中的可选abnormal_percent须剔除。候选DAG为scan WSI → sem_map转移灶证据 → 病例筛选/计数；大切片解码、patch量和患者分组成本高。尚无本轮证据说明通用Agent使用此工具比固定全patch程序更好，也不宣称论文已经证明。

## 5. 两个正式D&B候选的降级理由

**BLINK-Twice**：正式[NeurIPS D&B页面](https://proceedings.neurips.cc/paper_files/paper/2025/hash/2b76873e897f3de3069b2f360c65e0c2-Abstract-Datasets_and_Benchmarks_Track.html)，正式PDF已读取。第4节/图6明确重复观察对Gemini2.0-flash-thinking/Qwen2VL72B改善，对GPT4o/Qwen2.5VL72B收益有限；o3工具行为是案例，不是同模型禁用工具随机对照。官方[仓库](https://github.com/PicoTrex/BLINK-Twice)commit `8f7911c48eda6f43c1e8b519b19148ed1b28079a`仅README/assets/license，指向HF数据。345基础图、103由GPT4o图像编辑生成的对抗样本，不能统称自然独立照片。异质错觉并不是具体生产业务；降为感知压力测试。

**MIRAGE**：正式[NeurIPS D&B页面](https://proceedings.neurips.cc/paper_files/paper/2025/hash/1fdee6bdc130776e489719d25d422073-Abstract-Datasets_and_Benchmarks_Track.html)确认录用；[官方库](https://github.com/MIRAGE-Benchmark/MIRAGE-Benchmark)与[数据卡](https://huggingface.co/datasets/MIRAGE-Benchmark/MIRAGE)提供真实农业咨询图文、专家回复、单轮/多轮配置。真实来源是优势，但欠定用户输入是其核心设计，不能通过只给首轮来构造直接模型失败。需要完整已知对话，并找到同一病害/同作物足量案例与外部独立参考手册；本轮未完成。原论文主要是benchmark/训练研究，不是已证实工具增益。AgriRAG虽有同域检索效果，却是CVPR2026 Workshop，不能替代主会证据或混入本轮主推荐。

## 对抗结论

- 研究方提出RuleArena、Chain-of-Table、Magneto的规则/关系批任务更接近研究单位；发现方接受，它们应优先于无family统计的视频QA。
- 输入方证明STAR核心视觉工具真实计算，但否定现成批业务任务、完整工具实现和缺失样本安全处理；发现方将其保留为方法桥梁。
- OralGPT-Plus有具体共享器官结构与可计算对侧比较，不依赖外部答案才能生成视图；但训练消融、LLM评分和MMOral-X发布缺口未解决，因此只推荐下一轮实物审计，不进入质量实验。
- Ano-NAViLa词库确有实物，但固定词库直接效果较差、完整方法有私有训练和版本差异，降为固定专家工具。
- 正式顶会录用不保证本项目证据链成立。AgentIAD本轮未核正式录用，AnomalyClaw预印本、VLA-AD/AgriRAG workshop均不作主会推荐。

检索产物：正式论文阅读使用web和urllib/pdftotext；轻量GitHub tree/README/词库读取，无源码执行。0模型调用、0软件测试、0新数据划分、0实际效果复现；未commit/push。所有表数字为正式论文转述，未验证可复现性。
