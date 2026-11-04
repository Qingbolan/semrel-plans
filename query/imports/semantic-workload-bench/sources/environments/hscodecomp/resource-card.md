# hscodecomp 共享环境与输入

632商品字段与原平台类别；HTS原JSON、35950行含无编号父节点的树、29932编码catalog；4429页完整同版PDF及全文。question换为共享任务，hs_code隔离。

原来源：https://github.com/AIDC-AI/Marco-DeepResearch。版本：`ee329e98f92b51bd797785f648c7c4e42e678ad7 + HTS2025Revision15`。精确消费文件、字节、SHA256、用途和公开复制白名单在 [sources.lock.json](sources.lock.json)。锁文件仅构造侧使用，不挂载给模型。

资源用途：通过完整定义、规则或编码表支持Q1的候选检索与语义选择；原文件及全文衍生物并存，文本提取不替代原PDF/DOCX。构造不会按当前gold裁剪共享环境。

输入和gold由各领域projection分开；private包含source-map、原gold、现有争议审计和construction。原始源目录不能整体交给模型。已有文件哈希只证明字节一致，不证明许可、充分性或科学有效。

图片、单位价格、外部裁定及汇率事实未闭合；不可用缺事实造成的失败证明Agent优势。

许可按[原审查卡](../../docs/shared-environment-strict-audit-hscodecomp.md)逐资产处理；本构造不新增再发布授权，不外发原件。

构造：[五湖指南](../../docs/shared-environment-five-lakes-build.md)；查询：[工作负载](../../workloads/hscodecomp-batch/workload-card.md)。
