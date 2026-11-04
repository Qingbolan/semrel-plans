"""Prepare resumable Chinese query translations; source text remains immutable."""
import concurrent.futures
import hashlib
import json
from pathlib import Path
import re
import time
import urllib.parse
import urllib.request

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / 'config/translations/queries-zh.json'
PROTECTED = re.compile(r'`[^`]+`|\b[A-Za-z][A-Za-z0-9]*_[A-Za-z0-9_]+\b|(?<!\w)[+-]?\d+(?:[.,:/-]\d+)*(?:%|st\b|nd\b|rd\b|th\b)?')


def translate(row):
    source = row['title']
    tokens = []
    def protect(match):
        tokens.append(match.group())
        return f'ZXQ{len(tokens)-1:04d}QXZ'
    text = PROTECTED.sub(protect, source)
    # Disambiguate the ranking sense of ties, which generic MT confuses with relationships.
    text = re.sub(r'break (?:a tie|ties)(?: at the cutoff)? by', 'for equal ranked values, order by', text, flags=re.I)
    url = 'https://translate.googleapis.com/translate_a/single?' + urllib.parse.urlencode(
        dict(client='gtx', sl='en', tl='zh-CN', dt='t', q=text))
    for attempt in range(5):
        try:
            with urllib.request.urlopen(url, timeout=30) as response:
                payload = json.load(response)
            translated = ''.join(part[0] for part in payload[0] if part[0])
            for i, token in enumerate(tokens):
                marker = f'ZXQ{i:04d}QXZ'
                if translated.count(marker) != 1:
                    raise ValueError('Protected token missing or duplicated: ' + marker)
                translated = translated.replace(marker, token)
            if not re.search(r'[\u4e00-\u9fff]', translated):
                raise ValueError('No Chinese translation')
            return row['query_id'], {'source': source, 'zh': translated,
                'source_sha256': hashlib.sha256(source.encode()).hexdigest()}
        except ValueError:
            raise
        except Exception:
            if attempt == 4:
                raise
            time.sleep(1 + attempt * 2)


def save(records):
    temporary = OUTPUT.with_suffix('.tmp')
    temporary.write_text(json.dumps(records, ensure_ascii=False, indent=2) + '\n')
    temporary.replace(OUTPUT)


if __name__ == '__main__':
    records = json.loads(OUTPUT.read_text()) if OUTPUT.exists() else {}
    rows = [json.loads(line) for line in (ROOT / 'query/queries.jsonl').read_text().splitlines()]
    rows = [r for r in rows if r['benchmark_id'] in ('8-17', '7-30')]
    pending = [r for r in rows if records.get(r['query_id'], {}).get('source') != r['title']]
    errors = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
        futures = {pool.submit(translate, row): row for row in pending}
        for count, future in enumerate(concurrent.futures.as_completed(futures), 1):
            try:
                qid, entry = future.result()
                records[qid] = entry
            except Exception as exc:
                errors.append((futures[future]['query_id'], str(exc)))
                print('ERROR', futures[future]['query_id'], str(exc), flush=True)
            if count % 50 == 0:
                save(records)
                print(f'{count}/{len(pending)} processed; {len(records)}/{len(rows)} translated; errors={len(errors)}', flush=True)
    save(records)
    print(json.dumps(errors, ensure_ascii=False), flush=True)
    if errors:
        raise SystemExit(1)
