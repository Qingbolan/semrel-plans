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
    try {
      let result;
      if(location.protocol==='file:') {
        if(query.imported) throw new Error('导入 EAL 需要本地编译服务：python3 scripts/serve.py');
        result = query.eal.snapshot;
      } else {
        const response = await fetch(query.imported ? '/api/compile' : '/api/plan?query_id='+encodeURIComponent(query.query_id), {
          method:query.imported?'POST':'GET', cache:'no-store', signal:this.controller.signal,
          ...(query.imported?{headers:{'Content-Type':'application/json'},body:JSON.stringify({source:query.importedSource})}:{})
        });
        if(!response.headers.get('content-type')?.includes('application/json')) throw new Error('请使用 python3 scripts/serve.py 启动图册，普通静态服务器不能编译 EAL。');
        result = await response.json();
        if(revision!==this.revision) return;
        if(!response.ok) {this.state.source=result.source||query.importedSource||'';throw new Error(result.error||'无法编译 EAL');}
      }
      if(revision!==this.revision) return;
      this.state = {status:'ready', ...result, error:''};
    } catch(error) {
      if(revision!==this.revision) return;
      this.state = {...this.state,status:'error',error:error.message};
    }
    this.onChange();
  }
}
