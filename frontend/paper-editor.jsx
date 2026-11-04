import React, {useEffect, useState} from 'react';
import {createRoot} from 'react-dom/client';
import {LexicalComposer} from '@lexical/react/LexicalComposer';
import {useLexicalComposerContext} from '@lexical/react/LexicalComposerContext';
import {RichTextPlugin} from '@lexical/react/LexicalRichTextPlugin';
import {ContentEditable} from '@lexical/react/LexicalContentEditable';
import {LexicalErrorBoundary} from '@lexical/react/LexicalErrorBoundary';
import {HistoryPlugin} from '@lexical/react/LexicalHistoryPlugin';
import {ListPlugin} from '@lexical/react/LexicalListPlugin';
import {LinkPlugin} from '@lexical/react/LexicalLinkPlugin';
import {ClickableLinkPlugin} from '@lexical/react/LexicalClickableLinkPlugin';
import {TablePlugin} from '@lexical/react/LexicalTablePlugin';
import {$getRoot,$getSelection,$isRangeSelection,$createParagraphNode,FORMAT_TEXT_COMMAND,UNDO_COMMAND,REDO_COMMAND} from 'lexical';
import {HeadingNode,QuoteNode,$createHeadingNode,$createQuoteNode} from '@lexical/rich-text';
import {ListNode,ListItemNode,INSERT_UNORDERED_LIST_COMMAND,INSERT_ORDERED_LIST_COMMAND} from '@lexical/list';
import {LinkNode,AutoLinkNode,TOGGLE_LINK_COMMAND} from '@lexical/link';
import {TableNode,TableCellNode,TableRowNode,INSERT_TABLE_COMMAND} from '@lexical/table';
import {CodeNode,CodeHighlightNode,$createCodeNode} from '@lexical/code';
import {$generateNodesFromDOM} from '@lexical/html';
import {$setBlocksType} from '@lexical/selection';

const paths={edit:'m15 5 4 4M4 20l4-1L20 7a2.8 2.8 0 0 0-4-4L4 15z',eye:'M2 12s3-7 10-7 10 7 10 7-3 7-10 7S2 12 2 12Zm10-3a3 3 0 1 0 0 6 3 3 0 0 0 0-6',undo:'M8 5 3 10l5 5M3 10h11a6 6 0 0 1 0 12',redo:'m16 5 5 5-5 5m5-5H10a6 6 0 0 0 0 12',list:'M8 6h13M8 12h13M8 18h13M3 6h.01M3 12h.01M3 18h.01',link:'m10 13 4-4m-7 5-2 2a4 4 0 0 0 6 6l4-4m2-8 2-2a4 4 0 0 0-6-6L9 6',table:'M3 3h18v18H3zM3 9h18M9 3v18M3 15h18M15 3v18'};
const Icon=({name})=><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round" aria-hidden="true"><path d={paths[name]}/></svg>;

/** Each paper aspect owns its own persisted Lexical document. Source records stay immutable. */
export class PaperDocumentStore {
  constructor(storage=localStorage){this.storage=storage;}
  key(paper,section){return `semrel-paper-document:v1:${paper}:${section}`;}
  read(paper,section){return this.storage.getItem(this.key(paper,section));}
  save(paper,section,state){this.storage.setItem(this.key(paper,section),JSON.stringify(state.toJSON()));}
}
const store=new PaperDocumentStore();

function EditorControls({paper,section,label}){
  const [editor]=useLexicalComposerContext();
  const [editing,setEditing]=useState(false),[status,setStatus]=useState(''),[formats,setFormats]=useState({});
  useEffect(()=>editor.registerUpdateListener(({editorState,dirtyElements,dirtyLeaves})=>{
    editorState.read(()=>{const s=$getSelection();if($isRangeSelection(s))setFormats(Object.fromEntries(['bold','italic','underline','strikethrough','code'].map(f=>[f,s.hasFormat(f)])));});
    if(!editor.isEditable()||(!dirtyElements.size&&!dirtyLeaves.size))return;
    try{store.save(paper,section,editorState);setStatus(label('已保存到此浏览器','Saved in this browser'));}
    catch{setStatus(label('保存失败，请勿关闭页面','Save failed. Keep this page open'));}
  }),[editor,paper,section]);
  function toggle(){editor.setEditable(!editing);setEditing(!editing);if(!editing)editor.focus();}
  function block(type){editor.update(()=>{const s=$getSelection();if($isRangeSelection(s))$setBlocksType(s,()=>type==='p'?$createParagraphNode():type==='quote'?$createQuoteNode():type==='code'?$createCodeNode():$createHeadingNode(type));});}
  function button(title,child,action,active){return <button type="button" title={title} aria-label={title} aria-pressed={active} onMouseDown={e=>e.preventDefault()} onClick={action}>{child}</button>;}
  return <>
    {editing&&<div className="paper-editor-toolbar" role="toolbar" aria-label={label('文本格式','Text formatting')}>
      <select aria-label={label('段落样式','Block style')} defaultValue="p" onChange={e=>block(e.target.value)}>{[['p','正文','Paragraph'],['h2','标题','Heading'],['h3','小标题','Subheading'],['quote','引用','Quote'],['code','代码块','Code block']].map(([id,zh,en])=><option key={id} value={id}>{label(zh,en)}</option>)}</select>
      {['bold','italic','underline','strikethrough','code'].map((f,i)=><React.Fragment key={f}>{button(label(['加粗','斜体','下划线','删除线','行内代码'][i],f),<span className={'format-'+f}>{['B','I','U','S','<>'][i]}</span>,()=>editor.dispatchCommand(FORMAT_TEXT_COMMAND,f),formats[f]||false)}</React.Fragment>)}
      <span className="editor-divider"/>
      {button(label('无序列表','Bullet list'),<Icon name="list"/>,()=>editor.dispatchCommand(INSERT_UNORDERED_LIST_COMMAND))}
      {button(label('有序列表','Numbered list'),'1.',()=>editor.dispatchCommand(INSERT_ORDERED_LIST_COMMAND))}
      {button(label('插入链接','Insert link'),<Icon name="link"/>,()=>{const url=window.prompt(label('链接地址（留空移除链接）','Link URL (empty to remove)'),'https://');if(url!==null&&(!url||/^(https?:\/\/|#|mailto:)/i.test(url)))editor.dispatchCommand(TOGGLE_LINK_COMMAND,url||null);})}
      {button(label('插入表格','Insert table'),<Icon name="table"/>,()=>editor.dispatchCommand(INSERT_TABLE_COMMAND,{columns:'3',rows:'3',includeHeaders:true}))}
      <span className="editor-divider"/>
      {button(label('撤销','Undo'),<Icon name="undo"/>,()=>editor.dispatchCommand(UNDO_COMMAND))}
      {button(label('重做','Redo'),<Icon name="redo"/>,()=>editor.dispatchCommand(REDO_COMMAND))}
    </div>}
    <div className="paper-editor-mode"><span role="status" className="editor-save-status">{editing?status:''}</span><button onClick={toggle} aria-label={editing?label('预览','Preview'):label('编辑','Edit')} title={editing?label('切换为预览','Switch to preview'):label('切换为编辑','Switch to edit')}><Icon name={editing?'eye':'edit'}/><span>{editing?label('预览','Preview'):label('编辑','Edit')}</span></button></div>
    <ClickableLinkPlugin disabled={editing}/>
  </>;
}

export function mountPaperEditor(element,{paper,section,html,label}){
  const root=createRoot(element);
  const saved=store.read(paper,section);
  root.render(<LexicalComposer initialConfig={{namespace:`paper-${paper}-${section}`,editable:false,
    nodes:[HeadingNode,QuoteNode,ListNode,ListItemNode,LinkNode,AutoLinkNode,TableNode,TableCellNode,TableRowNode,CodeNode,CodeHighlightNode],
    theme:{text:{bold:'format-bold',italic:'format-italic',underline:'format-underline',strikethrough:'format-strikethrough',code:'format-code'},code:'paper-editor-code'},
    onError:error=>{throw error;},
    editorState:saved||((editor)=>{$getRoot().append(...$generateNodesFromDOM(editor,new DOMParser().parseFromString(html,'text/html')));})}}>
      <EditorControls paper={paper} section={section} label={label}/>
      <RichTextPlugin contentEditable={<ContentEditable className="paper-prose paper-editor-surface" aria-label={label('论文正文','Paper content')} lang="zh-CN" data-verbatim/>} ErrorBoundary={LexicalErrorBoundary}/>
      <HistoryPlugin/><ListPlugin/><LinkPlugin/><TablePlugin/>
    </LexicalComposer>);
  return ()=>root.unmount();
}
