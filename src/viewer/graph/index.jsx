import React, { memo, useCallback, useEffect, useMemo, useState } from 'react';
import { createRoot } from 'react-dom/client';
import { ReactFlow, ReactFlowProvider, BaseEdge, Handle, Position,
  useNodesState, useReactFlow, useNodesInitialized } from '@xyflow/react';
import '@xyflow/react/dist/style.css';
import './style.css';
import { operatorAppearance } from './operator-appearance.mjs';
import { layoutMission, dependencyScope, NODE_WIDTH, NODE_HEIGHT } from './layout.mjs';

function ToolButton({label,path,onClick,pressed}) {
  return <button type="button" title={t(label)} aria-label={t(label)} aria-pressed={pressed} onClick={onClick}><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round" aria-hidden="true"><path d={path}/></svg></button>;
}

const t=value=>window.AtlasI18n.t(value);
const families = {relational:'结构化算子',semantic:'语义算子',input:'数据输入',ability:'Ability'};

const OperatorNode = memo(function OperatorNode({data,selected}) {
  const horizontal = data.direction === 'LR';
  const appearance=operatorAppearance(data.arguments?.operator_type);
  const name = data.arguments?.operator_type?.replaceAll('_',' ') || data.ability;
  const description = t(data.label).replace(new RegExp('^'+(data.arguments?.operator_type || '__none__')+'\\s*'), '').trim();
  const redundant = data.label.replaceAll('_',' ').toUpperCase() === name.toUpperCase();
  return <div className={`operator-card pattern-${appearance.pattern} ${appearance.symbol?'has-algebra-symbol':''} family-${data.family} ${selected?'is-selected':''}`} title={t(data.label)} style={{height:data.height}}>
    {appearance.symbol&&<span className="operator-watermark" aria-hidden="true">{appearance.symbol}</span>}
    <div className="operator-heading"><strong>{name}</strong><span title={t(families[data.family])}>{t(data.family==='semantic'?'语义':data.family==='input'?'输入':'')}</span></div>
    {!redundant&&<div className="operator-label">{description}</div>}
    <code className="node-binding">{data.id}</code>
    {data.ports.map(port=><Handle key={port.id} type={port.type} id={port.id}
      position={horizontal?(port.type==='source'?Position.Right:Position.Left):(port.type==='source'?Position.Top:Position.Bottom)}
      style={{left:port.x,top:port.y,right:'auto',bottom:'auto',transform:'translate(-50%, -50%)'}}
      title={port.type==='source'?'output':port.id} isConnectable={false}><span className={`port-name ${port.type==='source'?'output-port':'input-port'}`}>{port.type==='source'?'output':port.id}</span></Handle>)}
  </div>;
});
function RoutedEdge({id,data,style,markerEnd,label,labelStyle,labelBgStyle,labelBgPadding}) {
  const path=data.path;
  const {x,y}=data.labelPoint;
  return <BaseEdge id={id} path={path} style={style} markerEnd={markerEnd} label={label}
    labelX={x} labelY={y} labelStyle={labelStyle} labelBgStyle={labelBgStyle} labelBgPadding={labelBgPadding}/>;
}
const edgeTypes={routed:RoutedEdge};
const nodeTypes = {operator:OperatorNode};
const fitOptions = {padding:0.2,maxZoom:1,minZoom:0.08};

function Inspector({node,model,onClose,onSource,onFocus}) {
  const inputs=model.edges.filter(e=>e.parent===node.id);
  const outputs=model.edges.filter(e=>e.child===node.id);
  const emits=(model.emits||[]).filter(e=>e.value?.type==='binding'&&e.value.binding===node.binding);
  const metadata=new Set(['label','family','node_id','query_id','operator_type','plan_origin']);
  const params=Object.entries(node.arguments||{}).filter(([key])=>!metadata.has(key));
  return <section className="flow-inspector" aria-label={t('节点详情')}>
    <div className="inspector-heading"><strong>{node.id}</strong><button onClick={onClose} aria-label={t('关闭节点详情')}>×</button></div>
    <h3>{node.ability}</h3><p>{t(node.label)}</p>
    <h4>{t('输入 ')}<span>{inputs.length}</span></h4><div className="io-list">{inputs.map(e=><button key={e.port} onClick={()=>onFocus(e.child)}><code>{e.child}.output</code><span>→</span><code>{e.port}</code></button>)}{!inputs.length&&<p>{t('无上游调用输入')}</p>}</div>
    <h4>{t('输出')}</h4><code className="output-binding">{node.binding?node.binding+'.output':t('未绑定返回值')}</code>
    <div className="io-list">{outputs.map(e=><button key={e.parent+e.port} onClick={()=>onFocus(e.parent)}><span>→</span><code>{e.parent}.{e.port}</code></button>)}{emits.map((e,i)=><div className="emit-row" key={i}><span>→ emit</span><code>{e.name}</code><small>{e.kind}</small></div>)}</div>
    {!outputs.length&&!emits.length&&<p className="inspector-muted">{t('未被其他调用引用')}</p>}
    <h4>{t('调用参数')}</h4>{params.length?<dl>{params.map(([key,value])=><React.Fragment key={key}><dt>{key}</dt><dd><code>{typeof value==='string'?value:JSON.stringify(value)}</code></dd></React.Fragment>)}</dl>:<p className="inspector-muted">{t('文件未提供独立表达式参数。')}</p>}
    <details><summary>{t('目标与计划元数据')}</summary><pre>{JSON.stringify({target:node.target,...node.arguments},null,2)}</pre></details>
    <button className="source-button" onClick={()=>onSource(node)}>{t('查看 EAL 源码')}</button>
  </section>;
}
function MissionCanvas({model,onSource}) {
  const [direction,setDirection] = useState('BT');
  const [expanded,setExpanded] = useState(false);
  const [selected,setSelected] = useState(null);
  const [layout,setLayout] = useState({nodes:[],edges:[]});
  const [routing,setRouting] = useState(true);
  const [layoutError,setLayoutError] = useState('');
  const [nodes,setNodes,onNodesChange] = useNodesState([]);
  useEffect(()=>{
    let cancelled=false;setRouting(true);setLayoutError('');setNodes([]);setLayout({nodes:[],edges:[]});setSelected(null);
    layoutMission(model,direction).then(result=>{if(!cancelled){setLayout(result);setNodes(result.nodes);setRouting(false);}})
      .catch(error=>{if(!cancelled){setLayoutError(error.message);setRouting(false);}});
    return ()=>{cancelled=true;};
  },[model,direction,setNodes]);
  const {fitView,setCenter,zoomIn,zoomOut} = useReactFlow();
  const initialized = useNodesInitialized();

  useEffect(()=>{
    if(!initialized)return;
    const frame=requestAnimationFrame(()=>fitView(fitOptions));
    return ()=>cancelAnimationFrame(frame);
  },[initialized,layout,expanded,fitView]);
  useEffect(()=>{
    if(!expanded)return;
    const onKey=e=>{if(e.key==='Escape')setExpanded(false);};
    document.addEventListener('keydown',onKey);
    return ()=>document.removeEventListener('keydown',onKey);
  },[expanded]);
  const select = useCallback(id=>{
    setSelected(id);
    setNodes(current=>current.map(n=>({...n,selected:n.id===id})));
  },[setNodes]);
  const focus = id=>{select(id);const n=nodes.find(n=>n.id===id);if(n)setCenter(n.position.x+NODE_WIDTH/2,n.position.y+NODE_HEIGHT/2,{zoom:1,duration:200});};
  const selectedNode = model.nodes.find(n=>n.id===selected);
  const scope = useMemo(()=>dependencyScope(model,selected),[model,selected]);
  const displayNodes = useMemo(()=>nodes.map(node=>({...node,ariaLabel:t(node.data.label),style:{opacity:scope.has(node.id)?1:0.2}})),[nodes,scope]);
  const edges = useMemo(()=>layout.edges.map(edge=>{
    const active = !selected || (scope.has(edge.source)&&scope.has(edge.target));
    const direct = selected && (edge.source===selected||edge.target===selected);
    return {...edge, label:direct?`${edge.source}.output → ${edge.targetHandle}`:undefined,
      style:{stroke:direct?'#344b56':'#8a989e',strokeWidth:direct?1.65:1.15,opacity:active?1:0.12},
      markerEnd:{...edge.markerEnd,color:direct?'#344b56':'#8a989e'},
      labelStyle:{fill:'#202b30',fontSize:'var(--text-small)'},labelBgStyle:{fill:'#fff',fillOpacity:1},labelBgPadding:[6,4],
    };
  }),[layout,selected,scope]);
  return <div className={`mission-canvas ${expanded?'is-expanded':''}`}>
    <div className={`flow-workspace ${selectedNode?'has-inspector':''}`}><div className="flow-stage">
      <ReactFlow nodes={displayNodes} edges={edges} nodeTypes={nodeTypes} edgeTypes={edgeTypes} nodesDraggable={false} onNodesChange={onNodesChange}
        onNodeClick={(_,node)=>select(node.id)} onPaneClick={()=>select(null)}
        fitView fitViewOptions={fitOptions} minZoom={0.08} maxZoom={2.5}
        nodesConnectable={false} edgesReconnectable={false} deleteKeyCode={null}
        onNodesDelete={()=>{}} ariaLabelConfig={{'controls.zoomIn.ariaLabel':'放大','controls.zoomOut.ariaLabel':'缩小','controls.fitView.ariaLabel':'适配全图'}}>
        
      </ReactFlow>
      <div className="flow-legend" aria-label={t('图例')}><span className="relational">{t('结构化')}</span><span className="semantic">{t('语义')}</span><span className="input">{t('输入')}</span></div>
      <div className="flow-actions" role="toolbar" aria-label={t('画布操作')}>
        <ToolButton label={t('放大')} path="M12 5v14M5 12h14" onClick={()=>zoomIn()}/>
        <ToolButton label={t('缩小')} path="M5 12h14" onClick={()=>zoomOut()}/>
        <ToolButton label={t('适配全图')} path="M8 3H3v5m13-5h5v5M3 16v5h5m13-5v5h-5" onClick={()=>fitView(fitOptions)}/>
        <ToolButton label={direction==='BT'?'横向布局':'纵向布局'} path="M3 6h18m-4-4 4 4-4 4M21 18H3m4-4-4 4 4 4" onClick={()=>setDirection(d=>d==='BT'?'LR':'BT')}/>
        <ToolButton label={t('重置布局')} path="M20 7v5h-5M20 12a8 8 0 1 0-2 6" onClick={()=>{setNodes(layout.nodes);setSelected(null);requestAnimationFrame(()=>fitView(fitOptions));}}/>
        {selected&&<ToolButton label={t('聚焦输入输出')} path="M12 2v4m0 12v4M2 12h4m12 0h4M8 8h8v8H8z" onClick={()=>fitView({...fitOptions,nodes:nodes.filter(n=>n.id===selected||model.edges.some(e=>(e.parent===selected&&e.child===n.id)||(e.child===selected&&e.parent===n.id))),maxZoom:1})}/>}
        <ToolButton label={expanded?'收起画布':'展开画布'} path={expanded?'M3 8h5V3m13 5h-5V3M3 16h5v5m13-5h-5v5':'M3 9V3h6m6 0h6v6M3 15v6h6m6 0h6v-6'} pressed={expanded} onClick={()=>setExpanded(v=>!v)}/>
      </div>
      {(routing||layoutError||!model.nodes.length)&&<div className="flow-empty" role="status">{t(routing?'正在自动布线…':layoutError||'这个 mission 没有调用节点。')}</div>}
    </div>
      {selectedNode&&<Inspector node={selectedNode} model={model} onClose={()=>select(null)} onSource={onSource} onFocus={focus}/>}
    </div>

  </div>;
}

/** Single owner for the React root. The atlas disposes it before replacing its panel. */
export function mount(element, model, onSource) {
  const root = createRoot(element);
  root.render(<ReactFlowProvider><MissionCanvas model={model} onSource={onSource}/></ReactFlowProvider>);
  return ()=>root.unmount();
}
