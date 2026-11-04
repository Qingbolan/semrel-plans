"""Atlas file server with explicit public origins and compile-only EAL endpoints."""
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import json
import html
import io
from pathlib import Path
import threading
from urllib.parse import parse_qs, urlsplit, quote
from hosting import HostingPolicy
from plan_store import PlanStore, PlanReadError
from eal_reader import EalCompiler, CompileError, MAX_SOURCE_BYTES


class AtlasServer(ThreadingHTTPServer):
    daemon_threads = True

    def __init__(self, address, root, compiler=None, public_origins=()):
        self.root = Path(root).resolve()
        self.compiler = compiler or EalCompiler()
        self.compile_slots = threading.BoundedSemaphore(2)
        self.plans = PlanStore(self.root)
        super().__init__(address, partial(AtlasHandler, directory=str(self.root)))
        self.hosting = HostingPolicy(self.root, self.server_port, public_origins)


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
            return self.respond(503, {'error': '编译器忙，请稍后重新加载。', 'source': source, 'error_kind': 'busy'})
        try:
            self.respond(200, self.server.compiler.compile(source))
        except CompileError as exc:
            self.respond(422, {'error': str(exc), 'source': source, 'error_kind': 'compile'})
        finally:
            self.server.compile_slots.release()

    def permitted_request(self):
        return self.server.hosting.permits_request(self.headers.get('Host', ''), self.headers.get('Origin'))

    def list_directory(self, path):
        directory = Path(path)
        relative = directory.relative_to(self.server.root)
        if not relative.parts or relative.parts[0] not in {'data', 'environment', 'query', 'exports'}:
            self.send_error(404, 'Directory listing is disabled')
            return None
        links = []
        for child in sorted(directory.iterdir()):
            if not self.server.hosting.permits_file(child):
                continue
            name = child.name + ('/' if child.is_dir() else '')
            links.append(f'<li><a href="{quote(name)}">{html.escape(name)}</a></li>')
        title = html.escape(relative.as_posix())
        payload = (f'<!doctype html><meta charset="utf-8"><title>{title}</title>'
                   f'<h1>{title}</h1><ul>{"".join(links)}</ul>').encode()
        self.send_response(200)
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        self.send_header('Content-Length', str(len(payload)))
        self.end_headers()
        return io.BytesIO(payload)

    def translate_path(self, path):
        # The base class normalises the URL (.., %-escapes) against the repository root; map it to the publishing file.
        relative = Path(super().translate_path(path)).relative_to(self.server.root).as_posix()
        self.url_relative = '' if relative == '.' else relative
        return str(self.server.hosting.locate(self.url_relative))

    def send_head(self):
        path = Path(self.translate_path(self.path))
        if path.is_dir() and not self.url_relative:
            path = path / 'index.html'
        published = self.server.hosting.url_path(path)
        if not self.permitted_request() or published is None or published.strip('/') != (self.url_relative.strip('/') or 'index.html'):
            self.send_error(403, 'Not a published resource')
            return None
        return super().send_head()

    def do_GET(self):
        url = urlsplit(self.path)
        if url.path == '/api/health':
            if not self.permitted_request():
                return self.respond(403, {'error': 'Origin is not configured'})
            # Catalog plans ship as build-time snapshots, so a missing compiler only disables EAL import.
            hosting = self.server.hosting
            ready = hosting.locate('index.html').is_file() and hosting.locate('assets/plans.js').is_file()
            return self.respond(200 if ready else 503, {'status': 'ready' if ready else 'missing_catalog',
                                                        'eal_import': bool(getattr(self.server.compiler, 'executable', True))})
        if url.path != '/api/plan':
            return super().do_GET()
        if not self.permitted_request():
            return self.respond(403, {'error': '请求域名或 Origin 未配置。'})
        query_id = parse_qs(url.query).get('query_id', [''])[0]
        try:
            path = self.server.plans.resolve(query_id)
        except PlanReadError as exc:
            return self.respond(exc.status, {'error': str(exc), 'error_kind': exc.kind})
        try:
            if path.stat().st_size > MAX_SOURCE_BYTES:
                raise CompileError('EAL 文件不能超过 1 MiB。')
            source = path.read_text(encoding='utf-8')
        except (OSError, UnicodeError, CompileError) as exc:
            return self.respond(422, {'error': f'无法读取 EAL：{exc}', 'error_kind': 'file'})
        self.compile_source(source)

    def do_POST(self):
        if self.path != '/api/compile':
            return self.respond(404, {'error': '未知接口。'})
        if not self.permitted_request():
            return self.respond(403, {'error': '请求域名或 Origin 未配置。'})
        try:
            length = int(self.headers.get('Content-Length', '0'))
            if not 0 < length <= MAX_SOURCE_BYTES * 2:
                return self.respond(413, {'error': '请求大小无效或超过限制。'})
            payload = json.loads(self.rfile.read(length))
            source = payload['source']
        except (ValueError, KeyError, TypeError):
            return self.respond(400, {'error': '请求必须包含 EAL source 字符串。'})
        self.compile_source(source)
