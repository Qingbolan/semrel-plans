"""Loopback atlas server with a compile-only EAL endpoint."""
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import json
from pathlib import Path
import threading
from urllib.parse import parse_qs, urlsplit
from eal_reader import EalCompiler, CompileError, MAX_SOURCE_BYTES


class AtlasServer(ThreadingHTTPServer):
    daemon_threads = True

    def __init__(self, address, root, compiler=None):
        self.root = Path(root).resolve()
        self.compiler = compiler or EalCompiler()
        self.compile_slots = threading.BoundedSemaphore(2)
        manifest = json.loads((self.root / 'exports/eal/manifest.json').read_text())
        self.paths = {e['query_id']: e['path'] for e in manifest}
        super().__init__(address, partial(AtlasHandler, directory=str(self.root)))


class AtlasHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store')
        self.send_header('X-Content-Type-Options', 'nosniff')
        super().end_headers()

    def respond(self, status, value):
        payload = json.dumps(value, ensure_ascii=False).encode()
        self.send_response(status)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Content-Length', str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

    def compile_source(self, source):
        if not self.server.compile_slots.acquire(blocking=False):
            return self.respond(503, {'error': '编译器忙，请稍后重新加载。', 'source': source})
        try:
            self.respond(200, self.server.compiler.compile(source))
        except CompileError as exc:
            self.respond(422, {'error': str(exc), 'source': source})
        finally:
            self.server.compile_slots.release()

    def local_request(self):
        host = self.headers.get('Host', '')
        allowed = {f'127.0.0.1:{self.server.server_port}', f'localhost:{self.server.server_port}'}
        return host in allowed and self.headers.get('Origin', f'http://{host}') == f'http://{host}'

    def do_GET(self):
        url = urlsplit(self.path)
        if url.path != '/api/plan':
            return super().do_GET()
        if not self.local_request():
            return self.respond(403, {'error': '仅支持本地图册请求。'})
        query_id = parse_qs(url.query).get('query_id', [''])[0]
        relative = self.server.paths.get(query_id)
        if relative is None:
            return self.respond(404, {'error': '查询不在 EAL 清单中。'})
        path = (self.server.root / relative).resolve()
        if not path.is_relative_to(self.server.root / 'exports/eal'):
            return self.respond(400, {'error': '无效 EAL 路径。'})
        try:
            if path.stat().st_size > MAX_SOURCE_BYTES:
                raise CompileError('EAL 文件不能超过 1 MiB。')
            source = path.read_text(encoding='utf-8')
        except (OSError, UnicodeError, CompileError) as exc:
            return self.respond(422, {'error': f'无法读取 EAL：{exc}'})
        self.compile_source(source)

    def do_POST(self):
        if self.path != '/api/compile':
            return self.respond(404, {'error': '未知接口。'})
        if not self.local_request():
            return self.respond(403, {'error': '仅支持本地图册请求。'})
        try:
            length = int(self.headers.get('Content-Length', '0'))
            if not 0 < length <= MAX_SOURCE_BYTES * 2:
                return self.respond(413, {'error': '请求大小无效或超过限制。'})
            payload = json.loads(self.rfile.read(length))
            source = payload['source']
        except (ValueError, KeyError, TypeError):
            return self.respond(400, {'error': '请求必须包含 EAL source 字符串。'})
        self.compile_source(source)
