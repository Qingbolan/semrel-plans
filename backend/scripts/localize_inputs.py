"""Materialize catalog input bindings inside data/ before preparing a portable release."""
import hashlib
import json
import shutil
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]

def destination(path):
    text=str(path)
    anchors=[('/Awesome-Dymatic-Operator/chat/benchmark/8-17 data agent query and data/data/','8-17'),('/semantic-workload-bench/data/','semantic-workload-bench')]
    for anchor,name in anchors:
        if anchor in text:return ROOT/'data/source-inputs'/name/text.split(anchor,1)[1]
    return ROOT/'data/source-inputs'/hashlib.sha256(text.encode()).hexdigest()[:12]/path.name

def main():
    contracts=[json.loads(line) for line in (ROOT/'query/input_contracts.jsonl').read_text().splitlines()]
    bindings=set()
    for contract in contracts:
        for row in contract['tables']+contract['environment']['resources']:
            if isinstance(row,dict) and isinstance(row.get('path'),str) and row['path'].startswith('/'):
                bindings.add(Path(row['path']))
    queries=[json.loads(line) for line in (ROOT/'query/queries.jsonl').read_text().splitlines()]
    environments=[ROOT/'environment'/identity/'manifest.json' for identity in sorted({q['environment_id'] for q in queries})]
    datasets={json.loads(path.read_text())['dataset_id'] for path in environments}
    manifests=environments+[ROOT/'data'/identity/'manifest.json' for identity in sorted(datasets)]
    for path in manifests:
        value=json.loads(path.read_text()).get('local_path')
        if isinstance(value,str) and value.startswith('/'):bindings.add(Path(value))
    roots=[]
    for path in sorted(bindings,key=lambda p:(len(p.parts),str(p))):
        if not any(path.is_relative_to(parent) for parent in roots):roots.append(path)
    mappings=[]
    for i,source in enumerate(roots,1):
        if not source.exists():raise ValueError(f'Missing external input: {source}')
        target=destination(source);target.parent.mkdir(parents=True,exist_ok=True)
        if source.is_dir():shutil.copytree(source,target,dirs_exist_ok=True)
        else:shutil.copy2(source,target)
        mappings.append({'source':str(source),'path':target.relative_to(ROOT).as_posix()})
        if i%10==0:print(f'Copied {i}/{len(roots)} input roots',flush=True)
    def rewrite(value):
        if isinstance(value,str) and value.startswith('/'):
            for row in mappings:
                if value==row['source'] or value.startswith(row['source']+'/'):
                    return row['path']+value[len(row['source']):]
        if isinstance(value,dict):return {key:rewrite(item) for key,item in value.items()}
        if isinstance(value,list):return list(map(rewrite,value))
        return value
    (ROOT/'query/input_contracts.jsonl').write_text(''.join(json.dumps(rewrite(row),ensure_ascii=False)+'\n' for row in contracts))
    for path in manifests:
        data=json.loads(path.read_text());updated=rewrite(data)
        if updated!=data:
            if updated.get('availability')=='local_external':updated['availability']='local_files'
            path.write_text(json.dumps(updated,ensure_ascii=False,indent=2)+'\n')
    receipt=ROOT/'exports/input-relocations.json'
    previous=json.loads(receipt.read_text()) if receipt.exists() else []
    receipt.write_text(json.dumps(previous+mappings,ensure_ascii=False,indent=2)+'\n')
    print(f'Localized {len(mappings)} roots; original query texts and supplied task JSON remain unchanged',flush=True)

if __name__=='__main__':main()
