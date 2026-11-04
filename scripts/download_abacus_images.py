"""Acquire selected MMQA image files from the official ZIP via HTTP ranges; verify CRCs."""
import io,json,urllib.request,zipfile,struct,zlib,concurrent.futures,time,hashlib
from pathlib import Path
root=Path(__file__).resolve().parents[1]
url='https://multimodalqa-images.s3-us-west-2.amazonaws.com/final_dataset_images/final_dataset_images.zip'
size=2362869144

def fetch(start,end):
 for attempt in range(5):
  try:
   req=urllib.request.Request(url,headers={'Range':f'bytes={start}-{end}'})
   with urllib.request.urlopen(req,timeout=90) as res:
    assert res.status==206
    return res.read()
  except Exception:
   if attempt==4:raise
   time.sleep(2**attempt)
class Remote(io.RawIOBase):
 def __init__(self):self.pos=0
 def seekable(self):return True
 def seek(self,offset,whence=0):
  self.pos=offset if whence==0 else self.pos+offset if whence==1 else size+offset
  return self.pos
 def tell(self):return self.pos
 def read(self,n=-1):
  n=size-self.pos if n<0 else min(n,size-self.pos)
  if not n:return b''
  data=fetch(self.pos,self.pos+n-1);self.pos+=len(data);return data
pools=json.loads((root/'environment/abacus/mmqa/pools.json').read_text())
ids={x for p in pools.values() for x in p['image']}
with zipfile.ZipFile(Remote()) as z:infos=z.infolist()
lookup={Path(i.filename).stem:i for i in infos if not i.is_dir()}
missing=ids-set(lookup);assert not missing,missing
out=root/'data/abacus/mmqa/images';out.mkdir(exist_ok=True)
def download(id):
 info=lookup[id];path=out/Path(info.filename).name
 if not path.exists() or path.stat().st_size!=info.file_size:
  data=fetch(info.header_offset,info.header_offset+30+len(info.filename.encode())+len(info.extra)+info.compress_size+65535-1)
  header=struct.unpack('<4s5H3I2H',data[:30]);start=30+header[-2]+header[-1];raw=data[start:start+info.compress_size]
  content=zlib.decompress(raw,-15) if info.compress_type==8 else raw
  assert len(content)==info.file_size and zlib.crc32(content)==info.CRC,id
  path.write_bytes(content)
 return dict(image_id=id,path=path.relative_to(root).as_posix(),bytes=path.stat().st_size,sha256=hashlib.sha256(path.read_bytes()).hexdigest(),archive_member=info.filename)
with concurrent.futures.ThreadPoolExecutor(max_workers=12) as pool:
 rows=[]
 for row in pool.map(download,sorted(ids)):
  rows.append(row)
  if len(rows)%50==0:print(len(rows),'/',len(ids),flush=True)
(root/'data/abacus/mmqa/image-manifest.json').write_text(json.dumps(dict(source_url=url,images=rows),indent=2)+'\n')
print('Downloaded and CRC-verified',len(rows),'images',flush=True)
