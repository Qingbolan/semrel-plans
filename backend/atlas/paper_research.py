"""Project reading notes and per-paper workloads, kept separate from original papers."""
from collections import defaultdict
import json
import re
from pathlib import Path
from urllib.parse import quote


class PaperResearch:
    def __init__(self, root):
        self.root=Path(root)

    def document(self, path):
        """Resolve links against the archived document, without inventing missing assets."""
        document=self.root/path
        def link(match):
            label,target=match.groups()
            if re.match(r'https?://|#',target):return match.group(0)
            target=target.strip('<>')
            resolved=(document.parent/target).resolve()
            if resolved.is_file() and resolved.is_relative_to(self.root.resolve()):
                return f'[{label}]({quote(resolved.relative_to(self.root.resolve()).as_posix())})'
            return label
        return re.sub(r'\[([^\]]+)\]\(([^)]+)\)',link,document.read_text())

    def apply(self, papers, queries):
        literature=self.root/'query/imports/semantic-workload-bench/literature.json'
        if not literature.exists():return
        grouped=defaultdict(set)
        for entry in json.loads(literature.read_text()):
            paper=next(p for p in papers if entry['source_id'] in p.get('source_ids',[]))
            grouped[paper['id']].update(entry['documents'])
        for paper in papers:
            if paper['id'] in grouped:
                docs=sorted(grouped[paper['id']])
                paper['research_documents']=docs
                blocks=['# 来源项目研究记录']
                for path in docs:
                    text=self.document(path)
                    # Retain the complete source note with its own evidence and qualifications.
                    blocks.append(f'\n[来源文档]({quote(path)})\n\n{text}')
                paper['sections']['research']='\n\n---\n\n'.join(blocks)
            linked=[q for q in queries if any(r['role']=='paper' and r['source_id'] in paper.get('source_ids',[]) for r in q['provenance'])]
            if not linked:continue
            lines=['# 查询与任务清单','| 集合 | 序号 | 查询 | 论文关系 |','|---|---:|---|---|']
            labels={'query_source':'查询来源','dataset_origin':'派生任务的数据来源','system_implementation':'系统源码示例'}
            for q in linked:
                ref=next(r for r in q['provenance'] if r['role']=='paper' and r['source_id'] in paper.get('source_ids',[]))
                title=q['task_record']['query'].replace('|','\\|').replace('\n',' ')
                lines.append(f"| {q['collection_name']} | {q['display_number']} | [{title}](#{quote(q['query_id'],safe='')}) | {labels.get(ref.get('relationship'),'已有图册记录')} |")
            paper['sections']['queries']='\n'.join(lines)
