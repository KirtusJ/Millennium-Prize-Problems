import numpy as np
exec(open('analyze.py').read().split("out={}")[0])
for nm,S in(('TRAIN',range(16)),('HELD',range(16,32))):
    C,_=CD(S); e=np.linalg.eigvalsh(C); print(nm,e[:6],e[-1],(e<1e-12*e[-1]).sum())
    print(sum(m[i] for i in S))
print([m[i] for i in range(32)])
