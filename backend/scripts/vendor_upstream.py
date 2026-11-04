"""Make the repository self-contained: copy referenced upstream files into data/source-inputs and
rewrite every absolute workspace path to a repository-relative path (or a GitHub URL for whole repos).

Run after any importer that reads a sibling checkout:  python3 backend/scripts/vendor_upstream.py [--dry-run]
"""
import argparse
import os
import re
import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
WORKSPACE = str(ROOT.parent) + '/'
SCAN = ['config', 'query', 'backend', 'src', 'docs', 'Survey', 'research', 'environment', 'exports', 'data', 'tests', 'deploy', 'files', 'artifacts']
SKIP = {'.git', 'node_modules', '__pycache__', 'source-inputs', 'eal'}
# Verbatim upstream snapshots are hash-checked; paths inside them are historical text, never read.
VERBATIM = ('query/imports/', 'query/source-snapshots/', 'research/2026-10-14/data-agents/evidence/', 'research/2026-10-14/data-agents/publisher-evidence/')
TEXT = {'.json', '.jsonl', '.md', '.py', '.js', '.mjs', '.cjs', '.jsx', '.txt', '.eal', '.yaml', '.yml', '.csv', '.html', '.toml', '.sql', ''}
# Earlier localisation already placed these trees here; keep the layout so nothing is copied twice.
ANCHORS = [('Awesome-Dymatic-Operator/chat/benchmark/8-17 data agent query and data/data/', 'data/source-inputs/8-17/'),
           ('semantic-workload-bench/data/', 'data/source-inputs/semantic-workload-bench/')]
PATTERN = re.compile(re.escape(WORKSPACE) + r'[^"\n`<>|*\\]*')


def existing_prefix(raw):
    """Prose often runs straight into the path; keep the longest prefix that exists on disk."""
    text = raw.rstrip()
    while len(text) > len(WORKSPACE) and not os.path.exists(text):
        text = text[:-1]
    return text if len(text) > len(WORKSPACE) else None


def remote(repo):
    try:
        url = subprocess.run(['git', '-C', WORKSPACE + repo, 'remote', 'get-url', 'origin'], capture_output=True, text=True).stdout.strip()
    except OSError:
        url = ''
    return url.removesuffix('.git') or f'upstream:{repo}'


def replacement(path):
    relative = path[len(WORKSPACE):]
    repo, _, inner = relative.partition('/')
    if repo == ROOT.name:
        return inner or '.', None
    if not inner.strip('/'):
        return remote(repo), None
    for anchor, target in ANCHORS:
        if relative.startswith(anchor):
            return target + relative[len(anchor):], path
    return f'data/source-inputs/{relative}', path


def text_files():
    for top in SCAN:
        for directory, dirs, files in os.walk(ROOT / top):
            dirs[:] = [d for d in dirs if d not in SKIP]
            for name in files:
                path = Path(directory) / name
                if path.relative_to(ROOT).as_posix().startswith(VERBATIM):
                    continue
                if path.suffix.lower() in TEXT and path.stat().st_size < 300_000_000:
                    yield path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()
    found = {}
    for path in text_files():
        text = path.read_text(errors='ignore')
        if WORKSPACE not in text:
            continue
        for match in PATTERN.finditer(text):
            resolved = existing_prefix(match.group(0))
            if resolved:
                found.setdefault(resolved, set()).add(path)
            else:
                print('UNRESOLVED', path.relative_to(ROOT), match.group(0)[:120])
    plan = {source: replacement(source) for source in found}
    copied = 0
    for source, (target, copy_from) in sorted(plan.items()):
        if copy_from and not (ROOT / target).exists():
            copied += 1
            if not args.dry_run:
                (ROOT / target).parent.mkdir(parents=True, exist_ok=True)
                (shutil.copytree if os.path.isdir(source) else shutil.copy2)(source, ROOT / target)
    rewritten = 0
    order = sorted(plan, key=len, reverse=True)
    for path in sorted({p for paths in found.values() for p in paths}):
        text = original = path.read_text()
        for source in order:
            text = text.replace(source, plan[source][0])
        if text != original:
            rewritten += 1
            if not args.dry_run:
                path.write_text(text)
    print(f'{len(plan)} referenced paths, {copied} copied into data/source-inputs, {rewritten} files rewritten'
          + (' (dry run)' if args.dry_run else ''))


if __name__ == '__main__':
    main()
