const EPS=0.01;
const between=(v,a,b)=>v>Math.min(a,b)+EPS&&v<Math.max(a,b)-EPS;
export function routingViolations(result) {
  const segments=result.edges.flatMap(edge=>edge.data.points.slice(1).map((p,i)=>({a:edge.data.points[i],b:p,edge:edge.id})));
  const issues=[];
  for(const s of segments){
    const horizontal=Math.abs(s.a.y-s.b.y)<EPS;
    if(!horizontal&&Math.abs(s.a.x-s.b.x)>EPS)issues.push('non-orthogonal');
    for(const node of result.nodes){
      const x=node.position.x,y=node.position.y,w=node.width,h=node.height;
      if(horizontal?between(s.a.y,y,y+h)&&Math.min(s.a.x,s.b.x)<x+w-EPS&&Math.max(s.a.x,s.b.x)>x+EPS:
        between(s.a.x,x,x+w)&&Math.min(s.a.y,s.b.y)<y+h-EPS&&Math.max(s.a.y,s.b.y)>y+EPS)issues.push('node-intersection');
    }
  }
  for(let i=0;i<segments.length;i++)for(let j=i+1;j<segments.length;j++){
    const a=segments[i],b=segments[j];if(a.edge===b.edge)continue;
    const ah=Math.abs(a.a.y-a.b.y)<EPS,bh=Math.abs(b.a.y-b.b.y)<EPS;
    if(ah!==bh){const h=ah?a:b,v=ah?b:a;if(between(v.a.x,h.a.x,h.b.x)&&between(h.a.y,v.a.y,v.b.y))issues.push('crossing');}
    else {const axis=ah?'x':'y',fixed=ah?'y':'x';if(Math.abs(a.a[fixed]-b.a[fixed])<EPS&&Math.min(Math.max(a.a[axis],a.b[axis]),Math.max(b.a[axis],b.b[axis]))-Math.max(Math.min(a.a[axis],a.b[axis]),Math.min(b.a[axis],b.b[axis]))>EPS)issues.push('overlap');}
  }
  return issues;
}
