import numpy as np
r=np.random.default_rng(1);N=10**6
q=r.normal(size=(N,4));q/=np.linalg.norm(q,axis=1)[:,None]
x=(2*q[:,0])**2;m=x.mean();se=x.std(ddof=1)/np.sqrt(N)
with open('control.txt','x') as f:f.write(f"E[(trU)^2] MC={m:.5f} SE={se:.5f} exact=1 z={(m-1)/se:.2f} within3SE={abs(m-1)<3*se}\n")
print(open('control.txt').read())
