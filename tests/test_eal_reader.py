import json
from pathlib import Path
import shutil
import sys
import tempfile
import threading
import unittest
from urllib.error import HTTPError
from urllib.request import Request, urlopen
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'src'))
from eal_reader import EalCompiler, CompileError
from server import AtlasServer


@unittest.skipUnless(shutil.which('easynet'), 'EasyNet compiler not installed')
class ReaderTest(unittest.TestCase):
    def test_graph_preserves_shared_node_and_ports(self):
        source = '''mission "shared" {
          let a = call "scan" on "worker" with { label = "source" }
          let b = call "join" on "worker" with { left = a.output, right = a.output }
        }'''
        result = EalCompiler().compile(source)
        self.assertEqual(result['source'], source)
        self.assertEqual(len(result['graph']['nodes']), 2)
        edges = result['graph']['edges']
        self.assertEqual({e['port'] for e in edges}, {'left', 'right'})
        self.assertEqual(edges[0]['child'], edges[1]['child'])

    def test_invalid_eal_reports_compiler_error(self):
        with self.assertRaises(CompileError):
            EalCompiler().compile('mission "broken" { let')

    def test_limits_and_missing_compiler(self):
        for value in ('', 10, 'a' * (1024 * 1024 + 1)):
            with self.assertRaises(CompileError):
                EalCompiler().compile(value)
        with self.assertRaisesRegex(CompileError, '无法启动'):
            EalCompiler('/nonexistent/semrel-test-easynet').compile('mission "x" {}')

    def test_live_reload_import_and_error_recovery(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / 'exports/eal').mkdir(parents=True)
            path = root / 'exports/eal/one.eal'
            manifest = [{'query_id': 'one', 'path': 'exports/eal/one.eal'}]
            (root / 'exports/eal/manifest.json').write_text(json.dumps(manifest))
            source = 'mission "first" { let x = call "scan" on "worker" with { label = "old" } }'
            path.write_text(source)
            server = AtlasServer(('127.0.0.1', 0), root)
            thread = threading.Thread(target=server.serve_forever, daemon=True)
            thread.start()
            base = f'http://127.0.0.1:{server.server_port}'
            try:
                def get():
                    with urlopen(base + '/api/plan?query_id=one') as response:
                        return json.load(response)
                self.assertEqual(get()['graph']['nodes'][0]['label'], 'old')
                path.write_text(source.replace('old', 'new'))
                self.assertEqual(get()['graph']['nodes'][0]['label'], 'new')
                path.write_text('invalid')
                with self.assertRaises(HTTPError) as error:
                    get()
                self.assertEqual(error.exception.code, 422)
                self.assertEqual(json.load(error.exception)['source'], 'invalid')
                error.exception.close()
                path.write_text(source)
                self.assertEqual(get()['graph']['name'], 'first')
                request = Request(base + '/api/compile', data=json.dumps({'source': source}).encode(), headers={'Content-Type': 'application/json'})
                with urlopen(request) as response:
                    self.assertEqual(json.load(response)['graph']['name'], 'first')
                request.add_header('Origin', 'https://unrelated.example')
                with self.assertRaises(HTTPError) as error:
                    urlopen(request)
                self.assertEqual(error.exception.code, 403)
                error.exception.close()
                with self.assertRaises(HTTPError) as error:
                    urlopen(base + '/api/plan?query_id=../../etc/passwd')
                self.assertEqual(error.exception.code, 404)
                error.exception.close()
            finally:
                server.shutdown()
                server.server_close()
                thread.join()
