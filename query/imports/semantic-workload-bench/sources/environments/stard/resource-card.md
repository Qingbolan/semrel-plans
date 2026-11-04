# stard 共享环境与输入

question records 与共享法条 catalog.jsonl（id/name/content）。原始 literal backslash-n 规范化为换行；source qrels、相关法规、match_id/name 都不公开。

原来源：https://github.com/oneal2000/STARD。版本：`bae10e1f358685446c3af4b15e7b94724f83bc9e`。精确消费文件、字节、SHA256、用途和公开复制白名单在 [sources.lock.json](sources.lock.json)。锁文件仅构造侧使用，不挂载给模型。

资源用途：通过完整定义、规则或编码表支持Q1的候选检索与语义选择；原文件及全文衍生物并存，文本提取不替代原PDF/DOCX。构造不会按当前gold裁剪共享环境。

输入和gold由各领域projection分开；private包含source-map、原gold、现有争议审计和construction。原始源目录不能整体交给模型。已有文件哈希只证明字节一致，不证明许可、充分性或科学有效。

原相关性标签不保证完整依据或回答充分性；全量关联校验不等于语义正确。

许可按[原审查卡](../../docs/shared-environment-strict-audit-stard.md)逐资产处理；本构造不新增再发布授权，不外发原件。

构造：[五湖指南](../../docs/shared-environment-five-lakes-build.md)；查询：[工作负载](../../workloads/stard-batch/workload-card.md)。
