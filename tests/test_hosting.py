import json
from pathlib import Path
import sys
import tempfile
import threading
import unittest
from urllib.request import Request, urlopen
from urllib.error import HTTPError
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from hosting import HostingPolicy
from server import AtlasServer

class Compiler:
    def compile(self, source): return {'source': source, 'graph': {'nodes': [{'id':'one'}]}, 'ir': {}}

class HostingTest(unittest.TestCase):
    def test_explicit_origins(self):
        p=HostingPolicy(Path('/tmp/site'),8765,['https://atlas.example.com'])
        self.assertTrue(p.permits_request('atlas.example.com','https://atlas.example.com'))
        self.assertFalse(p.permits_request('atlas.example.com','https://evil.example'))
        self.assertFalse(p.permits_request('evil.example'))
        self.assertFalse(p.permits_request('localhost:8765','https://atlas.example.com'))
        with self.assertRaises(ValueError):HostingPolicy(Path('/tmp'),8765,['https://atlas.example.com/path'])

    def test_public_surface_and_compilation(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);(root/'exports/eal').mkdir(parents=True)
            (root/'index.html').write_text('atlas')
            (root/'.env').write_text('private')
            (root/'exports/eal/one.eal').write_text('mission')
            (root/'exports/eal/manifest.json').write_text(json.dumps([{'query_id':'one','path':'exports/eal/one.eal'}]))
            (root/'assets').mkdir();(root/'assets/plans.js').write_text('window.SEMREL_PLANS = [];');(root/'assets/escape').symlink_to(root/'.env')
            server=AtlasServer(('127.0.0.1',0),root,Compiler(),['https://atlas.example.com'])
            thread=threading.Thread(target=server.serve_forever,daemon=True);thread.start()
            def request(path,origin=None):
                headers={'Host':'atlas.example.com'}
                if origin:headers['Origin']=origin
                return urlopen(Request(f'http://127.0.0.1:{server.server_port}'+path,headers=headers))
            try:
                for path in ['/','/api/health','/api/plan?query_id=one']:
                    with request(path,'https://atlas.example.com') as response:self.assertEqual(response.status,200)
                for path in ['/.env','/assets/escape','/src/server.py','/deploy/.env','/assets/']:
                    with self.assertRaises(HTTPError) as caught:request(path)
                    self.assertIn(caught.exception.code,[403,404]);caught.exception.close()
                with self.assertRaises(HTTPError) as caught:request('/api/plan?query_id=one','https://evil.example')
                self.assertEqual(caught.exception.code,403);caught.exception.close()
            finally:server.shutdown();server.server_close();thread.join()

if __name__=='__main__':unittest.main()
