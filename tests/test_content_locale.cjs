const fs=require('node:fs');const vm=require('node:vm');const assert=require('node:assert/strict');
const content=JSON.parse(fs.readFileSync('config/content-en.json','utf8'));
const context={window:{SEMREL_CONTENT_EN:content},localStorage:{getItem:()=> 'en'},document:{documentElement:{}}};
vm.runInNewContext(fs.readFileSync('src/viewer/i18n.js','utf8'),context);
const locale=context.window.AtlasI18n;const queries=JSON.parse(fs.readFileSync('assets/plans.json','utf8')).queries;
let count=0;
function check(value){if(typeof value==='string'&&/[\u4e00-\u9fff]/.test(value)){assert(!/[\u4e00-\u9fff]/.test(locale.t(value)),value);const translated=locale.t(value);locale.language='zh';assert.equal(locale.t(value),value);locale.language='en';assert.notEqual(translated,value);count++;}}
for(const q of queries){for(const key of ['title','status','mixed','note','group'])check(q[key]);for(const ref of q.provenance)for(const value of Object.values(ref))check(value);for(const node of q.eal.snapshot.graph.nodes)check(node.label);}
assert.equal(locale.t('input_0 = n004.output'),'input_0 = n004.output');
console.log(`Content locale: ${queries.length} queries; ${count} Chinese content occurrences covered; Chinese originals and identifiers preserved`);
