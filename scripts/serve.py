"""Serve the atlas with live, compile-only EAL reading."""
import argparse
from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'src'))
from server import AtlasServer

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--port', type=int, default=8765)
    args = parser.parse_args()
    try:
        server = AtlasServer(('127.0.0.1', args.port), ROOT)
    except OSError as exc:
        parser.exit(1, f'无法启动图册：{exc}\n')
    print(f'SemRel Atlas: http://127.0.0.1:{args.port}', flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
