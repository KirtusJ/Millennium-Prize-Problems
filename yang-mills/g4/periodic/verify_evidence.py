"""Verify the periodic proof's recorded-byte chain, optionally deep-replaying PCP registers."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import sys

p=argparse.ArgumentParser(description=__doc__)
p.add_argument('--runtime',type=Path)
p.add_argument('--method',type=Path)
a=p.parse_args()
root=Path(__file__).resolve().parent
evidence=root/'evidence'
sha=lambda raw: hashlib.sha256(raw).hexdigest()
read=lambda name: json.loads((evidence/name).read_bytes())
manifest=read('manifest.json')
actual={f.relative_to(evidence).as_posix() for f in evidence.rglob('*')
        if f.is_file() and f!=evidence/'manifest.json'}
assert set(manifest)==actual,'Unindexed or missing evidence'
for name,expected in manifest.items():
    raw=(evidence/name).read_bytes()
    assert sha(raw)==expected['sha256'] and len(raw)==expected['bytes'],name

source=(root/'PeriodicReflectionPositivity.lean').read_bytes()
digest=sha(source)
native=read('native/receipt.json')
assert native['kernel_sha256']=='d2fae4ef3df316ff4fa0c1a88744e66cc17bd794856979fa55188b8402f7222f'
assert native['kernel_measurement']=='0232c02a8946d66216da0ac65953a246ce3d41d7a966ae31aa83c3335b3259e3'
assert native['method_manifest_sha256']=='3949b2401d0a835cb116c22e44821993cbac59bbd2b281572ebb1b04e8296c18'
assert native['core_sha256']=='39efd83b4122545455124f20420f212590a06064f391b259e93ea968449e6b7f'
parent=read('compiler/receipt.json')
child=read('compiler/child/receipt.json')
review=read('final-review/receipt.json')
assert native['source_sha256']==parent['source_sha256']==child['source_sha256']==review['candidate_sha256']==digest
assert parent['passed'] and child['passed'] and review['passed']
assert parent['checker_sha256']==child['checker_sha256']==sha((root/'check_periodic.py').read_bytes())
assert parent['mutations_sha256']==child['mutations_sha256']==sha((root/'mutations.json').read_bytes())
mutations=json.loads((root/'mutations.json').read_bytes())
assert [(r['label'],r['exit_code']) for r in child['records']]==[('positive',0)]+[(m['label'],1) for m in mutations]
for receipt,directory in [(parent,evidence/'compiler'),(child,evidence/'compiler/child')]:
    assert receipt['verification']['ok']
    for rec in receipt['records']:
        assert rec['control_passed'] and rec['start_ns']<=rec['exit_observed_ns']<=rec['post_exit_readback_ns']
        assert sha((directory/(rec['label']+'.log')).read_bytes())==rec['output_sha256']
for mutation in mutations:
    assert source.decode().count(mutation['find'])==1
    expected=source.decode().replace(mutation['find'],mutation['replace'],1).encode()
    assert (evidence/'compiler/child'/(mutation['label']+'.lean')).read_bytes()==expected
    log=(evidence/'compiler/child'/(mutation['label']+'.log')).read_text(encoding='utf8')
    assert 'error:' in log and mutation['diagnostic'] in log

positive=(evidence/'compiler/child/positive.log').read_text(encoding='utf8')
expected=re.findall(r'^#print axioms (\w+)\r?$',source.decode(),re.M)
found=[(m.group(1),m.group(2) or '') for m in re.finditer(
    r"'Millennium\.G4\.PeriodicRP\.(\w+)' (?:depends on axioms: \[([^\]]*)\]|does not depend on any axioms)",positive)]
assert len(expected)==27 and expected==[name for name,_ in found]
assert set(expected)==set(re.findall(r'^(?:theorem|def) (\w+)',source.decode(),re.M))
assert all(set(x.strip() for x in axioms.split(',') if x.strip())<={'propext','Classical.choice','Quot.sound'}
           for _,axioms in found)
assert 'sorryAx' not in positive and 'error:' not in positive

cases=dict(exact=0,changed=1,truncated=1,appended=1,missing=2,denied=3,proof0=0,proof1=0,proof2=0)
assert len(native['observations'])==9
assert {r['case']:r['guest_exit'] for r in native['observations']}==cases
for rec in native['observations']:
    log=(evidence/'native'/rec['case']/'serial.log').read_bytes()
    assert sha(log)==rec['serial_sha256'] and rec['exit_code']==33
    assert rec['start_ns']<=rec['exit_observed_ns']<=rec['readback_ns']
    assert b'verifies and replays without a problem' in log and b'ALL SELF-TESTS PASS' in log
emitted=b''
for role in range(3):
    log=(evidence/'native'/('proof'+str(role))/'serial.log').read_text(encoding='utf8')
    emitted+=bytes.fromhex(''.join(re.findall(r'^G4 LEANHEX ([0-9a-f]+)$',log,re.M)))
assert emitted==source

registers=['transport','transport/draft','transport/challenge',
           'features','features/draft','features/challenge','geometry','geometry/draft','geometry/challenge',
           'final-review','final-review/challenge','compiler','compiler/child','dependency','controls']
for name in registers:
    receipt=read(name+'/receipt.json')
    assert receipt['verification']['ok']
    if receipt.get('readback_sha256'):
        assert sha((evidence/name/'model_reply.txt').read_bytes())==receipt['readback_sha256']
for name in ['transport','features','geometry','final-review']:
    receipt=read(name+'/receipt.json')
    assert receipt['passed']
    for rec in receipt['records']:
        assert rec['passed'] and rec['exit_code']==0
        assert rec['start_ns']<=rec['exit_observed_ns']<=rec['readback_ns']
        assert sha((evidence/name/rec['label']/'receipt.json').read_bytes())==rec['receipt_sha256']
    if name!='final-review':
        assert receipt['candidate_sha256']==sha((evidence/name/'draft/model_reply.txt').read_bytes())

dependency=read('dependency/receipt.json')
assert dependency['passed'] and dependency['exit_code']==0
assert dependency['source_sha256']==sha((root.parent/'wilson/WilsonReflectionPositivity.lean').read_bytes())
assert dependency['start_ns']<=dependency['exit_observed_ns']<=dependency['readback_ns']
assert dependency['log_sha256']==sha((evidence/'dependency/compiler.log').read_bytes())
old_dependency=json.loads((root.parent/'wilson/evidence/dependency/receipt.json').read_bytes())
old_complex=json.loads((root.parent/'integral/evidence/dependency/receipt.json').read_bytes())
assert old_dependency['passed'] and old_dependency['exit_code']==0 and old_complex['passed']
assert old_dependency['source_sha256']==sha((root.parent/'integral/IntegralReflectionPositivity.lean').read_bytes())
assert old_complex['source_sha256']==sha((root.parent/'complex/ComplexReflectionPositivity.lean').read_bytes())
assert dependency['dependency_olean_sha256']=={
    'ComplexReflectionPositivity.olean':old_complex['module_sha256'],
    'IntegralReflectionPositivity.olean':old_dependency['module_sha256']}
assert parent['dependency_olean_sha256']==child['dependency_olean_sha256']=={
    **dependency['dependency_olean_sha256'],'WilsonReflectionPositivity.olean':dependency['module_sha256']}
dep_log=(evidence/'dependency/compiler.log').read_text(encoding='utf8')
assert 'sorryAx' not in dep_log and 'error:' not in dep_log
assert len(re.findall(r"^'Millennium\.G4\.WilsonRP\.\w+' (?:depends on axioms|does not depend on any axioms)",dep_log,re.M))==87
control=read('controls/receipt.json')
assert control['passed'] and control['exit_code']==0
assert control['source_sha256']==sha((root/'check_holonomy.py').read_bytes())
assert control['output_sha256']==sha((evidence/'controls/control.log').read_bytes())
assert control['start_ns']<=control['exit_observed_ns']<=control['readback_ns']

replayed=[]
if a.runtime or a.method:
    if not (a.runtime and a.method):
        p.error('Provide both --runtime and --method')
    sys.path.insert(0,str(a.runtime.resolve()))
    os.environ['PCPOS_METHOD']=str(a.method.resolve())
    from pcpos.ops import Ops
    from pcpos.store import Workspace
    for name in registers:
        result=Ops(Workspace(evidence/name/'register'),'host').verify(deep=True)
        assert result['ok'] and result['head']==read(name+'/receipt.json')['verification']['head'],name
        replayed.append({'name':name,'head':result['head'],'events':result['events']})
print(json.dumps({'evidence_files':len(manifest),'source_sha256':digest,'axiom_reports':len(found),
    'native_cases':9,'negative_controls':len(mutations),'register_replays':replayed,
    'limit':'Recorded-byte verification; no fresh Lean, native boot or independent-party audit.'},indent=2))
