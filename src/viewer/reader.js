/* Per-query plan snapshots and records live in assets/details; script tags also work from file://. */
globalThis.SemRelDetails = {
  pending: new Map(),
  receive(queryId, detail) { this.pending.get(queryId)?.resolve(detail); },
  load(q) {
    if(!q || q.imported || !q.detail_path || q.detailLoaded) return null;
    if(q.detailPromise) return q.detailPromise;
    q.detailPromise = new Promise((resolve, reject) => {
      const script = document.createElement('script');
      this.pending.set(q.query_id, {resolve: detail => {
        const {snapshot, ...fields} = detail; Object.assign(q, fields);
        if(q.eal && snapshot) q.eal.snapshot = snapshot;
        q.detailLoaded = true; this.pending.delete(q.query_id); script.remove(); resolve(q);
      }});
      script.onerror = () => { this.pending.delete(q.query_id); q.detailPromise = null; script.remove(); reject(new Error('无法读取查询详情：' + q.detail_path)); };
      script.src = q.detail_path;
      document.head.append(script);
    });
    return q.detailPromise;
  },
};

/* Each selection owns one load lifecycle; superseded requests cannot update it. */
class EalDocument {
  constructor(onChange) {
    this.onChange = onChange;
    this.revision = 0;
    this.state = {status:'idle', source:'', graph:null, ir:null, error:''};
  }
  async load(query) {
    const revision = ++this.revision;
    this.controller?.abort();
    this.controller = new AbortController();
    this.state = {status:'loading', source:'', graph:null, ir:null, error:''};
    this.onChange();
    let errorKind='read';
    try {
      const detail = globalThis.SemRelDetails.load(query);
      if(detail) { await detail; if(revision!==this.revision) return; }
      if(query.plan_format==='reference_program') {
        this.state = {status:'reference',source:'',graph:null,ir:null,error:''};
        this.onChange();
        return;
      }
      let result;
      // Catalog plans are compiled at build time; only imported EAL needs the compile service.
      if(!query.imported && query.eal?.snapshot) {
        result = query.eal.snapshot;
      } else if(location.protocol==='file:') {
        throw new Error('导入 EAL 需要本地编译服务：python3 backend/scripts/serve.py');
      } else {
        const response = await fetch(query.imported ? '/api/compile' : '/api/plan?query_id='+encodeURIComponent(query.query_id), {
          method:query.imported?'POST':'GET', cache:'no-store', signal:this.controller.signal,
          ...(query.imported?{headers:{'Content-Type':'application/json'},body:JSON.stringify({source:query.importedSource})}:{})
        });
        if(!response.headers.get('content-type')?.includes('application/json')) throw new Error('请使用 python3 backend/scripts/serve.py 启动图册，普通静态服务器不能编译 EAL。');
        result = await response.json();
        if(revision!==this.revision) return;
        if(!response.ok) {errorKind=result.error_kind||(response.status===422?'compile':'read');this.state.source=result.source||query.importedSource||'';throw new Error(result.error||'无法编译 EAL');}
      }
      if(revision!==this.revision) return;
      this.state = {status:'ready', ...result, error:''};
    } catch(error) {
      if(revision!==this.revision) return;
      this.state = {...this.state,status:'error',error:error.message,errorKind};
    }
    this.onChange();
  }
}
