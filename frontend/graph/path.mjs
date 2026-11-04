const distanceToSegment = (p,a,b) => {
  const dx=b.x-a.x,dy=b.y-a.y,length=dx*dx+dy*dy;
  const t=length?Math.max(0,Math.min(1,((p.x-a.x)*dx+(p.y-a.y)*dy)/length)):0;
  return Math.hypot(p.x-a.x-t*dx,p.y-a.y-t*dy);
};

/** Each bend stays inside a clearance disk, never borrowing an adjacent route's lane. */
export function cornerRadii(edge,edges,nodes) {
  return edge.data.points.map((point,i,points)=>{
    if(!i||i===points.length-1)return 0;
    let clearance=Infinity;
    for(const other of edges)for(let j=1;j<other.data.points.length;j++){
      if(other.id===edge.id&&(j===i||j===i+1))continue;
      clearance=Math.min(clearance,distanceToSegment(point,other.data.points[j-1],other.data.points[j]));
    }
    for(const node of nodes){
      const x=Math.max(node.position.x,Math.min(point.x,node.position.x+node.width));
      const y=Math.max(node.position.y,Math.min(point.y,node.position.y+node.height));
      clearance=Math.min(clearance,Math.hypot(point.x-x,point.y-y));
    }
    return Math.min(32,clearance*.45);
  });
}

/** Cubic circular fillets: tangent-continuous joins and a straight lead into every port. */
export function roundedRoute(points, radius = 32) {
  if (!points.length) return '';
  let path = `M ${points[0].x} ${points[0].y}`;
  const k=0.5522847498;
  for(let i=1;i<points.length-1;i++) {
    const a=points[i-1],b=points[i],c=points[i+1];
    const incoming=Math.hypot(b.x-a.x,b.y-a.y),outgoing=Math.hypot(c.x-b.x,c.y-b.y);
    const r=Math.max(0,Math.min(Array.isArray(radius)?radius[i]:radius,incoming*.45,outgoing*.45));
    const cross=(b.x-a.x)*(c.y-b.y)-(b.y-a.y)*(c.x-b.x);
    if(!r||Math.abs(cross)<1e-8){if(incoming)path+=` L ${b.x} ${b.y}`;continue;}
    const ux=(b.x-a.x)/incoming,uy=(b.y-a.y)/incoming,vx=(c.x-b.x)/outgoing,vy=(c.y-b.y)/outgoing;
    const entry={x:b.x-ux*r,y:b.y-uy*r},exit={x:b.x+vx*r,y:b.y+vy*r};
    path+=` L ${entry.x} ${entry.y} C ${entry.x+ux*r*k} ${entry.y+uy*r*k} ${exit.x-vx*r*k} ${exit.y-vy*r*k} ${exit.x} ${exit.y}`;
  }
  if(points.length>1){const end=points.at(-1);path+=` L ${end.x} ${end.y}`;}
  return path;
}

/** Pen-tool style: two aligned handles, one uninterrupted cubic between ports. */
export function penRoute(points,direction) {
  const start=points[0],end=points.at(-1),horizontal=direction==='LR';
  const gap=Math.abs(horizontal?end.x-start.x:end.y-start.y);
  const handle=gap*.55;
  const a=horizontal?{x:start.x+handle,y:start.y}:{x:start.x,y:start.y-handle};
  const b=horizontal?{x:end.x-handle,y:end.y}:{x:end.x,y:end.y+handle};
  return `M ${start.x} ${start.y} C ${a.x} ${a.y} ${b.x} ${b.y} ${end.x} ${end.y}`;
}

export function samplePath(path) {
  const tokens=path.match(/[MLC]|-?\d+(?:\.\d+)?(?:e[+-]?\d+)?/gi)||[];
  const points=[];let cursor=0,last;
  const point=()=>({x:Number(tokens[cursor++]),y:Number(tokens[cursor++])});
  while(cursor<tokens.length){
    const command=tokens[cursor++];
    if(command==='M'||command==='L'){last=point();points.push(last);}
    else if(command==='C'){
      const a=last,b=point(),c=point(),d=point();
      for(let i=1;i<=64;i++){const t=i/64,u=1-t;points.push({x:u*u*u*a.x+3*u*u*t*b.x+3*u*t*t*c.x+t*t*t*d.x,y:u*u*u*a.y+3*u*u*t*b.y+3*u*t*t*c.y+t*t*t*d.y});}
      last=d;
    }
  }
  return points;
}
const cross=(a,b,c)=>(b.x-a.x)*(c.y-a.y)-(b.y-a.y)*(c.x-a.x);
function intersects(a,b,c,d) {
  if(Math.max(a.x,b.x)<Math.min(c.x,d.x)||Math.max(c.x,d.x)<Math.min(a.x,b.x)||Math.max(a.y,b.y)<Math.min(c.y,d.y)||Math.max(c.y,d.y)<Math.min(a.y,b.y))return false;
  return cross(a,b,c)*cross(a,b,d)<-1e-9&&cross(c,d,a)*cross(c,d,b)<-1e-9;
}
export function pathConflicts(points,otherPaths,nodes) {
  for(const node of nodes){
    const x=node.position.x+.1,y=node.position.y+.1,r=x+node.width-.2,b=y+node.height-.2;
    const rect=[{x,y},{x:r,y},{x:r,y:b},{x,y:b}];
    if(points.some(p=>p.x>x&&p.x<r&&p.y>y&&p.y<b))return true;
    for(let i=1;i<points.length;i++)for(let j=0;j<4;j++)if(intersects(points[i-1],points[i],rect[j],rect[(j+1)%4]))return true;
  }
  for(const other of otherPaths)for(let i=1;i<points.length;i++)for(let j=1;j<other.length;j++)if(intersects(points[i-1],points[i],other[j-1],other[j]))return true;
  return false;
}

/** Prefer a single curve; retain obstacle waypoints only when the direct corridor is blocked. */
export function routeCurves(edges,nodes,direction) {
  const paths=edges.map(edge=>roundedRoute(edge.data.points,edge.data.radii));
  const samples=paths.map(samplePath);
  for(let i=0;i<edges.length;i++){
    const candidate=penRoute(edges[i].data.points,direction),sample=samplePath(candidate);
    if(!pathConflicts(sample,samples.filter((_,j)=>j!==i),nodes)){paths[i]=candidate;samples[i]=sample;}
    edges[i].data.path=paths[i];
    const middle=samples[i][Math.floor(samples[i].length/2)];
    edges[i].data.labelPoint=middle;
  }
}
