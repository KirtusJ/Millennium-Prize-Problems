"""Diagnostic of null space of C(TRAIN) (read-only, predicates: D restricted to null(C) is ~0 => problem well-posed on range(C);
else eigenproblem has infinite/undefined eigenvalues.) Expectation: D null part ~0."""
import numpy as np
exec(open('an.py').read().split("print('D sym err'")[0].split('"""',2)[2])
CT,DT=CD(range(16))
e,U=np.linalg.eigh(CT); print('eigs C',e)
N=U[:,e<1e-12]; print('null dim',N.shape[1])
print('max|N^T D N|',np.abs(N.T@DT@N).max(),' max|D N|',np.abs(DT@N).max(), 'max |DT|',np.abs(DT).max())
# nullspace of C also for HELD
CH,DH=CD(range(16,32)); eh,UH=np.linalg.eigh(CH); print('held eigs',eh[:5])
print('null of C train vs held overlap', np.abs(N.T@CH@N).max())
for j in range(N.shape[1]):
    print([ (names[i],round(N[i,j],3)) for i in range(n) if abs(N[i,j])>1e-6])
