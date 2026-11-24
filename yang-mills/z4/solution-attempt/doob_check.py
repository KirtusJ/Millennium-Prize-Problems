"""Check of the identity S_1 = Doob transform of C by phi = W*Omega (no gauge projection; finite state).
PREDICATES (fixed before the run): for 200 random instances (n in 3..12): C symmetric with positive entries,
W positive diagonal, L = W C W, (Lam0, Omega) Perron pair, S1 = diag(1/Omega) L diag(Omega)/Lam0,
P[x,y] = C[x,y] phi[y] / (C phi)[x] with phi = W Omega.
 D1 max |S1 - P| <= 1e-10;  D2 rows of P sum to 1 within 1e-10;  D3 Omega^2-reversibility: |Om[x]^2 P[x,y] - Om[y]^2 P[y,x]| <= 1e-10.
Seed 11. Output doob_result.txt (not overwritten)."""
import numpy as np
rng=np.random.default_rng(11); m1=m2=m3=0
for _ in range(200):
    n=rng.integers(3,13); C=rng.random((n,n))+0.05; C=(C+C.T)/2; W=np.diag(rng.random(n)+0.2)
    L=W@C@W; ev,V=np.linalg.eigh(L); Om=np.abs(V[:,-1]); Lam=ev[-1]
    S1=np.diag(1/Om)@L@np.diag(Om)/Lam; phi=np.diag(W)*Om; P=C*phi[None,:]/(C@phi)[:,None]
    m1=max(m1,np.abs(S1-P).max()); m2=max(m2,np.abs(P.sum(1)-1).max())
    R=(Om**2)[:,None]*P; m3=max(m3,np.abs(R-R.T).max())
out="D1 %.2e %s\nD2 %.2e %s\nD3 %.2e %s\n"%(m1,"MET" if m1<=1e-10 else "FAILED",m2,"MET" if m2<=1e-10 else "FAILED",m3,"MET" if m3<=1e-10 else "FAILED")
open('doob_result.txt','x').write(out); print(out)
