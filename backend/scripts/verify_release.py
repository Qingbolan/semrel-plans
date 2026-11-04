"""Verify transferred content and, optionally, an already running atlas."""
import argparse
import hashlib
import json
import tarfile
from pathlib import Path
from urllib.request import urlopen


def verify(root):
    root = root.resolve()
    manifest = json.loads((root / 'release-manifest.json').read_text())
    for row in manifest['files']:
        path = (root / row['path']).resolve()
        if not path.is_relative_to(root) or not path.is_file():
            raise ValueError(f'Missing or unsafe path: {row["path"]}')
        digest = hashlib.sha256()
        with path.open('rb') as stream:
            for chunk in iter(lambda: stream.read(1024 * 1024), b''):
                digest.update(chunk)
        if path.stat().st_size != row['bytes'] or digest.hexdigest() != row['sha256']:
            raise ValueError(f'Checksum mismatch: {row["path"]}')
    print(f'Verified {len(manifest["files"])} files; {manifest["query_count"]} queries')

def verify_archive(path):
    actual = {}
    manifest = None
    with tarfile.open(path, 'r|') as archive:
        for member in archive:
            name = member.name
            if not member.isfile() or Path(name).is_absolute() or '..' in Path(name).parts or name in actual:
                raise ValueError('Invalid archive member: ' + name)
            if member.mode != 0o644:
                raise ValueError('Unreadable public-file permissions: ' + name)
            stream = archive.extractfile(member)
            if name == 'release-manifest.json':
                manifest = json.load(stream)
                continue
            digest = hashlib.sha256()
            for chunk in iter(lambda: stream.read(1024 * 1024), b''):
                digest.update(chunk)
            actual[name] = (member.size, digest.hexdigest())
    if manifest is None:
        raise ValueError('Archive has no release manifest')
    expected = {row['path']:(row['bytes'],row['sha256']) for row in manifest['files']}
    if actual != expected:
        raise ValueError('Archive content does not match the release manifest')
    print(f'Verified archive: {len(actual)} files; {manifest["query_count"]} queries; all files mode 0644')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    target=parser.add_mutually_exclusive_group(required=True)
    target.add_argument('--root', type=Path)
    target.add_argument('--archive', type=Path)
    parser.add_argument('--url', help='Optional public origin of the running atlas')
    args = parser.parse_args()
    if args.archive:
        if args.url:parser.error('--url requires --root')
        verify_archive(args.archive)
    else:verify(args.root)
    if args.url:
        with urlopen(args.url.rstrip('/') + '/api/health', timeout=20) as response:
            assert json.load(response)['status'] == 'ready'
        records = json.loads((args.root / 'exports/eal/manifest.json').read_text())
        from urllib.parse import quote
        with urlopen(args.url.rstrip('/') + '/api/plan?query_id=' + quote(records[0]['query_id'], safe=''), timeout=20) as response:
            assert json.load(response)['graph']['nodes']
        print('Public health and DAG compilation passed')
