import numpy as np
th0=1.2
n=2_000_001
chi=np.linspace(np.pi-th0,np.pi,n); f=(2/np.pi)*np.sin(chi)**2
h=chi[1]-chi[0]; Pq=h/3*(f[0]+f[-1]+4*f[1:-1:2].sum()+2*f[2:-1:2].sum())
Pex=(th0-np.sin(th0)*np.cos(th0))/np.pi
rng=np.random.default_rng(12345)
N=2_000_000; cnt=0
for _ in range(4):
    v=rng.standard_normal((N//4,4)); v/=np.linalg.norm(v,axis=1,keepdims=True)
    th=np.arccos(-v[:,0]); cnt+=int((th<th0).sum())
p=cnt/N; se=np.sqrt(p*(1-p)/N)
s=f"quadrature={Pq:.8f}\nclosed_form={Pex:.8f}\nMC={p:.6f} +- {se:.6f} (N={N}, seed 12345)\npull(MC-quad)/se={(p-Pq)/se:.2f}\n"
with open('haar_result.txt','x') as o: o.write(s)
print(s)
