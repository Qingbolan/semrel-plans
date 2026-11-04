# MMQA VenueLake：capacity-conflict 的 discovery 可审定性审查

## 结论与范围

**当前不应把 `venue-capacity-conflict-v1` 提升为已成立的主标杆。** 全部 605 个 discovery 源行的 exact URL 文本路径很稀疏；十个定向深读案例中，没有建立满足“同配置、同参照期间”的明确冲突正例。观察到的障碍主要是源表/正文容量时间未绑定、座位与总容纳人数口径不同、历史改造、近似数字，以及一行实际上包含多个球场。

这不证明 discovery 或整个湖没有正例，也不是模型准确率或 UNKNOWN 比例。没有读取 private gold，没有产生 gold 标签，没有运行模型 benchmark，没有对 confirmatory 标签做筛选。十例是按 apparent mismatch、等值、历史变化、复合源行、近似数值定向选取，并非随机样本。这里的“深读”是 assistant 对原始公开资源的可审定性阅读，不替代双人独立标注。

审查产物：[capacity-audit.json](../outputs/mmqa-venue-feasibility/capacity-audit.json)。其中保存全部 605 行的关联统计、64 个 exact 文本原文、正则定义、10 例完整原表行及阅读依据；`gold_labels_written=0`，十例 `gold_state=null`。

## 数据身份与冻结边界

- 数据：MMQA-VenueLake v1，来自 MultiModalQA 的 Wikipedia 派生表格/文本；上游代码 commit `4dd14328c6d02a4daa357cc6032915a0b14602e3`，来源 ICLR 2021，非期刊。
- 公共湖：`outputs/mmqa-venue-lake-v1`；本次 manifest SHA-256 为 `db7decc4a4e996c8ee9d113c54f4b7c0ec1954bf928c72b6fdb48280c5a845b4`。
- 上游初始发布日记录为 2021-04-23。此日期与本地快照时间都不是某个球场容量的生效日期，不可用来补全同期间 gold。
- 只分析 `partitions.jsonl` 标记 discovery 的全部 605 行，无抽样排除；在公共湖全部文本中按源行 `venue_cell_urls` 与 `resources.source_url` 精确相等枚举文本。城市链接保留为候选，没有假定 URL 已绑定物理球场。
- 湖边界包含 218,285 个文本、10,042 张表及 177 张 cell-linked 候选图；本次结构扫描只枚举 exact URL 文本路线，不是全文检索、别名消歧或对全世界证据的穷尽审核。
- 公开文本 payload 仅有正文，缺少逐 statement 的容量生效日期或已绑定版本元数据；有日期 token 不代表容量日期。数据及图片再分发许可仍沿湖 manifest 的未核实状态，本次只在本地研究目录生成审查。

## 结构统计：不是标签统计

| 统计项 | 数量 |
|---|---:|
| Discovery 原始行 / 来源表 | 605 / 39 |
| 有至少一个 cell URL 的行 | 453 |
| 容量可解析为无修饰整数的行 | 545 |
| 有 exact URL 文本候选的行 | 65 |
| 没有 exact URL 文本候选的行 | 540 |
| Row-text 关联对 / 去重文本 | 101 / 64 |
| 有宽松容量词信号文本的行 | 29 |
| 同一个文本同时有容量词与年份 token 的行 | 20 |
| 同一个文本同时有容量词与配置词信号的行 | 19 |
| 来源表页面标题包含年份 token 的行 | 457 |
| 去重 exact 文本字符总量 | 27,349 |
| 重复展开全部 row-text 后字符总量 | 49,040 |
| 每行最多文本数 / 最多文本字符 | 5 / 2,962 |
| 单文本字符中位数 / 最大值 | 367.5 / 976 |

容量词信号使用 `capacity/capacities`、`seat/seats/seated/seating`、`spectator`、`all-seater`、`accommodate`、`hold`、`fan`、`crowd` 的显式正则变体。这个宽松统计包括非容量用法：Minsk 的 “seat of the Executive Secretary”、Greater Nevada Field 年度观众量、Grünwalder 的最高到场人数都不能直接作为容量。首次窄词表扫描遗漏了 Coca-Cola Park 的 “accommodates 10,178 fans”，因此最终产物明确保存较宽词表；29 仍然是词法命中数，不是有效容量证据数。

年份 token 范围为 1800–2099，可能是开幕、命名权、球队成立、赛事历史等。`Founded`、`Joined`、`Opened` 和历史联赛标题均不能自动当作 capacity 的 reference period。

## 十个真实 discovery 例

以下 row index 为零基。完整 resource IDs 与全部对应原文同时保存在 JSON 中；每个案例保持未标 gold。

| 原表与行 | 数值和证据阅读 | 可审定范围 / 未解决问题 |
|---|---|---|
| `table:7ac2df0a979ad1cc2aebd13811b2eb2e`, row 5，Ghadir | 表38,900；`text:7d8e2e9f07492bb817fe71ac70f979b1` 也是38,900 | 该配对数值相等，可否定这一个文本作为冲突证据；不能据此宣称全湖无其他冲突。表Clubs与正文new均未绑定绝对日期。 |
| `table:3c2e86fd6a054bc4a5cd28f4c9221430`, row 1，Coca-Cola Park | 表10,100；`text:3261fb276113d3253055e39bebb7f106` 为8,278-seat；`text:d48bf1663f70e4c3a2c8be4d35c7122a` 为10,178 fans且包含辅助区域 | 座位数与包括草坪/套间等区域的总容纳量不是同口径。10,178与10,100依然缺同期间证据。正文2007是命名权日期；表2008/2007是球队成立/关联年份。 |
| 同表 row 11，Victory Field | 表14,230；`text:e596633b4fd121ed6dd6704ea19cf79c` 记录开幕13,300座位、含草坪15,696，2005拆1,000座位，14,667是首场到场 | 历史值、配置和 attendance 都需区分；表Current teams没有绝对容量参照日，不能做直接不等式冲突。 |
| `table:9f50724ea0512312c8687970f4fdccb5`, row 11，Mata Real | 表6,404；`text:ebb2e00a41582f13c9ddbfc3a6b5ff86` 明确2017新north stand后9,077 seats | 文本有扩建时期，表Attendance无赛季。不能默认表位于2017前或后，也不能自动判reconciled。 |
| 同表 row 17，Municipal 25 de Abril | 表6,153；`text:8028e26a35d6ebfd55e493d85d93e2fe` currently5,103，提1930/1934建设开放、1974改名、2000改造 | currently无绝对容量日期；改造未说明容量影响。同日期、配置尚未建立。 |
| `table:832e6053a2e73f9671787ec4517788c0`, row 8，Marconi/Campbelltown | 一行两球场与`11,000 21,000`；`text:776ac4ff97d4de8dd26c482d836a2952` Campbelltown nominal20,000，20,527是2005纪录；`text:5eab1614096a9809935a4bf8be8585ee` Marconi无容量 | 当前“the venue/this row capacity”单实体语义不完整。须先定义多场馆量词与可核验配对，不能让模型自行选择ANY/ALL，也不能将问题定义缺失藏为UNKNOWN。 |
| `table:ba7deab99e42394881e1b309ddad2b8e`, row 3，Jalan Besar | 2014 Malaysia Super League表8,000；`text:c6476a637628391135f9a829677a2e4a` 6,000-capacity，无日期 | 表`Capacity 1`、`Stadium 2`有脚注标记但抽取中未给脚注；2014联赛年份不能独立证明capacity配置日期。 |
| `table:221e10a81f1b5112f03d8f7ffb0f1ab6`, row 1，Luzhniki | 表81,000；`text:be675455f023eeb6a138fb0f0898d31e` total seating81,000；其他匹配文本是赛事史和Moscow城市 | 配对数值相等；源标题1991、Opened1956、正文赛事2018都不能补出容量有效期。不要自行用外部记忆修改历史容量。 |
| `table:bbf0fc43c1ef0b004287c9624554518b`, row 9，Percival Molson | 表23,420；`text:028e8ed9243e24ae46b28e18f5a1bebd` current23,420，并解释2009后从20,202增至over25,000、2014减座 | 可审定局部历史数值差有变化说明，当前值相等；不能用一个已解释历史值为全湖无冲突背书。 |
| `table:f7720ccbf3536685213822ce1cc74e5e`, row 9，Samsung/Stjörnuvöllur | 表1,440；`text:42d6e0505d044a1bef0c2a453b34a4d0` 990座位加about410站位 | 990不同口径；约1,400不是精确总容量，任务未定义近似容差，正文也无容量日期。源页2019只能确认赛季，不能代替statement日期。 |

除 venue exact 文本外，还读取十例来源页面的 exact 文本。International League 有两段联赛介绍，W-League 有两段制度介绍，Azadegan 有两段沿革介绍，2019 Úrvalsdeild 有一段赛季介绍；Primeira Liga、2014 Malaysia Super League、1991 Soviet Top League、List of stadiums in Canada 对应 source URL 无正文资源。它们没有补齐上述容量期间义务。该有限阅读仍不等于全文检索后的穷尽证据审计。

## 最强固定流程攻击与决策

整个 discovery 的 exact 文本只有27,349字符，每行最多2,962字符。应先使用 **一次批量 exact URL join + 共享文本缓存 + 固定结构化抽取 + 确定比较/例外检查** 作为强对照，不应为这些已知关联制造每行通用 Agent 探索。

固定抽取字段至少包括：物理实体、容量数值与单位、精确/近似、座位/站位/草坪等口径、容量有效期、日期所修饰的事件、历史改造、record attendance。这个对照尚未运行；小上下文只说明固定取证便宜，不证明其语义质量。

下一步判断顺序：

1. 先明确多球场源行的语义和 linked-description 的量词范围。不能悄悄把“全湖关于该实体的文本”改成“exact URL返回的文本”，两者是不同任务版本。
2. 在 discovery 中证明有足够数量的同配置、同期间可审定冲突和可审定非冲突，并做独立标注。不要用不等数值自动生成正例；不要用540个无exact文本的行制造UNKNOWN。
3. 对缺容量期间的候选，检查其他自然可达资源是否能补证。若必须补充原湖不存在的新资料，应创建新快照并让所有比较臂访问；新增人工生成时间戳不能当来源事实。
4. 若真实来源无法支持期间/配置核验，停止把本任务当主gap任务，保留为数据可审定性诊断。可以另行研究更窄的“数值差异候选审计”任务，但必须新命名和新规格，不能冒充原命题已经解决。

## 可复现扫描

从仓库根目录运行以下命令，读取当前公开湖和本审查中的显式正则，重新计算全部结构统计并与保存结果比较。只读取资源，不运行模型、不读取gold、不覆盖审查文件。

```bash
python - <<'PY'
from pathlib import Path
from collections import Counter
import hashlib, json, re, sqlite3, statistics
from semfilter_bench.lake.venues import SnapshotVerifier, read_jsonl
a = json.loads(Path('outputs/mmqa-venue-feasibility/capacity-audit.json').read_text())
root = Path(a['source_lake'])
SnapshotVerifier(root).verify()
assert hashlib.sha256((root/'manifest.json').read_bytes()).hexdigest() == a['snapshot_manifest_sha256']
splits = {p['record_id']: p['split'] for p in read_jsonl(root/'partitions.jsonl')}
rows = [r for r in read_jsonl(root/'relations/venues.jsonl') if splits[r['record_id']] == 'discovery']
rx = {k: re.compile(v, re.I) for k, v in a['method']['patterns'].items()}
db = sqlite3.connect((root/'lake.sqlite').as_uri() + '?mode=ro', uri=True)
counts, documents, pairs = Counter(), {}, []
for row in rows:
    matches = {}
    for url in row['venue_cell_urls']:
        for rid, _, _, payload in db.execute(a['method']['sql'], (url,)):
            text = json.loads(payload)['text']
            matches[rid] = documents[rid] = text
    flags = [{k: bool(p.search(t)) for k,p in rx.items()} for t in matches.values()]
    counts['discovery_rows'] += 1
    counts['rows_with_cell_urls'] += bool(row['venue_cell_urls'])
    counts['rows_with_exact_text'] += bool(matches)
    counts['row_text_pairs'] += len(matches)
    counts['rows_with_exact_capacity_integer'] += row['capacity_value'] is not None
    counts['rows_with_text_capacity_signal'] += any(f['capacity_signal'] for f in flags)
    counts['rows_with_text_capacity_signal_and_year_token'] += any(f['capacity_signal'] and f['year_token'] for f in flags)
    counts['rows_with_text_capacity_and_configuration_signals'] += any(f['capacity_signal'] and f['configuration_signal'] for f in flags)
    counts['rows_with_source_title_year_token'] += bool(rx['year_token'].search(row['source_title']))
    pairs.append((len(matches), sum(map(len,matches.values()))))
counts['unique_exact_texts'] = len(documents)
for name in ('capacity_signal','year_token','configuration_signal'):
    counts['unique_texts_with_'+name] = sum(bool(rx[name].search(t)) for t in documents.values())
counts['unique_texts_with_capacity_signal_and_year_token'] = sum(bool(rx['capacity_signal'].search(t) and rx['year_token'].search(t)) for t in documents.values())
counts['unique_texts_with_capacity_and_configuration_signals'] = sum(bool(rx['capacity_signal'].search(t) and rx['configuration_signal'].search(t)) for t in documents.values())
counts['unique_source_table_ids'] = len({r['table_id'] for r in rows})
lengths = list(map(len, documents.values()))
counts.update(unique_exact_text_characters=sum(lengths), row_text_pair_characters_with_repetition=sum(n for _,n in pairs), max_exact_texts_per_row=max(n for n,_ in pairs), max_exact_text_characters_per_row=max(n for _,n in pairs), median_unique_text_characters=statistics.median(lengths), max_unique_text_characters=max(lengths))
assert dict(counts) == a['counts'], (dict(counts), a['counts'])
print(json.dumps(dict(counts), indent=2))
db.close()
PY
```

代码/模型版本：结构扫描使用当前本地 `semfilter_bench.lake` 与 Python 标准库，湖身份由 manifest SHA 固定；没有提交新的 git revision。模型、prompt、推理参数、重试、模型成本、任务准确率均不适用，因本次没有模型实验。图像未在本次任务三审查中检查，不能从此审查推出多模态必要性。
