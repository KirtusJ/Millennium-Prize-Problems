"""P3: special configurations and horizontal values. Predicates fixed before first run:
 H1: pi-flux: c_full = 8 within 1e-9 AND c_H = 8 within 1e-9 (claim of the task; eigh-accuracy tol 1e-9).
 H2: for ALL final iterates saved in results/p2_{a,b,c}.npy plus pi-flux and 'one link -1' and identity: c_full<=12+1e-9; report
     number of configs qualifying / tested, and max c_full, max c_H over them.
 H3 (measured only): ascent from pi-flux perturbed by 0.05*random (seed 5), 25 iterations of p2-type ascent on c_full: does c exceed 8?
 H4 (measured only): ascent from 'one link=-1' start (link 0), 25 iterations.
Output results/p3.txt (mode x)."""
import numpy as np, glob, lgt
from lgt import *
def lam(U):
    w,v=np.linalg.eigh(Hmat(U)); return w[0],v[:,0]
def grad(U,v,h=1e-6):
    T=v.reshape(64,3); q0=qform(U,T); B=np.zeros((192,64,3))
    for i in range(192): B[i,i//3,i%3]=h
    return (qform(expm_su2(B)@U[None],T)-q0)/h
def ascend(U,n):
    l,v=lam(U); eta=0.05
    for it in range(n):
        g=grad(U,v); ok=False
        for _ in range(12):
            Un=expm_su2(-eta*g.reshape(64,3))@U; ln,vn=lam(Un)
            if -ln>-l: ok=True;break
            eta/=2
        if not ok: break
        U,l,v=Un,ln,vn; eta*=1.5
    return U,-l
out=open('results/p3.txt','x')
one=np.tile(np.eye(2,dtype=complex),(64,1,1)); one[0]*=-1
ident=np.tile(np.eye(2,dtype=complex),(64,1,1))
cfgs={'piflux':piflux(),'onelink-1':one,'identity':ident}
for f in sorted(glob.glob('results/p2_[abc].npy')):
    for i,U in enumerate(np.load(f)): cfgs[f'{f[-5]}{i}']=U
res={}
for k,U in cfgs.items(): res[k]=(cfull(U),cH(U)); out.write(f"{k}: c_full={res[k][0]:.9f} c_H={res[k][1]:.9f}\n")
out.write(f"H1 piflux: {'PASS' if abs(res['piflux'][0]-8)<1e-9 and abs(res['piflux'][1]-8)<1e-9 else 'FAIL'}\n")
q=sum(1 for v in res.values() if v[0]<=12+1e-9)
out.write(f"H2: {q}/{len(res)} configs satisfy c<=12+1e-9; max c_full={max(v[0] for v in res.values()):.9f}; max c_H={max(v[1] for v in res.values()):.9f}\n")
rng=np.random.default_rng(5)
Up=expm_su2(0.05*rng.normal(size=(64,3)))@piflux(); Ua,ca=ascend(Up,25)
out.write(f"H3 ascent from perturbed piflux: c_final={ca:.9f} c_H={cH(Ua):.9f}\n")
Ub,cb=ascend(one,25); out.write(f"H4 ascent from one link -1: c_final={cb:.9f} c_H={cH(Ub):.9f}\n")
out.close(); print(open('results/p3.txt').read())
