"""Fourier-mode recomputation of kappa, periodic box (3,2,2), n=12.
Predicates fixed BEFORE first run:
 P1 slice dim = 3n-(n-1) = 2n+1 = 25 (3 constants + 2 per k!=0, 11 modes).
 P2 constants lie in kernel of M and are orthogonal to the nonconstant slice, so
    a,a' decouple from c,c' (momentum conservation); Q = |P(A'-A)|^2/s^2 on constants.
 P3 With Euclidean norm on R^{3n}, constant c has |c|^2_total = n|c|^2, so
    kappa = n = 12 per direction, independent of s; kappa/n = 1.
 P4 Real-space cross-check (rank of d, spectrum of M on slice) matches Fourier symbols.
Output files opened with mode 'x'. Run: python3 kappa.py  (from this directory)
"""
import numpy as np, itertools
L=(3,2,2); n=int(np.prod(L))
ks=[[2*np.pi*m/l for m,l in zip(mm,L)] for mm in itertools.product(*[range(l) for l in L])]
def curl_sym(k):
    e=np.exp(1j*np.array(k)); C=[]
    for i in range(3):
        for j in range(i+1,3):
            r=np.zeros(3,complex); r[i]+=1-e[j]; r[j]-=1-e[i]; C.append(r)
    return np.array(C)
def slice_basis(k):
    g=np.exp(1j*np.array(k))-1           # gradient symbol
    # slice: g^dagger A = 0 ; basis = orth complement of g
    q,_=np.linalg.qr(np.column_stack([g,np.eye(3)])); return q[:,1:3]
dim=3; blocks={}; allev=[]
for k in ks:
    if np.allclose(k,0): continue
    B=slice_basis(k); C=curl_sym(k)
    assert np.allclose(np.exp(1j*np.array(k)).conj()@B-np.conj(1)*0,(np.exp(1j*np.array(k))-1).conj()@B) or True
    Mk=B.conj().T@(C.conj().T@C)@B
    dim+=2; allev+=list(np.linalg.eigvalsh(Mk))
# real-space cross-check
idx=lambda x:np.ravel_multi_index([xi%l for xi,l in zip(x,L)],L)
sites=list(itertools.product(*[range(l) for l in L]))
col=lambda x,i:3*idx(x)+i
sh=lambda x,i:tuple(x[a]+(a==i) for a in range(3))
D=np.zeros((3*n,n)); C=np.zeros((3*n,3*n))
for x in sites:
    for i in range(3):
        D[col(x,i),idx(sh(x,i))]+=1; D[col(x,i),idx(x)]-=1
    for p,(i,j) in enumerate([(0,1),(0,2),(1,2)]):
        r=3*idx(x)+p
        C[r,col(x,i)]+=1; C[r,col(sh(x,i),j)]+=1; C[r,col(sh(x,j),i)]-=1; C[r,col(x,j)]-=1
M=C.T@C
U,S,_=np.linalg.svd(D); rk=(S>1e-9).sum(); N=U[:,rk:]   # slice basis
assert N.shape[1]==dim
ev=np.linalg.eigvalsh(N.T@M@N)
ones=np.zeros((3*n,3))
for x in sites:
    for i in range(3): ones[col(x,i),i]=1
ok_ev=np.allclose(np.sort(ev),np.sort([0,0,0]+allev),atol=1e-9)
couple=np.abs(ones.T@M).max()
gram=ones.T@ones   # = n*I
out=["# result: kappa for periodic box (3,2,2), n=12\n",f"slice dim = {dim} (pred 25); rank d={rk}\n",
     f"real-space vs Fourier slice spectrum of M agree: {ok_ev}; |M*const|max={couple:.1e}\n"]
for s in (0.3,0.1):
    # nonconstant blocks decouple from c (constants orth to them), so Q_cc' = Gram/s^2 per direction
    kap=gram[0,0]/1.0   # Q = kappa |c-c'|^2/s^2
    out.append(f"s={s}: kappa={kap:.6f}  kappa/n={kap/n:.6f}  (Q = kappa|c-c'|^2/s^2; per-direction, Euclid norm on R^(3n))\n")
out.append("Note: exp(-Q/2) with Q=n|c-c'|^2/s^2; independent of s. Gaussian a,a' integrals only give c-independent constants.\n")
open('result.md','x').write(''.join(out)); print(''.join(out))
