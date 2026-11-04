"""Refresh the completion queue from the built catalog, keyed by canonical paper URL."""
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'src'))
from papers import PaperExporter


def refresh():
    identity = PaperExporter(ROOT).identity
    destination = ROOT / 'research/paper-completion/queue.json'
    queue = json.loads(destination.read_text())
    previous = {identity(p['url']): p for p in queue['papers']}
    reviews = {identity(p['url']): p for p in json.loads(
        (ROOT / 'research/paper-completion/reviews.json').read_text())}
    catalog = json.loads((ROOT / 'assets/papers.js').read_text().removeprefix(
        'window.SEMREL_PAPERS = ').rstrip(';\n'))
    required = ['motivation', 'problem', 'novelty', 'workload', 'usecase', 'benchmark']
    result = []
    for paper in catalog:
        missing = [k for k in required if not (paper['sections'].get(k) or
                   (paper.get('usecase') if k == 'usecase' else '') or '').strip()]
        key = identity(paper['url'])
        review = reviews.get(key)
        if not missing and not review:
            continue
        entry = dict(previous.get(key, {}))
        entry.update(id=paper['id'], title=paper['title'], url=paper['url'],
                     has_queries=bool(paper['sections'].get('queries')),
                     remaining_sections=missing)
        entry.setdefault('missing_sections', missing)
        if review:
            if missing:
                raise ValueError('Published review still has missing sections: ' + key)
            entry.update(status=review['status'], batch=review['batch'], review_path=review['note_directory'])
        else:
            entry.setdefault('status', 'pending')
        result.append(entry)
    queue['papers'] = result
    queue['current_library_count'] = len(catalog)
    queue['progress'] = {'tracked': len(result), 'read': len(reviews),
                         'remaining': sum(bool(p['remaining_sections']) for p in result)}
    destination.write_text(json.dumps(queue, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(queue['progress']))


if __name__ == '__main__':
    refresh()
