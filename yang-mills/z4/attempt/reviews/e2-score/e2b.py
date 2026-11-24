"""e2b: direct check on the ACTUAL transported marks (with their conjugations and transport):
 B1 for colours 0,2,3 and 500 random configs (seed 11): the FD mixed derivative matrix M_ab of the
    selected mark Y_j w.r.t. right generators on the selected pair satisfies sum_ab M_ab^2 = 2+Y_j^2
    within 1e-6 (FD central difference h=1e-4: truncation ~h^2 * O(1) = 1e-8, roundoff ~eps/h^2 = 2e-8)
    and |M_ab|<=1+1e-6.
 B2 measured only: colour 1, same quantity for F's mixed matrix *4 (Y1+Y3 contributions).
"""
import numpy as np, sys, math
sys.argv += [] ; exec(open('e2_lib2.py').read())
out = open(sys.argv[1], "x")
def log(s): print(s); out.write(s+"\n"); out.flush()
rng = np.random.default_rng(11); h = 1e-4; E = np.eye(4)
pos = {'u':0,'v':1,'w':2,'z':3}; touch = {0:('u','w'),1:('v','w'),2:('u','z'),3:('v','z')}; sel = {0:0,2:2,3:3}
worst = 0; maxabs = 0; c1 = []
for trial in range(500):
    L = list(rq(rng,4)); fr = list(rq(rng,9)); Ys = Fval(L, fr)
    for c,(p,q) in touch.items():
        ip, iq = pos[p], pos[q]; Mx = np.zeros((3,3)); MF = np.zeros((3,3))
        for a in range(1,4):
            for b in range(1,4):
                def Fs(s,t):
                    LL = list(L); LL[ip] = qm(L[ip], expq(s*E[a][1:])); LL[iq] = qm(L[iq], expq(t*E[b][1:]))
                    return np.array(Fval(LL, fr))
                m = (Fs(h,h)-Fs(h,-h)-Fs(-h,h)+Fs(-h,-h))/(4*h*h)
                MF[a-1,b-1] = m.sum()
                if c in sel: Mx[a-1,b-1] = m[sel[c]]
        if c in sel:
            worst = max(worst, abs((Mx**2).sum() - 2 - Ys[sel[c]]**2)); maxabs = max(maxabs, np.abs(Mx).max())
        else:
            c1.append((MF**2).sum())
log(f"B1 max|sum M^2 - 2 - Y_j^2| = {worst:.2e}, max|M_ab| = {maxabs:.6f}")
log(f"[{'PASS' if worst<=1e-6 and maxabs<=1+1e-6 else 'FAIL'}] B1")
c1 = np.array(c1); log(f"B2 measured only colour 1: sum (4 D E F)^2 over 500 configs: min {c1.min():.4f} mean {c1.mean():.4f} max {c1.max():.4f}")
