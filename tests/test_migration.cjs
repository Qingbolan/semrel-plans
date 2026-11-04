const assert=require('node:assert/strict');
const Backup=require('../src/viewer/migration.js');
class Storage {
 constructor(entries={}){this.items=new Map(Object.entries(entries));}
 get length(){return this.items.size;}
 key(i){return [...this.items.keys()][i];}
 getItem(k){return this.items.get(k)??null;}
 setItem(k,v){this.items.set(k,v);}
 removeItem(k){this.items.delete(k);}
}
global.location={origin:'http://localhost:8765'};
const source=new Storage({'semrel-language':'en','semrel-paper-document:v1:paper:overview':'{"root":{"children":[]}}','unrelated-token':'private'});
const backup=Backup.capture(source);assert.equal(Object.keys(backup.entries).length,2);assert.equal(backup.entries['unrelated-token'],undefined);
const target=new Storage({'semrel-language':'zh','other':'keep'});Backup.restore(target,backup);assert.equal(target.getItem('semrel-language'),'en');assert.equal(target.getItem('other'),'keep');
assert.throws(()=>Backup.restore(target,{...backup,entries:{'unrelated-token':'bad'}}));
const before=target.getItem('semrel-language');assert.throws(()=>Backup.restore(target,{...backup,entries:{'semrel-language':'zh','semrel-paper-document:v1:paper:overview':'invalid'}}));assert.equal(target.getItem('semrel-language'),before);
console.log('Browser backup roundtrip and rejection checks passed');
const quota=new Storage({'semrel-language':'zh'});let writes=0;
const set=quota.setItem.bind(quota);quota.setItem=(k,v)=>{if(++writes===2)throw new Error('quota exceeded');set(k,v);};
assert.throws(()=>Backup.restore(quota,backup));assert.equal(quota.getItem('semrel-language'),'zh');assert.equal(quota.getItem('semrel-paper-document:v1:paper:overview'),null);
console.log('Partial-write rollback passed');
