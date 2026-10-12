import ELK from 'elkjs/lib/elk.bundled.js';
import {cornerRadii,routeCurves} from './path.mjs';

export const NODE_WIDTH = 220;
export const NODE_HEIGHT = 104;
const elk = new ELK();

/** Ports, node order and orthogonal paths are laid out together by one routing owner. */
export async function layoutMission(model, direction = 'BT') {
  const horizontal = direction === 'LR';
  const nodeIds = new Set(model.nodes.map(n=>n.id));
  const edges = model.edges.map((edge,i)=>{
    if(!nodeIds.has(edge.child)||!nodeIds.has(edge.parent)) throw new Error('Mission IR contains a dangling input');
    return {id:`edge-${i}`,source:edge.child,target:edge.parent,sourceHandle:`output-${i}`,targetHandle:edge.port,
      type:'routed',markerEnd:{type:'arrowclosed',width:10,height:10},data:{port:edge.port}};
  });
  const portId = (node,handle)=>JSON.stringify([node,handle]);
  const children = model.nodes.map(node=>{
    const inputs = edges.filter(e=>e.target===node.id);
    const outputs = edges.filter(e=>e.source===node.id);
    return {id:node.id,width:NODE_WIDTH,height:Math.max(NODE_HEIGHT,32*(Math.max(inputs.length,outputs.length)+1)),
      layoutOptions:{'elk.portConstraints':'FIXED_SIDE'},
      ports:[...inputs.map(e=>({id:portId(node.id,e.targetHandle),width:0,height:0,layoutOptions:{'elk.port.side':horizontal?'WEST':'SOUTH'}})),
        ...outputs.map(e=>({id:portId(node.id,e.sourceHandle),width:0,height:0,layoutOptions:{'elk.port.side':horizontal?'EAST':'NORTH'}}))]};
  });
  const result = await elk.layout({id:'mission',layoutOptions:{
    'elk.algorithm':'layered','elk.direction':horizontal?'RIGHT':'UP','elk.edgeRouting':'ORTHOGONAL',
    'elk.layered.crossingMinimization.strategy':'LAYER_SWEEP','elk.layered.thoroughness':'30',
    'elk.spacing.nodeNode':'60','elk.layered.spacing.nodeNodeBetweenLayers':'110',
    'elk.spacing.edgeEdge':'20','elk.layered.spacing.edgeEdgeBetweenLayers':'20','elk.spacing.edgeNode':'24',
    'elk.layered.mergeEdges':'false','elk.padding':'[top=30,left=30,bottom=30,right=30]'
  },children,edges:edges.map(e=>({id:e.id,sources:[portId(e.source,e.sourceHandle)],targets:[portId(e.target,e.targetHandle)]}))});
  const nodes = result.children.map(layout=>{
    const node=model.nodes.find(n=>n.id===layout.id);
    const ports=layout.ports.map(port=>{const [,handle]=JSON.parse(port.id);return {id:handle,x:port.x,y:port.y,type:handle.startsWith('output-')?'source':'target'};});
    return {id:node.id,type:'operator',position:{x:layout.x,y:layout.y},width:layout.width,height:layout.height,
      data:{...node,direction,height:layout.height,ports,inputs:model.edges.filter(e=>e.parent===node.id).map(e=>({port:e.port,source:e.child}))}};
  });
  for(const edge of edges){
    const routed=result.edges.find(e=>e.id===edge.id);
    if(routed.sections?.length!==1) throw new Error('Unable to produce an unambiguous route');
    const section=routed.sections[0];
    edge.data.points=[section.startPoint,...(section.bendPoints||[]),section.endPoint];
  }
  for(const edge of edges) edge.data.radii=cornerRadii(edge,edges,nodes);
  routeCurves(edges,nodes,direction);
  return {nodes,edges};
}

/** All producers and consumers reachable from a selected call, without unrelated siblings. */
export function dependencyScope(model, selected) {
  const ids = new Set(selected ? [selected] : model.nodes.map(n => n.id));
  if (!selected) return ids;
  for (const upstream of [true, false]) {
    const queue = [selected], visited = new Set(queue);
    while (queue.length) {
      const id = queue.pop();
      for (const edge of model.edges) {
        const from = upstream ? edge.parent : edge.child;
        const to = upstream ? edge.child : edge.parent;
        if (from === id && !visited.has(to)) {visited.add(to);ids.add(to);queue.push(to);}
      }
    }
  }
  return ids;
}
