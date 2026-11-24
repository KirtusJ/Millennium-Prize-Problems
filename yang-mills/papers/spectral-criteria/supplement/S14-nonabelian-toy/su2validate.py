"""Validation of the spin-network machinery of su2net.py, independent of any physics.
PREDICATES (fixed before the first run; the same checks had been made once during development):
 V1 the vertex tensors used as intertwiner bases are annihilated by the total generators, for all spins up to 2
    (loop spin up to 3/2): largest residual below 1e-12.
 V2 the basis functions (cut-off J = 3/2, 314 of them) are gauge invariant: their values at four random
    configurations (a, b, c, d) and at gauge transforms of them agree to 1e-12.
 V3 the five multiplication matrices (two plaquette traces, Tr c, Tr ab, Tr abc) reproduce pointwise
    multiplication: for every basis function with all spins at most 1/2 and four random configurations,
    f(x) Psi_s(x) = sum_s' M[s', s] Psi_s'(x) to 1e-12.
 V4 the five matrices are Hermitian to 1e-12.
 V5 Wigner matrices: D^{1/2}(g) = g, and D^j(g) D^j(h) = D^j(gh) for j = 1, 3/2, 2, to 1e-12.
Seed 1. Output su2validate_result.txt (not overwritten). Command: python3 su2validate.py"""
import numpy as np
from su2net import *
rng=np.random.default_rng(1); out=[]
def rsu2():
    q=rng.normal(size=4); q/=np.linalg.norm(q); return np.array([[q[0]+1j*q[3], q[2]+1j*q[1]],[-q[2]+1j*q[1], q[0]-1j*q[3]]])
g,h=rsu2(),rsu2(); v5=max([np.abs(Dmat(0.5,g)-g).max()]+[np.abs(Dmat(j,g)@Dmat(j,h)-Dmat(j,g@h)).max() for j in (1,1.5,2)])
v1=max(check_inv(j1,j2,j3) for j1 in (0,.5,1,1.5,2) for j2 in (0,.5,1,1.5,2) for j3 in (0,.5,1,1.5))
N=Net(1.5); W={k:N.assemble(k) for k in ('W0','W1','C','AB','ABC')}
v4=max(abs(M-M.conj().T).max() for M in W.values())
def allvals(a,b,c,d):
    v=np.zeros(N.n,complex)
    for key,(off,r0,r1) in N.blocks.items(): v[off:off+r0*r1]=N.evaluate(key,a,b,c,d)
    return v
v2=0; v3={k:0.0 for k in W}; H=lambda x:x.conj().T
for trial in range(4):
    a,b,c,d=[rsu2() for _ in range(4)]; g0,g1=rsu2(),rsu2()
    v=allvals(a,b,c,d); v2=max(v2,np.abs(v-allvals(g0@a@H(g1),g1@b@H(g0),g0@c@H(g0),g1@d@H(g1))).max())
    f={'W0':0.5*np.trace(a@d@H(a)@H(c)).real,'W1':0.5*np.trace(b@c@H(b)@H(d)).real,'C':np.trace(c).real,'AB':np.trace(a@b).real,'ABC':np.trace(a@b@c)}
    for k,M in W.items():
        for key in [key for key in N.blocks if max(key)<=0.5]:
            off,r0,r1=N.blocks[key]
            for e in range(r0*r1): v3[k]=max(v3[k],abs(f[k]*v[off+e]-M[:,off+e].toarray().ravel()@v))
for nm,val in (("V1",v1),("V2",v2),("V3",max(v3.values())),("V4",v4),("V5",v5)): out.append("%s largest error %.2e : %s"%(nm,val,"MET" if val<1e-12 else "FAILED"))
out.append("basis size at J = 3/2: %d ; pointwise errors by operator: %s"%(N.n," ".join("%s %.1e"%kv for kv in v3.items())))
open('su2validate_result.txt','x').write("\n".join(out)+"\n"); print("\n".join(out))
