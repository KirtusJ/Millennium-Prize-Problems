import numpy as np
exec(open('analyze.py').read().split("out={}")[0])
Ct,Dt=CD(range(16)); e,U=np.linalg.eigh(Ct); N=U[:,:4]
print(np.abs(Dt@N).max(), np.abs(N).max(), e[4]/e[-1])
Ch,Dh=CD(range(16,32)); e2,U2=np.linalg.eigh(Ch)
print('held null in train null?',np.abs(Ch@N).max(), np.abs(Dh@N).max())
