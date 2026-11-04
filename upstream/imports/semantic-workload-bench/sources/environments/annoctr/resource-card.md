# annoctr 共享环境与输入

records 给定 mention/context 和完整报告路径；catalog 为578技术，entity-definitions 为1266实体的定义投影。entity_context 过程示例、label/title/link/id 均不从源标注行公开。原报告自身ID/名称保留。

原来源：https://github.com/boschresearch/anno-ctr-lrec-coling-2024。版本：`d510b6949e1938d47c93a43eedd562dc538439dc`。精确消费文件、字节、SHA256、用途和公开复制白名单在 [sources.lock.json](sources.lock.json)。锁文件仅构造侧使用，不挂载给模型。

资源用途：通过完整定义、规则或编码表支持Q1的候选检索与语义选择；原文件及全文衍生物并存，文本提取不替代原PDF/DOCX。构造不会按当前gold裁剪共享环境。

输入和gold由各领域projection分开；private包含source-map、原gold、现有争议审计和construction。原始源目录不能整体交给模型。已有文件哈希只证明字节一致，不证明许可、充分性或科学有效。

正例条件选择不评价发现率；18条原链接缺KG定义；原文存在明示ID捷径；无跨报告实体独立性保证。

许可按[原审查卡](../../docs/shared-environment-strict-audit-annoctr.md)逐资产处理；本构造不新增再发布授权，不外发原件。

构造：[五湖指南](../../docs/shared-environment-five-lakes-build.md)；查询：[工作负载](../../workloads/annoctr-batch/workload-card.md)。

构造实测：3348条中11条源TECHNIQUE行指向软件实体，另18条技术链接缺KG；29条原gold不在技术输出目录，全部保留并在private/gold-outside-catalog.json登记，不改gold、不删输入、不把这类不可达目标算作模型机制失败。
