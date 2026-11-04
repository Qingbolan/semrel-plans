# VetClaims-JSON：福利裁决路线 Reject；句子分类不替代案件批量

已下载[原论文](https://ceur-ws.org/Vol-2385/paper1.pdf)及[完整官方仓库](https://github.com/LLTLab/VetClaims-JSON)。本地commit、哈希和协议规模见[收据](../artifact/evidence/shared-environment-strict-vetclaims/source.json)。134个tracked文件，75个JSON：原50例及新增25例。论文2019实验使用原50例，不把后来25例归入原论文实验。仓库MIT；论文允许私人/学术复制，不能混为同一许可。

实际读取原论文数据构造和规则/ML比较段、JSON样例及共享协议文件。6份句子角色协议共39 PDF页（8/5/8/6/6/6），517392 bytes。这是修辞角色标注规则，不是完整福利法规手册。完整历史法规、判例及原始医疗证据未冻结。

## 表1：入场审计

| A–H | 证据 | 判定 |
|---|---|---|
| A固定q | 原研究是句子角色分类；批准福利是另一任务 | 不得互换gold |
| B共享E | 6份角色协议可共享；ruleTree在每案JSON，包含truthValue字段 | 须区分纯规则与按案标注，不能整树公开 |
| C依据定位 | 本轮0/20完整案件依据审查；仅实读样例和源构造 | 未确认 |
| D静态不足 | 论文研究固定规则脚本及经典ML，未给同资源强现代固定流程不足证据 | 未确认；接近GENIA型角色分类 |
| E语义家族 | 角色标签、树节点数不等于执行家族K | K未知 |
| F天然批 | 75案件；论文5,797预处理句子是句子单位 | 福利裁决q不满足数百案件 |
| G充分无泄漏 | JSON有完整裁决、句子角色、ruleCondition和truthValue；无独立原始申请事实包 | 裁决预测需重建输入，不能直接用 |
| H获取 | 原论文和完整repo已下载；历史完整E未取得 | 核心可获取但非现成审批benchmark |
| Verdict | 现成福利裁决路线 | **Reject**；不否认句子分类数据用途 |

## 表2：Query × 具体数据

| Query | 数据湖数据1 | 数据湖数据2 | 私有gold/边界 |
|---|---|---|---|
| q1句子→修辞角色 | JSON `sentences[].text`，结合必要上下文 | 六份角色协议PDF | `rhetRole`人工标注；不是福利结果 |
| q2案件→是否应获福利（目标候选） | `text`是事后裁决全文，非无泄漏申请事实 | `ruleTree`包含法规逻辑，但真值/句子映射可能是按案答案 | 75案件上限；原始证据未提供，当前不可当强benchmark |

真实样例 `BVA1718378-LLT-PTSD.json`，docID1718378，decisionDate2017-05-25。第一句为裁决编号信息，角色为默认Sentence、ruleCondition为ADD；这不是疾病或法律实质判断。该样例根规则描述服务相关残疾，三个主条件包括现存残疾、服役期间发生/加重、关联关系；读到的root truthValue为空，不能推断整库均空，也不能据此填批准/拒绝。

## 表3：DAG

| 类Python DAG | 实值/单位 | 普通/语义 |
|---|---|---|
| `cases=scan(json_files)` | 75 JSON，原研究50 | 普通 |
| `sentences=project(text, context)` | 不公开rhetRole/ruleCondition | 普通；上下文属于记录 |
| `roles=sem_map(sentences, role_protocols)` | 示例编号句目标Sentence | 关键语义角色分类 |
| `selected=filter(roles==FindingSentence)` | 供检索/高亮，不产生福利批准结论 | 普通布尔过滤 |

## 表4：四路预期，均未实测

| 臂 | 预期关键操作结果 | 执行过程 | operator结构/风险 |
|---|---|---|---|
| LOTUS仅任务表 | 目标是人工角色，实测未知 | 固定句子分类 | `context→role` |
| LOTUS完整角色E | 同一角色目标，可能足够 | 39页协议整段或另设固定检索对照→分类 | 环境定义可以一次整理；无不足证明 |
| 逐记录Data Agent | 同一角色目标，无优势证据 | ==查角色定义和归属主体==→读取句子上下文→分类 | `retrieve_definition→classify` |
| 批Data Agent | 同一目标 | ==一次整理角色规则==→逐句分类 | 很可能是固定程序复用，非多个语义家族 |

ρE是协议读取，ρP是归属/角色判断，ρG未知，ρR是句子具体上下文；无比例或K估计的观测依据。Agent不能用私有ruleCondition或truthValue获得答案。最大固定基线风险是协议摘要＋上下文角色分类；此任务无需假设探索完整福利法规。

十问中q/E/x/gold/来源见上述；C/D/E/G缺口明确，尚不能证明区别于普通条件文本分类。因案件数硬性不足，停止为福利裁决路线补做20例正向认证；0/20不代表模型准确率。没有运行模型、作者代码、安装、数据构造或新划分。保留否定结果，不增加Strong计数。


## 输出与信息不足边界补充

句子角色q的输出是源协议角色集合，默认Sentence不是UNKNOWN的同义词。无法执行时可记ABSTAIN且按未完成计分，不能补造人工角色；福利裁决q缺独立输入与明确gold，本轮未定义可运行批准/拒绝/UNKNOWN契约。
