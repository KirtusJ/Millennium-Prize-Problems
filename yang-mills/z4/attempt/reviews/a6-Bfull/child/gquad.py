"""G(n) quadrature, n=0,1,2.  Predicates fixed BEFORE first run:
 Q1 G(0)=0.5 within 1e-6 at the finest grid (exact known; tolerance = expected O(L^-4)-ish midpoint
    error from the |k| non-analyticity at k=0, observed by grid-difference).
 Q2 successive-grid difference |G_L - G_{L/2}| < 1e-5 at finest L for n=0,1,2 (this is the reported error estimate).
 Q3 G(n) monotone-decreasing magnitude: |G(2)| < |G(1)| < G(0) (expectation only, 'measured').
Midpoint rule on (0,pi)^3 with L/2 points per axis equals full (-pi,pi)^3 midpoint grid with L points (symmetry)."""
import numpy as np, sys, json
out=sys.argv[1]
def G(n,L):
    h=L//2
    k=(np.arange(h)+.5)*np.pi/h
    a=4*np.sin(k/2)**2
    tot=0.0
    for i in range(h):
        s=a[i]+a[:,None]+a[None,:]
        s12=(a[i]+a[:,None])+0*a[None,:]
        m=np.arccosh(1+s/2)
        tot+=np.sum(s12*np.exp(-m*n)/(2*np.sinh(m)))
    return tot/h**3/ (1)   # mean over cube (0,pi)^3 == mean over (-pi,pi)^3
res={}
for L in (32,64,128,256,512):
    res[L]=[G(n,L) for n in (0,1,2)]
    print(L,res[L],flush=True)
Ls=sorted(res)
for n in range(3):
    print('n',n,'diff last two',abs(res[Ls[-1]][n]-res[Ls[-2]][n]),'prev',abs(res[Ls[-2]][n]-res[Ls[-3]][n]))
g=res[Ls[-1]]
err=[abs(res[Ls[-1]][n]-res[Ls[-2]][n]) for n in range(3)]
q1=abs(g[0]-.5)<1e-6; q2=all(e<1e-5 for e in err); q3=abs(g[2])<abs(g[1])<g[0]
print('Q1',q1,'Q2',q2,'Q3',q3)
with open(out,'x') as f: json.dump({'res':{str(k):v for k,v in res.items()},'err':err,'Q1':bool(q1),'Q2':bool(q2),'Q3':bool(q3)},f)
