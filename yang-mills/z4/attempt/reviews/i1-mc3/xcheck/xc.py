"""xc.py: read child-code output (sO, sOO per chain) and print the connected (A,B averaged) E correlator and S correlator.
Predicate XC (fixed before run): if the child's independent Metropolis at beta=4 shows NO floor, i.e. C_E(t=7) < 3 sigma
from 0 while my v1 heat-bath code shows C_E(7) ~ 1e-3, my code has a defect; if both show the floor, the exact value or the
interpretation is in question."""
import json,sys,numpy as np
d=json.load(open(sys.argv[1])); sO=np.array(d['sO']); sOO=np.array(d['sOO']); R=sO.shape[0]
def conn(idx):
    m=sO[idx].mean(0); c=sOO[idx].mean(0)
    return c-np.einsum('a,b->ab',m,m)[...,None]
full=conn(np.arange(R)); jk=np.array([conn(np.delete(np.arange(R),r)) for r in range(R)])
err=np.sqrt((R-1)/R*((jk-jk.mean(0))**2).sum(0))
E=(full[0,0]+full[1,1])/2; Ee=np.sqrt(((R-1)/R*(((jk[:,0,0]+jk[:,1,1])/2-((jk[:,0,0]+jk[:,1,1])/2).mean(0))**2).sum(0)))
print('E  C(t):',' '.join(f'{x:.2e}({e:.0e})' for x,e in zip(E,Ee)))
print('E/C0   :',' '.join(f'{x/E[0]:.4f}' for x in E))
print('S  C(t):',' '.join(f'{x:.2e}' for x in full[2,2]))
