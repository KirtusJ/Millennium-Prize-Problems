"""Predicates fixed before first run:
P1: c* = 2*int_0^{pi/2} sqrt(4 asinh(sin a)) da via a=u^2 and Gauss-Legendre; n=100 and n=200 agree to <5e-7;
    claim 4.6054132 holds if |c*-4.6054132|<5e-7.
P2: circle grid N points on [-pi,pi), N=256 and 512 (h*sqrt(beta)<=1/8 requires N>=202). Symmetric matrix
    M_ij = e^{-eps_i/2} h k(x_i-x_j) e^{-eps_j/2}; parity sectors via shift N/2. Predicates: Delta>0;
    -log(Delta)/sqrt(beta) agrees between grids to <1e-6 (relative converged).
Result file opened mode 'x'."""
import numpy as np
L=[]
def c(n):
    t,w=np.polynomial.legendre.leggauss(n); U=np.sqrt(np.pi/2); u=(t+1)*U/2; w=w*U/2
    return 2*(w*2*u*np.sqrt(4*np.arcsinh(np.sin(u*u)))).sum()
c1,c2=c(100),c(200)
L.append("c* (n=100) = %.9f, (n=200) = %.9f, diff %.2e"%(c1,c2,abs(c1-c2)))
L.append("P1 convergence (<5e-7): %s; claim 4.6054132 within 5e-7: %s"%(abs(c1-c2)<5e-7,abs(c2-4.6054132)<5e-7))
beta=16.
def run(N):
    h=2*np.pi/N; a=-np.pi+h*np.arange(N); eps=2*np.arcsinh(np.abs(np.sin(a)))
    d=a[:,None]-a[None,:]
    k=sum(np.exp(-beta*(d+2*np.pi*j)**2/2) for j in range(-2,3))*np.sqrt(beta/(2*np.pi))
    e=np.exp(-eps/2); M=e[:,None]*k*h*e[None,:]; n=N//2
    A=M[:n,:n]; B=M[:n,n:]
    le=np.linalg.eigh(A+B)[0][-1]; lo=np.linalg.eigh(A-B)[0][-1]
    D=le-lo; return h,le,lo,D,-np.log(D)/np.sqrt(beta)
R=[]
for N in (256,512):
    r=run(N); R.append(r)
    L.append("N=%d h*sqrt(beta)=%.4f lam_e=%.12f lam_o=%.12f Delta=%.10e -log(Delta)/sqrt(beta)=%.8f"%(N,r[0]*4,*r[1:]))
L.append("P2 Delta>0: %s; grid diff in -logD/sqrtb = %.2e (<1e-6: %s)"%(all(r[3]>0 for r in R),abs(R[0][4]-R[1][4]),abs(R[0][4]-R[1][4])<1e-6))
s="\n".join(L)+"\n"; print(s)
with open('report.md','x') as f: f.write("# Report\n\n"+s)
