const KEY='semrel-paper-groups';
export class PaperGroups {
  constructor(){
    this.state={groups:[],memberships:{}};
    try{const saved=JSON.parse(localStorage.getItem(KEY));if(Array.isArray(saved?.groups)&&saved.memberships){this.state={groups:saved.groups.filter(g=>typeof g.id==='string'&&typeof g.name==='string'&&/^#[0-9a-f]{6}$/i.test(g.color)),memberships:saved.memberships};}}catch{}
  }
  groupsFor(id){const ids=this.state.memberships[id]||[];return this.state.groups.filter(g=>Array.isArray(ids)&&ids.includes(g.id));}
  save(state){localStorage.setItem(KEY,JSON.stringify(state));this.state=state;document.dispatchEvent(new Event('atlas-groups-change'));}
  edit(paper,label,onSave){
    const draft=structuredClone(this.state);const selected=new Set(draft.memberships[paper.id]||[]);
    const dialog=document.createElement('dialog');dialog.className='paper-group-dialog';dialog.setAttribute('aria-label',label('分组','Groups'));
    const heading=document.createElement('h2');heading.textContent=label('分组','Groups');
    const title=document.createElement('p');title.textContent=paper.title;
    const list=document.createElement('div');list.className='group-editor-list';
    const draw=()=>{list.replaceChildren();for(const group of draft.groups){
      const row=document.createElement('div');row.className='group-editor-row';
      const check=document.createElement('input');check.type='checkbox';check.checked=selected.has(group.id);check.setAttribute('aria-label',label('加入 ','Assign ')+group.name);check.onchange=()=>check.checked?selected.add(group.id):selected.delete(group.id);
      const color=document.createElement('input');color.type='color';color.value=group.color;color.setAttribute('aria-label',label('分组颜色','Group color'));color.oninput=()=>group.color=color.value;
      const name=document.createElement('input');name.value=group.name;name.maxLength=50;name.setAttribute('aria-label',label('分组名称','Group name'));name.oninput=()=>group.name=name.value;
      const remove=document.createElement('button');remove.textContent='×';remove.title=label('删除分组','Delete group');remove.setAttribute('aria-label',remove.title);remove.onclick=()=>{draft.groups=draft.groups.filter(g=>g.id!==group.id);selected.delete(group.id);for(const key in draft.memberships)draft.memberships[key]=draft.memberships[key].filter(id=>id!==group.id);draw();};
      row.append(check,color,name,remove);list.append(row);
    }};draw();
    const add=document.createElement('button');add.textContent=label('＋ 新建分组','＋ New group');add.onclick=()=>{const group={id:crypto.randomUUID(),name:label('新分组','New group'),color:['#648477','#b58a52','#687fa3','#a5758b'][draft.groups.length%4]};draft.groups.push(group);selected.add(group.id);draw();list.lastElementChild.querySelector('input[aria-label="'+label('分组名称','Group name')+'"]').select();};
    const actions=document.createElement('div');actions.className='group-editor-actions';
    const error=document.createElement('p');error.setAttribute('role','alert');
    const cancel=document.createElement('button');cancel.textContent=label('取消','Cancel');cancel.onclick=()=>dialog.close();
    const save=document.createElement('button');save.textContent=label('保存','Save');save.onclick=()=>{if(draft.groups.some(g=>!g.name.trim())){error.textContent=label('请输入分组名称','Enter a group name');return;}draft.groups.forEach(g=>g.name=g.name.trim());draft.memberships[paper.id]=[...selected];try{this.save(draft);onSave();dialog.close();}catch{error.textContent=label('无法保存，请检查浏览器存储权限','Could not save. Check browser storage permissions.');}};
    actions.append(cancel,save);dialog.append(heading,title,list,add,error,actions);dialog.onclose=()=>dialog.remove();document.body.append(dialog);dialog.showModal();
  }
}
