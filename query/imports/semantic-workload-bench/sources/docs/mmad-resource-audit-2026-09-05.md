# MMAD 批异常筛选资源核查

本次为来源与构造可行性核查，未构造图片快照、调用模型或证明资源/Agent增益。保留现有其他路线结果。

## 本次核验

官方仓库 https://github.com/jam-cc/MMAD 当前 main 经 GitHub API 解析为 `1490f887b9570613565fa6a7b15d5f81aa183c54`，与历史登记一致。直接读取固定commit两个JSON并在内存解析：

| 文件 | bytes | SHA256 |
|---|---:|---|
| dataset/MMAD/domain_knowledge.json | 144260 | f9e24f815f72b93929757e14a23b3dd1550615e8f96ec5103e916c5610ee3176 |
| dataset/MMAD/mmad.json | 30404720 | 95dc8159340f21cd9d7d77acb6575fdf855d5c40a0eed7048a5a669d6e0b4b35 |

实际8366图片记录、39670 conversation条目；README称39672，差异仍未解释。Anomaly Detection类型8297条，不等于8366：尚未逐图审计缺题/重复及映射一致性，不可假定每图恰有一题。知识目录覆盖MVTec15、LOCO5、VisA12、GoodsAD6类。

LOCO候选图片1566：breakfast_box275、juice_bottle330、pushpins310、screw_bag341、splicing_connectors310。这是元数据候选数，不是本地已取得图片数或独立确认数。

记录字段含image_path、conversation、mask_path、similar_templates、random_templates；QA字段含Question、Answer、Options、type、annotation。公开输入必须allowlist重建；Answer/annotation/mask_path和含good/缺陷名的当前实例原路径留在private。不要把异常定位/描述问题作为二分类输入，它们可能预设异常存在。参考图选择需核验来源和选择机制，不因字段名而自动认定可安全挂载。

## 文档适用性

[官方说明](https://github.com/jam-cc/MMAD#domain-knowledge)称专家在LLM辅助下整理类别正常特征、异常分类与描述，未在已读材料中提供足以排除测试图参与的逐条来源链。知识JSON按数据集/产品/缺陷类型组织，包含对所观察图像批次的总结性措辞。这是来源审计线索，不是已证明泄漏。

[固定版本知识](https://github.com/jam-cc/MMAD/blob/1490f887b9570613565fa6a7b15d5f81aa183c54/dataset/MMAD/domain_knowledge.json)中，screw_bag正常描述没有给出每类零件完整应有数量；logical条目提示缺件、过量及尺寸差异，却未冻结完整判定规则。不能仅凭“有文档”声称逻辑异常任务输入已充分。不要根据本轮测试gold补写规则；先从上游规范与独立正常训练材料核验。

官方README 2026-01-14公告计划提供错误更少的精简版本。该公告不代表新版本已经发布；当前构造仍须版本锁定和gold一致性审计。

## 建议的最小实验边界（尚未执行）

从LOCO一个产品类别开始，固定语义为“是否存在异常（包括结构或逻辑异常）”，scan → sem_filter → project opaque record ID → count。若只研究逻辑异常，单独版本化并核验该标签映射，不用通用异常QA代替。

先做来源/许可、逐图异常QA与上游标签一致性、完整正常规则、训练参考来源、历史暴露和近重复审计，再冻结开发关系。知识全文按产品类别提供，不能按当前实例gold挑缺陷条目。确认集按源实体隔离；当前浏览过的元数据需记录为开发暴露。

资源消融：同模型待检图 / 加文档 / 加正常参考 / 文档与参考均加。各臂共享明确的任务定义和必要正常规则；只有辅助解释与参考发生变化，不能通过扣掉必要规则制造基线错误。

方法比较：传统静态LOTUS、同资源固定检索/工具流程、一次Coding Agent生成批程序、可共享计划/缓存的Data Agent。固定方法也允许同样检索、裁剪与真实感知工具；若引入工具，需另测其增量。LogiCode读取同名人工JSON的历史实现仅可作为annotation-given诊断，不能当原图检测器。

先测文档/参考的配对改正与退步、异常macro-F1/recall、coverage、清单precision/recall、count error及成本；再判断是否有同资源Agent质量改善。两道门槛通过后才进入单次真实轨迹提取与新批次冻结执行。复用材料、手写程序、一次无轨迹生成代码分别是不同对照，不能都称单轨迹提取。

本次没有下载图像或大包，没有运行测试/模型，没有修改运行器、现有快照、旧评分或研究主张状态。
