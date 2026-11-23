"""PCP OS Python host supervisor; actual process and artifact read-back evidence.

Runtime and method are deliberately separate from the newer installed plugins.
This is a bounded model commission, not a claim of native-kernel execution.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import time

parser = argparse.ArgumentParser()
parser.add_argument('--runtime', type=Path, required=True)
parser.add_argument('--method', type=Path, required=True)
parser.add_argument('--out', type=Path, required=True)
parser.add_argument('--task', type=Path, required=True)
a = parser.parse_args()
sys.path.insert(0, str(a.runtime))
from pcpos.ops import Ops
from pcpos.method import verify_dir

a.out.mkdir(parents=True, exist_ok=False)
os.environ['PCPOS_METHOD'] = str(a.method.resolve())
os.environ['G4_ATTEMPT'] = str(a.out.resolve())
method = verify_dir(a.method)
ops, _ = Ops.init(a.out / 'register', label='G4-Yang-Mills-worker',
                 principal='Kirtus', principal_name='Kirtus Justus',
                 method_path=str(a.method), require_method=True)
ops.participant_add('G4-supervisor', name='G4 Python process supervisor', lineage='PROGRAM')
ops.participant_add('G4-formalizer', name='G4 PCP proof worker', lineage='Codex CLI; same provider family as Director G4')
ops = Ops(ops.ws, 'G4-supervisor')
ops.adopt('Kirtus', 'RELAYED by Director G4: 2026-11-22 direct user commission for PCP workers and Lean proofs in Millennium Prize Problems. Actor attribution remains DECLARED, not authenticated.')
event, _ = ops._write('TASK_STARTED', {'label': 'reflection-positivity-draft',
    'worker': 'MODEL', 'parent_task': None, 'quiet_limit': 0, 'budget': 260,
    'budget_units': 'wall seconds', 'observer': 'G4-supervisor'})
task_id = event['body']['id']
command = subprocess.list2cmdline([sys.executable, '-B', str((Path(__file__).parent.parent / 'worker_provider.py').resolve())])
argv = [sys.executable, '-B', str(a.runtime / 'pcp_os.py'), 'run', '--ws',
        str(ops.ws.root), '--provider', 'command', '--command', command,
        '--participant', 'G4-formalizer', '--kernel', 'kernel', '--name',
        'positivity-draft', '--task', '@' + str(a.task.resolve())]
started = time.time_ns()
with (a.out / 'host_stdout.txt').open('wb') as so, (a.out / 'host_stderr.txt').open('wb') as se:
    p = subprocess.Popen(argv, stdout=so, stderr=se, env=os.environ.copy(),
                         creationflags=getattr(subprocess, 'CREATE_NO_WINDOW', 0))
    try:
        code = p.wait(timeout=270)
    except subprocess.TimeoutExpired:
        subprocess.run(['taskkill', '/PID', str(p.pid), '/T', '/F'], capture_output=True, timeout=20)
        code = p.wait(timeout=15)
exited = time.time_ns()
digest = None
if code == 0:
    raw = (a.out / 'model_reply.txt').read_bytes()
    _, digest = ops.add_bytes(raw, name='G4-post-exit-readback', origin='PRODUCED',
                             extra={'producer_task': task_id, 'observer': 'G4-supervisor'})
    if ops.ws.get(digest) != raw:
        raise ValueError('Stored output disagrees with post-exit bytes')
ops._write('TASK_ENDED', {'id': task_id, 'outcome': 'DONE' if code == 0 else 'FAILED',
    'result': digest, 'read_back': digest, 'note': 'Supervisor read exact output after host exit; source correctness needs separate compiler and review.',
    'spent': int((exited-started)/1e9), 'spent_units': 'wall seconds'}, actor='host')
verification = ops.verify(deep=True)
receipt = {'method': method, 'runtime': str(a.runtime), 'native_execution': False,
    'host_pid': p.pid, 'start_ns': started, 'exit_observed_ns': exited, 'exit_code': code,
    'readback_sha256': digest, 'verification': verification,
    'hierarchy': 'Director G4 -> PCP Python supervisor -> PCP hosted Codex model',
    'auth': 'DECLARED; principal instruction relayed', 'proof_compilation': 'NOT YET PERFORMED'}
(a.out / 'receipt.json').write_text(json.dumps(receipt, indent=2)+'\n', encoding='utf8')
print(json.dumps({'exit_code': code, 'readback_sha256': digest, 'verification': verification}))
raise SystemExit(0 if code == 0 and verification['ok'] else 1)
