"""Predicate: with p3=0 and q=0 slack is exactly 0; test with p3=0,q!=0 (q along 3-axis, and q small) slack relative to scale. Seed 7, 10^5, files mode x."""
import numpy as np
rng=np.random.default_rng(7);N=10**5
p=rng.normal(size=(N,3));p[:,2]=0
q=rng.normal(size=(N,3))*10.0**rng.uniform(-6,1,N)[:,None]
u=p+q/2;w=q/2-p
g=lambda v:(v[:,0]**2+v[:,1]**2)/(2*np.linalg.norm(v,axis=1))
L=4*g(u)*g(w);rhs=p[:,0]**2+p[:,1]**2-p[:,2]**2-.75*(q**2).sum(1)
d=L-rhs;qq=(q**2).sum(1)
r=d/qq
with open('tight.txt','x') as f:
    s=f"p3=0,q!=0: min slack={d.min():.3e}, min slack/|q|^2={r.min():.4f}, max viol count={(d<-1e-12*(p**2).sum(1)).sum()}"
    f.write(s+'\n');print(s)
