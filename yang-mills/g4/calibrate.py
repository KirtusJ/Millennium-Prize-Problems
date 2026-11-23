"""Bounded positive/adverse controls for the PCP Python host actually used."""
import argparse
import hashlib
import json
from pathlib import Path
import sys

p = argparse.ArgumentParser()
p.add_argument('--runtime', type=Path, required=True)
p.add_argument('--method', type=Path, required=True)
p.add_argument('--out', type=Path, required=True)
a = p.parse_args()
sys.path.insert(0, str(a.runtime))
from pcpos.ops import Ops
from pcpos.base import PcposError
from pcpos.method import verify_dir

a.out.mkdir(parents=True, exist_ok=False)
ident = verify_dir(a.method)
ops, _ = Ops.init(a.out/'register', label='G4-isolated-calibration',
                 principal='calibration-principal', method_path=str(a.method), require_method=True)
ops.participant_add('checker', lineage='deterministic Python calibration program')
ops = Ops(ops.ws, 'checker')
ev, _ = ops._write('TASK_STARTED', {'label':'readback-control', 'worker':'PROGRAM',
    'quiet_limit':0, 'budget':10, 'budget_units':'seconds'})
task = ev['body']['id']
result = {'method': ident, 'controls': []}

def reject(label, body):
    before = (ops.ws.root/'register.jsonl').read_bytes()
    try:
        ops._write('TASK_ENDED', body, actor='host')
    except PcposError as e:
        after = (ops.ws.root/'register.jsonl').read_bytes()
        if before != after:
            raise AssertionError('Refusal changed the register')
        result['controls'].append({'name':label, 'rejected':True, 'register_unchanged':True,
                                   'reason':str(e)})
    else:
        raise AssertionError('Invalid completion accepted')

base = {'id':task, 'outcome':'DONE', 'result':None, 'read_back':None, 'spent':0,
        'spent_units':'seconds', 'note':'Synthetic calibration, not a research result'}
reject('missing-result', base)
_, digest = ops.add_bytes(b'G4 calibration artifact\n', name='control-output', origin='PRODUCED')
reject('wrong-readback', dict(base, result=digest, read_back='0'*64))
readback = hashlib.sha256(ops.ws.get(digest)).hexdigest()
ops._write('TASK_ENDED', dict(base, result=digest, read_back=readback), actor='host')
result['controls'].append({'name':'valid-readback', 'accepted':True, 'digest':digest})
result['verification'] = ops.verify(deep=True)
if not result['verification']['ok']:
    raise AssertionError('Deep replay failed')
result['limits'] = ['Python host only; no native Rust or freestanding kernel execution',
    'Local integrity and selected guard behavior, not actor authentication or mathematical correctness',
    'Old runtime method identity is distinct from current enterprise and historical Fidelity Lab sources']
(a.out/'calibration.json').write_text(json.dumps(result, indent=2)+'\n', encoding='utf8')
print(json.dumps(result))
