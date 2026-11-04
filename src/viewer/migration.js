/* Versioned, allowlisted browser-state backup; no unrelated localStorage entries. */
class BrowserBackup {
  static allows(key) { return ['semrel-paper-groups','semrel-language','semrel-catalog-group'].includes(key)||/^semrel-paper-document:v1:[^:]+:[^:]+$/.test(key); }
  static capture(storage) {
    const entries={};
    for(let i=0;i<storage.length;i++){const key=storage.key(i);if(this.allows(key))entries[key]=storage.getItem(key);}
    return {format:'semrel-browser-backup',version:1,created_at:new Date().toISOString(),origin:location.origin,entries};
  }
  static validate(value) {
    if(value?.format!=='semrel-browser-backup'||value.version!==1||!value.entries||typeof value.entries!=='object'||Array.isArray(value.entries))throw new Error('备份格式不正确');
    for(const [key,item] of Object.entries(value.entries)){
      if(!this.allows(key)||typeof item!=='string')throw new Error('备份包含不支持的记录');
      if(key==='semrel-paper-groups'){
        const groups=JSON.parse(item);
        if(!Array.isArray(groups.groups)||!groups.memberships||typeof groups.memberships!=='object')throw new Error('分组格式不正确');
      }
      if(key.startsWith('semrel-paper-document:')&&!JSON.parse(item)?.root)throw new Error('论文编辑格式不正确');
    }
    return value;
  }
  static restore(storage,value) {
    this.validate(value);
    const before=new Map(Object.keys(value.entries).map(key=>[key,storage.getItem(key)]));
    try {for(const [key,item] of Object.entries(value.entries))storage.setItem(key,item);}
    catch(error){for(const [key,item] of before)item===null?storage.removeItem(key):storage.setItem(key,item);throw error;}
  }
  static download(value) {
    const url=URL.createObjectURL(new Blob([JSON.stringify(value,null,2)],{type:'application/json'}));
    const a=document.createElement('a');a.href=url;a.download=`semrel-browser-${Date.now()}.json`;a.click();setTimeout(()=>URL.revokeObjectURL(url),1000);
  }
}
if(typeof module!=='undefined')module.exports=BrowserBackup;
if(typeof document!=='undefined'){
  let pending=null;
  const status=document.querySelector('#status'),restore=document.querySelector('#restore');
  document.querySelector('#export').onclick=()=>{BrowserBackup.download(BrowserBackup.capture(localStorage));status.textContent='已导出当前浏览器的数据。';};
  document.querySelector('#file').onchange=async event=>{
    pending=null;restore.disabled=true;
    try{const file=event.target.files[0];if(!file)return;if(file.size>20*1024*1024)throw new Error('备份超过 20 MiB');pending=BrowserBackup.validate(JSON.parse(await file.text()));document.querySelector('#preview').textContent=`来源：${pending.origin||'未记录'}\n记录数：${Object.keys(pending.entries).length}`;restore.disabled=false;}
    catch(error){status.textContent=error.message;}
  };
  restore.onclick=()=>{try{BrowserBackup.download(BrowserBackup.capture(localStorage));BrowserBackup.restore(localStorage,pending);status.textContent='已导入。返回图册后刷新页面即可读取。';restore.disabled=true;}catch(error){status.textContent=`导入失败：${error.message}`;}};
}
