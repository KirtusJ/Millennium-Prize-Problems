"""G(n)=int d^3k/(2pi)^3 (s1+s2) r^n/sqrt(A^2-4), A=2+s1+s2+s3, r=(A-sqrt(A^2-4))/2
(k0 integral closed form: int dk/2pi e^{ikn}/(A-2cos k)=r^n/sqrt(A^2-4)).
3D midpoint rule on [0,pi]^3 (x8 by symmetry), N=64,128,256.
Predicates (fixed before first run):
 P1 G(0)=0.5 within 1e-3 at N=256 (midpoint rule, integrand ~|k| cusp at 0 => error ~N^-3..-4; tolerance from N=64->128 change).
 P2 |G(n;256)-G(n;128)| < 1e-4 for n<=16 (self-convergence; tolerance = what I'd quote as abs. accuracy).
 P3 G(n)>0 for n=1..16 (reflection positivity: F12 even under x0 reflection).
 P4 fitted p in [3.7,4.3] for n 8..16 (continuum: G ~ 1/(pi^2 n^4)=0.1013/n^4).
"""
import numpy as np, sys
def G(N, nmax=16):
    k=(np.arange(N)+0.5)*np.pi/N; s=4*np.sin(k/2)**2
    out=np.zeros(nmax+1)
    s2,s3=np.meshgrid(s,s,indexing='ij')
    for i in range(N):
        a=s[i]+s2+s3; A=2+a; sq=np.sqrt(A*A-4); r=(A-sq)/2
        w=(s[i]+s2)/sq; t=w.copy()
        for n in range(nmax+1):
            out[n]+=t.sum(); t=t*r
    return out*8/N**3/(2*np.pi)**3*np.pi**3
if __name__=="__main__":
    res={N:G(N) for N in (64,128,256)}
    with open("G_results.txt","x") as f:
        for n in range(17):
            f.write("%d %.10f %.10f %.10f\n"%(n,res[64][n],res[128][n],res[256][n]))
    g=res[256]; d=np.abs(res[256]-res[128])
    print("G0",g[0],"maxdiff",d.max())
    n=np.arange(8,17); p,lc=np.polyfit(np.log(n),np.log(g[8:]),1)
    print("p",-p,"c",np.exp(lc))
    # local exponents
    print("local p",[round(-np.log(g[i+1]/g[i])/np.log((i+1)/i),3) for i in range(8,16)])
    print("P1",abs(g[0]-.5)<1e-3,"P2",d.max()<1e-4,"P3",(g[1:]>0).all(),"P4",3.7<-p<4.3)
