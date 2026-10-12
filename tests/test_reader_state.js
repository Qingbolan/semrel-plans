// Lifecycle regression: a slow response must not replace a newer selection.
const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');
const pending = [];
const context = vm.createContext({AbortController, location:{protocol:'http:'}, fetch:()=>new Promise(resolve=>pending.push(resolve))});
vm.runInContext(fs.readFileSync(require('node:path').join(__dirname,'../src/viewer/reader.js'),'utf8')+'\nthis.Reader = EalDocument;',context);
const response = (name,ok=true) => ({ok,headers:{get:()=> 'application/json'},json:async()=>ok?{source:name,graph:{name},ir:{}}:{source:name,error:'syntax error'}});
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
  assert.equal(reader.state.graph,null);
  console.log('Reader lifecycle: stale response and error clearing passed');
})().catch(error=>{console.error(error);process.exitCode=1;});
