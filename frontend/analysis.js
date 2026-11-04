/** Cross-query analysis: facet filters, distributions, operator matrix and a sortable, exportable table. */
const AnalysisLabels = {
  origin: {
    source_reconstruction: ['源码重建', 'Source reconstruction', 'verified'],
    baseline_reconstruction: ['手写基线重建', 'Baseline reconstruction', 'verified'],
    supplied_reference: ['提供的参考计划', 'Supplied reference', 'supplied'],
    supplied_analysis: ['提供的分析转换', 'Supplied analysis', 'supplied'],
    end_to_end_interpretation: ['人工解释重建', 'Manual interpretation', 'derived'],
    derived_workload: ['本仓派生任务', 'Derived workload', 'derived'],
    proposed_missing_sql: ['拟议计划（SQL 缺失）', 'Proposed (SQL missing)', 'caution'],
    intent_sql_mismatch: ['意图计划（SQL 有差异）', 'Intent plan (SQL differs)', 'caution'],
  },
  kind: {natural_language: ['自然语言', 'Natural language'], sql: ['SQL', 'SQL'], python_plan: ['Python 计划', 'Python plan'], local_definition: ['本地定义', 'Local definition'], local_sql: ['本地 SQL', 'Local SQL'], local_natural_language: ['本地自然语言', 'Local natural language']},
  tr(pair) { return pair ? (AtlasI18n.language === 'en' ? pair[1] : pair[0]) : ''; },
  origin_(id) { return this.tr(this.origin[id]) || id; },
  tier(id) { return this.origin[id]?.[2] || 'derived'; },
  mixed(value) { return !value || value.startsWith('Not inferred') ? this.tr(['未标注', 'Not annotated']) : AtlasI18n.t(value); },
};

class AnalysisView {
  constructor(queries, onOpen) {
    this.onOpen = onOpen;
    // Scope: plans that contain at least one semantic operator; relational-only plans carry no semantic-operator signal.
    this.total = queries.length;
    this.rows = queries.filter(q => q.eal?.semantic > 0).map(q => {
      const nodes = q.eal.ops;
      const depth = Math.max(0, ...nodes.map(n => n.phase || 0));
      const semantic = nodes.filter(n => n.family === 'semantic');
      return {
        q, source: q.collection_name, origin: q.plan_origin, nodes: q.eal.nodes, semantic: q.eal.semantic,
        ops: [...new Set(semantic.map(n => n.op))],
        allOps: [...new Set(nodes.map(n => n.op))],
        semanticPositions: semantic.map(n => depth ? (n.phase || 0) / depth : 0),
        text: [q.query_id, q.title, AtlasI18n.queryZh[q.title] || '', q.original_query?.text || ''].join(' ').toLowerCase(),
      };
    });
    this.defaults = {q: '', source: '', origin: '', op: ''};
    this.filters = {...this.defaults};
    this.sort = {key: 'source', dir: 1};
    this.limit = 100;
  }
  t(zh, en) { return AtlasI18n.language === 'en' ? en : zh; }
  readParams(params) { for (const key of Object.keys(this.defaults)) this.filters[key] = params.get(key) || ''; this.limit = 100; }
  hash() {
    const params = new URLSearchParams(Object.entries(this.filters).filter(([, v]) => v));
    params.set('tab', 'analysis');
    return '#overall?' + params;
  }
  matches(r, skip) {
    const f = this.filters;
    return (skip === 'source' || !f.source || r.source === f.source)
      && (skip === 'origin' || !f.origin || r.origin === f.origin)
      && (skip === 'op' || !f.op || r.allOps.includes(f.op))
      && (!f.q || r.text.includes(f.q.toLowerCase()));
  }
  filtered() { return this.rows.filter(r => this.matches(r)); }

  render(root) {
    const options = (key, values, label) => `<label>${label}<select data-filter="${key}"><option value="">${this.t('全部', 'All')}</option>${values.map(([v, text, n]) => `<option value="${esc(v)}" ${this.filters[key] === v ? 'selected' : ''}>${esc(text)}${n === undefined ? '' : ' (' + n + ')'}</option>`).join('')}</select></label>`;
    const count = (field) => { const c = new Map(); for (const r of this.rows) for (const v of [].concat(r[field])) c.set(v, (c.get(v) || 0) + 1); return [...c].sort((a, b) => b[1] - a[1]); };
    const offline = location.protocol === 'file:';
    const semanticOps = new Set(this.rows.flatMap(r => r.ops));
    root.innerHTML = `<section class="overall analysis">
      <div class="analysis-heading"><div><h1>${this.t('语义算子分析', 'Semantic operator analysis')}</h1>
      <p class="overall-lead">${this.t(`统计范围：含至少一个语义算子的 ${this.rows.length} 个逻辑计划（目录共 ${this.total} 条记录）。所有统计随筛选联动；计划均未执行，节点数不代表模型调用次数。`, `Scope: ${this.rows.length} logical plans with at least one semantic operator (${this.total} catalog records). All statistics follow the filters; no plan has been executed, and node counts are not model calls.`)}</p></div>
      <p class="build-line">Build ${esc(window.SEMREL_BUILD)}${offline ? ` · <span class="snapshot-badge">${this.t('离线快照，非实时编译', 'Offline snapshot, not live-compiled')}</span>` : ''}</p></div>
      <div class="analysis-filters" role="search">
        <label>${this.t('关键词', 'Keyword')}<input data-filter="q" type="search" value="${esc(this.filters.q)}" placeholder="${this.t('标题、原始查询或 query_id', 'Title, original query or query_id')}"></label>
        ${options('source', count('source').map(([v, n]) => [v, v, n]), this.t('来源', 'Source'))}
        ${options('origin', count('origin').map(([v, n]) => [v, AnalysisLabels.origin_(v), n]), this.t('计划来源', 'Plan origin'))}
        <label>${this.t('包含算子', 'Contains operator')}<select data-filter="op"><option value="">${this.t('全部', 'All')}</option>${[['ops', this.t('语义算子', 'Semantic operators')], ['allOps', this.t('其他算子', 'Other operators')]].map(([field, label]) => `<optgroup label="${label}">${count(field).filter(([v]) => field === 'ops' || !semanticOps.has(v)).map(([v, n]) => `<option value="${esc(v)}" ${this.filters.op === v ? 'selected' : ''}>${esc(v)} (${n})</option>`).join('')}</optgroup>`).join('')}</select></label>
        <div class="analysis-reset"><button type="button" data-action="reset">${this.t('清除筛选', 'Clear filters')}</button></div>
      </div>
      <div id="analysis-results"></div>
      <div class="resource-links"><a href="exports/query_statistics.csv" download>${AtlasIcons.render('download')}${this.t('逐查询统计 CSV', 'Per-query statistics CSV')}</a><a href="exports/query_inputs.csv" download>${AtlasIcons.render('download')}${this.t('逐查询输入与环境清单', 'Per-query inputs & environments')}</a><a href="exports/catalog.sqlite" download>${AtlasIcons.render('database')}SQLite</a><a href="docs/data-model.md">${AtlasIcons.render('document')}${this.t('数据模型', 'Data model')}</a><a href="docs/eal.md">${AtlasIcons.render('document')}${this.t('EAL 说明', 'EAL guide')}</a><a href="docs/benchmark-coverage.md">${AtlasIcons.render('document')}${this.t('Benchmark 收录核对', 'Benchmark coverage')}</a></div>
    </section>`;
    root.querySelectorAll('[data-filter]').forEach(el => {
      const update = () => { this.filters[el.dataset.filter] = el.value.trim(); this.limit = 100; this.commit(root); };
      el.addEventListener(el.type === 'search' ? 'input' : 'change', update);
    });
    root.querySelector('[data-action=reset]').onclick = () => { this.filters = {...this.defaults}; this.render(root); this.commit(root); };
    this.renderResults(root);
  }
  commit(root) {
    history.replaceState(null, '', this.hash());
    root.querySelectorAll('select[data-filter]').forEach(el => { el.value = this.filters[el.dataset.filter]; });
    this.renderResults(root);
  }
  setFilter(root, values) { Object.assign(this.filters, values); this.limit = 100; this.commit(root); }

  renderResults(root) {
    const rows = this.filtered();
    const target = root.querySelector('#analysis-results');
    const empty = `<p class="empty">${this.t('没有符合筛选条件的查询。', 'No queries match these filters.')}</p>`;
    target.innerHTML = `<div class="overall-stats">
        ${[[rows.length, this.t('计划', 'Plans'), 'document'], [rows.reduce((s, r) => s + r.semantic, 0), this.t('语义算子实例', 'Semantic operator instances'), 'semantic'], [new Set(rows.flatMap(r => r.ops)).size, this.t('语义算子类型', 'Semantic operator types'), 'overview']].map(([v, label, icon]) => `<span class="stat-labelled">${AtlasIcons.render(icon)}<strong>${v}</strong><small>${label}</small></span>`).join('')}
      </div>
      ${rows.length ? `<div class="analysis-grid">
        ${this.bars(this.t('计划来源（可信度）', 'Plan origin (trust)'), this.group(this.rows.filter(r => this.matches(r, 'origin')), r => r.origin), 'origin', v => AnalysisLabels.origin_(v), 0, v => 'tier-' + AnalysisLabels.tier(v))}
        ${this.bars(this.t('计划规模（节点数）', 'Plan size (nodes)'), this.buckets(rows.map(r => r.nodes), [[2, '≤2'], [3, '3'], [5, '4–5'], [8, '6–8'], [12, '9–12'], [Infinity, '13+']]))}
        ${this.bars(this.t('每个计划的语义算子数', 'Semantic operators per plan'), this.buckets(rows.map(r => r.semantic), [[1, '1'], [2, '2'], [3, '3'], [Infinity, '4+']]))}
        ${this.bars(this.t('语义算子在计划中的位置', 'Where semantic operators sit'), this.buckets(rows.flatMap(r => r.semanticPositions), [[0.34, this.t('靠近输入', 'Near inputs')], [0.67, this.t('中段', 'Middle')], [Infinity, this.t('靠近输出', 'Near output')]]), '', v => v, 0, null, this.t('按拓扑层归一化：0 = 数据输入层，1 = 最终输出层。', 'Normalized topological layer: 0 = input layer, 1 = final output.'))}
      </div>
      ${this.matrix(rows, 'ops', this.t('语义算子 × 来源', 'Semantic operator × source'), this.t('数字为包含该语义算子的计划数；颜色深浅为该来源语义计划中的占比。点击单元格筛选。', 'Counts are plans containing the semantic operator; shading is its share of that source’s semantic plans. Click a cell to filter.'))}
      ${this.table(rows)}` : empty}`;
    target.querySelectorAll('[data-set]').forEach(b => b.onclick = () => this.setFilter(root, JSON.parse(b.dataset.set)));
    target.querySelectorAll('[data-sort]').forEach(b => b.onclick = () => { const key = b.dataset.sort; this.sort = {key, dir: this.sort.key === key ? -this.sort.dir : (['nodes', 'semantic'].includes(key) ? -1 : 1)}; this.renderResults(root); root.querySelector(`[data-sort="${key}"]`)?.focus(); });
    target.querySelectorAll('[data-open]').forEach(tr => { const open = () => this.onOpen(this.rows[Number(tr.dataset.open)].q); tr.onclick = open; tr.onkeydown = e => { if (e.key === 'Enter') open(); }; });
    const more = target.querySelector('[data-action=more]'); if (more) more.onclick = () => { this.limit += 200; this.renderResults(root); };
    const csv = target.querySelector('[data-action=csv]'); if (csv) csv.onclick = () => this.download(rows);
    target.querySelectorAll('[data-expand]').forEach(b => b.onclick = () => { b.closest('.analysis-card').classList.add('expanded'); b.remove(); });
  }
  group(rows, key) { const c = new Map(); for (const r of rows) c.set(key(r), (c.get(key(r)) || 0) + 1); return [...c].sort((a, b) => b[1] - a[1]); }
  buckets(values, edges) { const c = edges.map(([, label]) => [label, 0]); for (const v of values) c[edges.findIndex(([max]) => v <= max)][1]++; return c; }
  bars(title, entries, filterKey = '', label = v => v, fold = 0, tone = null, note = '') {
    const max = Math.max(1, ...entries.map(([, n]) => n)), total = entries.reduce((s, [, n]) => s + n, 0);
    const row = ([v, n], i) => {
      const active = filterKey && this.filters[filterKey] === v;
      const inner = `<span class="bar-label">${esc(label(v))}</span><span class="bar-track"><span class="bar-fill ${tone ? tone(v) : ''}" style="width:${(n / max * 100).toFixed(1)}%"></span></span><span class="bar-value">${n}<small>${total ? Math.round(n / total * 100) : 0}%</small></span>`;
      return filterKey ? `<button class="bar-row ${fold && i >= fold && !active ? 'folded' : ''}" aria-pressed="${active}" data-set='${esc(JSON.stringify({[filterKey]: active ? '' : v}))}'>${inner}</button>` : `<div class="bar-row">${inner}</div>`;
    };
    const hidden = fold ? entries.slice(fold) : [];
    return `<section class="analysis-card"><h2>${title}</h2>${note ? `<p class="card-note">${note}</p>` : ''}${entries.map(row).join('')}${hidden.length ? `<button class="fold-toggle" data-expand>${this.t(`其余 ${hidden.length} 个（${hidden.reduce((s, [, n]) => s + n, 0)} 条）`, `${hidden.length} more (${hidden.reduce((s, [, n]) => s + n, 0)} queries)`)}</button>` : ''}</section>`;
  }
  matrix(rows, field, title, note) {
    if (!rows.length) return '';
    const sources = this.group(rows, r => r.source), top = sources.slice(0, 8).map(([s]) => s);
    const columns = [...top.map(s => [s, rows.filter(r => r.source === s)]), ...(sources.length > 8 ? [[this.t('其他来源', 'Other sources'), rows.filter(r => !top.includes(r.source))]] : []), [this.t('合计', 'Total'), rows]];
    const ops = this.group(rows.flatMap(r => r[field].map(op => ({op}))), r => r.op).map(([op]) => op);
    const cell = (op, [name, rows], i) => {
      const n = rows.filter(r => r[field].includes(op)).length, share = rows.length ? n / rows.length : 0;
      const filter = i < top.length ? {source: name, op} : {op};
      return `<td>${n ? `<button class="${share > 0.5 ? 'strong' : ''}" data-set='${esc(JSON.stringify(filter))}' title="${esc(`${op} · ${name}: ${n} / ${rows.length} (${Math.round(share * 100)}%)`)}" style="--share:${share.toFixed(3)}">${n}</button>` : ''}</td>`;
    };
    return `<section class="analysis-card matrix-card"><h2>${title}</h2><p class="card-note">${note}</p>
      <div class="matrix-scroll"><table class="op-matrix"><thead><tr><th>${this.t('算子', 'Operator')}</th>${columns.map(([name, rows]) => `<th title="${esc(name)}"><span>${esc(name)}</span><small>${rows.length}</small></th>`).join('')}</tr></thead>
      <tbody>${ops.map(op => `<tr><th>${esc(op)}</th>${columns.map((c, i) => cell(op, c, i)).join('')}</tr>`).join('')}</tbody></table></div></section>`;
  }
  sorted(rows) {
    const {key, dir} = this.sort;
    const value = r => key === 'title' ? AtlasI18n.queryTitle(r.q) : key === 'origin' ? AnalysisLabels.origin_(r.origin) : key === 'number' ? r.q.display_number : r[key] ?? -1;
    return [...rows].sort((a, b) => { const x = value(a), y = value(b); return (typeof x === 'number' && typeof y === 'number' ? x - y : String(x).localeCompare(String(y))) * dir || a.q.display_number - b.q.display_number; });
  }
  table(rows) {
    const head = [['source', this.t('来源', 'Source')], ['number', '#'], ['title', this.t('查询', 'Query')], ['origin', this.t('计划来源', 'Plan origin')], ['nodes', this.t('节点', 'Nodes')], ['semantic', this.t('语义', 'Sem.')]];
    const sorted = this.sorted(rows), shown = sorted.slice(0, this.limit);
    const index = new Map(this.rows.map((r, i) => [r, i]));
    return `<section class="analysis-card table-card"><div class="table-heading"><h2>${this.t('查询列表', 'Queries')} <small>${this.t(`显示 ${shown.length} / ${rows.length} 条`, `Showing ${shown.length} of ${rows.length}`)}</small></h2><button data-action="csv">${AtlasIcons.render('download')}${this.t('导出当前筛选 CSV', 'Export filtered CSV')}</button></div>
      <div class="matrix-scroll"><table class="query-table"><thead><tr>${head.map(([key, label]) => `<th aria-sort="${this.sort.key === key ? (this.sort.dir > 0 ? 'ascending' : 'descending') : 'none'}"><button data-sort="${key}">${label}${this.sort.key === key ? (this.sort.dir > 0 ? ' ↑' : ' ↓') : ''}</button></th>`).join('')}<th>${this.t('语义算子', 'Semantic operators')}</th></tr></thead>
      <tbody>${shown.map(r => `<tr tabindex="0" data-open="${index.get(r)}"><td>${esc(r.source)}</td><td>${r.q.display_number}</td><td class="query-cell" data-verbatim><span>${esc(AtlasI18n.queryTitle(r.q))}</span></td><td><span class="origin-badge tier-${AnalysisLabels.tier(r.origin)}">${esc(AnalysisLabels.origin_(r.origin))}</span></td><td>${r.nodes ?? '—'}</td><td>${r.semantic ?? '—'}</td><td class="ops-cell">${r.ops.map(op => `<code>${esc(op)}</code>`).join(' ')}</td></tr>`).join('')}</tbody></table></div>
      ${rows.length > shown.length ? `<button class="fold-toggle" data-action="more">${this.t('再显示 200 条', 'Show 200 more')}</button>` : ''}</section>`;
  }
  download(rows) {
    const cells = ['query_id', 'source', 'display_number', 'title', 'original_query', 'original_query_kind', 'plan_origin', 'nodes', 'semantic_nodes', 'semantic_operators'];
    const quote = v => { const s = v === null || v === undefined ? '' : String(v); return /[",\n\r]/.test(s) ? '"' + s.replaceAll('"', '""') + '"' : s; };
    const lines = [cells.join(','), ...this.sorted(rows).map(r => [r.q.query_id, r.source, r.q.display_number, r.q.title, r.q.original_query?.text, r.q.original_query?.kind, r.origin, r.nodes, r.semantic, r.ops.join(' ')].map(quote).join(','))];
    const link = document.createElement('a');
    link.href = URL.createObjectURL(new Blob(['﻿' + lines.join('\n')], {type: 'text/csv;charset=utf-8'}));
    link.download = 'semrel-queries-filtered.csv'; link.click(); setTimeout(() => URL.revokeObjectURL(link.href), 1000);
  }
}
