"""Read the currently published EAL catalog; never retain stale membership."""
import json
from pathlib import Path


class PlanReadError(ValueError):
    def __init__(self, message, status, kind):
        super().__init__(message)
        self.status, self.kind = status, kind


class PlanStore:
    def __init__(self, root):
        self.root = Path(root).resolve()
        self.directory = self.root / 'exports/eal'

    def resolve(self, query_id):
        try:
            manifest = json.loads((self.directory / 'manifest.json').read_text(encoding='utf-8'))
            if not isinstance(manifest, list):
                raise ValueError('清单必须是数组')
            paths = {}
            for entry in manifest:
                qid, path = entry['query_id'], entry['path']
                if not isinstance(qid, str) or not isinstance(path, str) or qid in paths:
                    raise ValueError('清单含无效或重复条目')
                paths[qid] = path
        except (OSError, UnicodeError, ValueError, KeyError, TypeError) as exc:
            raise PlanReadError(f'EAL 清单不可用：{exc}', 503, 'catalog') from exc
        if query_id not in paths:
            raise PlanReadError('查询不在当前 EAL 清单中。请重新构建图册并刷新页面。', 404, 'catalog')
        path = (self.root / paths[query_id]).resolve()
        if not path.is_relative_to(self.directory) or path.suffix != '.eal':
            raise PlanReadError('无效 EAL 路径。', 400, 'catalog')
        return path
