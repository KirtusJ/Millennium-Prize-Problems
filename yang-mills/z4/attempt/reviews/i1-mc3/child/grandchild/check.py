"""Check SU(2) commutator and center-even identities on random matrices.

Predicates (declared before first run):
 P1: max |(1/2)Re Tr(Ui Uj Ui^-1 Uj^-1) - (1 - 2(|ui|^2|uj|^2 - (ui.uj)^2))| < 1e-12
 P2: max dev of Q=((1/2)Tr U)^2 and P_ij under Ui->-Ui           < 1e-12
 P3: same under Uj->-Uj                                           < 1e-12
 P4: same under simultaneous conjugation by random SU(2) g        < 1e-12
 (P_ij = (1/2)Re Tr(Ui Uj Ui^-1 Uj^-1).)
Seed 12345, N=20000. Result file results.txt opened with mode "x"
(delete it to rerun). Rerun: OMP_NUM_THREADS=1 python3 check.py
"""
import numpy as np
rng = np.random.default_rng(12345)
N = 20000
S = np.array([[[0,1],[1,0]],[[0,-1j],[1j,0]],[[1,0],[0,-1]]])
def quat(n):
    q = rng.normal(size=(n,4)); return q/np.linalg.norm(q,axis=1,keepdims=True)
def mat(q):
    return q[:,0,None,None]*np.eye(2) + 1j*np.einsum('nk,kab->nab',q[:,1:],S)
def dag(U): return np.conj(np.swapaxes(U,1,2))
def P(Ui,Uj): return 0.5*np.real(np.trace(Ui@Uj@dag(Ui)@dag(Uj),axis1=1,axis2=2))
def Q(U): return (0.5*np.real(np.trace(U,axis1=1,axis2=2)))**2
qi,qj,qg = quat(N),quat(N),quat(N)
Ui,Uj,g = mat(qi),mat(qj),mat(qg)
ui,uj = qi[:,1:],qj[:,1:]
pred = 1-2*((ui**2).sum(1)*(uj**2).sum(1)-(ui*uj).sum(1)**2)
p0 = P(Ui,Uj)
d = {}
d['P1 commutator formula'] = np.abs(p0-pred).max()
def dev(Ui2,Uj2):
    return max(np.abs(Q(Ui2)-Q(Ui)).max(),np.abs(Q(Uj2)-Q(Uj)).max(),np.abs(P(Ui2,Uj2)-p0).max())
d['P2 Ui->-Ui'] = dev(-Ui,Uj)
d['P3 Uj->-Uj'] = dev(Ui,-Uj)
d['P4 conjugation'] = dev(g@Ui@dag(g),g@Uj@dag(g))
out = []
for k,v in d.items():
    out.append(f"{k}: maxdev={v:.3e} {'met' if v<1e-12 else 'FAILED'}")
out.append(f"met {sum(v<1e-12 for v in d.values())}/4")
s = "\n".join(out); print(s)
with open('results.txt','x') as f: f.write(s+"\n")
