const assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm');
let saved=JSON.stringify({groups:[{id:'custom',name:'My group',color:'#123456'}],memberships:{q:['custom']}});
const context={localStorage:{getItem:()=>saved,setItem:(_,s)=>saved=s},document:{dispatchEvent:()=>{}},Event:class{}};
vm.createContext(context);vm.runInContext(fs.readFileSync('frontend/paper-groups.js','utf8').replace('export class','class')+'\nthis.Groups=PaperGroups;',context);
const seed={version:1,groups:[{id:'sem-operator',name:'Sem-operator',color:'#123456'}],memberships:{q:['sem-operator']}};
const groups=new context.Groups();groups.seed(seed);
assert.deepEqual(Array.from(groups.groupsFor('q'),g=>g.id),['custom','sem-operator']);
groups.save({...groups.state,groups:groups.state.groups.filter(g=>g.id!=='sem-operator'),memberships:{q:['custom']}});
const reopened=new context.Groups();reopened.seed(seed);
assert.deepEqual(Array.from(reopened.groupsFor('q'),g=>g.id),['custom']);
console.log('Default groups preserve existing memberships and do not restore user-deleted groups.');

const fresh=new context.Groups();fresh.state={groups:seed.groups,memberships:{q:[]},seedVersion:1};
fresh.seed({...seed,memberships:{q:['sem-operator'],newQuery:['sem-operator']}});
assert.equal(fresh.groupsFor('q').length,0);
assert.deepEqual(Array.from(fresh.groupsFor('newQuery'),g=>g.id),['sem-operator']);
reopened.seed({...seed,memberships:{q:['sem-operator'],newQuery:['sem-operator']}});
assert.equal(reopened.groupsFor('newQuery').length,0);
console.log('Newly imported queries join existing default groups without restoring user removals.');
