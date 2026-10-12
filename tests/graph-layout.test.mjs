import {roundedRoute,cornerRadii,penRoute,samplePath,pathConflicts} from '../src/viewer/graph/path.mjs';
import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import {routingViolations} from './route-geometry.mjs';
import {layoutMission,dependencyScope,NODE_WIDTH,NODE_HEIGHT} from '../src/viewer/graph/layout.mjs';
const catalog=JSON.parse(fs.readFileSync(new URL('../assets/plans.json',import.meta.url)));
test('all catalog DAGs preserve node identity, port edges, and nonoverlapping layout',async()=>{
  for(const query of catalog.queries) for(const direction of ['BT','LR']) {
    const model=query.eal.snapshot.graph;
    const result=await layoutMission(model,direction);
    assert.equal(result.nodes.length,model.nodes.length,query.query_id);
    assert.deepEqual(routingViolations(result),[],`${query.query_id} ${direction}: route conflict`);
    const byId=new Map(result.nodes.map(n=>[n.id,n]));
    const curves=result.edges.map(e=>samplePath(e.data.path));
    for(let i=0;i<curves.length;i++)assert.equal(pathConflicts(curves[i],curves.filter((_,j)=>i!==j),result.nodes),false,`${query.query_id} ${direction}: curve conflict`);
    for(const [i,e] of result.edges.entries()) {
      assert.equal(e.source,model.edges[i].child);
      assert.equal(e.target,model.edges[i].parent);
      assert.equal(e.targetHandle,model.edges[i].port);
      for(const [id,handle,point] of [[e.source,e.sourceHandle,e.data.points[0]],[e.target,e.targetHandle,e.data.points.at(-1)]]){
        const n=byId.get(id),port=n.data.ports.find(p=>p.id===handle);
        assert.ok(Math.abs(n.position.x+port.x-point.x)<0.01);
        assert.ok(Math.abs(n.position.y+port.y-point.y)<0.01);
      }
      const from=byId.get(e.source).position,to=byId.get(e.target).position;
      assert.ok(direction==='BT'?from.y>to.y:from.x<to.x);
    }
    for(let i=0;i<result.nodes.length;i++) for(let j=i+1;j<result.nodes.length;j++) {
      const a=result.nodes[i].position,b=result.nodes[j].position;
      assert.ok(Math.abs(a.x-b.x)>=NODE_WIDTH||Math.abs(a.y-b.y)>=NODE_HEIGHT,`${query.query_id}: overlapping nodes`);
    }
  }
});
test('shared input remains one node and preserves both named ports',async()=>{
  const result=await layoutMission({nodes:[{id:'scan'},{id:'join'}],edges:[{child:'scan',parent:'join',port:'left'},{child:'scan',parent:'join',port:'right'}]});
  assert.equal(result.nodes.length,2);
  assert.equal(result.edges.length,2);
  assert.deepEqual(result.nodes.find(n=>n.id==='join').data.inputs.map(i=>i.port),['left','right']);
  assert.notEqual(result.edges[0].id,result.edges[1].id);
  assert.notEqual(result.edges[0].sourceHandle,result.edges[1].sourceHandle);
  assert.deepEqual(routingViolations(result),[]);
});

test('dependency emphasis excludes a sibling branch while retaining producers and consumers',()=>{
  const model={nodes:['a','b','c','root'].map(id=>({id})),edges:[{child:'a',parent:'b'},{child:'b',parent:'root'},{child:'c',parent:'root'}]};
  assert.deepEqual([...dependencyScope(model,'b')].sort(),['a','b','root']);
  assert.equal(dependencyScope(model,null).size,4);
});

test('curved routes retain endpoints, tangents and short-segment clearance',()=>{
  const path=roundedRoute([{x:0,y:0},{x:0,y:40},{x:40,y:40}]);
  assert.ok(path.startsWith('M 0 0 L 0 22 C 0 '));
  assert.ok(path.endsWith('18 40 L 40 40'));
  const short=roundedRoute([{x:0,y:0},{x:0,y:4},{x:4,y:4}]);
  assert.ok(short.startsWith('M 0 0 L 0 2.2 C 0 '));
  assert.ok(short.endsWith('1.8 4 L 4 4'));
  assert.equal(roundedRoute([{x:0,y:0},{x:0,y:0},{x:0,y:40}]),'M 0 0 L 0 40');
});

test('curvature contracts near another route or a node',()=>{
  const edge={id:'a',data:{points:[{x:0,y:0},{x:0,y:100},{x:100,y:100}]}};
  const neighbour={id:'b',data:{points:[{x:-10,y:0},{x:-10,y:150}]}};
  assert.equal(cornerRadii(edge,[edge],[])[1],32);
  assert.equal(cornerRadii(edge,[edge,neighbour],[])[1],4.5);
  assert.equal(cornerRadii(edge,[edge],[{position:{x:5,y:95},width:20,height:20}])[1],2.25);
});

test('pen connection uses one cubic with aligned departure and arrival handles',()=>{
  assert.equal(penRoute([{x:0,y:100},{x:100,y:0}],'BT'),'M 0 100 C 0 44.99999999999999 100 55.00000000000001 100 0');
  const samples=samplePath(penRoute([{x:0,y:100},{x:100,y:0}],'BT'));
  assert.deepEqual(samples[0],{x:0,y:100});
  assert.deepEqual(samples.at(-1),{x:100,y:0});
});
