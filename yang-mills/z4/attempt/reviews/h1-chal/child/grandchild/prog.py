import numpy as np
beta=64.0; alpha=2**(-1/3); NMAX=200
def kappas():
    x=beta/2; out=[]
    def I(m):
        t=1.0
        for j in range(1,m+1): t*=x/j
        s=0.0;k=0
        while True:
            s+=t; k+=1; t*=x*x/(k*(k+m))
            if t<s*1e-20 and k>x: break
        return s
    I1=I(1)
    return np.array([I(n+1)/I1 for n in range(NMAX+1)])
def run(N):
    t,w=np.polynomial.legendre.leggauss(N)
    a=(t+1)*np.pi/2; w=w*np.pi/2
    f=lambda a:np.exp(-alpha*beta**(2/3)*a*a)
    g=f(a)+f(np.pi-a)
    wt=(2/np.pi)*np.sin(a)**2
    N0=np.sum(w*wt*g*g)
    n=np.arange(NMAX+1)[:,None]
    # chi_n*sin^2 = sin((n+1)a) sin a
    c=(2/np.pi)*(np.sin((n+1)*a)*np.sin(a)*g*w).sum(1)
    return N0,c
k=kappas()
res={}
for N in (800,1600,3200):
    N0,c=run(N); S=np.sum(k*c*c)
    res[N]=(N0,S,S/N0,abs(np.sum(c*c)-N0))
    print(N,res[N])
N0,S,r,pr=res[1600]
d=np.diff(k)
lines=[("N0",N0),("S",S),("S_over_N0",r),("parseval_residual",pr),
("kappa0_minus1",k[0]-1),("kappa_max_diff",d.max()),
("dN0_800_to_1600",res[1600][0]-res[800][0]),("dN0_1600_to_3200",res[3200][0]-res[1600][0]),
("dS_800_to_1600",res[1600][1]-res[800][1]),("dS_1600_to_3200",res[3200][1]-res[1600][1]),
("parseval_3200",res[3200][3]),
("pred_parseval_lt1e-10",pr<1e-10),("pred_S_le_N0",S<=N0),("pred_kappa0",abs(k[0]-1)<1e-12),("pred_kappa_strict_dec",bool((d<0).all()))]
with open('answer.txt','x') as fh:
    for n_,v in lines: fh.write(f"{n_} {v!r}\n")
print(open('answer.txt').read())
