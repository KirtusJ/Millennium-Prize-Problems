"""Observe an actual finite-holonomy control process and read back its output in PCP."""
import argparse,hashlib,json,os,subprocess,sys,time
from pathlib import Path
p=argparse.ArgumentParser(description=__doc__)
for name in ['runtime','method','out']:p.add_argument('--'+name,type=Path,required=True)
a=p.parse_args()
for name in ['runtime','method','out']:setattr(a,name,getattr(a,name).resolve())
a.out.mkdir(exist_ok=False)
sys.path.insert(0,str(a.runtime));os.environ['PCPOS_METHOD']=str(a.method)
from pcpos.ops import Ops
ops,_=Ops.init(a.out/'register',label='G4-Periodic-holonomy-control',principal='Kirtus',
    principal_name='Kirtus Justus',method_path=str(a.method),require_method=True)
ops.participant_add('checker',lineage='PROGRAM: finite sign-cycle enumerator')
ops=Ops(ops.ws,'checker')
ops.adopt('Kirtus','RELAYED: standing autonomous PCP/Lean research continuation; DECLARED attribution.')
ev,_=ops._write('TASK_STARTED',{'label':'period-two-holonomy','worker':'PROGRAM','quiet_limit':0,
    'budget':60,'budget_units':'wall seconds'})
source=Path(__file__).with_name('check_holonomy.py')
sha=lambda raw:hashlib.sha256(raw).hexdigest()
source_digest=sha(source.read_bytes())
start=time.time_ns()
with subprocess.Popen([sys.executable,'-B',str(source)],stdout=subprocess.PIPE,stderr=subprocess.STDOUT,
    creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0)) as proc:
    output,_=proc.communicate(timeout=60)
exited=time.time_ns()
(a.out/'control.log').write_bytes(output)
raw=(a.out/'control.log').read_bytes()
readback=time.time_ns()
okay=proc.returncode==0 and sha(source.read_bytes())==source_digest
_,digest=ops.add_bytes(raw,name='holonomy-control-output',origin='PRODUCED')
assert ops.ws.get(digest)==raw
ops._write('TASK_ENDED',{'id':ev['body']['id'],'outcome':'DONE' if okay else 'FAILED',
    'result':digest,'read_back':digest,'spent':int((exited-start)/1e9),'spent_units':'wall seconds'},actor='host')
v=ops.verify(deep=True)
receipt={'source_sha256':source_digest,'exit_code':proc.returncode,'pid':proc.pid,'start_ns':start,
    'exit_observed_ns':exited,'readback_ns':readback,'output_sha256':sha(raw),'verification':v,
    'passed':okay and v['ok'],'scope':'Floating-point exhaustive finite sign-cycle control, not a Lean theorem.'}
(a.out/'receipt.json').write_bytes((json.dumps(receipt,indent=2)+'\n').encode())
print(json.dumps(receipt));raise SystemExit(0 if receipt['passed'] else 1)
