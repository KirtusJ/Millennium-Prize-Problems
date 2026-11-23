"""P2: maximize c(U)=-lambda_min(Hess V) by gradient ascent (Hellmann-Feynman, FD gradient of v^T H v w.r.t.
left-trivialized perturbations exp(d_e)U_e, step h=1e-6), backtracking step, 30 iterations. Usage: p2_search.py k0 k1 tag
Starts: seed k (rng default_rng(1000+k)) Haar-random U, for k in [k0,k1); k=-1: pi-flux; k=-2..-65: all ones except link (-2-k) = -1 (only first 3 run unless tag says).
Predicates fixed before first run:
 S1 (for all U visited): c(U) <= 12 + 1e-9. Report number of visited points qualifying (every accepted iterate) and the max c seen.
 S2: c(pi-flux) = 8 within 1e-9 (full spectrum).  S3 measured only: final c per start.
 Tolerance 1e-9 from eigh accuracy ~1e-13 on 192x192 with entries O(1).
Output results/p2_<tag>.txt (mode x) and results/p2_<tag>.npy of final U."""
import numpy as np, sys, lgt
from lgt import *
k0,k1,tag=int(sys.argv[1]),int(sys.argv[2]),sys.argv[3]
def start(k):
    if k>=0: return randU(np.random.default_rng(1000+k))
    if k==-1: return piflux()
    U=np.tile(np.eye(2,dtype=complex),(64,1,1)); U[-2-k]*=-1; return U
def lam(U):
    w,v=np.linalg.eigh(Hmat(U)); return w[0],v[:,0]
def grad(U,v,h=1e-6):
    T=v.reshape(64,3); q0=qform(U,T)
    B=np.zeros((192,64,3)); 
    for i in range(192): B[i,i//3,i%3]=h
    Ub=expm_su2(B)@U[None]   # (192,64,2,2)
    return (qform(Ub,T)-q0)/h
out=open(f'results/p2_{tag}.txt','x'); finals=[]; nvis=0; nok=0; cmax=-1e9
for k in range(k0,k1):
    U=start(k); l,v=lam(U); eta=0.05; c0=-l
    nvis+=1; nok+= (c0<=12+1e-9); cmax=max(cmax,c0)
    for it in range(30):
        g=grad(U,v)  # d q ; ascent on c => descend q
        ok=False
        for _ in range(12):
            Un=expm_su2(-eta*g.reshape(64,3))@U; ln,vn=lam(Un)
            if -ln>-l: ok=True;break
            eta/=2
        if not ok: break
        U,l,v=Un,ln,vn; eta*=1.5; nvis+=1; nok+=(-l<=12+1e-9); cmax=max(cmax,-l)
    finals.append(U); 
    out.write(f"start {k}: c_start={c0:.6f} c_final={-l:.6f} iters={it}\n"); out.flush()
out.write(f"visited={nvis} qualifying(c<=12+1e-9)={nok} max_c_seen={cmax:.9f}\n"); out.close()
np.save(f'results/p2_{tag}.npy',np.array(finals)); print(open(f'results/p2_{tag}.txt').read())
