"""Explicit public origins and published-file boundary for local and hosted atlases.

URL layout: the built frontend (index.html, migration.html, assets/, viewer/) and the data roots are published side by side.
In the repository the frontend lives in dist/ and data roots at the top level; a release archive is flat (no dist/).
"""
from pathlib import Path, PurePosixPath
from urllib.parse import urlsplit

FRONTEND_FILES = ('index.html', 'migration.html')
FRONTEND_ROOTS = ('assets', 'viewer')
DATA_ROOTS = ('data', 'environment', 'exports', 'files', 'query', 'research', 'docs', 'Survey')
PUBLIC_FILES = FRONTEND_FILES
PUBLIC_ROOTS = FRONTEND_ROOTS + DATA_ROOTS
HIDDEN_ALLOWED = ('.chroma-biodex', '.chroma-mmqa')


class HostingPolicy:
    def __init__(self, root, port, origins=()):
        self.root = Path(root).resolve()
        self.site = self.root / 'dist' if (self.root / 'dist').is_dir() else self.root
        self.origins = {f'http://127.0.0.1:{port}', f'http://localhost:{port}'}
        for origin in origins:
            parsed = urlsplit(origin)
            if parsed.scheme not in ('http', 'https') or not parsed.hostname or parsed.username or parsed.password or parsed.path or parsed.query or parsed.fragment:
                raise ValueError('Public origins must be exact http(s) origins without a path or trailing slash')
            self.origins.add(origin)
        self.hosts = {urlsplit(origin).netloc for origin in self.origins}

    def permits_request(self, host, origin=None):
        return host in self.hosts and (origin is None or (origin in self.origins and urlsplit(origin).netloc == host))

    @staticmethod
    def frontend(relative):
        parts = PurePosixPath(relative).parts
        return relative in FRONTEND_FILES or bool(parts) and parts[0] in FRONTEND_ROOTS

    def locate(self, relative):
        """Map a URL path (relative, normalised) to the file that publishes it."""
        relative = relative.strip('/') or 'index.html'
        return (self.site if self.frontend(relative) else self.root) / relative

    def url_path(self, path):
        """Inverse of locate for a published file, or None when the file is not published."""
        path = Path(path).resolve()
        for base in dict.fromkeys((self.site, self.root)):
            if not path.is_relative_to(base):
                continue
            relative = path.relative_to(base)
            if any(part.startswith('.') and part not in HIDDEN_ALLOWED for part in relative.parts):
                return None
            text = relative.as_posix()
            if base == self.site and self.frontend(text):
                return text
            if base == self.root and relative.parts and relative.parts[0] in DATA_ROOTS:
                return text
        return None

    def permits_file(self, path):
        return self.url_path(path) is not None

    def published(self):
        """Every published file as (url_path, filesystem path)."""
        candidates = [self.site / name for name in FRONTEND_FILES]
        candidates += [p for name in FRONTEND_ROOTS for p in (self.site / name).rglob('*')]
        candidates += [p for name in DATA_ROOTS for p in (self.root / name).rglob('*')]
        for path in sorted(set(candidates)):
            if path.is_symlink():
                raise ValueError(f'Symlink must be materialized before release: {path}')
            url = self.url_path(path) if path.is_file() else None
            if url:
                yield url, path
