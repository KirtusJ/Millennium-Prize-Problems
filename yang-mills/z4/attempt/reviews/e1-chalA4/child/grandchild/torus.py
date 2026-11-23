"""Torus-sum recomputation of lattice Maxwell covariance c(m)=C(m e_1).
Usage: python3 torus.py control   -> writes control.txt (mode 'x') with c(0), N=32
       python3 torus.py results   -> writes results.txt (mode 'x') for N=32,48
Predicates (stated in advance):
 P1: |c(0)-0.5| < 1e-6 for N=32 and 48 (exact symmetry on torus; expected
     deviation is 1/(2N^4) = 4.8e-7 (N=32), 9.4e-8 (N=48) from omitted p=0).
 P2: |c_N48(m)-c_N32(m)| < 1e-3 for m=1,2,3 (finite-size tolerance, soft).
"""
import sys, numpy as np
def c_of(N, M=9):
    k = np.arange(N); h2 = (2*np.sin(np.pi*k/N))**2
    H = h2[:,None,None,None]+h2[None,:,None,None]+h2[None,None,:,None]+h2[None,None,None,:]
    num = h2[None,:,None,None]+h2[None,None,:,None]+0*H   # h1^2+h2^2
    f = np.zeros_like(H); nz = H > 0; f[nz] = num[nz]/H[nz]
    g = f.sum(axis=(0,2,3))/N**4          # marginal over p0,p2,p3 -> function of p1
    m = np.arange(M)
    return np.array([(g*np.cos(2*np.pi*k*mm/N)).sum() for mm in m])
if sys.argv[1]=="control":
    c = c_of(32)
    with open("control.txt","x") as f: f.write("%.6f\n" % c[0])
else:
    with open("results.txt","x") as f:
        r = {}
        for N in (32,48):
            c = c_of(N); r[N]=c
            X = 2*c[2]+c[1]+c[3]
            f.write("N=%d c0=%.8f c1=%.8f c2=%.8f c3=%.8f X1=%.8f\n"%(N,c[0],c[1],c[2],c[3],X))
        for m in (0,1,2,3): f.write("diff m=%d: %.3e\n"%(m,r[48][m]-r[32][m]))
        f.write("P1 %s\nP2 %s\n"%(all(abs(r[N][0]-.5)<1e-6 for N in r), all(abs(r[48][m]-r[32][m])<1e-3 for m in (1,2,3))))
