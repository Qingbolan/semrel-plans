"""Build a portable site archive and a minimal deployment context; no external paths."""
import argparse
import hashlib
import json
import shutil
import sys
import tarfile
from datetime import datetime, timezone
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'backend' / 'atlas'))
from hosting import HostingPolicy


def digest(path):
    result = hashlib.sha256()
    with path.open('rb') as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b''):
            result.update(chunk)
    return result.hexdigest()

STATIC_GUIDE = '''# SemRel 图册：静态部署

{queries} 条查询，{files} 个站点文件，约 {gib:.1f} GiB。全部为静态文件，服务器只需要 nginx（无 Python、无 Docker、无后端进程）。

1. 上传本目录到服务器，例如 `/srv/semrel/package`。
2. 解包：`sudo mkdir -p /srv/semrel/site && sudo tar -xf site.tar -C /srv/semrel/site`
3. 配置：`sudo cp deploy/nginx-static.conf /etc/nginx/conf.d/semrel.conf`，改 `server_name` 和 `root`。
4. 检查并生效：`sudo nginx -t && sudo systemctl reload nginx`；HTTPS 可用 `sudo certbot --nginx -d 你的域名`。
5. 验收：打开首页，任选几条查询查看“逻辑计划 / 原始 JSON / 环境与输入”，再打开一篇论文。

更新：在开发机 `npm run build` 后重新打包，把新的 site.tar 解到新目录，再把 nginx 的 root 切过去（旧目录保留即可回滚）。
页面里的“打开 .eal”导入需要本机编译服务，静态部署中不可用；其余功能均可用。
'''


class ReleaseBuilder:
    def __init__(self, root, checksums=True, static=False, exclude=()):
        self.root = root.resolve()
        self.exclude = tuple(exclude)
        self.checksums = checksums
        self.static = static
        self.policy = HostingPolicy(self.root, 8765)

    def inventory(self):
        # Archive paths are URL paths, so the release is a flat site: frontend from dist/, data roots beside it.
        self.sources = {}
        rows = []
        for url, path in self.policy.published():
            if url.startswith(self.exclude):
                continue
            self.sources[url] = path
            rows.append({'path': url, 'bytes': path.stat().st_size, **({'sha256': digest(path)} if self.checksums else {})})
        return rows

    @staticmethod
    def public_metadata(info):
        info.mode = 0o644
        info.uid = info.gid = 0
        info.uname = info.gname = ''
        return info

    def prepare(self, output):
        if output.exists():
            raise ValueError('Choose a new output directory; existing releases are immutable')
        contracts = [json.loads(line) for line in (self.root / 'catalog/input_contracts.jsonl').read_text().splitlines()]
        for contract in contracts:
            for binding in contract['tables'] + contract['environment']['resources']:
                path = (binding.get('path') or '') if isinstance(binding, dict) else ''
                if path.startswith('/'):
                    raise ValueError('Run backend/scripts/vendor_upstream.py first: ' + path)
                if path and '://' not in path and not (self.root / path).exists():
                    raise ValueError('Missing input binding: ' + path)
        output.mkdir(parents=True)
        rows = self.inventory()
        published = {row['path'] for row in rows}
        catalog = json.loads(self.policy.locate('assets/plans.json').read_text())
        required = {'index.html', 'migration.html', 'assets/plans.js', 'exports/eal/manifest.json'}
        required.update(q['task_path'] for q in catalog['queries'])
        required.update(row['path'] for row in json.loads((self.root / 'exports/eal/manifest.json').read_text()))
        missing = sorted(r for r in required - published if not r.startswith(self.exclude))
        if missing:
            raise ValueError(f'Missing required release files: {missing[:20]}')
        manifest = {'schema_version': 1, 'created_at': datetime.now(timezone.utc).isoformat(), 'query_count': catalog['count'], 'total_bytes': sum(r['bytes'] for r in rows), 'files': rows}
        (output / 'release-manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
        with tarfile.open(output / 'site.tar.partial', 'w') as archive:
            for row in rows:
                archive.add(self.sources[row['path']], arcname=row['path'], recursive=False, filter=self.public_metadata)
            archive.add(output / 'release-manifest.json', arcname='release-manifest.json', filter=self.public_metadata)
        (output / 'site.tar.partial').rename(output / 'site.tar')
        # Keep application code separate from the public website mount.
        runtime = ['.dockerignore', 'backend/scripts/serve.py', 'backend/scripts/verify_release.py', 'backend/atlas/server.py', 'backend/atlas/hosting.py', 'backend/atlas/plan_store.py', 'backend/atlas/eal_reader.py', 'backend/atlas/eal_strings.py', 'deploy/Dockerfile', 'deploy/compose.yaml', 'deploy/.env.example', 'deploy/nginx.conf.example', 'docs/deployment.md']
        if self.static:
            runtime = ['deploy/nginx-static.conf']
            (output / 'DEPLOY.md').write_text(STATIC_GUIDE.format(queries=catalog['count'], files=len(rows), gib=manifest['total_bytes'] / 2**30))
        for name in runtime:
            target = output / name
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(self.root / name, target)
        if not self.static:
            (output / 'deploy/bin').mkdir(exist_ok=True)
        checksum = digest(output / 'site.tar') if self.checksums else None
        if checksum:
            (output / 'SHA256SUMS').write_text(f'{checksum}  site.tar\n')
        print(json.dumps({'release': str(output), 'files': len(rows), 'queries': catalog['count'], 'bytes': manifest['total_bytes'], 'archive_sha256': checksum}))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', required=True, type=Path)
    parser.add_argument('--no-checksums', action='store_true', help='skip SHA256 of every file and of site.tar (much faster)')
    parser.add_argument('--static', action='store_true', help='package for plain nginx hosting (no application server)')
    parser.add_argument('--exclude', action='append', default=[], help='URL path prefix to leave out, e.g. data/source-inputs/ (repeatable)')
    args = parser.parse_args()
    ReleaseBuilder(ROOT, checksums=not args.no_checksums, static=args.static, exclude=args.exclude).prepare(args.output.resolve())
