import numpy as np
beta=3.276133577
def simpson(y,x):
    h=x[1]-x[0]; return h/3*(y[0]+y[-1]+4*y[1:-1:2].sum()+2*y[2:-1:2].sum())
chi=np.linspace(0,np.pi,2_000_001); a=np.cos(chi); w=np.sin(chi)**2*np.exp(beta*a)
Z=simpson(w,chi); m1=simpson(w*a,chi)/Z; m2=simpson(w*a*a,chi)/Z
I=lambda n: simpson(np.exp(beta*np.cos(chi))*np.cos(n*chi),chi)/np.pi
r=I(2)/I(1)
rng=np.random.default_rng(777); N=1_000_000; out=np.empty(0)
while out.size<N:
    M=N
    r1,r2,r3,r4=(1-rng.random(M) for _ in range(4))
    lam2=-(np.log(r1)+np.cos(2*np.pi*r2)**2*np.log(r3))/(2*beta)
    ok=r4**2<=1-lam2
    out=np.concatenate([out,1-2*lam2[ok]])
a0=out[:N]
rho=np.sqrt(1-a0**2); d=rng.standard_normal((N,3)); d/=np.linalg.norm(d,axis=1,keepdims=True)
q=np.column_stack([a0,rho[:,None]*d]); nrm=np.abs((q**2).sum(1)-1).max()
mean=a0.mean(); se=a0.std(ddof=1)/np.sqrt(N)
mean2=(a0**2).mean(); se2=(a0**2).std(ddof=1)/np.sqrt(N)
s=(f"beta={beta}\nquad <a0>={m1:.8f}  I2/I1={r:.8f}\nquad <a0^2>={m2:.8f}\n"
 f"KP <a0>={mean:.6f} +- {se:.6f}  pull={(mean-m1)/se:.2f} sigma\n"
 f"KP <a0^2>={mean2:.6f} +- {se2:.6f}  pull={(mean2-m2)/se2:.2f} sigma\n"
 f"max |norm-1|={nrm:.2e}; N={N}, seed 777\n")
with open('link_result.txt','x') as o: o.write(s)
print(s)
