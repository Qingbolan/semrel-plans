"""Read EAL using the EasyNet compiler; never execute missions or abilities."""
import json
import shutil
import subprocess
import tempfile
from pathlib import Path

MAX_SOURCE_BYTES = 1024 * 1024


class CompileError(ValueError):
    pass


class EalCompiler:
    def __init__(self, executable=None):
        self.executable = executable or shutil.which('easynet')

    def compile(self, source):
        if not isinstance(source, str) or not source.strip():
            raise CompileError('EAL 源码不能为空。')
        if len(source.encode('utf-8')) > MAX_SOURCE_BYTES:
            raise CompileError('EAL 文件不能超过 1 MiB。')
        if not self.executable:
            raise CompileError('未找到 easynet，请安装 EasyNet CLI 并加入 PATH。')
        with tempfile.TemporaryDirectory(prefix='semrel-compile-') as directory:
            path = Path(directory) / 'mission.eal'
            path.write_text(source, encoding='utf-8')
            try:
                result = subprocess.run([self.executable, 'mission', 'compile', str(path), '--emit-ir'],
                                        capture_output=True, text=True, timeout=15)
            except subprocess.TimeoutExpired as exc:
                raise CompileError('EAL 编译超过 15 秒，请检查文件。') from exc
            except OSError as exc:
                raise CompileError('无法启动 EasyNet 编译器。') from exc
            if result.returncode:
                raise CompileError((result.stderr or result.stdout or 'EAL 编译失败').replace(str(path), 'mission.eal')[:16000])
            try:
                ir = json.loads(result.stdout)
            except json.JSONDecodeError as exc:
                raise CompileError('EasyNet 编译器未返回有效 Mission IR。') from exc
        return {'source': source, 'ir': ir, 'graph': MissionGraph(ir).project()}


class MissionGraph:
    """Project flat Mission IR into a unique-node graph, including named ports."""
    def __init__(self, ir):
        self.ir = ir

    def project(self):
        steps = self.ir.get('steps', [])
        if any('ability' not in s for s in steps):
            raise CompileError('当前图册支持平面调用 DAG，暂不支持 loop 控制流的图形展示。')
        bindings = {s['output_binding']: s['step_id'] for s in steps if s.get('output_binding')}
        nodes, edges = [], []
        phases = {i: phase for phase, r in enumerate(self.ir.get('phases', [])) for i in range(r['start'], r['end'])}
        for i, step in enumerate(steps):
            args = step.get('static_arguments', {})
            family = args.get('family', 'ability')
            nodes.append({'id': step['step_id'], 'binding': step.get('output_binding'),
                          'label': args.get('label', step['ability']), 'ability': step['ability'],
                          'family': family if family in ('relational', 'semantic', 'input') else 'ability',
                          'phase': phases.get(i, 0), 'arguments': args, 'target': step.get('target')})
            for port, binding in step.get('input_refs', {}).items():
                if binding not in bindings:
                    raise CompileError(f'无法解析输入引用：{binding}')
                edges.append({'parent': step['step_id'], 'child': bindings[binding], 'port': port})
        return {'name': self.ir.get('name', ''), 'nodes': nodes, 'edges': edges, 'emits': self.ir.get('emits', [])}
