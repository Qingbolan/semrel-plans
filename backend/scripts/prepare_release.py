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
from hosting import HostingPolicy, PUBLIC_ROOTS, PUBLIC_FILES


def digest(path):
    result = hashlib.sha256()
    with path.open('rb') as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b''):
            result.update(chunk)
    return result.hexdigest()

class ReleaseBuilder:
    def __init__(self, root):
        self.root = root.resolve()
        self.policy = HostingPolicy(self.root, 8765)

    def inventory(self):
        candidates = [self.root / name for name in PUBLIC_FILES]
        for directory in PUBLIC_ROOTS:
            candidates.extend((self.root / directory).rglob('*'))
        rows = []
        for path in sorted(set(candidates)):
            if path.is_symlink():
                raise ValueError(f'Symlink must be materialized before release: {path}')
            if path.is_file() and self.policy.permits_file(path):
                rows.append({'path': path.relative_to(self.root).as_posix(), 'bytes': path.stat().st_size, 'sha256': digest(path)})
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
        contracts = [json.loads(line) for line in (self.root / 'query/input_contracts.jsonl').read_text().splitlines()]
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
        catalog = json.loads((self.root / 'assets/plans.json').read_text())
        required = {'index.html', 'migration.html', 'assets/plans.js', 'exports/eal/manifest.json'}
        required.update(q['task_path'] for q in catalog['queries'])
        required.update(row['path'] for row in json.loads((self.root / 'exports/eal/manifest.json').read_text()))
        missing = sorted(required - published)
        if missing:
            raise ValueError(f'Missing required release files: {missing[:20]}')
        manifest = {'schema_version': 1, 'created_at': datetime.now(timezone.utc).isoformat(), 'query_count': catalog['count'], 'total_bytes': sum(r['bytes'] for r in rows), 'files': rows}
        (output / 'release-manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
        with tarfile.open(output / 'site.tar.partial', 'w') as archive:
            for row in rows:
                archive.add(self.root / row['path'], arcname=row['path'], recursive=False, filter=self.public_metadata)
            archive.add(output / 'release-manifest.json', arcname='release-manifest.json', filter=self.public_metadata)
        (output / 'site.tar.partial').rename(output / 'site.tar')
        # Keep application code separate from the public website mount.
        runtime = ['.dockerignore', 'backend/scripts/serve.py', 'backend/scripts/verify_release.py', 'backend/atlas/server.py', 'backend/atlas/hosting.py', 'backend/atlas/plan_store.py', 'backend/atlas/eal_reader.py', 'backend/atlas/eal_strings.py', 'deploy/Dockerfile', 'deploy/compose.yaml', 'deploy/.env.example', 'deploy/nginx.conf.example', 'docs/deployment.md']
        for name in runtime:
            target = output / name
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(self.root / name, target)
        (output / 'deploy/bin').mkdir(exist_ok=True)
        checksum = digest(output / 'site.tar')
        (output / 'SHA256SUMS').write_text(f'{checksum}  site.tar\n')
        print(json.dumps({'release': str(output), 'files': len(rows), 'queries': catalog['count'], 'bytes': manifest['total_bytes'], 'archive_sha256': checksum}))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    ReleaseBuilder(ROOT).prepare(args.output.resolve())
