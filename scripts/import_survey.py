"""Import an explicit snapshot of existing reading notes, never synthesize research."""
from pathlib import Path
import argparse
import hashlib
import json
import re
import shutil

FILES = ['README.md', '出发点分析.md', '解决的问题分析.md', 'Novelty分析.md', 'workload分析.md']

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('source', type=Path)
    args = parser.parse_args()
    destination = Path(__file__).resolve().parents[1] / 'Survey'
    manifest = []
    for folder in sorted(args.source.iterdir()):
        if not folder.is_dir():
            continue
        missing = [name for name in FILES if not (folder / name).is_file()]
        if missing:
            raise ValueError(f'{folder.name}: missing {missing}')
        target = destination / folder.name
        target.mkdir(parents=True, exist_ok=True)
        hashes = {}
        for name in FILES:
            shutil.copyfile(folder / name, target / name)
            hashes[name] = hashlib.sha256((target / name).read_bytes()).hexdigest()
        if not re.search(r'\]\(https?://', (folder / 'README.md').read_text()):
            for pdf in folder.glob('*.pdf'):
                shutil.copyfile(pdf, target / pdf.name)
                hashes[pdf.name] = hashlib.sha256(pdf.read_bytes()).hexdigest()
        manifest.append({'folder': folder.name, 'source': str(folder.resolve()), 'sha256': hashes})
    (destination / 'manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
    print(f'Imported {len(manifest)} papers / {len(manifest) * len(FILES)} documents')

if __name__ == '__main__':
    main()
