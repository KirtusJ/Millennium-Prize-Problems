"""Compile the pinned G4 complex module; record compiler and module readback in PCP."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import time

p=argparse.ArgumentParser(description=__doc__)
for key in ['runtime','method','mathlib','leanbin','source','out']:
    p.add_argument('--'+key,type=Path,required=True)
a=p.parse_args()
a.out.mkdir(parents=True,exist_ok=False)
raw=a.source.read_bytes()
sha=lambda data: hashlib.sha256(data).hexdigest()
assert sha(raw)=='47c67d26f29d0f47eade1e9505b78b33112f8ef896957a2cc952ce5bef0f5cc6'
sys.path.insert(0,str(a.runtime))
os.environ['PCPOS_METHOD']=str(a.method)
os.environ['PATH']=str(a.leanbin)+os.pathsep+os.environ['PATH']
from pcpos.ops import Ops
ops,_=Ops.init(a.out/'register',label='G4-integral-dependency',principal='Kirtus',
              principal_name='Kirtus Justus',method_path=str(a.method),require_method=True)
ops.participant_add('builder',lineage='PROGRAM: pinned G4 module compiler')
ops=Ops(ops.ws,'builder')
ops.adopt('Kirtus','RELAYED: integral reflection-positivity commission; declared local actor attribution.')
event,_=ops._write('TASK_STARTED',{'label':'compile-complex-module','worker':'PROGRAM','quiet_limit':0,
                                  'budget':900,'budget_units':'wall seconds'})
module=a.out/'ComplexReflectionPositivity.olean'
argv=[str(a.leanbin/'lake.exe'),'env','lean','--root='+str(a.source.parent),'-o',str(module),str(a.source)]
start=time.time_ns()
with subprocess.Popen(argv,cwd=a.mathlib,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,
                      creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0)) as proc:
    try:
        output,_=proc.communicate(timeout=900)
    except subprocess.TimeoutExpired:
        subprocess.run(['taskkill','/PID',str(proc.pid),'/T','/F'],capture_output=True,timeout=20)
        output,_=proc.communicate(timeout=15)
exited=time.time_ns()
(a.out/'compiler.log').write_bytes(output)
readback=(a.out/'compiler.log').read_bytes()
expected=re.findall(r'^#print axioms (\w+)\r?$',raw.decode(),re.M)
found=re.findall(r"'Millennium\.G4\.ComplexRP\.(\w+)' depends on axioms: \[([^\]]*)\]",readback.decode())
okay=proc.returncode==0 and a.source.read_bytes()==raw and module.exists()
okay=okay and len(expected)==33 and expected==[name for name,_ in found]
okay=okay and all(set(x.strip() for x in axioms.split(','))<={'propext','Classical.choice','Quot.sound'}
                  for _,axioms in found)
record={'source_sha256':sha(raw),'module_sha256':sha(module.read_bytes()) if module.exists() else None,
        'module_bytes':module.stat().st_size if module.exists() else 0,'exit_code':proc.returncode,
        'pid':proc.pid,'command':argv,'start_ns':start,'exit_observed_ns':exited,
        'readback_ns':time.time_ns(),'log_sha256':sha(readback),'passed':okay}
_,digest=ops.add_bytes(json.dumps(record,sort_keys=True).encode(),name='dependency-readback',origin='PRODUCED')
assert sha(ops.ws.get(digest))==digest
ops._write('TASK_ENDED',{'id':event['body']['id'],'outcome':'DONE' if okay else 'FAILED','result':digest,
          'read_back':digest,'spent':int((exited-start)/1e9),'spent_units':'wall seconds',
          'note':'Read compiler output and generated module after process exit.'},actor='host')
record['verification']=ops.verify(deep=True)
record['passed']=okay and record['verification']['ok']
(a.out/'receipt.json').write_bytes((json.dumps(record,indent=2)+'\n').encode())
print(json.dumps(record))
raise SystemExit(0 if record['passed'] else 1)
