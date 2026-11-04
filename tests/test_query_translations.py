"""All imported query titles must have source-matched, lossless identifier translations."""
import hashlib
import json
from pathlib import Path
import re
import sys
import tempfile
import unittest
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'backend' / 'atlas'))
from query_translations import QueryTranslations


def numeric_values(text):
    """Compare values while allowing localized ordinals, grouping and units."""
    from decimal import Decimal
    text = re.sub(r'(?<=\d)[, ](?=\d{3}(?:\D|$))', '', text)
    text = re.sub(r'\s*(?:百万|百萬)', ' million', text)
    text = text.translate(str.maketrans('一二两三四五六七八九', '1223456789'))
    text = text.replace('十', '10')
    values = set()
    for match in re.finditer(r'\d+(?:\.\d+)?(?:万|亿| billion| million|[kK]\b)?', text):
        token = match.group()
        number = re.match(r'\d+(?:\.\d+)?', token).group()
        unit = token[len(number):]
        values.add(Decimal(number) * {'万':10000,'亿':100000000,' billion':1000000000,' million':1000000,'k':1000,'K':1000}.get(unit, 1))
    return values


class QueryTranslationTest(unittest.TestCase):
    def test_full_coverage_and_protected_content(self):
        queries = [json.loads(line) for line in (ROOT / 'catalog/queries.jsonl').read_text().splitlines()]
        translations = QueryTranslations(ROOT, queries)
        # 8-17/7-30 carry full translations; other entries are short generated titles (SQL summaries) that may omit details.
        full = {q['query_id'] for q in queries if q['benchmark_id'] in ('8-17', '7-30')}
        self.assertEqual(len(full), 3348)
        for qid, entry in translations.records.items():
            with self.subTest(query=qid):
                self.assertRegex(entry['zh'], r'[\u4e00-\u9fff]')
                if qid not in full:
                    continue
                self.assertNotRegex(entry['zh'], r'ZXQ\d+QXZ')
                for token in re.findall(r'`[^`]+`|\b[A-Za-z][A-Za-z0-9]*_[A-Za-z0-9_]+\b',entry['source']):
                    self.assertIn(token,entry['zh'])
                self.assertFalse(numeric_values(entry['source']) - numeric_values(entry['zh']), entry)

    def test_stale_translation_blocks_build(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            (root/'config/translations').mkdir(parents=True)
            records={'q':{'source':'Old query','zh':'旧问题','source_sha256':hashlib.sha256(b'Old query').hexdigest()}}
            (root/'config/translations/queries-zh.json').write_text(json.dumps(records))
            with self.assertRaisesRegex(ValueError,'Stale'):
                QueryTranslations(root,[{'query_id':'q','title':'New query','benchmark_id':'8-17'}])
