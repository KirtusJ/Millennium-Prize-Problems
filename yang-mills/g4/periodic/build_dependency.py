"""Compile the pinned G4 integral module and bind its complex dependency; record compiler and module readback in PCP."""
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
p.add_argument('--dependency-dir',type=Path,required=True)
a=p.parse_args()
for key in ['runtime','method','mathlib','leanbin','source','out','dependency_dir']:
    setattr(a,key,getattr(a,key).resolve())
a.out.mkdir(parents=True,exist_ok=False)
raw=a.source.read_bytes()
sha=lambda data: hashlib.sha256(data).hexdigest()
assert sha(raw)=='465d565057c6b5a1b0b196cf24a1bb3285eaf63c41f75141d2959ef9bf906f3f'
sys.path.insert(0,str(a.runtime))
os.environ['PCPOS_METHOD']=str(a.method)
os.environ['PATH']=str(a.leanbin)+os.pathsep+os.environ['PATH']
from pcpos.ops import Ops
dependencies={
 'ComplexReflectionPositivity.olean':'e813aff6c86181bf9493cf9ce3264df5827e1c0c0ecbd845a6a0d2a3ef52e74a',
 'IntegralReflectionPositivity.olean':'0c3173bd7d655d0d4bfe4b4a530c531b47ff1acaff01d975f8e18fc62974e083'}
for name,digest in dependencies.items():
    module_raw=(a.dependency_dir/name).read_bytes()
    assert sha(module_raw)==digest
    (a.out/name).write_bytes(module_raw)
os.environ['LEAN_PATH']=str(a.out)+os.pathsep+os.environ.get('LEAN_PATH','')
ops,_=Ops.init(a.out/'register',label='G4-Periodic-dependency',principal='Kirtus',
              principal_name='Kirtus Justus',method_path=str(a.method),require_method=True)
ops.participant_add('builder',lineage='PROGRAM: pinned G4 module compiler')
ops=Ops(ops.ws,'builder')
ops.adopt('Kirtus','RELAYED: periodic reflection-positivity continuation; declared local actor attribution.')
event,_=ops._write('TASK_STARTED',{'label':'compile-wilson-module','worker':'PROGRAM','quiet_limit':0,
                                  'budget':900,'budget_units':'wall seconds'})
module=a.out/'WilsonReflectionPositivity.olean'
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
found=re.findall(r"'Millennium\.G4\.WilsonRP\.(\w+)' (?:depends on axioms: \[([^\]]*)\]|does not depend on any axioms)",readback.decode())
okay=proc.returncode==0 and a.source.read_bytes()==raw and module.exists()
okay=okay and len(expected)==87 and expected==[name for name,_ in found]
okay=okay and all(set(x.strip() for x in axioms.split(',') if x.strip())<={'propext','Classical.choice','Quot.sound'}
                  for _,axioms in found)
record={'dependency_olean_sha256':dependencies,'source_sha256':sha(raw),'module_sha256':sha(module.read_bytes()) if module.exists() else None,
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
