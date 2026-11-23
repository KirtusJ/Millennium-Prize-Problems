"""Direct 4D midpoint-grid sum for G(n)=int d^4k/(2pi)^4 e^{i k0 n}(s1+s2)/(s0+s1+s2+s3).
Grid: k=pi*(2j+1)/N-pi, j<N (even N never hits k=0). Integral = grid mean.
PREDICATES (written before first run):
 P1 G(0)=0.5 to 1e-10 (hypercubic symmetry; grid is symmetric under axis permutations -> exact up to roundoff).
 P2 imag part of G(1) < 1e-12 (grid symmetric k0->-k0).
 P3 G(1) stable across N: integrand is degree-0 homogeneous (non-smooth) at k=0, so
    midpoint error expected ~ c/N^4 (maybe slower); require |G(48)-G(32)| < 1e-4 and
    successive differences shrinking. Extrapolation: Richardson assuming N^-4 using
    N=32,48; error estimate = |extrapolated - G(48)| and spread vs N^-2 assumption.
 P4 sanity: |G(1)| < 0.5 .
Seeds: none needed (deterministic); np.random.seed(0) set for form.
Run: python3 g4d.py   (results opened with mode 'x'; remove nothing, use new names to rerun)
"""
import numpy as np, sys
np.random.seed(0)
def G(N,n):
    k=np.pi*(2*np.arange(N)+1)/N-np.pi
    s=4*np.sin(k/2)**2
    # rest of 3D sum for each (k1,k2,k3): precompute over k1,k2,k3 in slices of k1
    tot=0j
    s2d=s[:,None]+s[None,:]  # s2+s3
    for a in range(N):  # k1 slice
        den3=s[a]+s2d  # s1+s2+s3 over (k2,k3) -- need full 4D with k0
        # arrays: k0 (N,1,1), k2,k3 (N,N)
        num=(s[a]+s[None,:,None])*np.ones((N,1,N))  # s1+s2, shape (N,N,N)? build explicitly
        D=s[:,None,None]+s[a]+s[None,:,None]+s[None,None,:]
        Nn=s[a]+s[None,:,None]+0*s[:,None,None]+0*s[None,None,:]
        w=np.exp(1j*k*n)[:,None,None]
        tot+=np.sum(w*Nn/D)
    return tot/N**4
out=open('results.txt','x')
vals={}
for N in (16,24,32,48):
    g0,g1=G(N,0),G(N,1); vals[N]=(g0,g1)
    out.write(f"N={N} G0={g0.real:.15f}{g0.imag:+.1e}j G1={g1.real:.15f}{g1.imag:+.1e}j\n"); out.flush()
    print(out and f"N={N} G0={g0} G1={g1}",flush=True)
g=[vals[N][1].real for N in (16,24,32,48)]
Ns=np.array([16,24,32,48.])
res=[]
for p in (2,4):
    for (i,j) in ((2,3),(1,3),(0,3)):
        a,b=Ns[i],Ns[j]
        e=(g[j]*b**p-g[i]*a**p)/(b**p-a**p); res.append((p,int(a),int(b),e))
        out.write(f"Richardson p={p} N=({int(a)},{int(b)}) -> {e:.12f}\n")
# least-squares fit g = G + c/N^4
A=np.vstack([np.ones(4),Ns**-4]).T; sol=np.linalg.lstsq(A,g,rcond=None)[0]
out.write(f"LSQ G+c/N^4 over all 4: G={sol[0]:.12f} c={sol[1]:.4f}\n")
chk={'P1':abs(vals[48][0]-0.5)<1e-10 and all(abs(vals[N][0]-.5)<1e-10 for N in vals),
 'P2':all(abs(vals[N][1].imag)<1e-12 for N in vals),
 'P3':abs(g[3]-g[2])<1e-4 and abs(g[3]-g[2])<abs(g[2]-g[1]),
 'P4':all(abs(x)<0.5 for x in g)}
out.write(f"predicates {chk}\n"); out.close(); print(chk,res,sol)
