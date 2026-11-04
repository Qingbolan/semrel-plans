"""Explicit public origins and published-file boundary for local and hosted atlases."""
from pathlib import Path
from urllib.parse import urlsplit

PUBLIC_ROOTS = ('assets', 'data', 'environment', 'exports', 'files', 'query', 'research', 'docs', 'Survey', 'src/viewer')
PUBLIC_FILES = ('index.html', 'migration.html')

class HostingPolicy:
    def __init__(self, root, port, origins=()):
        self.root = Path(root).resolve()
        self.origins = {f'http://127.0.0.1:{port}', f'http://localhost:{port}'}
        for origin in origins:
            parsed = urlsplit(origin)
            if parsed.scheme not in ('http', 'https') or not parsed.hostname or parsed.username or parsed.password or parsed.path or parsed.query or parsed.fragment:
                raise ValueError('Public origins must be exact http(s) origins without a path or trailing slash')
            self.origins.add(origin)
        self.hosts = {urlsplit(origin).netloc for origin in self.origins}

    def permits_request(self, host, origin=None):
        return host in self.hosts and (origin is None or (origin in self.origins and urlsplit(origin).netloc == host))

    def permits_file(self, path):
        path = Path(path).resolve()
        if not path.is_relative_to(self.root):
            return False
        relative = path.relative_to(self.root)
        if any(part.startswith('.') and part not in ('.chroma-biodex', '.chroma-mmqa') for part in relative.parts):
            return False
        return relative.as_posix() in PUBLIC_FILES or any(path.is_relative_to(self.root / folder) for folder in PUBLIC_ROOTS)
