"""Serve the atlas with live, compile-only EAL reading."""
import argparse
import os
from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'backend' / 'atlas'))
from server import AtlasServer

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--port', type=int, default=8765)
    parser.add_argument('--host', default=os.getenv('ATLAS_HOST', '127.0.0.1'))
    parser.add_argument('--root', type=Path, default=Path(os.getenv('ATLAS_ROOT', str(ROOT))))
    parser.add_argument('--public-origin', action='append', default=[v for v in os.getenv('ATLAS_PUBLIC_ORIGINS', '').split(',') if v])
    args = parser.parse_args()
    try:
        server = AtlasServer((args.host, args.port), args.root, public_origins=args.public_origin)
    except (OSError, ValueError) as exc:
        parser.exit(1, f'无法启动图册：{exc}\n')
    print(f'SemRel Atlas: http://{args.host}:{args.port}', flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
