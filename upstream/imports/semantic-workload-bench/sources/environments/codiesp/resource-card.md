# codiesp 共享环境与输入

1000病例TXT；冻结repo的87170条操作词表；四本2018 PDF及全文文本、原任务DOCX及文本。119个无P标签报告保留。P gold和X原始断续偏移仅private。

原来源：https://github.com/TeMU-BSC/CodiEsp-Evaluation-Script。版本：`976fc1119845d0cd252f1f1103c799c280f32a1d + Zenodo3837305 v1.4 + CIE10ES2018`。精确消费文件、字节、SHA256、用途和公开复制白名单在 [sources.lock.json](sources.lock.json)。锁文件仅构造侧使用，不挂载给模型。

资源用途：通过完整定义、规则或编码表支持Q1的候选检索与语义选择；原文件及全文衍生物并存，文本提取不替代原PDF/DOCX。构造不会按当前gold裁剪共享环境。

输入和gold由各领域projection分开；private包含source-map、原gold、现有争议审计和construction。原始源目录不能整体交给模型。已有文件哈希只证明字节一致，不证明许可、充分性或科学有效。

原标签已有侧别及词义冲突；119份无P标注只作原集合空集；SEDOM历史资源未闭合；X不与P混评。

许可按[原审查卡](../../docs/shared-environment-strict-audit-codiesp.md)逐资产处理；本构造不新增再发布授权，不外发原件。

构造：[五湖指南](../../docs/shared-environment-five-lakes-build.md)；查询：[工作负载](../../workloads/codiesp-batch/workload-card.md)。
