"""Check the published byte chain; this does not rerun Lean or authenticate actors."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import sys

p=argparse.ArgumentParser(description=__doc__)
p.add_argument('--runtime',type=Path,help='Optional pinned PCP Python implementation')
p.add_argument('--method',type=Path,help='Matching historical method for deep register replay')
a=p.parse_args()
root=Path(__file__).resolve().parent
evidence=root/'evidence'

def sha(raw):
    return hashlib.sha256(raw).hexdigest()

def read(name):
    return json.loads((evidence/name).read_bytes())

manifest=read('manifest.json')
actual={f.relative_to(evidence).as_posix() for f in evidence.rglob('*')
        if f.is_file() and f!=evidence/'manifest.json'}
assert set(manifest)==actual, 'Missing or unindexed evidence'
for name,row in manifest.items():
    raw=(evidence/name).read_bytes()
    assert len(raw)==row['bytes'] and sha(raw)==row['sha256'], name

source=(root/'ReflectionPositivity.lean').read_bytes()
native=read('native/receipt.json')
parent=read('compiler/receipt.json')
child=read('compiler/child/receipt.json')
assert native['source_sha256']==parent['source_sha256']==child['source_sha256']==sha(source)
assert parent['passed'] and child['passed']
expected_cases=dict(exact=0,changed=1,truncated=1,appended=1,missing=2,denied=3,proof0=0,proof1=0,proof2=0)
assert {r['case']:r['guest_exit'] for r in native['observations']}==expected_cases
assert len(native['observations'])==len(expected_cases)
for rec in native['observations']:
    log=(evidence/'native'/rec['case']/'serial.log').read_bytes()
    assert sha(log)==rec['serial_sha256'] and rec['exit_code']==33
    assert rec['start_ns']<=rec['exit_observed_ns']<=rec['readback_ns']
    assert b'verifies and replays without a problem' in log
    assert b'ALL SELF-TESTS PASS' in log
emitted=b''
for role in range(3):
    text=(evidence/'native'/('proof'+str(role))/'serial.log').read_text()
    emitted+=bytes.fromhex(''.join(re.findall(r'^G4 LEANHEX ([0-9a-f]+)$',text,re.M)))
assert emitted==source

for receipt,directory in [(parent,evidence/'compiler'),(child,evidence/'compiler/child')]:
    assert receipt['verification']['ok']
    for rec in receipt['records']:
        assert rec['control_passed']
        assert rec['start_ns']<=rec['exit_observed_ns']<=rec['post_exit_readback_ns']
        assert sha((directory/(rec['label']+'.log')).read_bytes())==rec['output_sha256']
assert [(r['label'],r['exit_code']) for r in child['records']]==[('positive',0),('negative',1)]
positive=(evidence/'compiler/child/positive.log').read_text()
expected=re.findall(r'^#print axioms (\w+)\r?$',source.decode(),re.M)
found=re.findall(r"'Millennium\.G4\.(\w+)' depends on axioms: \[([^\]]*)\]",positive)
assert len(expected)==11 and expected==[name for name,_ in found]
assert all(set(x.strip() for x in axioms.split(','))<={'propext','Classical.choice','Quot.sound'}
           for _,axioms in found)
negative=(evidence/'compiler/child/negative.log').read_text()
assert 'error: type mismatch' in negative and 'qlim t < 0' in negative

replayed=[]
if a.runtime or a.method:
    if not (a.runtime and a.method):
        p.error('Both --runtime and --method are required for register replay')
    sys.path.insert(0,str(a.runtime))
    os.environ['PCPOS_METHOD']=str(a.method)
    from pcpos.ops import Ops
    from pcpos.store import Workspace
    for name in ['model','host-calibration','compiler','compiler/child']:
        ops=Ops(Workspace(evidence/name/'register'),'host')
        result=ops.verify(deep=True)
        assert result['ok'], name
        replayed.append({'name':name,'head':result['head'],'events':result['events']})
print(json.dumps({'evidence_files':len(manifest),'source_sha256':sha(source),
                  'native_cases':len(expected_cases),'accepted_axiom_reports':len(found),
                  'register_replays':replayed,
                  'limit':'Recorded byte-chain verification, not a new Lean or native kernel execution.'},indent=2))
