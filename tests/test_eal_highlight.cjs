const assert=require('node:assert/strict');
const fs=require('node:fs');const vm=require('node:vm');
const code=vm.runInNewContext(fs.readFileSync('src/viewer/eal-code.js','utf8')+';EalCode');
const source='// call "comment"\nmission "<img onerror=alert(1)>" {\n let x = call "a\\"b" with { input = prev.output, n = 42, enabled = true }\n}';
const html=code.highlight(source,2);
const decoded=html.replace(/<[^>]*>/g,'').replace(/&quot;/g,'"').replace(/&#39;/g,"'").replace(/&lt;/g,'<').replace(/&gt;/g,'>').replace(/&amp;/g,'&');
assert.equal(decoded,source);assert(!html.includes('<img'));assert(html.includes('token type'));assert(html.includes('token keyword'));assert.equal((html.match(/id="source-target"/g)||[]).length,1);
for(const name of fs.readdirSync('exports/eal')){if(name.endsWith('.eal')){const text=fs.readFileSync('exports/eal/'+name,'utf8');const result=code.highlight(text).replace(/<[^>]*>/g,'').replace(/&quot;/g,'"').replace(/&#39;/g,"'").replace(/&lt;/g,'<').replace(/&gt;/g,'>').replace(/&amp;/g,'&');assert.equal(result,text);}}
console.log('EAL highlighting: escaping, tokens, line targeting, and catalog round-trip passed');
