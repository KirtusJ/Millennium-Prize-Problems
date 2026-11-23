"""Recursive PCP supervisor -> child PCP supervisors -> bounded model workers."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import time

p=argparse.ArgumentParser(description=__doc__)
for name in ['runtime','method','out']:
    p.add_argument('--'+name,type=Path,required=True)
p.add_argument('--candidate',type=Path,help='Review a fixed final source instead of generating another draft')
p.add_argument('--task-dir',type=Path,help='Optional directory containing formalizer_task.txt and reviewer_task.txt')
a=p.parse_args()
for name in ['runtime','method','out','candidate','task_dir']:
    value=getattr(a,name)
    if value is not None:
        setattr(a,name,value.resolve())
root=Path(__file__).resolve().parent
task_dir=a.task_dir or root
a.out.mkdir(parents=True,exist_ok=False)
sys.path.insert(0,str(a.runtime))
os.environ['PCPOS_METHOD']=str(a.method)
from pcpos.ops import Ops
from pcpos.method import verify_dir
method=verify_dir(a.method)
assert method['matches_required']
ops,_=Ops.init(a.out/'register',label='G4-Periodic-formalization',principal='Kirtus',
              principal_name='Kirtus Justus',method_path=str(a.method),require_method=True)
ops.participant_add('G4-coordinator',lineage='PROGRAM: recursive supervisor of PCP child commissions')
ops=Ops(ops.ws,'G4-coordinator')
ops.adopt('Kirtus','RELAYED: direct user commission to formalize periodic Wilson RP under the standing autopilot commission with recursive PCP workers. DECLARED attribution.')
records=[]

def phase(label,task):
    event,_=ops._write('TASK_STARTED',{'label':label,'worker':'PROGRAM','quiet_limit':0,
                                      'budget':300,'budget_units':'wall seconds'})
    argv=[sys.executable,'-B',str(root/'run_worker.py'),'--runtime',str(a.runtime),
          '--method',str(a.method),'--out',str(a.out/label),'--task',str(task)]
    start=time.time_ns()
    with subprocess.Popen(argv,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,
                          creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0)) as proc:
        try:
            output,_=proc.communicate(timeout=300)
        except subprocess.TimeoutExpired:
            subprocess.run(['taskkill','/PID',str(proc.pid),'/T','/F'],capture_output=True,timeout=20)
            output,_=proc.communicate(timeout=15)
    exited=time.time_ns()
    (a.out/(label+'.log')).write_bytes(output)
    child_path=a.out/label/'receipt.json'
    okay=proc.returncode==0 and child_path.exists()
    raw=child_path.read_bytes() if child_path.exists() else output
    if okay:
        child=json.loads(raw)
        okay=child['verification']['ok'] and child['exit_code']==0
        answer=(a.out/label/'model_reply.txt').read_bytes()
        okay=okay and hashlib.sha256(answer).hexdigest()==child['readback_sha256']
    _,digest=ops.add_bytes(raw,name=label+'-child-post-exit',origin='PRODUCED')
    assert ops.ws.get(digest)==raw
    readback=time.time_ns()
    ops._write('TASK_ENDED',{'id':event['body']['id'],'outcome':'DONE' if okay else 'FAILED',
              'result':digest,'read_back':digest,'spent':int((exited-start)/1e9),
              'spent_units':'wall seconds','note':'Child exited; receipt and produced output read back.'},actor='host')
    records.append({'label':label,'pid':proc.pid,'exit_code':proc.returncode,'start_ns':start,
                    'exit_observed_ns':exited,'readback_ns':readback,'receipt_sha256':digest,'passed':okay})
    return okay

okay=True if a.candidate else phase('draft',task_dir/'formalizer_task.txt')
if okay:
    candidate=a.candidate.read_bytes() if a.candidate else (a.out/'draft/model_reply.txt').read_bytes()
    prompt=(task_dir/'reviewer_task.txt').read_bytes()+b'\n\nSOURCE TO AUDIT:\n'+candidate
    review=a.out/'review-task.txt'
    review.write_bytes(prompt)
    okay=phase('challenge',review)
verification=ops.verify(deep=True)
receipt={'method':method,'hierarchy':'Director -> PCP program coordinator -> PCP child supervisor -> PCP model',
         'records':records,'passed':okay and verification['ok'],'verification':verification,
         'native_execution':False,'independent_party_review':False,
         'candidate_sha256':hashlib.sha256(candidate).hexdigest() if okay else None}
(a.out/'receipt.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf8')
print(json.dumps(receipt))
raise SystemExit(0 if receipt['passed'] else 1)
