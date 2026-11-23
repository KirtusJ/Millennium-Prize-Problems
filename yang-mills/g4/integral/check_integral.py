"""Recursive PCP program workers checking Lean and a deliberately invalid control.

Director -> program supervisor -> program checker -> Lean compiler.
Two PCP registers; imported complex module is compiled separately; no claim of separate model judgement or native Rust execution.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import time

p = argparse.ArgumentParser()
for key in ('runtime','method','mathlib','leanbin','source','out'):
    p.add_argument('--'+key, type=Path, required=True)
p.add_argument('--child', action='store_true')
p.add_argument('--namespace',default='Millennium.G4')
p.add_argument('--mutations',type=Path)
p.add_argument('--extra-lean-path',type=Path)
a = p.parse_args()
for key in ('runtime','method','mathlib','leanbin','source','out','mutations','extra_lean_path'):
    value = getattr(a, key)
    if value is not None:
        setattr(a, key, value.resolve())
sys.path.insert(0, str(a.runtime))
from pcpos.ops import Ops

def save(path, value):
    path.write_text(json.dumps(value, indent=2)+'\n', encoding='utf8')

def sha(data):
    return hashlib.sha256(data).hexdigest()

a.out.mkdir(parents=True, exist_ok=False)
os.environ['PCPOS_METHOD'] = str(a.method)
os.environ['PATH'] = str(a.leanbin) + os.pathsep + os.environ['PATH']
if a.extra_lean_path:
    os.environ['LEAN_PATH'] = str(a.extra_lean_path) + os.pathsep + os.environ.get('LEAN_PATH','')
ops, _ = Ops.init(a.out/'register', label='G4-compiler-child' if a.child else 'G4-check-supervisor',
    principal='Kirtus', principal_name='Kirtus Justus', method_path=str(a.method), require_method=True)
ops.participant_add('checker', lineage='Python program; compiler results are mechanical observations')
ops = Ops(ops.ws, 'checker')
ops.adopt('Kirtus', 'RELAYED by G4: authorized 2026-11-22 PCP/Lean research commission. This local register uses DECLARED actor attribution.')
records = []

def execute(label, argv, expected_success, cwd, diagnostic='error:'):
    ev, _ = ops._write('TASK_STARTED', {'label':label, 'worker':'PROGRAM',
        'quiet_limit':0, 'budget':900 if a.child else 1900, 'budget_units':'wall seconds'})
    started = time.time_ns()
    with subprocess.Popen(argv, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
        creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0)) as proc:
        try:
            output, _ = proc.communicate(timeout=900 if a.child else 1900)
        except subprocess.TimeoutExpired:
            subprocess.run(['taskkill','/PID',str(proc.pid),'/T','/F'], capture_output=True, timeout=20)
            output, _ = proc.communicate(timeout=15)
    exited = time.time_ns()
    (a.out/(label+'.log')).write_bytes(output)
    readback = (a.out/(label+'.log')).read_bytes()
    success = (proc.returncode == 0) == expected_success
    success = success and a.source.read_bytes() == source_bytes
    if label == 'positive':
        expected = re.findall(r'^#print axioms (\w+)\r?$', source_bytes.decode(), re.M)
        found = [(m.group(1),m.group(2) or '') for m in re.finditer(
            "'"+re.escape(a.namespace)+r"\.(\w+)' (?:depends on axioms: \[([^\]]*)\]|does not depend on any axioms)",
            output.decode(errors='replace'))]
        allowed = {'propext', 'Classical.choice', 'Quot.sound'}
        success = success and bool(expected) and [name for name, _ in found] == expected
        success = success and all(set(x.strip() for x in axioms.split(',') if x.strip()) <= allowed
                                  for _, axioms in found)
        success = success and b'sorryAx' not in output and b'error:' not in output
    if label.startswith('negative'):
        success = success and b'error:' in output and diagnostic.encode() in output
    rec = {'label':label, 'pid':proc.pid, 'command':argv, 'exit_code':proc.returncode,
        'start_ns':started, 'exit_observed_ns':exited, 'post_exit_readback_ns':time.time_ns(),
        'output_sha256':sha(readback), 'expected_success':expected_success, 'control_passed':success}
    raw = json.dumps(rec,sort_keys=True).encode()
    _, digest = ops.add_bytes(raw, name=label+'-receipt', origin='PRODUCED')
    if ops.ws.get(digest) != raw:
        raise AssertionError('Receipt readback mismatch')
    ops._write('TASK_ENDED', {'id':ev['body']['id'], 'outcome':'DONE' if success else 'FAILED',
        'result':digest, 'read_back':sha(ops.ws.get(digest)), 'spent':int((exited-started)/1e9),
        'spent_units':'wall seconds', 'note':'Expected compiler/control outcome checked after process exit.'}, actor='host')
    records.append(rec)
    return success

source_bytes = a.source.read_bytes()
dependency_files = {p.name:sha(p.read_bytes()) for p in a.extra_lean_path.glob('*.olean')} if a.extra_lean_path else {}
if a.child:
    lake = str(a.leanbin/'lake.exe')
    okay = execute('positive', [lake,'env','lean',str(a.source)], True, a.mathlib)
    if okay:
        mutations = json.loads(a.mutations.read_bytes()) if a.mutations else [
            {'label':'negative','find':'∀ t, 0 ≤ qlim t := by','replace':'∀ t, qlim t < 0 := by',
             'diagnostic':'but is expected to have type'}]
        for mutation in mutations:
            if not re.fullmatch(r'negative(?:_[a-z0-9]+)*',mutation['label']):
                raise ValueError('Invalid mutation label')
            if source_bytes.decode().count(mutation['find'])!=1:
                raise AssertionError('Mutation target must occur exactly once')
            bad = source_bytes.decode().replace(mutation['find'],mutation['replace'],1)
            bad_path = a.out/(mutation['label']+'.lean')
            bad_path.write_bytes(bad.encode('utf8'))
            okay = execute(mutation['label'],[lake,'env','lean',str(bad_path)],False,a.mathlib,
                           mutation.get('diagnostic','error:')) and okay
else:
    argv = [sys.executable,'-B',str(Path(__file__).resolve()),'--child']
    for key in ('runtime','method','mathlib','leanbin','source'):
        argv += ['--'+key,str(getattr(a,key))]
    argv += ['--namespace',a.namespace]
    if a.extra_lean_path:
        argv += ['--extra-lean-path',str(a.extra_lean_path)]
    if a.mutations:
        argv += ['--mutations',str(a.mutations)]
    argv += ['--out',str(a.out/'child')]
    okay = execute('child',argv,True,Path(__file__).parent)
    child_file = a.out/'child'/'receipt.json'
    if child_file.exists():
        child_raw = child_file.read_bytes()
        child = json.loads(child_raw)
        okay = okay and child['passed'] and child['source_sha256'] == sha(source_bytes)
        _, child_digest = ops.add_bytes(child_raw,name='child-summary-post-exit',origin='PRODUCED')
        if ops.ws.get(child_digest) != child_raw:
            raise AssertionError('Child summary changed')
    else:
        okay = False
verification = ops.verify(deep=True)
okay = okay and dependency_files == ({p.name:sha(p.read_bytes()) for p in a.extra_lean_path.glob('*.olean')} if a.extra_lean_path else {})
receipt = {'source_sha256':sha(source_bytes), 'source':str(a.source), 'records':records,
    'passed':bool(okay and verification['ok']), 'verification':verification,
    'native_execution':False, 'worker_kind':'PROGRAM', 'depth':3 if a.child else 2,
    'namespace':a.namespace, 'checker_sha256':sha(Path(__file__).read_bytes()),
    'mutations_sha256':sha(a.mutations.read_bytes()) if a.mutations else None,
    'dependency_olean_sha256':dependency_files}
save(a.out/'receipt.json',receipt)
print(json.dumps(receipt))
raise SystemExit(0 if receipt['passed'] else 1)
