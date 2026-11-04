// Lifecycle regression: a slow response must not replace a newer selection.
const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');
const pending = [];
let networkFailure=false;
const context = vm.createContext({AbortController, location:{protocol:'http:'}, fetch:()=>networkFailure?Promise.reject(new TypeError('Load failed')):new Promise(resolve=>pending.push(resolve))});
vm.runInContext(fs.readFileSync(require('node:path').join(__dirname,'../frontend/reader.js'),'utf8')+'\nthis.Reader = EalDocument;',context);
const response = (name,ok=true) => ({ok,status:ok?200:422,headers:{get:()=> 'application/json'},json:async()=>ok?{source:name,graph:{name},ir:{}}:{source:name,error:'syntax error'}});
(async()=>{
  const reader = new context.Reader(()=>{});
  const first = reader.load({query_id:'old'});
  const second = reader.load({query_id:'new'});
  pending[1](response('new')); await second;
  pending[0](response('old')); await first;
  assert.equal(reader.state.graph.name,'new');
  const failed = reader.load({query_id:'broken'});
  assert.equal(reader.state.status,'loading');
  assert.equal(reader.state.graph,null);
  pending[2](response('broken',false)); await failed;
  assert.equal(reader.state.status,'error');
  assert.equal(reader.state.source,'broken');
  assert.equal(reader.state.errorKind,'compile');
  assert.equal(reader.state.graph,null);
  const delayed = reader.load({query_id:'delayed'});
  await reader.load({query_id:'reference',plan_format:'reference_program'});
  assert.equal(reader.state.status,'reference');
  assert.equal(reader.state.graph,null);
  pending[3](response('stale')); await delayed;
  assert.equal(reader.state.status,'reference');
  assert.equal(reader.state.source,'');
  for(const kind of ['catalog','file','busy']) {
    const request=reader.load({query_id:kind});
    pending.at(-1)({ok:false,status:503,headers:{get:()=> 'application/json'},json:async()=>({error:'unavailable',error_kind:kind})});
    await request;
    assert.equal(reader.state.status,'error');
    assert.equal(reader.state.errorKind,kind);
    assert.equal(reader.state.graph,null);
  }
  networkFailure=true;
  await reader.load({query_id:'offline-service'});
  assert.equal(reader.state.errorKind,'read');
  assert.equal(reader.state.graph,null);
  console.log('Reader lifecycle: stale response and error clearing passed');
})().catch(error=>{console.error(error);process.exitCode=1;});
